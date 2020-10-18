# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_bcrypt import Bcrypt
import re
import os, glob
import pathlib
import datetime
from werkzeug.utils import secure_filename
from PIL import Image
from resizeimage import resizeimage
import subprocess

import dbcn
import usuarios
import permisos as permisosU
import asientos as asi
import documentos as docu
import tipodocs as tdoc
import geo as geo
import img
import loc_img

# create the application object
app = Flask(__name__)
app.secret_key ='\xfd{H\xe7<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa7'
app.config['LOGIN_DISABLED'] = False
app.config['IMG_ASIENTOS'] = '/static/imgbd/asi'
app.config['IMG_RECINTOS'] = '/static/imgbd/reci'
app.config['SUBIR_PDF'] = '/static/pdfdoc'

ALLOWED_EXTENSIONS = set(['pdf'])

BCRYPT_LOG_ROUNDS = 15
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ''

# globales
usr = ""
usrdep = 99
usrid = 0
permisos_usr = []

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.before_request
def before_request_func():
    """
    This function will run before every request. Let's add something to the session & g.
    It's a good place for things like establishing database connections, retrieving
    """

    global cxms
    global cxpg
    cxms = dbcn.get_db_ms()
    cxpg = dbcn.get_db_pg()


@app.teardown_request
def teardown_request_func(error=None):
    """
    This function will run after a request, regardless if an exception occurs or not.
    It's a good place to do some cleanup, such as closing any database connections.
    """

    cxpg.close()
    cxms.close()

    if error:
        # Log the error
        print(str(error))


@login_manager.user_loader
def user_loader(txtusr):
    global usr
    global usrdep
    global usrid
    global permisos_usr
    user = usuarios.Usuarios(cxms)

    if user.get_usuario(txtusr):
        usr = user.usuario
        usrdep = user.dep
        usrid = user.id
        permisos_usr = user.get_permisos_name(usr)
        return user


@app.context_processor
def inject_global():
    print(str(datetime.datetime.now())[0:-3])
    return dict(idate=datetime.date.today(), idatetime=str(datetime.datetime.now())[0:-3], usuario=usr, usrdep=usrdep, usrid=usrid)


@app.errorhandler(401)
def access_error(error):
    return render_template('401.html'), 401


@app.route('/get_geo', methods=['GET', 'POST'])
def get_geo():
    lat = request.args.get('latitud', 0, type=float)
    long = request.args.get('longitud', 0, type=float)

    g = geo.LatLong(cxpg)
    if g.get_geo(lat, long):
        return jsonify(dep=g.dep,
                       departamento=g.departamento,
                       prov=g.prov,
                       provincia=g.provincia,
                       sec=g.sec,
                       municipio=g.municipio)
    else:
        return jsonify(dep='---',
                       departamento='COORDENADA',
                       prov='---',
                       provincia='INCORRECTA !!!',
                       sec='---',
                       municipio='INTENTE NUEVAMENTE....')

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    u = usuarios.Usuarios(cxms)

    error = None
    if request.method == 'POST':

        if u.get_usuario(request.form['uname']):
            pw_es_igual = bcrypt.check_password_hash(u.password, request.form['pswd'])

            if request.form['uname'] != u.usuario  or not pw_es_igual:
                error = 'Credencial Inválida. Por favor intente nuevamente.'
            else:
                if login_user(u):
                    print ('Login OK')
                else:
                    print ('Login Error')

                return redirect(url_for('habilitado'))
        else:
            error = 'Usuario no registrado previamente'

    return render_template('login.html', error=error)


@app.route('/change_pwd', methods=['GET', 'POST'])
@login_required
def change_pwd():
    u = usuarios.Usuarios(cxms)
    error = None

    if request.method == 'POST':
        if u.get_usuario_usr(usr):
            pw_es_igual = bcrypt.check_password_hash(u.password, request.form['pwdold'])
            if not pw_es_igual:   # valida usr
                error = "Password anterior NO coincide...!"
                return render_template('pwd.html', error=error, u=u, load_u=True)
            elif request.form['pwdnew'] != request.form['pwdnew2'] :
                error = "Error en password nuevo NO coincide con password confirmado...!"
                return render_template('pwd.html', error=error, u=u, load_u=True)
            else:
                pw_hash = bcrypt.generate_password_hash(request.form['pwdnew']).decode('UTF-8')
                u.upd_pwd_usuario(usr, \
                            pw_hash, \
                            )
                return render_template('welcome.html')

    return render_template('pwd.html', error=error, u=u, load_u=False)


@app.route('/registro/<usuario_id>', methods=['GET', 'POST'])
def registro(usuario_id=None):
    u = usuarios.Usuarios(cxms)
    error = None

    if request.method == 'POST':
        if usuario_id == '0':  # es NEW
            if u.get_usuario(request.form['uname']) == True:   # valida usr
                error = "El usuario: " + request.form['uname']  + " ya existe...!"
                return render_template('registro.html', error=error, u=u, load_u=True)
            else:
                pw_hash = bcrypt.generate_password_hash(request.form['pswd']).decode('UTF-8')
                u.add_usuario(request.form['uname'], \
                            request.form['nombre'], \
                            request.form['apellidos'], \
                            request.form['email'], \
                            pw_hash, \
                            request.form['dep'], \
                            1)
                return render_template('welcome.html')
        else: # es EDIT
            u.upd_usuario(usuario_id, \
                            request.form['nombre'], \
                            request.form['apellidos'], \
                            request.form['email'], \
                            request.form['dep'], \
                            1)
            if usr == 'admin':
                return render_template('usuarios.html', usuarios=u.get_usuarios())
            return render_template('home.html')

    else: # viene de listado USUARIOS
        if usuario_id != 0:  # EDIT
            if u.get_usuario_id(usuario_id) == True:
                return render_template('registro.html', error=error, u=u, load_u=True)

    return render_template('registro.html', error=error, u=u, load_u=False)


@app.route('/m_usuarios', methods=['GET', 'POST'])
@login_required
def m_usuarios():
    u = usuarios.Usuarios(cxms)
    rows = u.get_usuarios()
    if rows:
        return render_template('usuarios.html', usuarios=rows)
    else:
        print ('Sin usuarios...')


@app.route('/usuario_del/<usuario_id>', methods=['GET', 'POST'])
@login_required
def usuario_del(usuario_id):
    u = usuarios.Usuarios(cxms)
    u.del_usuario(usuario_id)

    rows = u.get_usuarios()
    if rows:
        return render_template('usuarios.html', usuarios=rows)
    else:
        print ('Sin usuarios...')


@app.route('/permisos/<usuario_id>', methods=['GET', 'POST'])
@login_required
def permisos(usuario_id):
    u = usuarios.Usuarios(cxms)
    p = permisosU.Permisos(cxms)

    if request.method == 'POST':
        # Grabando
        vl = request.form['values_li']
        if vl != 'salir':
            p.reset_permisos_de_usuario(usuario_id)
            p.save_permisos_txt(usuario_id, request.form['values_li'])

        rows = u.get_usuarios()
        if rows:
            return render_template('usuarios.html', usuarios=rows)
        else:
            print ('Sin usuarios...')
    else:
        if u.get_usuario_id(usuario_id):
            m_rows = p.get_modulos_sin_asignar(usuario_id)      # False or rows
            pu_rows =  p.get_permisos_de_usuario(usuario_id)  # False or rows
            return render_template('permisos.html', usuario=u, modulos=m_rows, permisos_usuario=pu_rows)


@app.route('/asiento_img/<idloc>/<string:nomloc>', methods=['GET', 'POST'])
@login_required
def asiento_img(idloc, nomloc):

    i = img.Img(cxms)
    li = loc_img.LocImg(cxms)

    with_img = li.get_loc_imgs(idloc)  # False or rows-img

    error = None

    if request.method == 'POST':
        img_ids_ = request.form.getlist('imgsa[]')  # options img for Asiento
        img_ids = list(img_ids_[0].split(","))      # list ok

        uploaded_files = request.files.getlist("filelist")

        for n in range(len(img_ids)):
            f  = uploaded_files[n]
            if f.filename != '':
                securef = secure_filename(f.filename)
                f.save(os.path.join('.' + app.config['IMG_ASIENTOS'], securef))
                fpath = os.path.join(app.config['IMG_ASIENTOS'], securef)
                arch, ext = os.path.splitext(fpath)
                name_only = str(idloc).zfill(5) + "_" + str(img_ids[n]).zfill(2)
                name_to_save = name_only + ext
                name_to_del = os.path.join('.' + app.config['IMG_ASIENTOS']) + '/' + name_only + '.*'
                for file_img_old in glob.glob(name_to_del):  # remove old
                    os.unlink(file_img_old)

                fpath_destino = os.path.join(app.config['IMG_ASIENTOS'], name_to_save)
                resize_save_file(fpath, name_to_save, (1024, 768))
                li.del_loc_img(idloc, img_ids[n]) # remove de tabla
                li.add_loc_img(idloc, img_ids[n], fpath_destino, datetime.datetime.now(), usr)
                os.remove(fpath[1:])   # arch. fuente

        return redirect(url_for('asientos_list'))

    else:
        if with_img:  # Edit
            return render_template('asiento_img_upd.html', rows=i.get_imgs('Asiento'), nomloc=nomloc,
                                puede_editar='Asientos - Edición' in permisos_usr,
                                imgs_loaded=with_img)
        else:  # New
            return render_template('asiento_img.html', rows=i.get_imgs('Asiento'), nomloc=nomloc,
                                puede_editar='Asientos - Edición' in permisos_usr)


def resize_save_file(in_file, out_file, size):
    with open('.' + in_file, 'rb') as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)

    image.save('.' + os.path.join(app.config['IMG_ASIENTOS'], out_file))
    image.close()
    #return(out_file)


@app.route('/asientos_list', methods=['GET', 'POST'])
@login_required
def asientos_list():
    a = asi.Asientos(cxms)
    rows = a.get_asientos_all(usrdep)

    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('asientos_list.html', asientos=rows, puede_adicionar='Asientos - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin asientos...')


@app.route('/documentos_list', methods=['GET', 'POST'])
@login_required
def documentos_list():
    d = docu.Documentos(cxms)
    rows = d.get_documentos_all(usrdep)

    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('documentos_list.html', documentos=rows, puede_adicionar='Documentos - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin Documentos...')

@app.route('/documento/<doc_id>', methods=['GET', 'POST'])
def documento(doc_id):
    d = docu.Documentos(cxms)
    tdocu = tdoc.TipoDocs(cxms)
    error = None

    if request.method == 'POST':
        if doc_id == '0':  # es NEW
            nextid = d.get_next_id_doc()
            tipo = d.tipo_doc(request.form['doc'])
            tipo = tipo.lower()
            f = request.files['archivo']
            if allowed_file(f.filename):
                filename = secure_filename(f.filename)
                filename = doc_id + '_' + filename
                f.save(os.path.join('.' + app.config['SUBIR_PDF'], filename))
                fpath = os.path.join(app.config['SUBIR_PDF'], filename)
                fpath1 = os.path.join('.' + app.config['SUBIR_PDF'] + '/')
                arch, ext = os.path.splitext(fpath)
                name_to_save = str(nextid) + "_" + str(tipo) + ext
                ruta = app.config['SUBIR_PDF'] + '/' + name_to_save
                os.rename(fpath1 + filename, fpath1 + name_to_save)
            else:
                flash('Debe cargar solo archivos PDFs')
                return render_template('documento.html', error=error, d=d, load_d=False, titulo='Registro de Documentos', tdocumentos=tdocu.get_tipo_documentos(usrdep))
            d.add_documento(request.form['doc'], \
                        request.form['dep'], \
                        request.form['cite'], \
                        ruta, \
                        request.form['fechadoc'], \
                        request.form['obs'], \
                        request.form['fecharegistro'], \
                        request.form['usuario'], \
                        request.form['fechaingreso'])
            return render_template('documentos_list.html', documentos=d.get_documentos_all(usrdep), puede_adicionar='Documentos - Adición' in permisos_usr)
        else: # es EDIT
            f = request.files['archivo']
            if allowed_file(f.filename):
                tipodo = d.tipo_doc(request.form['tipodocu'])
                tipodo = doc_id + "_" + tipodo + '.pdf'
                tipodo = tipodo.lower()
                ejemplo_dir = os.path.join('.' + app.config['SUBIR_PDF'] + '/')
                directorio = pathlib.Path(ejemplo_dir)
                for fichero in directorio.iterdir():
                    if fichero.name == tipodo:
                            os.remove(ejemplo_dir + fichero.name)

                tipo = d.tipo_doc(request.form['doc'])
                tipo = tipo.lower()
                f = request.files['archivo']
                filename = secure_filename(f.filename)
                filename = doc_id + '_' + filename
                f.save(os.path.join('.' + app.config['SUBIR_PDF'], filename))
                fpath = os.path.join(app.config['SUBIR_PDF'], filename)
                fpath1 = os.path.join('.' + app.config['SUBIR_PDF'] + '/')
                arch, ext = os.path.splitext(fpath)
                name_to_save = doc_id + "_" + str(tipo) + ext
                ruta = app.config['SUBIR_PDF'] + '/' + name_to_save
                os.rename(fpath1 + filename, fpath1 + name_to_save)
            else:
                tipo = d.tipo_doc(request.form['doc'])
                tipo = tipo.lower()
                name_to_save = doc_id + "_" + str(tipo) + '.pdf'
                tipodo = d.tipo_doc(request.form['tipodocu'])
                tipodo = tipodo.lower()
                name_to_save1 = doc_id + "_" + str(tipodo) + '.pdf'
                ruta = app.config['SUBIR_PDF'] + '/' + name_to_save
                ejemplo_dir = os.path.join('.' + app.config['SUBIR_PDF'] + '/')
                directorio = pathlib.Path(ejemplo_dir)
                for fichero in directorio.iterdir():
                    if fichero.name == name_to_save1:
                            os.rename(ejemplo_dir + fichero.name, ejemplo_dir + name_to_save)

            fa = str(datetime.datetime.now())[:-7]
            d.upd_documento(doc_id, \
                        request.form['doc'], \
                        request.form['dep'], \
                        request.form['cite'], \
                        ruta, \
                        request.form['fechadoc'], \
                        request.form['obs'], \
                        request.form['usuario'], \
                        fa)
            if usr == 'admin':
                return render_template('documentos_list.html', documentos=d.get_documentos())
            return render_template('documentos_list.html', documentos=d.get_documentos_all(usrdep), puede_adicionar='Documentos - Adición' in permisos_usr)

    else: # viene de listado DOCUMENTOS
        if doc_id != 0:  # EDIT
            if d.get_documento_id(doc_id) == True:
                return render_template('documento.html', error=error, d=d, load_d=True, titulo='Modificacion de Documentos', tdocumentos=tdocu.get_tipo_documentos(usrdep))

    return render_template('documento.html', error=error, d=d, load_d=False, titulo='Registro de Documentos', tdocumentos=tdocu.get_tipo_documentos(usrdep))


@app.route('/documento_pdf/<doc_id>/<string:tipo>', methods=['GET', 'POST'])
@login_required
def documento_pdf(doc_id, tipo):
    dp = dpdf.Documentos_pdf(cxms)
    error = None

    if request.method == 'POST':
        f = request.files['archivo']
        filename = secure_filename(f.filename)
        filename = doc_id + '_' + filename
        f.save(os.path.join('.' + app.config['SUBIR_PDF'], filename))
        fpath = os.path.join(app.config['SUBIR_PDF'], filename)
        fpath1 = os.path.join('.' + app.config['SUBIR_PDF'] + '/')
        arch, ext = os.path.splitext(fpath)
        name_to_save = str(doc_id) + "_" + str(tipo) + ext
        ruta = app.config['SUBIR_PDF'] + '/' + name_to_save
        os.rename(fpath1 + filename, fpath1 + name_to_save)

        if dp.upd_documentopdf_id(doc_id, ruta) == True:
                return render_template('documentos_list.html', documentos=dp.get_documentospdf_all(usrdep), puede_adicionar='Documentos - Adición' in permisos_usr)

    return render_template('documento_pdf.html', error=error, dp=dp, load_dp=False, puede_editar='Documentos - Edición' in permisos_usr)


@app.route('/documento_del/<doc_id>/<tipo_d>', methods=['GET', 'POST'])
@login_required
def documento_del(doc_id, tipo_d):
    d = docu.Documentos(cxms)
    d.del_documento(doc_id)
    tipod = doc_id + "_" + tipo_d + '.pdf'
    tipod = tipod.lower()
    ejemplo_dir = os.path.join('.' + app.config['SUBIR_PDF'] + '/')
    directorio = pathlib.Path(ejemplo_dir)
    for fichero in directorio.iterdir():
        if fichero.name == tipod:
                os.remove(ejemplo_dir + fichero.name)
    rows = d.get_documentos_all(usrdep)
    if rows:
        return render_template('documentos_list.html', documentos=rows, puede_adicionar='Documentos - Adición' in permisos_usr)
    else:
        print ('Sin documentos...')


@app.route('/asiento/<idloc>', methods=['GET', 'POST'])
@login_required
def asiento(idloc):
    a = asi.Asientos(cxms)

    error = None
    p = ('Asientos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        if idloc == '0':  # es NEW
            if False:   # valida si neces POST
                #error = "El usuario: " + request.form['uname']  + " ya existe...!"
                #return render_template('asiento.html', error=error, u=u, load_u=True)
                print('msg-err')
            else:
                nextid = a.get_next_idloc()
                a.add_asiento(nextid, request.form['deploc'], request.form['provloc'], \
                              request.form['secloc'], request.form['nomloc'], request.form['poblacionloc'], \
                              request.form['poblacionelecloc'], request.form['fechacensoloc'], request.form['tipolocloc'], \
                              request.form['marcaloc'], request.form['latitud'], request.form['longitud'], \
                              request.form['estado'], '')

                a.add_asiento2(nextid, request.form['etapa'], request.form['docAct'], \
                              request.form['fechaDocAct'], request.form['obsUbicacion'], request.form['docRspNal'], \
                               request.form['fechaRspNal'], request.form['obs'], request.form['fechaIngreso'][:-7], \
                              fa, request.form['usuario'])

                rows = a.get_asientos_all(usrdep)
                return render_template('asientos_list.html', asientos=rows)  # render a template
        else: # Es Edit
            a.upd_asiento(idloc, request.form['nomloc'], request.form['poblacionloc'], \
                          request.form['poblacionelecloc'], request.form['fechacensoloc'], request.form['tipolocloc'], \
                          request.form['marcaloc'], request.form['latitud'], request.form['longitud'], \
                          request.form['estado'], '')


            fa = str(datetime.datetime.now())[:-7]     # fechaAct
            if a.existe_en_loc2(idloc):
                # Debe actualizar fechaAct y usuario

                a.upd_asiento2(idloc, request.form['etapa'], request.form['docAct'], \
                                request.form['fechaDocAct'], request.form['obsUbicacion'], request.form['docRspNal'], \
                               request.form['fechaRspNal'], request.form['obs'], str(request.form['fechaIngreso']), \
                               fa, usr)
            else:
                a.add_asiento2(idloc, request.form['etapa'], request.form['docAct'], \
                              request.form['fechaDocAct'], request.form['obsUbicacion'], request.form['docRspNal'], \
                               request.form['fechaRspNal'], request.form['obs'], request.form['fechaIngreso'], \
                              fa, request.form['usuario'])


            rows = a.get_asientos_all(usrdep)
            return render_template('asientos_list.html', asientos=rows)  # render a template
    else: # Viene de <asientos_list>
        if idloc != '0':  # EDIT
            if a.get_asiento_idloc(idloc) == True:
                if a.docAct == None:
                    a.docAct = ""
                if a.fechaIngreso == None:
                    a.fechaIngreso = str(datetime.datetime.now())[:-7]
                if a.fechaAct == None:
                    a.fechaAct = str(datetime.datetime.now())[:-7]
                if a.usuario == None:
                    a.usuario = usr

                return render_template('asiento.html', error=error, a=a, load=True, puede_editar=p)

    # New
    return render_template('asiento.html', error=error, a=a, load=False, puede_editar=p)


@app.route('/about')
def about():
    return render_template('public/about.html')


@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/habilitado')
@login_required
def habilitado():
    return render_template('habilitado.html')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():

    #user = current_user
    #user.authenticated = False
    #db.session.add(user)
    #db.session.commit()
    logout_user()
    return render_template('/logout.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

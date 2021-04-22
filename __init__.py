# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_bcrypt import Bcrypt
import webbrowser
import re
import os
import sys
import pathlib
import datetime
from werkzeug.utils import secure_filename
from PIL import Image
from resizeimage import resizeimage

import dbcn
import usuarios
import permisos as permisosU
import asientos as asi
import reportes as rep
import documentos as docu
import documentos_pdf as dpdf
import tipodocs as tdoc
import reportesPDF as rpdf
import exterior as ext
import recintos as reci
import reciespe as recie
import reciespeciales as recies
import reciasiento as recia
import zonas as zo
import geo as geo
import img
import loc_img
import reci_img

import paises
import deptos as deptoss
import provincias as provs
import municipios as muns
import bitacoras
import indcate
import indsubcate
import loc_cate
import asiento_indi as indi
import clas_grupo
import clasificadores
import clasif_get
import get_json

# create the application object
app = Flask(__name__)
app.secret_key ='\xfd{H\xe7<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa7'
app.config['LOGIN_DISABLED'] = False
app.config['PATH_APP'] = '/var/www/flasks/age/'
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

# path init - to save img, ..
chd = os.chdir(app.config['PATH_APP'])


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
def utility_processor():
    def current_date_format(date):
        months = ("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        hora = date.strftime('%H:%M:%S')
        messsage = "{}-{}-{} {}".format(day, month, year, hora)
        return messsage
    return dict(fecha=current_date_format)


@app.context_processor
def inject_global():
    print(str(datetime.datetime.now())[0:-3])
    return dict(idate=datetime.date.today(), idatetime=str(datetime.datetime.now())[0:-3], usuario=usr, usrdep=usrdep, usrid=usrid)


@app.errorhandler(401)
def access_error(error):
    return render_template('401.html'), 401



@app.route('/gjson_dep/<dep>', methods=['GET', 'POST'])
def gjson_dep(dep):
    j = get_json.GetJson(cxpg)
    geo_json = j.get_dep(dep)
    return render_template('gjson.html', geo_json = geo_json)


@app.route('/gjson_nal/', methods=['GET', 'POST'])
def gjson_nal():
    j = get_json.GetJson(cxpg)
    geo_json = j.get_nal()

    #with open ('/home/r/triandb4err.geojson', 'r') as f:
        #geo_json = f.read()

    #print(geo_json)
    return render_template('gjson.html', geo_json = geo_json)



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
                       municipio=g.municipio,
                       nrocircun=g.nrocircun)
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

    i = img.Img(cxms)  # conecta a la BD
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

                name_to_save = str(idloc).zfill(5) + "_" + str(img_ids[n]).zfill(2)  + ext
                fpath_destino = os.path.join(app.config['IMG_ASIENTOS'], name_to_save)
                resize_save_file(fpath, name_to_save, (1024, 768))

                if li.exist_img(idloc, img_ids[n]):   # si upd img
                    file_to_del = li.get_name_file_img(idloc, img_ids[n])
                    os.remove(file_to_del[1:]) # borra arch. de HD
                    li.del_loc_img(idloc, img_ids[n]) # borra de bd

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

'''
def resize_save_file(in_file, out_file, size):
    with open('.' + in_file, 'rb') as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)

    image.save('.' + os.path.join(app.config['IMG_ASIENTOS'], out_file))
    image.close()
    #return(out_file)
'''

#Codigo Grover-Inicio
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
        return render_template('documentos_list.html', puede_adicionar='Documentos - Adición' in permisos_usr)

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
#Codigo Grover-Final

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


@app.route('/asiento/<idloc>', methods=['GET', 'POST'])
@login_required
def asiento(idloc):
    a = asi.Asientos(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Asientos - Edición' in permisos_usr)  # t/f

    '''
    # historico
    IP_remoto = request.remote_addr
    hloc_loc2 = historicolocloc2.Historicolocloc2() # -> bdge
    #
'''
    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        if usrdep != 0:
            docRspNal = 0
        if usrdep == 0:
            docRspNal = request.form['docRspNal']
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']
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
                              request.form['estado'], '', \
                              request.form['etapa'], request.form['obsUbicacion'], request.form['obs'], \
                              request.form['fechaIngreso'][:-7], fa, request.form['usuario'], request.form['docAct'], docRspNal, docActF)

                d.upd_doc(request.form['docAct'], docRspNal, request.form['doc_idAct'], request.form['doc_idRspNal'], docActF)

                rows = a.get_asientos_all(usrdep)
                return render_template('asientos_list.html', asientos=rows, puede_adicionar='Asientos - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            a.upd_asiento(idloc, request.form['nomloc'], request.form['poblacionloc'], \
                          request.form['poblacionelecloc'], request.form['fechacensoloc'], request.form['tipolocloc'], \
                          request.form['marcaloc'], request.form['latitud'], request.form['longitud'], \
                          request.form['estado'], '', request.form['etapa'], \
                          request.form['obsUbicacion'], request.form['obs'], \
                          str(request.form['fechaIngreso']), fa, usr, request.form['docAct'], docRspNal, docActF)
            d.upd_doc(request.form['docAct'], 0, request.form['doc_idAct'], request.form['doc_idRspNal'], docActF)

            rows = a.get_asientos_all(usrdep)
            return render_template('asientos_list.html', asientos=rows, puede_adicionar='Asientos - Adición' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if idloc != '0':  # EDIT
            if a.get_asiento_idloc(idloc) == True:
                """if a.docAct == None:
                    a.docAct = """
                if a.fechaIngreso == None:
                    a.fechaIngreso = str(datetime.datetime.now())[:-7]
                if a.fechaAct == None:
                    a.fechaAct = str(datetime.datetime.now())[:-7]
                if a.usuario == None:
                    a.usuario = usr

                return render_template('asiento.html', error=error, a=a, load=True, puede_editar=p, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))

    # New
    return render_template('asiento.html', error=error, a=a, load=False, puede_editar=p, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))


@app.route('/exterior_list', methods=['GET', 'POST'])
@login_required
def exterior_list():
    ex = ext.Exterior(cxms)
    rows = ex.get_exterior_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('exterior_list.html', exteriors=rows, puede_adicionar='Exterior - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin asientos...')


@app.route('/exterior/<idloc>', methods=['GET', 'POST'])
@login_required
def exterior(idloc):
    ex = ext.Exterior(cxms)
    a = asi.Asientos(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Exterior - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        if idloc == '0':  # es NEW
            if False:   # valida si neces POST
                #error = "El usuario: " + request.form['uname']  + " ya existe...!"
                #return render_template('asiento.html', error=error, u=u, load_u=True)
                print('msg-err')
            else:
                nextid = a.get_next_idloc()
                a.add_asiento(nextid, request.form['dpto'], request.form['provincia'], \
                              request.form['municipio'], request.form['nomloc'], 0, \
                              request.form['poblacionelecloc'], '2007-01-01', 0, \
                              request.form['marcaloc'], request.form['latitud'], request.form['longitud'], \
                              request.form['estado'], request.form['cirConsulado'], request.form['etapa'], \
                              request.form['obsUbicacion'], request.form['obs'], request.form['fechaIngreso'][:-7], \
                              fa, request.form['usuario'], 0, request.form['docRspNal'], 0)

                d.upd_doc(0, request.form['docRspNal'], 0, request.form['doc_idRspNal'], 0)

                rows = ex.get_exterior_all(usrdep)
                return render_template('exterior_list.html', exteriors=rows, puede_adicionar='Exterior - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            a.upd_asiento_ex(idloc, request.form['dpto'], request.form['provincia'], \
                              request.form['municipio'], request.form['nomloc'], 0, \
                              request.form['poblacionelecloc'], 0, \
                              request.form['marcaloc'], request.form['latitud'], request.form['longitud'], \
                              request.form['estado'], request.form['cirConsulado'], request.form['etapa'], \
                              request.form['obsUbicacion'], request.form['obs'], \
                              str(request.form['fechaIngreso']), fa, usr, 0, request.form['docRspNal'])

            d.upd_doc(0, 0, 0, request.form['doc_idRspNal'], 0)

            rows = ex.get_exterior_all(usrdep)
            return render_template('exterior_list.html', exteriors=rows, puede_adicionar='Exterior - Adición' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if idloc != '0':  # EDIT
            if a.get_asiento_idloc(idloc) == True:

                if a.fechaIngreso == None:
                    a.fechaIngreso = str(datetime.datetime.now())[:-7]
                if a.fechaAct == None:
                    a.fechaAct = str(datetime.datetime.now())[:-7]
                if a.usuario == None:
                    a.usuario = usr

                return render_template('exterior.html', error=error, a=a, load=True, puede_editar=p, paises=ex.get_paises_all(usrdep),
                                       dptos=ex.get_departamentos_all(usrdep), provincias=ex.get_provincias_all(usrdep),
                                       municipios=ex.get_municipios_all(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))
    # New
    return render_template('exterior.html', error=error, a=a, load=False, puede_editar=p, paises=ex.get_paises_all(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))

''' dup c/ obtenido de rep - resultado idem
@app.route('/get_departamentos_all', methods=['GET', 'POST'])
def get_departamentos_all():
    ex = ext.Exterior(cxms)
    rows = ex.get_departamentos_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='NO',
                       provincia='EXISTE !!!',
                       municipio='DEPARTAMENTO....')
'''

@app.route('/get_geo_all', methods=['GET', 'POST'])
def get_geo_all():
    a = asi.Asientos(cxms)
    rows = a.get_geo_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='COORDENADA',
                       provincia='INCORRECTA !!!',
                       municipio='INTENTE NUEVAMENTE....')


@app.route('/reportes', methods=['GET', 'POST'])
@login_required
def reportes():
    r = rep.Reportes(cxms)
    return render_template('reportes.html', load_r=False, puede_consultar='Reportes - Consulta' in permisos_usr)


@app.route('/reportespdf', methods=['GET', 'POST'])
def reportespdf():
    new = 2
    rp = rpdf.ReportesPDF(cxms)
    if request.method == 'POST':
        if request.form.get('cir1') == None:
            cir1 = request.form.get('cir1', 0)
        else:
            cir1 = request.form['cir1']

        if request.form.get('cir2') == None:
            cir2 = request.form.get('cir2', 0)
        else:
            cir2 = request.form['cir2']

        if request.form.get('cir3') == None:
            cir3 = request.form.get('cir3', 0)
        else:
            cir3 = request.form['cir3']

        if request.form.get('provincia') == None:
            provincia = ''
        else:
            provincia = request.form['provincia']

        if request.form.get('municipio') == None:
            municipio = ''
        else:
            municipio = request.form['municipio']

        if request.form['estado'] == "":
            estado = ''
        else:
            estado = request.form['estado']

        if request.form['inicio'] == "":
            inicio = ''
        else:
            inicio = request.form['inicio']

        if request.form['final'] == "":
            final = ''
        else:
            final = request.form['final']

        rows = rp.reporte_consulta(usrdep, request.form['dpto'], provincia, municipio,
                                   cir1, cir2, cir3, estado, inicio, final)
        if rows:
            url = "file:///home/r/pge/age/reporte.pdf"
            webbrowser.open(url,new=new)
            return ('PDF Generado')
        else:
            return ('PDF Generado')


@app.route('/get_provincias_all', methods=['GET', 'POST'])
def get_provincia_all():
    r = rep.Reportes(cxms)
    rows = r.get_provincias_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='COORDENADA',
                       provincia='INCORRECTA !!!',
                       municipio='INTENTE NUEVAMENTE....')


@app.route('/get_municipios_all', methods=['GET', 'POST'])
def get_municipios_all():
    r = rep.Reportes(cxms)
    rows = r.get_municipios_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='COORDENADA',
                       provincia='INCORRECTA !!!',
                       municipio='INTENTE NUEVAMENTE....')

#========== Modulo Recintos ============#

@app.route('/recintos_list', methods=['GET', 'POST'])
@login_required
def recintos_list():
    rc = reci.Recintos(cxms)
    rows = rc.get_recintos_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('recintos_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos...')


@app.route('/recinto/<idreci>/<idlocreci>', methods=['GET', 'POST'])
@login_required
def recinto(idreci, idlocreci):
    rc = reci.Recintos(cxms)
    rca = recia.Reciasiento(cxms)
    z = zo.Zonas(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Recintos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        """Valida si el campo docActF esta desactivado"""
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']
        """Valida si el campo ruereci esta desactivado"""
        if request.form.get('ruereci') == None:
            ruereci = 0
        else:
            ruereci = request.form['ruereci']
        """Valida si el campo edireci esta desactivado"""
        if request.form.get('edireci') == None:
            edireci = 0
        else:
            edireci = request.form['edireci']
        """Valida si el campo depenreci esta desactivado"""
        if request.form.get('depenreci') == None:
            depenreci = 0
        else:
            depenreci = request.form['depenreci']

        if idreci == '0':  # es NEW
            if False:   # valida si neces POST
                #error = "El usuario: " + request.form['uname']  + " ya existe...!"
                #return render_template('asiento.html', error=error, u=u, load_u=True)
                print('msg-err')
            else:
                nextid = rc.get_next_reci()
                idlocreci = request.form['asiento'].split(':')
                rc.add_recinto(idlocreci[1], nextid, request.form['nomreci'], request.form['zonareci'], \
                               request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                               request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                               ruereci, edireci, depenreci, \
                               request.form['pisosreci'], request.form['fechaIngreso'][:-7], fa, \
                               request.form['usuario'], request.form['etapa'], request.form['docAct'], docActF)

                rows = rc.get_recintos_all(usrdep)
                return render_template('recintos_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            idlocreci = request.form['asiento'].split(':')
            rc.upd_recinto(idlocreci[1], idreci, request.form['nomreci'], request.form['zonareci'], \
                               request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                               request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                               ruereci, edireci, depenreci, \
                               request.form['pisosreci'], request.form['fechaIngreso'], fa, \
                               usr, request.form['etapa'], request.form['docAct'], docActF)

            rows = rc.get_recintos_all(usrdep)
            return render_template('recintos_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if idreci != '0':  # EDIT
            if rc.get_recinto_idreci(idreci, idlocreci) == True:
                """if a.docAct == None:
                    a.docAct = """
                if rc.fechaIngreso == None:
                    rc.fechaIngreso = str(datetime.datetime.now())[:-7]
                if rc.fechaAct == None:
                    rc.fechaAct = str(datetime.datetime.now())[:-7]
                if rc.usuario == None:
                    rc.usuario = usr

                return render_template('recinto.html', error=error, rc=rc, load=True, puede_editar=p, asientoRecis=rca.get_asientos_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rc.get_estados(), trecintos=rc.get_tiporecintos(), tpdfsA=d.get_tipo_documentos_pdfA(usrdep))

    # New
    return render_template('recinto.html', error=error, rc=rc, load=False, puede_editar=p, estados=rc.get_estados(), trecintos=rc.get_tiporecintos(), titulo='Registro de Zonas y Distritos',
                           tpdfsA=d.get_tipo_documentos_pdfA(usrdep))


@app.route('/get_asientos_all1', methods=['GET', 'POST'])
def get_asientos_all1():
    dp = request.args.get('dpto')
    pro = request.args.get('provi')
    se = request.args.get('secci')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_asientos_all1(usrdep, dp, pro, se)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_asientos_all2', methods=['GET', 'POST'])
def get_asientos_all2():
    dp = request.args.get('dpto')
    pro = request.args.get('provi')
    se = request.args.get('secci')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_asientos_all2(usrdep, dp, pro, se)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='COORDENADA',
                       provincia='INCORRECTA !!!',
                       municipio='INTENTE NUEVAMENTE....')


@app.route('/get_zonas_all1', methods=['GET', 'POST'])
def get_zonas_all1():
    idloc = request.args.get('idloc')
    circun = request.args.get('circun')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_zonas_all1(usrdep, idloc, circun)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_distritos_all', methods=['GET', 'POST'])
def get_distritos_all():
    circun = request.args.get('circun')
    idlocreci = request.args.get('idlocreci')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_distritos_all(circun, idlocreci)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()

#========== Modulo GeoRecintos Pueblos Indigenas ============#

@app.route('/reciespe_list', methods=['GET', 'POST'])
@login_required
def reciespe_list():
    rce = recie.Reciespe(cxms)
    rows = rce.get_reciespe_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('reciespe_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos...')


@app.route('/reciespe/<idreci>/<idlocreci>', methods=['GET', 'POST'])
@login_required
def reciespe(idreci, idlocreci):
    rce = recie.Reciespe(cxms)
    rca = recia.Reciasiento(cxms)
    z = zo.Zonas(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Recintos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        """Valida si el campo docActF esta desactivado"""
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']
        """Valida si el campo ruereci esta desactivado"""
        if request.form.get('ruereci') == None:
            ruereci = 0
        else:
            ruereci = request.form['ruereci']
        """Valida si el campo edireci esta desactivado"""
        if request.form.get('edireci') == None:
            edireci = 0
        else:
            edireci = request.form['edireci']
        """Valida si el campo depenreci esta desactivado"""
        if request.form.get('depenreci') == None:
            depenreci = 0
        else:
            depenreci = request.form['depenreci']

        if idreci == '0':  # es NEW
            if False:   # valida si neces POST
                #error = "El usuario: " + request.form['uname']  + " ya existe...!"
                #return render_template('asiento.html', error=error, u=u, load_u=True)
                print('msg-err')
            else:
                nextid = rce.get_next_reci()
                idlocreci = request.form['asiento'].split(':')
                rce.add_recinto(idlocreci[1], nextid, request.form['nomreci'], request.form['zonareci'], \
                               request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                               request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                               ruereci, edireci, depenreci, \
                               request.form['pisosreci'], request.form['fechaIngreso'][:-7], fa, \
                               request.form['usuario'], request.form['etapa'], request.form['docAct'], docActF, request.form['pueblo'])

                rows = rce.get_reciespe_all(usrdep)
                return render_template('reciespe_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            idlocreci = request.form['asiento'].split(':')
            rce.upd_recinto(idlocreci[1], idreci, request.form['nomreci'], request.form['zonareci'], \
                               request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                               request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                               ruereci, edireci, depenreci, \
                               request.form['pisosreci'], request.form['fechaIngreso'], fa, \
                               usr, request.form['etapa'], request.form['docAct'], docActF, request.form['pueblo'])

            rows = rce.get_reciespe_all(usrdep)
            return render_template('reciespe_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if idreci != '0':  # EDIT
            if rce.get_recinto_idreci(idreci, idlocreci) == True:
                """if a.docAct == None:
                    a.docAct = """
                if rce.fechaIngreso == None:
                    rce.fechaIngreso = str(datetime.datetime.now())[:-7]
                if rce.fechaAct == None:
                    rce.fechaAct = str(datetime.datetime.now())[:-7]
                if rce.usuario == None:
                    rce.usuario = usr

                return render_template('reciespe.html', error=error, rce=rce, load=True, puede_editar=p, asientoRecis=rca.get_asientos_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rce.get_estados(), trecintos=rce.get_tiporecintos(), tpdfsA=d.get_tipo_documentos_pdfA(usrdep), naciones=rce.get_naciones())

    # New
    return render_template('reciespe.html', error=error, rce=rce, load=False, puede_editar=p, estados=rce.get_estados(), trecintos=rce.get_tiporecintos(), titulo='Registro de Zonas y Distritos',
                           tpdfsA=d.get_tipo_documentos_pdfA(usrdep))


@app.route('/get_geo_esp', methods=['GET', 'POST'])
def get_geo_esp():
    lat = request.args.get('latitud', 0, type=float)
    long = request.args.get('longitud', 0, type=float)
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_geoesp_all(lat, long)
    if rows:
        return jsonify(dep=rca.dep,
                       departamento=rca.departamento,
                       prov=rca.prov,
                       provincia=rca.provincia,
                       sec=rca.sec,
                       municipio=rca.municipio,
                       nrocircun=rca.nrocircun)
    else:
        return jsonify(dep='---',
                       departamento='CIRCUNSCRIPCION',
                       prov='---',
                       provincia='INCORRECTA !!!',
                       sec='---',
                       municipio='PUEBLO INDIGENA NO EXISTE',
                       nrocircun='NO EXISTE....')

@app.route('/get_pueblos_all', methods=['GET', 'POST'])
def get_pueblos_all():
    dep = request.args.get('dep')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_pueblos_all(dep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()

#========== Modulo Zonas y Distritos ============#

@app.route('/zonas_list', methods=['GET', 'POST'])
@login_required
def zonas_list():
    z = zo.Zonas(cxms)
    rows = z.get_zonas_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('zonas_list.html', zonas=rows, puede_adicionar='Zonas - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin zonas...')


@app.route('/zonas/<idloc>/<iddist>/<ban>', methods=['GET', 'POST'])
@login_required
def zonas(idloc, iddist, ban):
    z = zo.Zonas(cxms)

    error = None
    p = ('Zonas - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]

        if iddist == '0':  # es NEW
            if False:   # valida si neces POST
                #error = "El usuario: " + request.form['uname']  + " ya existe...!"
                #return render_template('asiento.html', error=error, u=u, load_u=True)
                print('msg-err')
            else:
                nextiddist = z.get_next_dist(request.form['idloc'])

                z.add_dist(request.form['idloc'], nextiddist, request.form['nrodist'], request.form['nomdist'], \
                           request.form['fechaIngreso'][:-7], fa, request.form['usuario'])
                if ban == '1':
                    flash('Registro grabado !!! CORRECTAMENTE !!!')
                    return render_template('zona.html', error=error, z=z, load_d=True, puede_editar=p, titulo='Registro de Distritos')
                else:
                    rows = z.get_zonas_all(usrdep)
                    return render_template('zonas_list.html', zonas=rows, puede_adicionar='Zonas - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            z.upd_dist(request.form['idloc'], iddist, request.form['nrodist'], request.form['nomdist'], fa, usr)

            rows = z.get_zonas_all(usrdep)
            return render_template('zonas_list.html', zonas=rows, puede_adicionar='Zonas - Adición' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if iddist != '0':  # EDIT
            if z.get_zonadist_idloc(idloc, iddist) == True:
                """if a.docAct == None:
                    a.docAct = """
                if z.fechaIngreso == None:
                    z.fechaIngreso = str(datetime.datetime.now())[:-7]
                if z.fechaAct == None:
                    z.fechaAct = str(datetime.datetime.now())[:-7]
                if z.usuario == None:
                    z.usuario = usr

                return render_template('zona.html', error=error, z=z, load=True, puede_editar=p, titulo='Modificación de Distritos')

    # New
    return render_template('zona.html', error=error, z=z, load=False, puede_editar=p, titulo='Registro de Distritos')


@app.route('/zonasr', methods=['POST'])
@login_required
def zonasr():
    z = zo.Zonas(cxms)
    fa = request.form['factual'][:-7]
    idloc = request.form['idloc']
    print(fa)
    print(request.form['fingreso'][:-7])

    nextidzona = z.get_next_zona(request.form['idloc'])
    ultimodist = z.get_ultimodist(request.form['idloc'])
    z.add_zona(request.form['idloc'], nextidzona, request.form['nomzona'], \
               ultimodist, request.form['fingreso'][:-7], fa, request.form['usuario'])

    if idloc:
        return jsonify({'name' : 'Registros grabados !!! CORRECTAMENTE !!!'})

    return jsonify({'error' : 'Error al Grabar Datos!'})


@app.route('/zonasre', methods=['GET', 'POST'])
@login_required
def zonasre():
    z = zo.Zonas(cxms)
    ban = 0
    error = None
    p = ('Recintos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        if request.form.get('idlocreci1') == None:
            idloc = request.form.get('idlocreci1', 0)
        else:
            idloc = request.form['idlocreci1']
        if request.form.get('nrodist1') == None:
            nrodist = request.form.get('nrodist1', 0)
        else:
            nrodist = request.form['nrodist1']
        if ban != 0:
            print('Otra Cosa')
        else:
            return render_template('zona.html', error=error, z=z, load=False, puede_editar=p, titulo='Registro de Distritos', idloc=idloc, nrodist=nrodist)


@app.route('/asientoz', methods=['GET', 'POST'])
def asientoz():
    azona = request.args.get('azona', 0, type=int)

    z = zo.Zonas(cxms)
    if z.asientoz(azona):
        return jsonify(nomasi=z.nomloc)
    else:
        return jsonify(nomasi='NO EXISTE ASIENTO')

#========== Final Modulo Zonas y Distritos ============#

#========== Modulo Recintos Casos Especiales ============#

@app.route('/reciespeciales_list', methods=['GET', 'POST'])
@login_required
def reciespeciales_list():
    rces = recies.Reciespeciales(cxms)
    rows = rces.get_reciespeciales_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('reciespeciales_list.html', reciespeciales=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos...')


@app.route('/reciespeciales/<idreci>/<idlocreci>', methods=['GET', 'POST'])
@login_required
def reciespeciales(idreci, idlocreci):
    rces = recies.Reciespeciales(cxms)
    rca = recia.Reciasiento(cxms)
    z = zo.Zonas(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Recintos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        """Valida si el campo docActF esta desactivado"""
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']
        """Valida si el campo ruereci esta desactivado"""
        if request.form.get('ruereci') == None:
            ruereci = 0
        else:
            ruereci = request.form['ruereci']
        """Valida si el campo edireci esta desactivado"""
        if request.form.get('edireci') == None:
            edireci = 0
        else:
            edireci = request.form['edireci']
        """Valida si el campo depenreci esta desactivado"""
        if request.form.get('depenreci') == None:
            depenreci = 0
        else:
            depenreci = request.form['depenreci']

        if idreci == '0':  # es NEW
            if False:   # valida si neces POST
                #error = "El usuario: " + request.form['uname']  + " ya existe...!"
                #return render_template('asiento.html', error=error, u=u, load_u=True)
                print('msg-err')
            else:
                nextid = rces.get_next_reciespecial()
                idlocreci = request.form['asiento'].split(':')
                rces.add_recinto(idlocreci[1], nextid, request.form['nomreci'], request.form['zonareci'], \
                               request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                               request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                               ruereci, edireci, request. depenreci, \
                               request.form['pisosreci'], request.form['fechaIngreso'][:-7], fa, \
                               request.form['usuario'], request.form['etapa'], request.form['docAct'], docActF)

                rows = rces.get_reciespeciales_all(usrdep)
                return render_template('reciespeciales_list.html', reciespeciales=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            idlocreci = request.form['asiento'].split(':')
            rces.upd_recinto(idlocreci[1], idreci, request.form['nomreci'], request.form['zonareci'], \
                               request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                               request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                               ruereci, edireci, depenreci, \
                               request.form['pisosreci'], request.form['fechaIngreso'], fa, \
                               usr, request.form['etapa'], request.form['docAct'], docActF)

            rows = rces.get_reciespeciales_all(usrdep)
            return render_template('reciespeciales_list.html', reciespeciales=rows, puede_adicionar='Recintos - Adición' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if idreci != '0':  # EDIT
            if rces.get_recinto_idreciespecial(idreci, idlocreci) == True:
                """if a.docAct == None:
                    a.docAct = """
                if rces.fechaIngreso == None:
                    rces.fechaIngreso = str(datetime.datetime.now())[:-7]
                if rces.fechaAct == None:
                    rces.fechaAct = str(datetime.datetime.now())[:-7]
                if rces.usuario == None:
                    rces.usuario = usr

                return render_template('reciespeciales.html', error=error, rces=rces, load=True, puede_editar=p, asientoRecis=rca.get_asientos_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rces.get_estados(), trecintos=rces.get_tiporecintos(), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep), tpdfsA=d.get_tipo_documentos_pdfA(usrdep),
                                       dptos=rces.get_depaespeciales_all(usrdep), provincias=rces.get_provespeciales_all(usrdep), municipios=rces.get_muniespeciales_all(usrdep))

    # New
    return render_template('reciespeciales.html', error=error, rces=rces, load=False, puede_editar=p, tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep), dptos=rces.get_depaespeciales_all(usrdep),
                            provincias=rces.get_provespeciales_all(usrdep), municipios=rces.get_muniespeciales_all(usrdep), estados=rces.get_estados(), trecintos=rces.get_tiporecintos(),
                            tpdfsA=d.get_tipo_documentos_pdfA(usrdep))

@app.route('/get_provespeciales_all', methods=['GET', 'POST'])
def get_provespeciales_all():
    cxms2 = dbcn.get_db_ms()
    rces = recies.Reciespeciales(cxm2)
    rows = rces.get_provespeciales_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_provespeciales_all1', methods=['GET', 'POST'])
def get_provespeciales_all1():
    dep = request.args.get('dep')
    cxms2 = dbcn.get_db_ms()
    rces = recies.Reciespeciales(cxms2)
    rows = rces.get_provespeciales_all1(dep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_muniespeciales_all', methods=['GET', 'POST'])
def get_muniespeciales_all():
    cxms2 = dbcn.get_db_ms()
    rces = recies.Reciespeciales(cxms2)
    rows = rces.get_muniespeciales_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='COORDENADA',
                       provincia='INCORRECTA !!!',
                       municipio='INTENTE NUEVAMENTE....')


@app.route('/get_muniespeciales_all1', methods=['GET', 'POST'])
def get_muniespeciales_all1():
    dep = request.args.get('dep')
    prov = request.args.get('prov')
    cxms2 = dbcn.get_db_ms()
    rces = recies.Reciespeciales(cxms2)
    rows = rces.get_muniespeciales_all1(dep, prov)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='COORDENADA',
                       provincia='INCORRECTA !!!',
                       municipio='INTENTE NUEVAMENTE....')

#========== Final Modulo Recintos Casos Especiales ============#

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

@app.route('/secret')
@login_required
def secret():
    return ('DEBERIA check only auths..')


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():

    #user = current_user
    #user.authenticated = False
    #db.session.add(user)
    #db.session.commit()
    logout_user()
    return render_template('/logout.html')  # render a template


@app.route('/asiento_ind/<idloc>/<string:nomloc>', methods=['GET', 'POST'])
@login_required
def asiento_ind(idloc, nomloc):
    """
    Modulo Indicadores Socio Econimicos
    """
    # conexiones a las tablas
    ind_cat = indcate.Indcate(cxms)
    ind_subcate = indsubcate.Indsubcate(cxms)
    lc = loc_cate.LocCate(cxms)

    with_cate = lc.get_loc_cates(idloc) # False or rows-img

    error = None
    print(request.method + ' TIPO')
    if request.method == 'POST':
        fa = str(datetime.datetime.now())[:-7]
        cat_ids_ = request.form.getlist('imgsa[]')  # options CATEGORIAS for Asiento
        cat_ids = list(cat_ids_[0].split(","))      # list ok

        # EN PANTALLA PARA NUEVO, SI NO HAY INDICADOR CREADO => SE SALE A LA LISTA DE ASIENTOS
        print('EXISTE REGISTRO ' + cat_ids[0])
        print(with_cate)

        if len(with_cate) :
            if  with_cate[0] != '' and cat_ids[0] == '':
                lc.del_loc_cate(with_cate[0])
                return redirect(url_for('asientos_list'))

        if cat_ids[0] == '':
            return redirect(url_for('asientos_list'))
        else:
            categ_ids = [int(x) for x in cat_ids]
        subcat_ids_ = request.form.getlist('filesa[]')  # options SUBCATEGORIAS for Asiento
        subcat_ids = list(subcat_ids_[0].split(","))      # list ok
        subcateg_ids = [int(x) for x in subcat_ids]    # lista con ids de subcategorias

        ind_obs_ = request.form.getlist('filesv[]')  # options Observaciones for Asiento
        ind_obs = list(ind_obs_[0].split(","))      # list ok  observaciones

        # DE LA CONSULTA CON idloc, si hay registros OBTENIDOS  => actualizar
        if with_cate:
            # verifica si todos loa elementos a ACTUALIZAR son distinos
            lc.del_loc_cate(idloc)
            for n in range(len(cat_ids)):
                # Graba
                lc.add_loc_cate(idloc, cat_ids[n], subcateg_ids[n], ind_obs[n], \
                fa, \
                usr, \
                fa)


        # DE LA CONSULTA CON idloc, si NO hay registros  => CREAR NEW para 'loc_cate'
        else:
            #INSERTANDO NEW DATOS
            # verifica si todos loa elementos a INSERTAR son distinos
            if(len(categ_ids) == len(set(categ_ids))):
                for n in range(len(cat_ids)):
                    #print(f'{idloc}, {cat_ids[n]}, {subcateg_ids[n]}')
                    #GUARDANDO DATOS
                    lc.add_loc_cate(idloc, cat_ids[n], subcateg_ids[n], ind_obs[n], \
                        fa, \
                        usr, \
                        fa)

            else:
                #GRABA
                for n in range(len(cat_ids)):
                    #print(f'{idloc}, {cat_ids[n]}, {subcateg_ids[n]}')
                    #GUARDANDO DATOS
                    lc.add_loc_cate(idloc, cat_ids[n], subcateg_ids[n], ind_obs[n], \
                        fa, \
                        usr, \
                        fa)

        return redirect(url_for('asientos_list'))

    else:
        if with_cate:  # Edit  ENTRA LA 1RA VEZ  POR Lista Asientos[Indice]
            #CREANDO UNA NEW ESTRUCTURA PARA DATOS REPETIDOS
            lista_with_cate = []
            nroReg = 0
            for n in with_cate:
                nroReg = nroReg + 1
                n = list(n)
                n.insert(0, nroReg)
                n = tuple(n)
                lista_with_cate.append(n)
            #print(with_cate)
            return render_template('asiento_ind_upd.html', rows=ind_cat.get_cate('admin'),subcat=ind_subcate.get_subcate_all('admin'), nomloc=nomloc,
                                puede_editar='Asientos - Edición' in permisos_usr,
                                loc_cate_loaded = with_cate, lista_with_cate=lista_with_cate)
        else:  # New  with_cate = False
            return render_template('asiento_ind.html', rows=ind_cat.get_cate('admin'),subcat=ind_subcate.get_subcate_all('admin'), nomloc=nomloc,
                                puede_editar='Asientos - Edición' in permisos_usr)

@app.route('/paises_list', methods=['GET', 'POST'])
@login_required
def paises_list():
    s = paises.Pais(cxms)
    rows = s.get_paises_all(usrdep)

    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('paises_list.html', paises=rows, puede_adicionar='Paises - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin paises...')

@app.route('/paisesABC/<pais_id>', methods=['GET', 'POST'])
@login_required
def paisesABC(pais_id):

    s = paises.Pais(cxms)
    error = None

    p = ('Paises - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = str(datetime.datetime.now())[:-7]
        if pais_id == '0':  # es NEW
            if False:   # valida si neces POST
                print('msg-err')
            else:
                nextid = s.get_next_idpais()
                s.add_pais(nextid, request.form['Pais'], request.form['NomPais'], request.form['Nal'], request.form['Estado'],
                           request.form['codInter'], request.form['codInterISO3166'], str(request.form['fecharegistro'])[:-8],
                           fa, usr)

                rows = s.get_paises_all(usrdep)
                return render_template('paises_list.html', paises=rows, puede_adicionar='Paises - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            s.upd_pais(pais_id, request.form['Pais'], request.form['NomPais'], request.form['Nal'], request.form['Estado'],
                       request.form['codInter'], request.form['codInterISO3166'], str(request.form['fecharegistro'])[:-7],
                       fa, usr)

            rows = s.get_paises_all(usrdep)
            return render_template('paises_list.html', paises=rows, puede_editar='Paises - Edicion' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if pais_id != '0':  # EDIT
            if s.get_pais_idpais(pais_id) == True:
                if s.fechaactual == None:
                    s.fechaactual = str(datetime.datetime.now())[:-7]
                if s.usuario == None:
                    s.usuario = usr

                return render_template('paisesABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de Pais',puede_editar=p)

    # New
    return render_template('paisesABC.html', error=error, s=s, load=False, titulo='Registro de Nuevo Pais', puede_editar=p)

@app.route('/deptos_list', methods=['GET', 'POST'])
@login_required
def deptos_list():
    s = deptoss.Departamento(cxms)
    rows = s.get_deptos_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('deptos_list.html', deptos=rows, puede_adicionar='Departamentos - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin Departamentos...')

@app.route('/deptosABC/<dep_id>', methods=['GET', 'POST'])
@login_required
def deptosABC(dep_id):
    s = deptoss.Departamento(cxms)
    error = None
    p = ('Departamentos - Edición' in permisos_usr)  # t/f
    if request.method == 'POST':
        fa = str(datetime.datetime.now())[:-7]
        if dep_id == '0':  # es NEW
            if False:   # valida si neces POST
                print('msg-err')
            else:
                nextid = s.get_next_iddep()
                s.add_depto(nextid, request.form['nomDep'], request.form['diputados'], request.form['diputadosUninominales'], request.form['pais'], request.form['descNivelId'],
                           str(request.form['fechaIngreso'])[:-8],
                           fa, usr)

                rows = s.get_deptos_all(usrdep)
                return render_template('deptos_list.html', deptos=rows, puede_adicionar='Departamentos - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            s.upd_depto(dep_id, request.form['nomDep'], request.form['diputados'], request.form['diputadosUninominales'], request.form['pais'], request.form['descNivelId'], fa, usr)
            rows = s.get_deptos_all(usrdep)
            return render_template('deptos_list.html', deptos=rows, puede_editar='Departamentos - Edicion' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if dep_id != '0':  # EDIT
            if s.get_depto_iddep(dep_id) == True:
                if s.fechaAct == None:
                    s.fechaAct = str(datetime.datetime.now())[:-7]
                if s.usuario == None:
                    s.usuario = usr
                return render_template('deptosABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de Departamentos', tpaises=s.get_combo_paises(usrdep), tdescNivel=s.get_combo_descNivel(usrdep),puede_editar=p)
    # New
    return render_template('deptosABC.html', error=error, s=s, load=False, titulo='Registro de Nuevo Departamento', tpaises=s.get_combo_paises(usrdep), tdescNivel=s.get_combo_descNivel(usrdep), puede_editar=p)

@app.route('/provs_list', methods=['GET', 'POST'])
@login_required
def provs_list():
    s = provs.Prov(cxms)
    rows = s.get_provs_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('provs_list.html', listaProvincias=rows, puede_adicionar='Provincias - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin provincias...')

@app.route('/provsABC/<dep_id>/<prov_id>', methods=['GET', 'POST'])
@login_required
def provsABC(dep_id, prov_id):
    s = provs.Prov(cxms)
    error = None
    p = ('Provincias - Edición' in permisos_usr)  # t/f
    if request.method == 'POST':
        fa = str(datetime.datetime.now())[:-7]
        if dep_id == '0' and prov_id == '0':  # es NEW
            if False:   # valida si neces POST
                print('msg-err')
            else:
                nextid = s.get_next_idprov(request.form['depto'])
                if nextid == None:
                    nextid =1

                s.add_prov(request.form['depto'], nextid, request.form['NomProv'], request.form['codprov'], request.form['descNivelId'],
                           str(request.form['fechaIngreso'])[:-8],
                           fa, usr)

                rows = s.get_provs_all(usrdep)
                return render_template('provs_list.html', listaProvincias=rows, puede_adicionar='Provincias - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            s.upd_prov(dep_id, prov_id, request.form['NomProv'], request.form['codprov'], request.form['descNivelId'],fa, usr)
            rows = s.get_provs_all(usrdep)
            return render_template('provs_list.html', listaProvincias=rows, puede_editar='Prov incias - Edicion' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if dep_id != '0' and prov_id != '0':  # EDIT
            if s.get_provs_id(dep_id, prov_id) == True:
                if s.fechaAct == None:
                    s.fechaAct = str(datetime.datetime.now())[:-7]
                if s.usuario == None:
                    s.usuario = usr

                return render_template('provsABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de Provincias', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tdescNivel=s.get_combo_descNivel(usrdep), puede_editar=p)
    # New
    return render_template('provsABC.html', error=error, s=s, load=False, titulo='Registro de Nueva Provincia', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tdescNivel=s.get_combo_descNivel(usrdep), puede_editar=p)

@app.route('/get_departamentos_all', methods=['GET', 'POST'])
def get_departamentos_all():
    s = rep.Reportes(cxms)
    cxms2 = dbcn.get_db_ms()
    rows = s.get_departamentos_all(usrdep)

    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='NO',
                       provincia='EXISTE !!!',
                       municipio='DEPARTAMENTO....')
    cxms2.close()


@app.route('/mun_list', methods=['GET', 'POST'])
@login_required
def mun_list():
    s = muns.Municipio(cxms)
    rows = s.get_mun_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('mun_list.html', municipios=rows, puede_adicionar='Municipios - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin provincias...')

@app.route('/munABC/<dep_id>/<prov_id>/<mun_id>', methods=['GET', 'POST'])
@login_required
def munABC(dep_id, prov_id, mun_id):
    s = muns.Municipio(cxms)
    error = None
    p = ('Municipios - Edición' in permisos_usr)  # t/f
    if request.method == 'POST':
        fa = str(datetime.datetime.now())[:-7]
        if dep_id == '0' and prov_id == '0' and mun_id == '0':  # es NEW

            nextid = s.get_next_idmun(request.form['depto'], request.form['prov'])
            if nextid == None:
                nextid =1

            s.add_mun(request.form['depto'], request.form['prov'], nextid, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'],
            str(request.form['fechaIngreso'])[:-8], fa, usr)

            rows = s.get_mun_all(usrdep)
            return render_template('mun_list.html', municipios=rows, puede_adicionar='Municipios - Adición' in permisos_usr)  # render a template
        else: # Es Edit
            s.upd_mun(dep_id, prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'],
                    fa, usr)
            rows = s.get_mun_all(usrdep)
            return render_template('mun_list.html', municipios=rows, puede_editar='Municipios - Edicion' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if dep_id != '0' and prov_id != '0' and mun_id != '0': # EDIT
            if s.get_mun_id(dep_id, prov_id, mun_id) == True:
                if s.fechaAct == None:
                    s.fechaAct = str(datetime.datetime.now())[:-7]
                if s.usuario == None:
                    s.usuario = usr
                return render_template('munABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de Municipios', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tprovs=s.get_combo_prov(dep_id,prov_id), tdescNivel=s.get_combo_descNivel(usrdep), puede_editar=p)
    # New
    return render_template('munABC.html', error=error, s=s, load=False, titulo='Registro de Nuevo Municipio', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tprovs=s.get_combo_prov_new(usrdep), tdescNivel=s.get_combo_descNivel(usrdep), puede_adicionar=p)


@app.route('/bitacora_list', methods=['GET', 'POST'])
@login_required
def bitacora_list():
    """ Modulo log de Transacciones """
    s = bitacoras.Bitacora(cxms)
    rows = s.get_bitacora_all(usrdep)

    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('bitacora_list.html', bitacoras=rows, puede_adicionar='Bitacoras - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin bitacora...')


@app.route('/clas_grupo_list', methods=['GET', 'POST'])
@login_required
def clas_grupo_list():
    s = clas_grupo.Grupo(cxms)
    rows = s.get_clas_grupos_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('clas_grupo_list.html', clas_grup=rows, puede_adicionar='Grupo - Adición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin Grupos...')

@app.route('/clas_grupo_ABC/<grupo_id>', methods=['GET', 'POST'])
@login_required
def clas_grupo_ABC(grupo_id):
    s = clas_grupo.Grupo(cxms)
    error = None
    p = ('clas_grupo - Edición' in permisos_usr)  # t/f
    print(request.method)
    if request.method == 'POST':
        if grupo_id == '0':  # es NEW
            if False:   # valida si neces POST
                print('msg-err')
            else:
                nextid = s.get_next_idgrupo()
                s.add_clas_grupo(nextid, request.form['descripcion'])

                rows = s.get_clas_grupos_all(usrdep)
                print('GRUPO ADICION')
                return redirect(url_for('clas_grupo_list'))
        else: # Es Edit
            s.upd_grupo(grupo_id, request.form['descripcion'])
            rows = s.get_clas_grupos_all(usrdep)
            return render_template('clas_grupo_list.html', clas_grup=rows, puede_editar='Grupo - Edicion' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if grupo_id != '0':  # EDIT
            if s.get_clas_grupo_idclasGrup(grupo_id) == True:
                return render_template('clas_grupo_ABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de grupos', puede_editar=p)
    # New
    return render_template('clas_grupo_ABC.html', error=error, s=s, load=False, titulo='Registro de Nuevo grupo', puede_editar=p)


@app.route('/clas_list/<grupo_id>', methods=['GET', 'POST'])
@login_required
def clas_list(grupo_id):
    s = clasificadores.Clasificador(cxms)
    if grupo_id != '0':  # EDIT
            if s.get_clas_idclas(grupo_id) != False:
                rows = s.get_clas_idclas(grupo_id)
                if not rows:
                    return render_template('clas_new.html', grupo_id=grupo_id)  # render a template
                else:
                    if permisos_usr:    # tiene pemisos asignados
                        return render_template('clas_list.html', clasificadores=rows, puede_adicionar='Clasificador - Edición' in permisos_usr)  # render a template
                    else:
                        print('sin permisos')
                        return render_template('msg.html', l1='Sin permisos asignados !!')


@app.route('/clas_new/<grupo_id>', methods=['GET', 'POST'])
@login_required
def clas_new(grupo_id):
    s = clasificadores.Clasificador(cxms)
    if grupo_id != '0':  # EDIT
            if s.get_clas_idclas(grupo_id) != False:
                rows = s.get_clas_idclas(grupo_id)
    else:
        print('Nuevo...')


@app.route('/clas_ABC/<clas_id>/<clas_grup_id>', methods=['GET', 'POST'])
@login_required
def clas_ABC(clas_id,clas_grup_id):
    s = clasificadores.Clasificador(cxms)
    error = None
    p = ('clasificadores - Edición' in permisos_usr)  # t/f
    print(request.method)
    if request.method == 'POST':
        if clas_id == '0':  # es NEW
            if False:   # valida si neces POST
                print('msg-err')
            else:
                nextid = s.get_next_idclas()
                s.add_clas(nextid, request.form['descripcion'], clas_grup_id,request.form['subgrupo'])
                rows = s.get_clas_idclas(clas_grup_id)
                return render_template('clas_list.html', clasificadores=rows, puede_adicionar='Clasificador - Adición' in permisos_usr)  # render a template

        else: # Es Edit
            s.upd_clas(clas_id, request.form['descripcion'],request.form['subgrupo'])
            rows = s.get_clas_idclas(request.form['grupo'])
            return render_template('clas_list.html', clasificadores=rows, puede_editar='Clasificador - Edicion' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if clas_id != '0':  # EDIT
            if s.get_clas_id(clas_id) == True:
                return render_template('clas_ABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de clasificadores', puede_editar=p)
    # New
    return render_template('clas_ABC.html', error=error, s=s, load=False, titulo='Registro de Nuevo clasificador', puede_editar=p)

@app.route('/recinto_img/<idloc>/<string:nomloc>/<idreci>', methods=['GET', 'POST'])
@login_required
def recinto_img(idloc, nomloc, idreci):

    i = clasif_get.ClasifGet(cxms)  # conecta a la BD
    li = reci_img.ReciImg(cxms)

    with_img = li.get_reci_imgs(idloc)  # False or rows-img

    error = None

    if request.method == 'POST':
        img_ids_ = request.form.getlist('imgsa[]')  # options img for Asiento
        img_ids = list(img_ids_[0].split(","))      # list ok
        uploaded_files = request.files.getlist("filelist")

        for n in range(len(img_ids)):
            f  = uploaded_files[n]
            if f.filename != '':
                securef = secure_filename(f.filename)
                f.save(os.path.join('.' + app.config['IMG_RECINTOS'], securef))
                fpath = os.path.join(app.config['IMG_RECINTOS'], securef)
                arch, ext = os.path.splitext(fpath)
                name_to_save = str(idloc).zfill(5) + "_" + str(idreci).zfill(5) + "_" + str(img_ids[n]).zfill(3)  + ext
                fpath_destino = os.path.join(app.config['IMG_RECINTOS'], name_to_save)

                #resize_save_file(fpath, name_to_save, (1024, 768), os.path.join(app.config['IMG_RECINTOS']))
                resize_save_file(fpath, name_to_save, (1024, 768))

                li.add_reci_img(idloc, img_ids[n], idreci, fpath_destino, datetime.datetime.now(), usr)
                os.remove(fpath[1:])   # arch. fuente

        return redirect(url_for('recintos_list'))

    else:
        if with_img:  # Edit
            return render_template('recinto_img_upd.html', rows=i.get_descripcion(5), nomloc=nomloc,
                                puede_editar='Recintos - Edición' in permisos_usr,
                                imgs_loaded=with_img)
        else:  # New
            return render_template('recinto_img.html', rows=i.get_descripcion(5), nomloc=nomloc,
                                puede_editar='Recintos - Edición' in permisos_usr)

#def resize_save_file(in_file, out_file, size, ruta_img):
def resize_save_file(in_file, out_file, size):
    with open('.' + in_file, 'rb') as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)

    #image.save('.' + ruta_img, out_file)
    #image.save('.' + os.path.join(app.config['IMG_RECINTOS'], out_file))
    image.save('.' + os.path.join(app.config['IMG_ASIENTOS'], out_file))
    image.close()
    #return(out_file)



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

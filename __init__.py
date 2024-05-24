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
import asiexcep as asiex
import reportes as rep
import gerencial as ger
import documentos as docu
import documentos_pdf as dpdf
import distritos as dist
import distritos as distr
import exterior as ext
import exteriorreci as extr
import recintos
import reciespe as recie
import reciespeciales as recies
import reciasiento as recia
import geo as geo
import sincro as sin
import img
import loc_img
import reci_img
import homologa as hom
import homologacion as homo
import homologacionPDF as hpdf
import jurisdiccion as jur
import jurisd_asi as jua
import tipodocs as tdoc
import zon as zon

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


# Create the application object
app = Flask(__name__)

app.secret_key ='\xfd{H\xe7<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa7'
app.config['LOGIN_DISABLED'] = False
app.config['PATH_APP'] = '/var/www/flasks/age/'
app.config['IMG_ASIENTOS'] = '/static/imgbd/asi'
app.config['IMG_RECINTOS'] = '/static/imgbd/reci'
app.config['SUBIR_PDF'] = '/static/pdfdoc'
#app.config['REPORTE_PDF'] = 'file:///var/www/flasks/age/reporteh.pdf'
#app.config['MODULO_REPORTES'] = 'file:///var/www/flasks/age/reporte.pdf'
app.config['HELP_DOC'] = 'static/helpdoc/_build/html/index.html'
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
usrtipo = 0
usrauth = 0

# path init - to save img, ..
chd = os.chdir(app.config['PATH_APP'])

# flag para homologaciones excep
hom_excep = False

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
    global usrtipo
    global usrauth
    user = usuarios.Usuarios(cxms)
    if user.get_usuario(txtusr):
        usr = user.usuario
        usrdep = user.dep
        usrid = user.id
        usrtipo = user.tipo_usr
        usrauth = user.authenticated
        permisos_usr = user.get_permisos_name(usr)
        print(permisos_usr) #ppp
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
    return dict(idate=datetime.date.today(), idatetime=str(datetime.datetime.now())[0:-3], anio=str(datetime.date.today())[0:-6], usuario=usr, usrdep=usrdep, usrid=usrid, usrtipo=usrtipo, usrauth=usrauth)


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
                       municipio=g.municipio,
                       nrocircun=g.nrocircun)
    else:
        return jsonify(dep='---',
                       departamento='COORDENADA',
                       prov='---',
                       provincia='INCORRECTA !!!',
                       sec='---',
                       municipio='INTENTE NUEVAMENTE....')


@app.route('/get_json_ptos', methods=['GET', 'POST'])
def get_json_ptos():
    lat = request.args.get('latitud', 0, type=float)
    long = request.args.get('longitud', 0, type=float)

    j = get_json.GetJson(cxpg)    
    gj_ptos = j.get_reci_mts(lat, long, 650)
    print(gj_ptos)
    return {'gj_ptos' : gj_ptos}


@app.route('/vs/<dep>', methods=['GET', 'POST'])
def vs(dep):
    j = get_json.GetJson(cxpg)

    dep=int(dep)
    #geo_json = j.get_loc(dep)
    return render_template('vs.html', 
                            gj_reci=j.get_reci(dep),
                            gj_asi=j.get_asi(dep), 
                            gj_cir=j.get_cir(dep),
                            gj_mun=j.get_mun(dep),
                            gj_prov=j.get_prov(dep))


@app.route('/ftwms/', methods=['GET', 'POST'])
def ftwms():
    return render_template('twms.html') 


@app.route('/ftwms2/', methods=['GET', 'POST'])
def ftwms2():
    return render_template('twms2.html') 


@app.route('/ftwms3/', methods=['GET', 'POST'])
def ftwms3():
    return render_template('twms3.html') 



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
        if request.form.get('tusr') == None:
            tusr = request.form['tusr1']
        else:
            tusr = request.form['tusr']

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
                            1, tusr)
                return render_template('welcome.html')
        else: # es EDIT
            u.upd_usuario(usuario_id, \
                            request.form['nombre'], \
                            request.form['apellidos'], \
                            request.form['email'], \
                            request.form['dep'], \
                            1, tusr)
            if usr == 'admin':
                return render_template('usuarios.html', usuarios=u.get_usuarios())
            return render_template('home.html')

    else: # viene de listado USUARIOS
        if usuario_id != 0:  # EDIT
            if u.get_usuario_id(usuario_id) == True:
                return render_template('registro.html', error=error, u=u, load_u=True, t_usuarios=u.get_tipo_usuario())

    return render_template('registro.html', error=error, u=u, load_u=False, t_usuarios=u.get_tipo_usuario())


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
    ''' Gestiona imágenes del asiento '''

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
                fpath = os.path.join(app.config['IMG_ASIENTOS'], securef)
                arch, ext = os.path.splitext(fpath)
                name_to_save = str(idloc).zfill(5) + "_" + str(img_ids[n]).zfill(2) + ext
                fpath_destino = os.path.join(app.config['IMG_ASIENTOS'], name_to_save)   # loc_img.ruta

                if li.exist_img(idloc, img_ids[n]):   # si upd img
                    file_to_del = li.get_name_file_img(idloc, img_ids[n]) # referencia en bd 
                    os.remove(file_to_del[1:]) # borra arch. de HD
                    li.upd_loc_img(idloc, img_ids[n], fpath_destino, datetime.datetime.now(), usr) # upd de bd
                else: # new
                    li.add_loc_img(idloc, img_ids[n], fpath_destino, datetime.datetime.now(), usr)

                f.save(os.path.join('.' + app.config['IMG_ASIENTOS'], securef))
                resize_save_file(fpath, name_to_save, (1024, 768))

                os.remove(fpath[1:])   # arch. fuente 

        return redirect(url_for('asientos_list'))
    else:
        if with_img:  # Edit
            return render_template('asiento_img_upd.html', rows=i.get_imgs(), nomloc=nomloc,
                                puede_editar='Asientos - Edición' in permisos_usr,
                                imgs_loaded=with_img)
        else:  # New
            return render_template('asiento_img.html', rows=i.get_imgs(), nomloc=nomloc,
                                puede_editar='Asientos - Edición' in permisos_usr)


@app.route('/asi_excep_img/<idloc>/<string:nomloc>', methods=['GET', 'POST'])
@login_required
def asi_excep_img(idloc, nomloc):
    ''' Gestiona imágenes del asiento '''

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
                fpath = os.path.join(app.config['IMG_ASIENTOS'], securef)
                arch, ext = os.path.splitext(fpath)
                name_to_save = str(idloc).zfill(5) + "_" + str(img_ids[n]).zfill(2) + ext
                fpath_destino = os.path.join(app.config['IMG_ASIENTOS'], name_to_save)   # loc_img.ruta

                if li.exist_img(idloc, img_ids[n]):   # si upd img
                    file_to_del = li.get_name_file_img(idloc, img_ids[n]) # referencia en bd 
                    os.remove(file_to_del[1:]) # borra arch. de HD
                    li.upd_loc_img(idloc, img_ids[n], fpath_destino, datetime.datetime.now(), usr) # upd de bd
                else: # new
                    li.add_loc_img(idloc, img_ids[n], fpath_destino, datetime.datetime.now(), usr)

                f.save(os.path.join('.' + app.config['IMG_ASIENTOS'], securef))
                resize_save_file(fpath, name_to_save, (1024, 768))

                os.remove(fpath[1:])   # arch. fuente 

        return redirect(url_for('asi_excep_list'))
    else:
        if with_img:  # Edit
            return render_template('asiexcep_img_upd.html', rows=i.get_imgs(), nomloc=nomloc,
                                puede_editar='Asiexcep - Edición' in permisos_usr,
                                imgs_loaded=with_img)
        else:  # New
            return render_template('asiexcep_img.html', rows=i.get_imgs(), nomloc=nomloc,
                                puede_editar='Asiexcep - Edición' in permisos_usr)


@app.route('/documentos_list', methods=['GET', 'POST'])
@login_required
def documentos_list():
    d = docu.Documentos(cxms)
    rows = d.get_documentos_all(usrdep)
    if rows:
        if 'Documentos - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('documentos_list.html', documentos=rows, puede_adicionar='Documentos - Adición' in permisos_usr, \
                                    puede_editar='Documentos - Edición' in permisos_usr, \
                                    puede_eliminar='Documentos - Eliminación' in permisos_usr
                                  )  # render a template
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
                #flash('Debe cargar solo archivos PDFs')
                return render_template('documento.html', error=error, d=d, load_d=False, titulo='Registro de Documentos', tdocumentos=tdocu.get_tipo_documentos(usrdep))
            
            if d.get_cite(request.form['cite']):
                d.add_documento(request.form['doc'], \
                            request.form['dep'], \
                            request.form['cite'], \
                            ruta, \
                            request.form['fechadoc'], \
                            request.form['obs'], \
                            request.form['fecharegistro'], \
                            request.form['usuario'], \
                            request.form['fechaingreso'])

            return render_template('documentos_list.html', documentos=d.get_documentos_all(usrdep),  puede_adicionar='Documentos - Adición' in permisos_usr, \
                                    puede_editar='Documentos - Edición' in permisos_usr, \
                                    puede_eliminar='Documentos - Eliminación' in permisos_usr
                                  )  # render a template
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

            row_to_upd = \
                doc_id, \
                request.form['doc'], \
                request.form['dep'], \
                request.form['cite'], \
                request.form['fechadoc'], \
                request.form['obs'], \
                request.form['usuario']

            fa = str(datetime.datetime.now())[:-7]
            if f.filename != '':
                d.upd_documento(doc_id, \
                            request.form['doc'], \
                            request.form['dep'], \
                            request.form['cite'], \
                            ruta, \
                            request.form['fechadoc'], \
                            request.form['obs'], \
                            request.form['usuario'], \
                            fa)
            else:
                if d.diff_old_new_doc(row_to_upd):
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
                return render_template('documentos_list.html', documentos=d.get_documentos(),  puede_adicionar='Documentos - Adición' in permisos_usr, \
                                        puede_editar='Documentos - Edición' in permisos_usr, \
                                        puede_eliminar='Documentos - Eliminación' in permisos_usr
                                      )  # render a template
            return render_template('documentos_list.html', documentos=d.get_documentos_all(usrdep),  puede_adicionar='Documentos - Adición' in permisos_usr, \
                                    puede_editar='Documentos - Edición' in permisos_usr, \
                                    puede_eliminar='Documentos - Eliminación' in permisos_usr
                                  )  # render a template

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


@app.route('/asientos_list', methods=['GET', 'POST'])
@login_required
def asientos_list():
    a = asi.Asientos(cxms)
    rows = a.get_loc_all(usrdep)
    if rows:
        if 'Asientos - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('asientos_list.html', asientos=rows, puede_adicionar='Asientos - Adición' in permisos_usr, \
                                    puede_editar='Asientos - Edición' in permisos_usr, \
                                    puede_eliminar='Asientos - Eliminación' in permisos_usr, \
                                    puede_consultar='Asientos - Consulta' in permisos_usr
                                  )# render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin asientos...')


@app.route('/asiento/<idloc>', methods=['GET', 'POST'])
@login_required
def asiento(idloc):
    '''
    Adición/Edición de asientos
    '''
    a = asi.Asientos(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Asientos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]

        if usrdep != 0: 
            if request.form.get('docRspNal') != None:
                docRspNal = request.form['docRspNal']
            else:
                docRspNal = 0

            if request.form.get('docRspNalT') != None:
                docRspNalT = request.form['docRspNalT']
            else:
                docRspNalT = 0

            if request.form.get('doc_idRspNalT') != None:
                doc_idRspNalT = request.form['doc_idRspNalT']
            else:
                doc_idRspNalT = 0

        if usrdep == 0:
            docRspNal = request.form['docRspNal']
            docRspNalT = request.form['docRspNalT']

        if request.form.get('docActF') == None:
            if request.form.get('doc_idActF') != None:
                docActF = request.form['doc_idActF']    
            else:
                docActF = 0
        else:
            docActF = request.form['docActF']

        if request.form.get('docActT') == None:
            if request.form.get('doc_idActT') != None:
                docActT = request.form['doc_idActT']    
            else:
                docActT = 0
        else:
            docActT = request.form['docActT']

        if request.form.get('docRspNalT') == None:
            if request.form.get('doc_idRspNalT') != None:
                docRspNalT = request.form['doc_idRspNalT']    
            else:
                docRspNalT = 0
        else:
            docRspNalT = request.form['docRspNalT']

        if request.form.get('urural') == None:
            urural = 0
        else:
            urural = request.form['urural']

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
                              request.form['latitud'], request.form['longitud'], request.form['estado'], '', \
                              request.form['etapa'], request.form['obsUbicacion'], request.form['obs'].strip(), \
                              request.form['fechaIngreso'][:-7], fa, request.form['usuario'], request.form['docAct'], docRspNal, \
                              docActF, urural, request.form['docActT'], docRspNalT)

                d.upd_doc(request.form['docAct'], docRspNal, request.form['doc_idAct'], request.form['doc_idRspNal'], docActF, request.form['docActT'], docRspNalT, docActT, docRspNalT)

                rows = a.get_loc_all(usrdep)
                return render_template('asientos_list.html', asientos=rows, puede_adicionar='Asientos - Adición' in permisos_usr, \
                                        puede_editar='Asientos - Edición' in permisos_usr, \
                                        puede_eliminar='Asientos - Eliminación' in permisos_usr
                                      ) # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            fcl = request.form['fechacensoloc']
            if fcl == '':
                fcl = None

            row_to_upd = \
                request.form['nomloc'], request.form['poblacionloc'], \
                request.form['poblacionelecloc'], fcl, request.form['tipolocloc'], \
                request.form['latitud'], request.form['longitud'], \
                request.form['estado'], '', request.form['etapa'], \
                request.form['obsUbicacion'], request.form['obs'].strip(), \
                str(request.form['fechaIngreso']), fa, usr, request.form['docAct'], docRspNal, \
                docActF, urural, request.form['docActT'], docRspNalT, idloc

            if usrauth == 3 and a.upd_asi_noauth(row_to_upd):   #tmpauth3 valida act datos no autoriz. show msg si err
                error = "Intenta actualizar datos NO autorizados."
                return render_template('asiento.html', error=error, a=a, load=True, puede_editar=p, estados=a.get_estados(), etapas=a.get_etapas_auth(usrdep, usrtipo), \
                                       tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep)
                                      )
            else:
                a.upd_asiento(row_to_upd)
                d.upd_doc(request.form['docAct'], docRspNal, request.form['doc_idAct'], request.form['doc_idRspNal'], docActF, request.form['docActT'], docRspNalT,  docActT, docRspNalT)

                rows = a.get_loc_all(usrdep)
                return render_template('asientos_list.html', asientos=rows, puede_adicionar='Asientos - Adición' in permisos_usr, \
                                        puede_editar='Asientos - Edición' in permisos_usr, \
                                        puede_eliminar='Asientos - Eliminación' in permisos_usr
                                      ) # render a template
    else: # Viene de <asientos_list>
        if idloc != '0':  # EDIT
            if a.get_asiento_idloc(idloc):
                if a.fechaIngreso == None:
                    a.fechaIngreso = str(datetime.datetime.now())[:-7]
                if a.fechaAct == None:
                    a.fechaAct = str(datetime.datetime.now())[:-7]
                if a.usuario == None:
                    a.usuario = usr

                if usrauth == 3:  #tmpauth3 
                    return render_template('asiento.html', error=error, a=a, load=True, puede_editar=p, estados=a.get_estados(), etapas=a.get_etapas_auth(usrdep, usrtipo), 
                                       tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))
                else:
                    return render_template('asiento.html', error=error, a=a, load=True, puede_editar=p, estados=a.get_estados(), etapas=a.get_etapas(usrtipo), 
                                       tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))
    # New
    return render_template('asiento.html', error=error, a=a, load=False, puede_editar=p, estados=a.get_estados(), etapas=a.get_etapas(usrtipo), 
                           tcircuns=a.get_tipocircun(), tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))


@app.route('/get_mapas_all', methods=['GET', 'POST'])
def get_mapas_all():
    j = get_json.GetJson(cxpg)
    ideploc = request.values.get('ideploc', type=int)
    gj_mun = j.get_mun(ideploc)
    gj_prov = j.get_prov(ideploc)
    gj_cir = j.get_cir(ideploc)
    if gj_mun or gj_prov or gj_cir:
        return jsonify(gj_mun, gj_prov, gj_cir)


@app.route('/asiento_vs/<idloc>', methods=['GET', 'POST'])
@login_required
def asiento_vs(idloc):
    ''' Coordenada en visor '''

    a = asi.Asientos(cxms)
    a.get_asiento_idloc(idloc)    # siempre debiera existir
     
    j = get_json.GetJson(cxpg)

    return render_template('coord_vs.html', 
                            gj_reci=j.get_reci(a.deploc), 
                            gj_asi=j.get_asi(a.deploc), 
                            gj_cir=j.get_cir(a.deploc),
                            gj_mun=j.get_mun(a.deploc),
                            gj_prov=j.get_prov(a.deploc),
                            latitud=a.latitud, 
                            longitud=a.longitud,
                            nombre=a.nomloc
                          )


@app.route('/asiento_vs_ext/<idloc>', methods=['GET', 'POST'])
@login_required
def asiento_vs_ext(idloc):
    ''' Coordenada en visor '''

    a = asi.Asientos(cxms)
    a.get_asiento_idloc(idloc)    # siempre debiera existir
     
    j = get_json.GetJson(cxpg)

    return render_template('coord_vs.html', 
                            gj_reci=j.get_reci(10), 
                            gj_asi=j.get_asi(10),
                            gj_cir=j.get_cir(9),
                            gj_mun=j.get_mun(9),
                            gj_prov=j.get_prov(9), 
                            latitud=a.latitud, 
                            longitud=a.longitud,
                            nombre=a.nomloc
                          )


@app.route('/recinto_vs/<idloc>/<reci>', methods=['GET', 'POST'])
@login_required
def recinto_vs(idloc, reci):
    ''' Coordenada en visor '''

    r = recintos.Recintos(cxms)
    r.get_recinto_idreci(reci, idloc)    # siempre debiera existir
     
    j = get_json.GetJson(cxpg)
    return render_template('coord_vs.html', 
                            gj_reci=j.get_reci(r.deploc), 
                            gj_asi=j.get_asi(r.deploc), 
                            gj_cir=j.get_cir(r.deploc),
                            gj_mun=j.get_mun(r.deploc),
                            gj_prov=j.get_prov(r.deploc),
                            latitud=r.latitud, 
                            longitud=r.longitud,
                            nombre=r.nomreci
                          )


@app.route('/recinto_vs_ext/<idloc>/<reci>', methods=['GET', 'POST'])
@login_required
def recinto_vs_ext(idloc, reci):
    ''' Coordenada en visor '''

    r = recintos.Recintos(cxms)
    r.get_recinto_idreci(reci, idloc)    # siempre debiera existir
     
    j = get_json.GetJson(cxpg)
    return render_template('coord_vs_ext.html', 
                            gj_reci=j.get_reci(10), 
                            gj_asi=j.get_asi(10),
                            gj_cir=j.get_cir(9),
                            gj_mun=j.get_mun(9),
                            gj_prov=j.get_prov(9), 
                            latitud=r.latitud, 
                            longitud=r.longitud,
                            nombre=r.nomreci
                          )


@app.route('/asi_excep_list', methods=['GET', 'POST'])
@login_required
def asi_excep_list():
    ax = asiex.Asi_excep(cxms)
    rows = ax.get_asi_excep_all(usrdep)
    if rows:
        if 'Asiexcep - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('asiexcep_list.html', asientos=rows, puede_adicionar='Asiexcep - Adición' in permisos_usr, \
                                    puede_editar='Asiexcep - Edición' in permisos_usr, \
                                    puede_eliminar='Asiexcep - Eliminación' in permisos_usr
                                  )# render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin asientos...')


@app.route('/asi_excep/<idloc>', methods=['GET', 'POST'])
@login_required
def asi_excep(idloc):
    ''' Casos Excepcionales '''

    ax = asiex.Asi_excep(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Asiexcep - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        if usrdep != 0: 
            if request.form.get('docRspNal') != None:
                docRspNal = request.form['docRspNal']
            else:
                docRspNal = 0

            if request.form.get('docRspNalT') != None:
                docRspNalT = request.form['docRspNalT']
            else:
                docRspNalT = 0

            if request.form.get('doc_idRspNalT') != None:
                doc_idRspNalT = request.form['doc_idRspNalT']
            else:
                doc_idRspNalT = 0

        if usrdep == 0:
            docRspNal = request.form['docRspNal']
            docRspNalT = request.form['docRspNalT']

        if request.form.get('docActF') == None:
            if request.form.get('doc_idActF') != None:
                docActF = request.form['doc_idActF']    
            else:
                docActF = 0
        else:
            docActF = request.form['docActF']

        if request.form.get('docActT') == None:
            if request.form.get('doc_idActT') != None:
                docActT = request.form['doc_idActT']    
            else:
                docActT = 0
        else:
            docActT = request.form['docActT']

        if request.form.get('docRspNalT') == None:
            if request.form.get('doc_idRspNalT') != None:
                docRspNalT = request.form['doc_idRspNalT']    
            else:
                docRspNalT = 0
        else:
            docRspNalT = request.form['docRspNalT']

        if request.form.get('urural') == None:
            urural = 0
        else:
            urural = request.form['urural']

        if idloc == '0':  # es NEW
            if False:   # valida si neces POST
                #error = "El usuario: " + request.form['uname']  + " ya existe...!"
                #return render_template('asiento.html', error=error, u=u, load_u=True)
                print('msg-err')
            else:
                nextid = ax.get_next_idloc()
                ax.add_asi_excep(nextid, request.form['deploc'], request.form['provloc'], \
                              request.form['secloc'], request.form['nomloc'], request.form['poblacionloc'], \
                              request.form['poblacionelecloc'], request.form['fechacensoloc'], request.form['tipolocloc'], \
                              request.form['latitud'], request.form['longitud'], request.form['estado'], '', \
                              request.form['etapa'], request.form['obsUbicacion'], request.form['obs'].strip(), \
                              request.form['fechaIngreso'][:-7], fa, request.form['usuario'], request.form['docAct'], docRspNal, \
                              docActF, urural, request.form['docActT'], docRspNalT)

                d.upd_doc(request.form['docAct'], docRspNal, request.form['doc_idAct'], request.form['doc_idRspNal'], docActF, request.form['docActT'], docRspNalT, docActT, docRspNalT)

                rows = ax.get_asi_excep_all(usrdep)
                return render_template('asiexcep_list.html', asientos=rows, puede_adicionar='Asiexcep - Adición' in permisos_usr, \
                                        puede_editar='Asiexcep - Edición' in permisos_usr, \
                                        puede_eliminar='Asiexcep - Eliminación' in permisos_usr
                                      ) # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            fcl = request.form['fechacensoloc']
            if fcl == '':
                fcl = None

            row_to_upd = \
                request.form['departamento'], request.form['provincia'], request.form['municipio'], \
                request.form['nomloc'], request.form['poblacionloc'], \
                request.form['poblacionelecloc'], fcl, request.form['tipolocloc'], \
                request.form['latitud'], request.form['longitud'], \
                request.form['estado'], '', request.form['etapa'], \
                request.form['obsUbicacion'], request.form['obs'].strip(), \
                str(request.form['fechaIngreso']), fa, usr, request.form['docAct'], docRspNal, \
                docActF, urural, request.form['docActT'], docRspNalT, idloc

            ax.upd_asi_excep(row_to_upd)
            d.upd_doc(request.form['docAct'], 0, request.form['doc_idAct'], request.form['doc_idRspNal'], docActF, request.form['docActT'], docRspNalT, docActT, docRspNalT)

            rows = ax.get_asi_excep_all(usrdep)
            return render_template('asiexcep_list.html', asientos=rows, puede_adicionar='Asiexcep - Adición' in permisos_usr, \
                                    puede_editar='Asiexcep - Edición' in permisos_usr, \
                                    puede_eliminar='Asiexcep - Eliminación' in permisos_usr
                                  ) # render a template
    else: # Viene de <asientos_list>
        if idloc != '0':  # EDIT
            if ax.get_asi_excep_idloc(idloc):
                if ax.fechaIngreso == None:
                    ax.fechaIngreso = str(datetime.datetime.now())[:-7]
                if ax.fechaAct == None:
                    ax.fechaAct = str(datetime.datetime.now())[:-7]
                if ax.usuario == None:
                    ax.usuario = usr

                return render_template('asiexcep.html', error=error, ax=ax, load=True, puede_editar=p, dptos=ax.get_depa_excep_all(usrdep), provincias=ax.get_prov_excep_all(usrdep), 
                                       municipios=ax.get_muni_excep_all(usrdep), estados=ax.get_estados(), etapas=ax.get_etapas(usrtipo), 
                                       tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))
    # New
    return render_template('asiexcep.html', error=error, ax=ax, load=False, puede_editar=p, dptos=ax.get_depa_excep_all(usrdep), provincias=ax.get_prov_excep_all(usrdep), 
                            municipios=ax.get_muni_excep_all(usrdep), estados=ax.get_estados(), etapas=ax.get_etapas(usrtipo), tcircuns=ax.get_tipocircun(),  
                            tpdfsA=d.get_tipo_documentos_pdfA(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep))


@app.route('/exterior_list', methods=['GET', 'POST'])
@login_required
def exterior_list():
    ex = ext.Exterior(cxms)
    rows = ex.get_exterior_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('exterior_list.html', exteriors=rows, puede_adicionar='Exterior - Adición' in permisos_usr, \
                                    puede_editar='Exterior - Edición' in permisos_usr)  # render a template
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
    j = get_json.GetJson(cxpg)

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
                ex.add_exterior(nextid, request.form['dpto'], request.form['provincia'], \
                              request.form['municipio'], request.form['nomloc'], 0, \
                              request.form['poblacionelecloc'], '2007-01-01', 0, \
                              request.form['latitud'], request.form['longitud'], \
                              request.form['estado'], request.form['cirConsulado'], request.form['etapa'], \
                              request.form['obsUbicacion'], request.form['obs'], request.form['fechaIngreso'][:-7], \
                              fa, request.form['usuario'], 0, request.form['docRspNal'], 0)

                d.upd_doc(0, request.form['docRspNal'], 0, request.form['doc_idRspNal'], 0)

                rows = ex.get_exterior_all(usrdep)
                return render_template('exterior_list.html', exteriors=rows, puede_adicionar='Exterior - Adición' in permisos_usr, \
                                        puede_editar='Exterior - Edición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            a.upd_asiento_ex(idloc, request.form['dpto'], request.form['provincia'], \
                              request.form['municipio'], request.form['nomloc'], 0, \
                              request.form['poblacionelecloc'], 0, \
                              request.form['latitud'], request.form['longitud'], \
                              request.form['estado'], request.form['cirConsulado'], request.form['etapa'], \
                              request.form['obsUbicacion'], request.form['obs'], \
                              str(request.form['fechaIngreso']), fa, usr, 0, request.form['docRspNal'])

            d.upd_doc(0, 0, 0, request.form['doc_idRspNal'], 0)

            rows = ex.get_exterior_all(usrdep)
            return render_template('exterior_list.html', exteriors=rows, puede_adicionar='Exterior - Adición' in permisos_usr, \
                                    puede_editar='Exterior - Edición' in permisos_usr)  # render a template
    else: # Viene de <asientos_list>
        if idloc != '0':  # EDIT
            if ex.get_exterior_idloc(idloc):
                if ex.fechaIngreso == None:
                    ex.fechaIngreso = str(datetime.datetime.now())[:-7]
                if ex.fechaAct == None:
                    a.fechaAct = str(datetime.datetime.now())[:-7]
                if ex.usuario == None:
                    ex.usuario = usr

                return render_template('exterior.html', error=error, a=ex, load=True, puede_editar=p, paises=ex.get_paises_all(usrdep),
                                       dptos=ex.get_departamentos_all(usrdep), provincias=ex.get_provincias_all(usrdep), estados=a.get_estados(),
                                       etapas=a.get_etapas(usrtipo), municipios=ex.get_municipios_all(usrdep), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep),
                                       gj_cir=j.get_cir(9),
                                       gj_mun=j.get_mun(9),
                                       gj_prov=j.get_prov(9))
    # New
    return render_template('exterior.html', error=error, a=a, load=False, puede_editar=p, paises=ex.get_paises_all(usrdep), estados=a.get_estados(), etapas=a.get_etapas(usrtipo), 
                            tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep),
                            gj_cir=j.get_cir(9),
                            gj_mun=j.get_mun(9),
                            gj_prov=j.get_prov(9))


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


@app.route('/recintos_list', methods=['GET', 'POST'])
@login_required
def recintos_list():
    ''' Recintos uninom y mixtos '''
    rc = recintos.Recintos(cxms)
    rows = rc.get_reci_uninom_mixto(usrdep)
    if rows:
        if 'Recintos - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('recintos_list.html', recintos=rows, \
                                    puede_adicionar='Recintos - Adición' in permisos_usr, \
                                    puede_editar='Recintos - Edición' in permisos_usr, \
                                    puede_consultar='Recintos - Consulta' in permisos_usr
                                  )# render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos...')
        return render_template('recintos_list.html', puede_adicionar='Recintos - Adición' in permisos_usr)


@app.route('/recinto/<idreci>/<idlocreci>', methods=['GET', 'POST'])
@login_required
def recinto(idreci, idlocreci):
    ''' Uninominales y mixtos '''
    rc = recintos.Recintos(cxms)
    rca = recia.Reciasiento(cxms)
    z = dist.Distritos(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Recintos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        # Valida si el campo docActF esta desactivado
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']

        if request.form.get('docTec') == None:
            if request.form.get('doc_idTec') != None:
                docTec = request.form['doc_idTec']    
            else:
                docTec = 0
        else:
            docTec = request.form['docTec']

        # Valida si el campo ruereci esta desactivado
        if request.form.get('ruereci') == None:
            ruereci = 0
        else:
            ruereci = request.form['ruereci']
        # Valida si el campo edireci esta desactivado
        if request.form.get('edireci') == None:
            edireci = 0
        else:
            edireci = request.form['edireci']
        # Valida si el campo depenreci esta desactivado
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
                               request.form['pisosreci'], request.form['fechaIngreso'][:-7], fa, request.form['usuario'], \
                               request.form['etapa'], request.form['docAct'], docActF, request.form['ambientes'], request.form['docTec'])

                d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF, docTec)

                rows = rc.get_reci_uninom_mixto(usrdep)
                return render_template('recintos_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr, \
                                        puede_editar='Recintos - Edición' in permisos_usr
                                      )# render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            idlocreci = request.form['asiento'].split(':')

            row_to_upd = \
                request.form['nomreci'], request.form['zonareci'], \
                request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                ruereci, edireci, depenreci, \
                request.form['pisosreci'], fa, usr, \
                request.form['etapa'], request.form['docAct'], docActF, request.form['ambientes'], request.form['docTec'], idlocreci[1], idreci

            if usrauth == 3 and rc.upd_reci_noauth(row_to_upd):   #tmpauth3 valida act datos no auth
                error = 'Intenta actualizar datos NO autorizados.'
                return render_template('recinto.html', error=error, rc=rc, load=True, puede_editar=p, asientoRecis=rca.get_loc_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rc.get_estados_reci(usrtipo), etapas=rc.get_etapas_auth(usrdep, usrtipo), dependencias=rc.get_dependencias(), trecintos=rc.get_tiporecintos(), tpdfsA=d.get_tipo_documentos_pdfA(usrdep))
            else:
                rc.upd_recinto(row_to_upd)
                d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF, docTec)

                rows = rc.get_reci_uninom_mixto(usrdep)
                return render_template('recintos_list.html', recintos=rows, puede_adicionar='Recintos - Adición' in permisos_usr, \
                                        puede_editar='Recintos - Edición' in permisos_usr
                                      )# render a template
    else: # Viene de <recintos_list>
        if idreci != '0':  # EDIT
            if rc.get_recinto_idreci(idreci, idlocreci):
                """if a.docAct == None:
                    a.docAct = """
                if rc.fechaIngreso == None:
                    rc.fechaIngreso = str(datetime.datetime.now())[:-7]
                if rc.fechaAct == None:
                    rc.fechaAct = str(datetime.datetime.now())[:-7]
                if rc.usuario == None:
                    rc.usuario = usr

                if usrauth == 3:    #tmpauth3 - get_etapas_auth
                    return render_template('recinto.html', error=error, rc=rc, load=True, puede_editar=p, asientoRecis=rca.get_loc_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rc.get_estados_reci(usrtipo), etapas=rc.get_etapas_auth(usrdep, usrtipo), dependencias=rc.get_dependencias(), trecintos=rc.get_tiporecintos(), tpdfsA=d.get_tipo_documentos_pdfA(usrdep))
                else:
                    return render_template('recinto.html', error=error, rc=rc, load=True, puede_editar=p, asientoRecis=rca.get_loc_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rc.get_estados_reci(usrtipo), etapas=rc.get_etapas(usrtipo), dependencias=rc.get_dependencias(), trecintos=rc.get_tiporecintos(), tpdfsA=d.get_tipo_documentos_pdfA(usrdep))

    # New from <recintos_list>
    return render_template('recinto.html', error=error, rc=rc, load=False, puede_editar=p, estados=rc.get_estados_reci(usrtipo), etapas=rc.get_etapas(usrtipo), trecintos=rc.get_tiporecintos(),
                            dependencias=rc.get_dependencias(), titulo='*-*', tpdfsA=d.get_tipo_documentos_pdfA(usrdep))


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


@app.route('/get_asientos_all3', methods=['GET', 'POST'])
def get_asientos_all3():
    pa = request.args.get('pais')
    dp = request.args.get('dpto')
    pro = request.args.get('provi')
    se = request.args.get('secci')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_asientos_all3(usrdep, pa, dp, pro, se)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(departamento='COORDENADA',
                       provincia='INCORRECTA !!!',
                       municipio='INTENTE NUEVAMENTE....')


@app.route('/get_asientos_all4', methods=['GET', 'POST'])
def get_asientos_all4():
    dp = request.args.get('dpto')
    pro = request.args.get('provi')
    se = request.args.get('secci')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_asientos_all4(usrdep, dp, pro, se)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_asiento_one', methods=['GET', 'POST'])
def get_asiento_one():
    idloc = request.args.get('idloc')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_asiento_one(usrdep, idloc)
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


@app.route('/get_zonas_all2', methods=['GET', 'POST'])
def get_zonas_all2():
    idloc = request.args.get('idloc')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_zonas_all2(usrdep, idloc)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_distritos_all', methods=['GET', 'POST'])
def get_distritos_all():
    ''' 
    (ajax) invocado por cargar.js (idloc, circun) param 7 
    ret: list(tupla) [(IdLocDist, Dist, CircunDist, NomDist), ...]
    '''

    circun = request.args.get('circun')
    idlocreci = request.args.get('idlocreci')

    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_distritos_all(circun, idlocreci) # en circun e idloc
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_dist_by_idloc', methods=['GET', 'POST'])
def get_dist_by_idloc():
    ''' 
    (ajax) invocado por zona_adm.html / getDistByIdloc  (idloc) 
    ret: list(tupla) [(IdLocDist, Dist, CircunDist, NomDist), ...]
    '''

    idloc = request.args.get('idloc')

    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    d = dist.Distritos(cxms2)
    rows = d.get_dists_en_idloc(idloc) # 
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_distritos_all2', methods=['GET', 'POST'])
def get_distritos_all2():
    idlocreci = request.args.get('idlocreci')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_distritos_all2(idlocreci)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/reci_espec_list', methods=['GET', 'POST'])
@login_required
def reci_espec_list():
    ''' Recintos Especiales / Indígenas list '''

    rce = recie.Reciespe(cxms)
    rows = rce.get_reci_espec(usrdep)
    if rows:
        if 'Especiales - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('reci_espec_list.html', recintos=rows, \
                                   puede_adicionar='Especiales - Adición' in permisos_usr, \
                                   puede_editar='Especiales - Edición' in permisos_usr, \
                                   puede_consultar='Especiales - Consulta' in permisos_usr
                                  )# render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos especiales...')
        return render_template('reci_espec_list.html', \
                               puede_adicionar='Especiales - Adición' in permisos_usr, \
                               puede_editar='Especiales - Edición' in permisos_usr, \
                               puede_consultar='Especiales - Consulta' in permisos_usr
                              ) # render a template


@app.route('/reciespe/<idreci>/<idlocreci>', methods=['GET', 'POST'])
@login_required
def reciespe(idreci, idlocreci):
    ''' Recintos Especiales/Indigenas '''
    rce = recie.Reciespe(cxms)
    rca = recia.Reciasiento(cxms)
    z = dist.Distritos(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Especiales - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        """Valida si el campo docActF esta desactivado"""
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']

        if request.form.get('docTec') == None:
            if request.form.get('doc_idTec') != None:
                docTec = request.form['doc_idTec']    
            else:
                docTec = 0
        else:
            docTec = request.form['docTec']

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
                               request.form['pisosreci'], request.form['fechaIngreso'][:-7], fa, request.form['usuario'], \
                               request.form['etapa'], request.form['docAct'], docActF, request.form['pueblo'], request.form['ambientes'], request.form['docTec'])

                d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF, docTec)

                rows = rce.get_reci_espec(usrdep)
                return render_template('reci_espec_list.html', recintos=rows, puede_adicionar='Especiales - Adición' in permisos_usr, \
                                        puede_editar='Especiales - Edición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            idlocreci = request.form['asiento'].split(':')

            row_to_upd = \
                request.form['nomreci'], request.form['zonareci'], \
                request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                ruereci, edireci, depenreci, \
                request.form['pisosreci'], fa, usr, \
                request.form['etapa'], request.form['docAct'], docActF, request.form['pueblo'], request.form['ambientes'], request.form['docTec'], idlocreci[1], idreci    

            if usrauth == 3 and rce.upd_reci_esp_noauth(row_to_upd):   #tmpauth3 valida act datos no auth
                error = 'Intenta actualizar datos NO autorizados.'
                return render_template('reciespe.html', error=error, rce=rce, load=True, puede_editar=p, asientoRecis=rca.get_loc_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rce.get_estados_reci(usrtipo), dependencias=rce.get_dependencias(), etapas=rce.get_etapas_auth(usrdep, usrtipo), trecintos=rce.get_tiporecintos(), 
                                       tpdfsA=d.get_tipo_documentos_pdfA(usrdep), naciones=rce.get_naciones())
            else:    
                rce.upd_recinto(row_to_upd)
                d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF, docTec)

                rows = rce.get_reci_espec(usrdep)
                return render_template('reci_espec_list.html', recintos=rows, puede_adicionar='Especiales - Adición' in permisos_usr, \
                                        puede_editar='Especiales - Edición' in permisos_usr)  # render a template
    else: # Viene de <recintos_list>
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

                if usrauth == 3:  #tmpauth3 - get_etapas_auth
                    return render_template('reciespe.html', error=error, rce=rce, load=True, puede_editar=p, asientoRecis=rca.get_loc_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                           estados=rce.get_estados_reci(usrtipo), dependencias=rce.get_dependencias(), etapas=rce.get_etapas_auth(usrdep, usrtipo), trecintos=rce.get_tiporecintos(),
                                           tpdfsA=d.get_tipo_documentos_pdfA(usrdep), naciones=rce.get_naciones())
                else:
                    return render_template('reciespe.html', error=error, rce=rce, load=True, puede_editar=p, asientoRecis=rca.get_loc_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                           estados=rce.get_estados_reci(usrtipo), dependencias=rce.get_dependencias(), etapas=rce.get_etapas(usrtipo), trecintos=rce.get_tiporecintos(),
                                           tpdfsA=d.get_tipo_documentos_pdfA(usrdep), naciones=rce.get_naciones())
    # New from <recintos_list>
    return render_template('reciespe.html', error=error, rce=rce, load=False, puede_editar=p, estados=rce.get_estados_reci(usrtipo), trecintos=rce.get_tiporecintos(), titulo='Registro de Zonas y Distritos',
                           dependencias=rce.get_dependencias(), etapas=rce.get_etapas(usrtipo), tpdfsA=d.get_tipo_documentos_pdfA(usrdep))


@app.route('/get_geo_esp', methods=['GET', 'POST'])
def get_geo_esp():
    lat = request.args.get('latitud', 0, type=float)
    long = request.args.get('longitud', 0, type=float)
    g = geo.LatLong(cxpg)
    rows = g.get_geo(lat, long)
    if rows:
        return jsonify(dep=g.dep,
                       departamento=g.departamento,
                       prov=g.prov,
                       provincia=g.provincia,
                       sec=g.sec,
                       municipio=g.municipio,
                       nrocircun=g.nrocircun)
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

@app.route('/distritos_list', methods=['GET', 'POST'])
@login_required
def distritos_list():
    z = dist.Distritos(cxms)
    rows = z.get_dist_all(usrdep)
    if rows:
        if 'Distritos - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('distritos_list.html', dists=rows, 
                                    puede_adicionar='Distritos - Adición' in permisos_usr, \
                                    puede_editar='Distritos - Edición' in permisos_usr, \
                                    puede_consultar='Distritos - Consulta' in permisos_usr
                                  )# render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin distritos...')


@app.route('/reci_dist_send', methods=['GET', 'POST'])
@login_required
def reci_dist_send():
    ''' Invocado por recinto.html/zona/Nuevo Dist. SEND variables '''

    z = dist.Distritos(cxms)
    error = None
    p = ('Distritos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        #idloc = request.form.get('idlocreci1', 0)
        idloc = request.form['idlocreci1']
        nomloc = request.form.get('nomloc', 0)     
        nrodist = request.form['nrodist1']

        return render_template('reci_dist_add.html', error=error, z=z, load=False, puede_editar=p, titulo='Adición de Nuevo Distrito', idloc=idloc, nomloc=nomloc, nrodist=nrodist)


@app.route('/dist_adm/<pidloc>/<pdist>/<pnalext>', methods=['GET', 'POST'])
@login_required
def dist_adm(pidloc, pdist, pnalext):
    ''' Adm de distritos - desde distritos_list '''
    '''     distritos_list - new: idloc= 0, dist= 0  nalext= 'adm'  '''
    '''     distritos_list - edit: idloc= n, dist= n  nalext= 'adm'  '''

    da = distr.Distritos(cxms)
    error = None
    p = ('Distritos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        idloc = request.form['idloc']
        dist = request.form['dist']
        nomdist = request.form['nomdist']
        circundist = request.form['circundist']

        if pidloc == '0' and pdist == '0':  # es NEW
            if nomdist.upper() == 'SIN DISTRITO':
                nextdist = 0
            else:
                nextdist = da.get_next_dist(request.form['idloc'])

            if  da.nomdist_existe(idloc, nomdist):  # valida si err en datos POST
                error = "El distrito: --" + nomdist + "-- ya existe en el asiento..."
                if pnalext == 'nal': # nal
                    return render_template('dist_adm.html', error=error, z=da, load=False, puede_editar=p, titulo='Adición de Distrito', idloc=idloc, nomloc='_', circundist=circundist, dook=None)
                if ban == '2': # ext
                    return render_template('zonareext.html', error=error, z=da, load=True, puede_editar=p, titulo='Registro de Distritos del Exterior')
            else:  # Adiciona distrito 
                if pnalext == 'nal':  # nal
                    da.add_dist(idloc, nextdist, circundist, nomdist, \
                               request.form['fechaIngreso'][:-7], request.form['fechaAct'], request.form['usuario'])
                    dook = 'Distrito Adicionado...'
                    return render_template('dist_adm.html', error=None, z=da, load=False, puede_editar=p, titulo='Adición de Distrito', idloc=idloc, nomloc='_', circundist=circundist, dook=dook)
                if ban == '2':  # ext
                    circundist = 0
                    da.add_dist(idloc, nextiddist, circundist, nomdist, \
                               request.form['fechaIngreso'][:-7], request.form['fechaAct'], request.form['usuario'])
                    return render_template('zonareext.html', error=error, z=da, load_d=True, puede_editar=p, titulo='Registro de Distritos del Exterior')
        else: # Edit - retorna de <distritos_list> con POST c/datos actualizados
            if da.nomdist_existe_edit(idloc, dist, nomdist)  :  # en edición actualiza a otro nom existente
                error = "El distrito: --" + nomdist + "-- ya existe en el asiento..."
                if pnalext == 'nal': # nal
                    da.get_zonadist_idloc(pidloc, pdist)
                    return render_template('dist_adm.html', error=error, d=da, load=True, puede_editar=p, titulo='Edición de Distrito', idloc=idloc, nomloc='', circundist=circundist, dook=None)
                if ban == '2': # ext
                    return render_template('zonareext.html', error=error, d=da, load=True, puede_editar=p, titulo='Registro de Distritos del Exterior')
            else: # upd dist
                if pnalext == 'nal':
                    fa = str(datetime.datetime.now())[:-7]
                    da.upd_dist(idloc, dist, circundist, nomdist, fa, usr)
                    dook = 'Distrito Actualizado...'
                    return render_template('dist_adm.html', error=None, z=da, load=False, puede_editar=p, titulo='Edición de Distrito', idloc=idloc, nomloc='_', circundist=circundist, dook=dook)

            rows = da.get_dist_all(usrdep)
            return render_template('distritos_list.html', dists=rows, \
                                    puede_adicionar='Distritos - Adición' in permisos_usr, \
                                    puede_editar='Distritos - Edición' in permisos_usr)
    else: # Viene de <distritos_list> edit
        if da.get_zonadist_idloc(pidloc, pdist) == True:
            return render_template('dist_adm.html', error=error, d=da, load=True, puede_editar=p, titulo='Edición de Distrito')

    # New - from <distritos_list> 
    return render_template('dist_adm.html', error=error, z=da, load=False, puede_editar=p, titulo='Adición de Distrito')


@app.route('/reci_dist_add/<nalext>', methods=['GET', 'POST'])
@login_required
def reci_dist_add(nalext):
    ''' Adición de Distrito desde form. recinto/zona '''
    ''' desde url_for param: nalext='nal'  '''

    z = dist.Distritos(cxms)
    error = None
    p = ('Distritos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
            idloc = request.form['idloc']
            nomdist = request.form['nomdist']
            circundist = request.form['nrodist']
            nomloc = request.form['nomloc']

            if nomdist.upper() == 'SIN DISTRITO':
                nextiddist = 0
            else:
                nextiddist = z.get_next_dist(request.form['idloc'])

            if z.nomdist_existe(idloc, nomdist):  # valida si err en datos POST
                error = "El distrito: --" + nomdist + "-- ya existe en el asiento debe verificar/complementar nombre..."

                if nalext == 'nal': # nal
                    return render_template('reci_dist_add.html', error=error, load=False, puede_editar=p, titulo='Adición de Nuevo Distrito', idloc=idloc, nomloc=nomloc, nrodist=circundist, dook=None)
                if nalext == 'ext': # ext
                    return render_template('zonareext.html', error=error, load_d=True, puede_editar=p, titulo='Registro de Distritos del Exterior')
            else:  # Adiciona distrito 
                if nalext == 'nal':  # nal
                    z.add_dist(idloc, nextiddist, circundist, nomdist, \
                               request.form['fechaIngreso'][:-7], request.form['fechaAct'], request.form['usuario'])
                    dook = 'Distrito Adicionado...'
                    return render_template('reci_dist_add.html', error=None, load=False, puede_editar=p, titulo='Adición de Nuevo Distrito', idloc=idloc, nomloc=nomloc, nrodist=circundist, dook=dook)
                if nalext == 'ext':  # ext
                    circundist = 0
                    z.add_dist(idloc, nextiddist, circundist, nomdist, \
                               request.form['fechaIngreso'][:-7], request.form['fechaAct'], request.form['usuario'])
                    return render_template('zonareext.html', error=error, load_d=True, puede_editar=p, titulo='Registro de Distritos del Exterior')


@app.route('/reci_zona_add', methods=['POST'])
@login_required
def reci_zona_add():
    ''' Invocado por ajax - adición de zonas (recinto.html) '''

    d = dist.Distritos(cxms)
    cxms_z = dbcn.get_db_ms()
    z = zon.Zon(cxms_z)   

    idloc = request.form['idloc']
    nomzona = request.form['nomzona'].upper()
    nomdist = request.form['nomdist']    # cod. DIST 

    # obtiene cod zona
    if nomzona == 'SIN ZONA':   # se debe asignar ZONA = 0
        if z.nomzona_existe(idloc, nomzona):
            return jsonify({'error' : 'Error, el nombre: --SIN ZONA-- ya existe en el asiento, debe verificar/complementar nombre.'})
        else:
            zona = 0
    else:
        zona = z.get_next_zona(idloc)

    if z.nomzona_existe(idloc, nomzona):
        return jsonify({'error' : 'Error, el nombre: --' + nomzona + '-- ya existe en el asiento, debe verificar/complementar nombre'})

    ultimodist = d.get_ultimodist(request.form['nomdist'], request.form['idloc'])
    
    z.add_zona(idloc, zona, nomzona, ultimodist, \
               request.form['fingreso'][:-7], request.form['factual'][:-7], request.form['usuario'])

    return jsonify({'name' : 'Zona adicionada...'})


@app.route('/zonasre_ext', methods=['GET', 'POST'])
@login_required
def zonasre_ext():
    z = dist.Distritos(cxms)
    ban = 0
    error = None
    p = ('Recintos - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        if request.form.get('idlocreci1') == None:
            idloc = request.form.get('idlocreci1', 0)
        else:
            idloc = request.form['idlocreci1']    
        if request.form.get('nomloc') == None:
            nomloc = request.form.get('nomloc', 0)
        else:
            nomloc = request.form['nomloc']
        if request.form.get('nrodist1') == None:
            nrodist = request.form.get('nrodist1', 0)
        else:
            nrodist = request.form['nrodist1']
        if ban != 0:
            print('Otra Cosa')
        else:
            return render_template('zonareext.html', error=error, z=z, load=False, puede_editar=p, titulo='Registro de Distritos del Exterior', idloc=idloc, nomloc=nomloc, nrodist=nrodist)


@app.route('/asientoz', methods=['GET', 'POST'])
def asientoz():
    azona = request.args.get('azona', 0, type=int)

    z = dist.Distritos(cxms)
    if z.asientoz(azona):
        return jsonify(nomasi=z.nomloc)
    else:
        return jsonify(nomasi='NO EXISTE ASIENTO')


@app.route('/get_nomloc', methods=['GET', 'POST'])
def get_nomloc():
    ''' invocado desde dist_adm, zona_adm - ajax'''

    idloc = request.args.get('idloc', 0, type=int)
    z = dist.Distritos(cxms)
    if z.asientoz(idloc):
        return jsonify(nomloc=z.nomloc)
    else:
        return jsonify(nomloc='NO EXISTE ASIENTO')


@app.route('/zonas_list', methods=['GET', 'POST'])
@login_required
def zonas_list():
    za = zon.Zon(cxms)
    rows = za.get_zon_all(usrdep)
    if rows:
        if 'Zonas - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('zonas_list.html', zonas=rows, \
                                    puede_adicionar='Zonas - Adición' in permisos_usr, \
                                    puede_editar='Zonas - Edición' in permisos_usr, \
                                    puede_consultar='Zonas - Consulta' in permisos_usr
                                  )# render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin zonas...')


@app.route('/zona_adm/<pidloczona>/<pzona>', methods=['GET', 'POST'])
@login_required
def zona_adm(pidloczona, pzona):
    '''
    Adm Zonas - desde zonas_list
        zonas_list - new: pidloczona= 0, pzona= 0
        zonas_list - edit: pidloczona= n, pzona= n
    '''
    za = zon.Zon(cxms)
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2) # p elim
    d = dist.Distritos(cxms2)
    error = None
    p = ('Zonas - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        idloczona = request.form['idloczona']
        zona = request.form['zona']
        nomzona = request.form['nomzona']
        distzona = request.form['distzona']

        if pidloczona == '0' and pzona == '0':  # es New 
            if nomzona.upper() == 'SIN ZONA':   # asigna cód 0 para SIN ZONA
                nextzona = 0
            else:
                nextzona = za.get_next_zon(idloczona)

            if za.nomzona_existe(idloczona, nomzona):   # valida si neces datos POST
                error = "La zona: --" + nomzona + "-- ya existe en el asiento"
                return render_template('zona_adm.html', error=error, load=False, za=za,
                                       distritos=d.get_dists_en_idloc(idloczona),
                                       puede_editar=p, titulo='Adición de Zona')
            else:   # add
                nextidzona = za.get_next_zon(idloczona)
                za.add_zon(idloczona, nextzona, nomzona, distzona, \
                           request.form['fechaIngreso'], request.form['fechaAct'], request.form['usuario'])     

            rows = za.get_zon_all(usrdep)
            return render_template('zonas_list.html', zonas=rows, \
                                   puede_adicionar='Zonas - Adición' in permisos_usr, \
                                   puede_editar='Zonas - Edición' in permisos_usr
                                  )# render a template
        else: # Edit - retorna de <zonas_list> POST c/datos act.
            if za.nomzona_existe_edit(idloczona, zona, nomzona):
                error = 'La zona: --' + nomzona + '-- actualizada ya existe en el asiento'
                return render_template('zona_adm.html', error=error, load=True, za=za,
                                       distritos=d.get_dists_en_idloc(idloczona),
                                       puede_editar=p, titulo='Edición de Zona -OBS-')
            else:
                fa = str(datetime.datetime.now())[:-7]
                za.upd_zon(idloczona, zona, nomzona, distzona, fa, usr)
                rows = za.get_zon_all(usrdep)
                return render_template('zonas_list.html', zonas=rows, \
                                       puede_adicionar='Zonas- Adición' in permisos_usr, \
                                       puede_editar='Zonas - Edición' in permisos_usr
                                      )# render a template

    else: # Edit - viene de <zonas_list> 
        if za.get_zona(pidloczona, pzona):
            return render_template('zona_adm.html', load=True, error=error, za=za, \
                                       distritos=d.get_dists_en_idloc(pidloczona), \
                                       puede_adicionar='Zonas - Adición' in permisos_usr, \
                                       puede_editar=p, titulo='Edición de Zona')
    # New
    return render_template('zona_adm.html', error=error, za=za, load=False, puede_editar=p, titulo='Adición de Zona')


@app.route('/get_distritos_all1', methods=['GET', 'POST'])
def get_distritos_all1():
    idloc = request.args.get('idloc')
    cxms2 = dbcn.get_db_ms()
    rca = recia.Reciasiento(cxms2)
    rows = rca.get_distritos_all1(idloc)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_circundist', methods=['GET', 'POST'])
def get_circundist():
    idloc = request.args.get('idloc')
    circd = request.args.get('circd')
    za = zon.Zon(cxms)
    rows = za.get_circundist(idloc, circd)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/reciespeciales_list', methods=['GET', 'POST'])
@login_required
def reciespeciales_list():
    '''Casos excepcionales - coordenadas/circun que no corresponden espacialmente (en opc/mod equiv Especiales)'''

    rces = recies.Reciespeciales(cxms)
    rows = rces.get_reciespeciales_all(usrdep)
    if rows:
        if 'Especiales - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('reciespeciales_list.html', reciespeciales=rows, puede_adicionar='Especiales - Adición' in permisos_usr, \
                                    puede_editar='Especiales - Edición' in permisos_usr
                                  )  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos...')
        return render_template('reciespeciales_list.html', puede_adicionar='Especiales - Adición' in permisos_usr, \
                                puede_editar='Especiales - Edición' in permisos_usr
                              )


@app.route('/reciespeciales/<idreci>/<idlocreci>', methods=['GET', 'POST'])
@login_required
def reciespeciales(idreci, idlocreci):
    '''Casos Excepcionales  - (opc Especiales en tabla modulo y archs '''

    rces = recies.Reciespeciales(cxms)
    rca = recia.Reciasiento(cxms)
    z = dist.Distritos(cxms)
    d = docu.Documentos(cxms)

    error = None
    p = ('Especiales - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        """Valida si el campo docActF esta desactivado"""
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']

        if request.form.get('docTec') == None:
            if request.form.get('doc_idTec') != None:
                docTec = request.form['doc_idTec']    
            else:
                docTec = 0
        else:
            docTec = request.form['docTec']
            
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
                               ruereci, edireci, depenreci, \
                               request.form['pisosreci'], request.form['fechaIngreso'][:-7], fa, request.form['usuario'], \
                               request.form['etapa'], request.form['docAct'], docActF, request.form['ambientes'], request.form['docTec'])

                d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF, docTec)

                rows = rces.get_reciespeciales_all(usrdep)
                return render_template('reciespeciales_list.html', reciespeciales=rows, puede_adicionar='Recintos - Adición' in permisos_usr, \
                                        puede_editar='Reci_espe - Edición' in permisos_usr)  # render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            idlocreci = request.form['asiento'].split(':')

            row_to_upd = \
                request.form['nomreci'], request.form['zonareci'], \
                request.form['mesasreci'], request.form['dirreci'], request.form['latitud'], \
                request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                ruereci, edireci, depenreci, \
                request.form['pisosreci'], fa, usr, \
                request.form['etapa'], request.form['docAct'], docActF, request.form['ambientes'], request.form['docTec'], idlocreci[1], idreci    

            rces.upd_recinto(row_to_upd)
            d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF, docTec)

            rows = rces.get_reciespeciales_all(usrdep)
            return render_template('reciespeciales_list.html', reciespeciales=rows, puede_adicionar='Recintos - Adición' in permisos_usr, \
                                    puede_editar='Reci_espe - Edición' in permisos_usr)  # render a template
    else: # Viene de <recintos_list>
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

                return render_template('reciespeciales.html', error=error, rces=rces, load=True, puede_editar=p, asientoRecis=rca.get_loc_all(usrdep), zonasRecis=rca.get_zonas_all(usrdep),
                                       estados=rces.get_estados(usrdep), trecintos=rces.get_tiporecintos(), tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep), tpdfsA=d.get_tipo_documentos_pdfA(usrdep),
                                       dependencias=rces.get_dependencias(), etapas=rces.get_etapas(usrtipo), dptos=rces.get_depaespeciales_all(usrdep), provincias=rces.get_provespeciales_all(usrdep), 
                                       municipios=rces.get_muniespeciales_all(usrdep))

    # New from <reciespeciales_list>
    return render_template('reciespeciales.html', error=error, rces=rces, load=False, puede_editar=p, tpdfsRN=d.get_tipo_documentos_pdfRN(usrdep), dptos=rces.get_depaespeciales_all(usrdep),
                            provincias=rces.get_provespeciales_all(usrdep), municipios=rces.get_muniespeciales_all(usrdep), estados=rces.get_estados(usrdep), trecintos=rces.get_tiporecintos(),
                            dependencias=rces.get_dependencias(), etapas=rces.get_etapas(usrtipo), tpdfsA=d.get_tipo_documentos_pdfA(usrdep))


@app.route('/get_provespeciales_all', methods=['GET', 'POST'])
def get_provespeciales_all():
    cxms2 = dbcn.get_db_ms()
    rces = recies.Reciespeciales(cxms2)
    rows = rces.get_provespeciales_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

    cxms2.close()


@app.route('/get_provespeciales_all1', methods=['GET', 'POST'])
def get_provespeciales_all1():
    ''' excepc '''

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

#========== Inicio Modulo Recintos Exterior ============#

@app.route('/exterior_reci_list', methods=['GET', 'POST'])
@login_required
def exterior_reci_list():
    exr = extr.Exteriorr(cxms)
    rows = exr.get_exterior_reci_all(usrdep)
    if rows:
        if permisos_usr:    # tiene pemisos asignados
            return render_template('exteriorreci_list.html', exteriorrecis=rows, puede_adicionar='Exterior_reci - Adición' in permisos_usr, \
                                    puede_editar='Exterior_reci - Edición' in permisos_usr)  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos del exterior...')


@app.route('/exterior_reci/<idreci>/<idlocreci>', methods=['GET', 'POST'])
@login_required
def exterior_reci(idreci, idlocreci):
    exr = extr.Exteriorr(cxms)
    z = dist.Distritos(cxms)
    d = docu.Documentos(cxms)
    j = get_json.GetJson(cxpg)  # jsons para mapa

    error = None
    p = ('Exterior_reci - Edición' in permisos_usr)  # t/f

    if request.method == 'POST':
        fa = request.form['fechaAct'][:-7]
        """Valida si el campo docActF esta desactivado"""
        if request.form.get('docActF') == None:
            docActF = 0
        else:
            docActF = request.form['docActF']
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
                nextid = exr.get_next_reciext()
                idlocreci = request.form['asiento']
                exr.add_recinto_ext(idlocreci, nextid, request.form['nomreci'], request.form['zonareci'], \
                                    0, request.form['dirreci'], request.form['latitud'], \
                                    request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                                    0, 0, depenreci, \
                                    request.form['pisosreci'], request.form['fechaIngreso'][:-7], fa, \
                                    request.form['usuario'], request.form['etapa'], request.form['docAct'], docActF, request.form['ambientes'])

                d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF)

                rows = exr.get_exterior_reci_all(usrdep)
                return render_template('exteriorreci_list.html', exteriorrecis=rows, puede_adicionar='Exterior_reci - Adición' in permisos_usr, \
                                        puede_editar='Exterior_reci - Edición' in permisos_usr
                                      )# render a template
        else: # Es Edit
            fa = str(datetime.datetime.now())[:-7]
            idlocreci = request.form['asiento']

            row_to_upd = \
                request.form['nomreci'], request.form['zonareci'], \
                0, request.form['dirreci'], request.form['latitud'], \
                request.form['longitud'], request.form['estado'], request.form['tiporeci'], \
                0, 0, depenreci, \
                request.form['pisosreci'], fa, usr, \
                request.form['etapa'], request.form['docAct'], docActF, request.form['ambientes'], idlocreci, idreci    

            exr.upd_recinto_ext(row_to_upd)
            d.upd_doc_r(request.form['docAct'], request.form['doc_idAct'], docActF)            

            rows = exr.get_exterior_reci_all(usrdep)
            return render_template('exteriorreci_list.html', exteriorrecis=rows, puede_adicionar='Exterior_reci - Adición' in permisos_usr, \
                                    puede_editar='Exterior_reci - Edición' in permisos_usr
                                  )# render a template
    else: # Viene de <recintos_list>
        if idreci != '0':  # EDIT
            if exr.get_exteriorreci_idreci(idreci, idlocreci):
                """if a.docAct == None:
                    a.docAct = """
                if exr.fechaIngreso == None:
                    exr.fechaIngreso = str(datetime.datetime.now())[:-7]
                if exr.fechaAct == None:
                    exr.fechaAct = str(datetime.datetime.now())[:-7]
                if exr.usuario == None:
                    exr.usuario = usr

                return render_template('exteriorreci.html', error=error, exr=exr, load=True, puede_editar=p, asientoRecis=exr.get_asiexterior_all(usrdep), zonasRecis=exr.get_zonexterior_all(usrdep),
                                       estados=exr.get_estados(usrdep), etapas=exr.get_etapas(usrtipo), dependencias=exr.get_dependencias(), trecintos=exr.get_tiporecintos(), tpdfsA=d.get_tipo_documentos_pdfRNExt(usrdep), 
                                       gj_cir=j.get_cir(9),
                                       gj_mun=j.get_mun(9),
                                       gj_prov=j.get_prov(9), paises=exr.get_paises_all(usrdep), dptos=exr.get_departamentos_all(usrdep), provincias=exr.get_provincias_all(usrdep),
                                       municipios=exr.get_municipios_all(usrdep))

    # New
    return render_template('exteriorreci.html', error=error, exr=exr, load=False, puede_editar=p, estados=exr.get_estados(usrdep), etapas=exr.get_etapas(usrtipo), trecintos=exr.get_tiporecintos(), 
                           paises=exr.get_paises_all(usrdep), dependencias=exr.get_dependencias(), titulo='Registro de Zonas y Distritos', tpdfsA=d.get_tipo_documentos_pdfRNExt(usrdep),
                           gj_cir=j.get_cir(9),
                           gj_mun=j.get_mun(9),
                           gj_prov=j.get_prov(9))

#========== Final Modulo Recintos Exterior ============#

@app.route('/help_doc', methods=['GET', 'POST'])
def help_doc():
    return redirect('static/helpdoc/_build/html/index.html')

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

""" Inicio de Indicadores """

@app.route('/asiento_indicadores/<idloc>/<string:nomloc>', methods=['GET', 'POST'])
@login_required
def asiento_indicadores(idloc, nomloc):
    lc = loc_cate.LocCate(cxms)
    ctgoria = lc.get_loc_cates(idloc);
    cate = lc.get_categorias_all();
    subctgoria = lc.get_subcategorias_all1();
    return render_template('asiento_ind.html', nomloc=nomloc, idloc=idloc, ctgorias=ctgoria, subctgorias=subctgoria, cates=cate, load=False, puede_editar='Asientos - Edición' in permisos_usr)


@app.route('/insertar_indicador', methods=['GET', 'POST'])
@login_required
def insertar_indicador():
    lc = loc_cate.LocCate(cxms)
    error = None
    if request.method == 'POST':
        fechaAct = str(datetime.datetime.now())[:-7]
        fechaIngreso = str(datetime.datetime.now())[:-7]
        loc_id = request.form['loc_id']
        nomloc = request.form['nomloc']
        cate_id = request.form['categoria']
        subcate_id = request.form['subcategoria']
        obs = request.form['obs']
        nextid = lc.get_next_idloccate(loc_id)
        lc.add_loc_cate(loc_id, cate_id, subcate_id, obs, fechaAct, usr, fechaIngreso, nextid)
        ctgoria = lc.get_loc_cates(loc_id);
        cate = lc.get_categorias_all();
        return render_template('asiento_ind.html', nomloc=nomloc, idloc=loc_id, ctgorias=ctgoria, cates=cate, load=False, puede_editar='Asientos - Edición' in permisos_usr)


@app.route('/modificar_indicador', methods=['GET', 'POST'])
@login_required
def modificar_indicador():
    lc = loc_cate.LocCate(cxms)
    error = None
    if request.method == 'POST':
        fechaAct = str(datetime.datetime.now())[:-7]
        loc_id = request.form['loc_id']
        nomloc = request.form['nomloc']
        sec = request.form['sec']
        cate_id = request.form['categoria']
        subcate_id = request.form['subcategoria']
        obs = request.form['obs']

        row_to_upd = cate_id, subcate_id, obs, fechaAct, usr, loc_id, sec
        lc.upd_loc_cate(row_to_upd)
        #lc.upd_loc_cate(loc_id, cate_id, subcate_id, obs, fechaAct, usr, sec)
        ctgoria = lc.get_loc_cates(loc_id);
        cate = lc.get_categorias_all();
        return render_template('asiento_ind.html', nomloc=nomloc, idloc=loc_id, ctgorias=ctgoria, cates=cate, load=False, puede_editar='Asientos - Edición' in permisos_usr)


@app.route('/eliminar_indicador', methods=['GET', 'POST'])
@login_required
def eliminar_indicador():
    lc = loc_cate.LocCate(cxms)
    error = None
    if request.method == 'POST':
        fechaAct = str(datetime.datetime.now())[:-7]
        loc_id = request.form['loc_id']
        nomloc = request.form['nomloc']
        sec = request.form['sec']
        lc.del_loc_cate(loc_id, sec)
        ctgoria = lc.get_loc_cates(loc_id);
        cate = lc.get_categorias_all();
        return render_template('asiento_ind.html', nomloc=nomloc, idloc=loc_id, ctgorias=ctgoria, cates=cate, load=False, puede_editar='Asientos - Edición' in permisos_usr)


@app.route('/asiento_ind', methods=['GET', 'POST'])
@login_required
def asiento_ind():
    lc = loc_cate.LocCate(cxms)
    idloc = request.args.get('idloc')
    rows = lc.get_loc_cates(idloc)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_subcategorias_all', methods=['GET', 'POST'])
def get_subcategorias_all():
    cxms2 = dbcn.get_db_ms()
    lc = loc_cate.LocCate(cxms2)
    cate_id = request.args.get('cate_id')
    rows = lc.get_subcategorias_all(cate_id)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

""" Final de Indicadores """

""" Inicio de Indicadores Excepcional"""

@app.route('/asi_excep_indicadores/<idloc>/<string:nomloc>', methods=['GET', 'POST'])
@login_required
def asi_excep_indicadores(idloc, nomloc):
    lc = loc_cate.LocCate(cxms)
    ctgoria = lc.get_loc_cates(idloc);
    cate = lc.get_categorias_all();
    subctgoria = lc.get_subcategorias_all1();
    return render_template('asiexcep_ind.html', nomloc=nomloc, idloc=idloc, ctgorias=ctgoria, subctgorias=subctgoria, cates=cate, load=False, puede_editar='Asiexcep - Edición' in permisos_usr)


@app.route('/insertar_indicador_excep', methods=['GET', 'POST'])
@login_required
def insertar_indicador_excep():
    lc = loc_cate.LocCate(cxms)
    error = None
    if request.method == 'POST':
        fechaAct = str(datetime.datetime.now())[:-7]
        fechaIngreso = str(datetime.datetime.now())[:-7]
        loc_id = request.form['loc_id']
        nomloc = request.form['nomloc']
        cate_id = request.form['categoria']
        subcate_id = request.form['subcategoria']
        obs = request.form['obs']
        nextid = lc.get_next_idloccate(loc_id)
        lc.add_loc_cate(loc_id, cate_id, subcate_id, obs, fechaAct, usr, fechaIngreso, nextid)
        ctgoria = lc.get_loc_cates(loc_id);
        cate = lc.get_categorias_all();
        return render_template('asiexcep_ind.html', nomloc=nomloc, idloc=loc_id, ctgorias=ctgoria, cates=cate, load=False, puede_editar='Asiexcep - Edición' in permisos_usr)


@app.route('/modificar_indicador_excep', methods=['GET', 'POST'])
@login_required
def modificar_indicador_excep():
    lc = loc_cate.LocCate(cxms)
    error = None
    if request.method == 'POST':
        fechaAct = str(datetime.datetime.now())[:-7]
        loc_id = request.form['loc_id']
        nomloc = request.form['nomloc']
        sec = request.form['sec']
        cate_id = request.form['categoria']
        subcate_id = request.form['subcategoria']
        obs = request.form['obs']

        row_to_upd = cate_id, subcate_id, obs, fechaAct, usr, loc_id, sec
        lc.upd_loc_cate(row_to_upd)
        #lc.upd_loc_cate(loc_id, cate_id, subcate_id, obs, fechaAct, usr, sec)
        ctgoria = lc.get_loc_cates(loc_id);
        cate = lc.get_categorias_all();
        return render_template('asiexcep_ind.html', nomloc=nomloc, idloc=loc_id, ctgorias=ctgoria, cates=cate, load=False, puede_editar='Asiexcep - Edición' in permisos_usr)


@app.route('/eliminar_indicador_excep', methods=['GET', 'POST'])
@login_required
def eliminar_indicador_excep():
    lc = loc_cate.LocCate(cxms)
    error = None
    if request.method == 'POST':
        fechaAct = str(datetime.datetime.now())[:-7]
        loc_id = request.form['loc_id']
        nomloc = request.form['nomloc']
        sec = request.form['sec']
        lc.del_loc_cate(loc_id, sec)
        ctgoria = lc.get_loc_cates(loc_id);
        cate = lc.get_categorias_all();
        return render_template('asiexcep_ind.html', nomloc=nomloc, idloc=loc_id, ctgorias=ctgoria, cates=cate, load=False, puede_editar='Asiexcep - Edición' in permisos_usr)


@app.route('/asi_excep_ind', methods=['GET', 'POST'])
@login_required
def asi_excep_ind():
    lc = loc_cate.LocCate(cxms)
    idloc = request.args.get('idloc')
    rows = lc.get_loc_cates(idloc)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_subcategorias_excep_all', methods=['GET', 'POST'])
def get_subcategorias_excep_all():
    cxms2 = dbcn.get_db_ms()
    lc = loc_cate.LocCate(cxms2)
    cate_id = request.args.get('cate_id')
    rows = lc.get_subcategorias_all(cate_id)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

""" Final de Indicadores Excepcional"""

""" Inicio de Asignar Homologaciones """

@app.route('/homologa_list', methods=['GET', 'POST'])
@login_required
def homologa_list():
    ''' Lista recintos susp/supr para ASIGNACION de homologación  '''

    global hom_excep
    hom_excep = False

    ahom = hom.Homologa(cxms)
    if request.method == 'POST':
        inicio = request.form['inicio']
        final = request.form['final']
    else:
        inicio = '00-00-0000'
        final = '00-00-0000'

    rows = ahom.get_homologa_all(usrdep, inicio, final)  # ret recintos susp/supr en rango de fechas
    if rows:
        if 'Homologa - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('homologa_list.html', homologas=rows, load=True, ban=True, inicio=inicio, final=final, puede_adicionar='Homologa - Adición' in permisos_usr, \
                                    puede_editar='Homologa - Edición' in permisos_usr
                                  )  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos para Homologación...')
        return render_template('homologa_list.html', puede_adicionar='Homologa - Adición' in permisos_usr, \
                                puede_editar='Homologa - Edición' in permisos_usr
                              )  # render a template)


@app.route('/homologa_list_excep', methods=['GET', 'POST'])
@login_required
def homologa_list_excep():
    ''' Lista recintos susp/supr para ASIGNACION de homologación Casos Excepcionales 
    -sólo difiere en hom_excep = True 
    -homologa_list.html (título)  
    -func. a_homologa (get all reci of dep) 
    '''

    global hom_excep
    hom_excep = True

    ahom = hom.Homologa(cxms)
    if request.method == 'POST':
        inicio = request.form['inicio']
        final = request.form['final']
    else:
        inicio = '00-00-0000'
        final = '00-00-0000'

    rows = ahom.get_homologa_all(usrdep, inicio, final)  # ret recintos susp/supr en rango de fechas
    if rows:
        if 'Homologa - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('homologa_list_excep.html', homologas=rows, load=True, ban=True, inicio=inicio, final=final, puede_adicionar='Homologa - Adición' in permisos_usr, \
                                    puede_editar='Homologa - Edición' in permisos_usr
                                  )  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin recintos para Homologación...')
        return render_template('homologa_list_excep.html', puede_adicionar='Homologa - Adición' in permisos_usr, \
                                puede_editar='Homologa - Edición' in permisos_usr
                              )  # render a template)


@app.route('/a_homologa/<idreci>/<idlocreci>/<inicio>/<final>/<ur>/<idlocdes>', methods=['GET', 'POST'])
@login_required
def a_homologa(idreci, idlocreci, inicio, final, ur, idlocdes):
    ''' Obtiene recintos destino para homologación '''

    ahom = hom.Homologa(cxms)
    error = None
    
    if idreci != '0' and idlocreci !='0':  # LISTA
        ahom.get_homologa_idlocreci(idreci, idlocreci)
        circun = ahom.circun
        dep = ahom.dep
        prov = ahom.prov
        sec = ahom.sec

        if hom_excep:  # si homolog excep: get all from dep p
            rtos = ahom.get_recintos_dep(dep)
        else:
            if ur == 'Urbano':
                rtos = ahom.get_recintos_idloc(idlocreci, circun);
            else:
                rtos = ahom.get_recintos_circun(dep, prov, sec, circun);

        if ahom.ver_homologa_idlocreci(idreci, idlocreci, idlocdes):
            #print('Modificar')
            return render_template('asigna_homologa.html', ho=ahom, inicio=inicio, final=final, recis=rtos, load=True, ban=False)
        else:
            if rtos != False:
                #print('Asignar')
                return render_template('asigna_homologa.html', ho=ahom, inicio=inicio, final=final, recis=rtos, load=True, ban=True)
            else:
                return render_template('asigna_homologa.html', inicio=inicio, final=final, load=False , ban=True)


@app.route('/a_homologa_m', methods=['GET', 'POST'])
@login_required
def a_homologa_m():
    ''' Upd/Add homologación con Reci destino seleccionado (Ajax) '''

    ahom = hom.Homologa(cxms)
    error = None
    if request.method == 'POST':
        idloc = request.form['idloc']
        reci = request.form['idlocreci']
        idloc2 = request.form['idloc2']
        reci2 = request.form['idlocreci2']
        idloc21 = request.form['idloc21']
        reci21 = request.form['idlocreci21']
        inicio = request.form['inicio']
        final = request.form['final']
        if ahom.verificar_homologa_idlocreci(idloc, reci, idloc21, reci21): #verifica si ya existe una asignacion previa
            f_actual = str(datetime.datetime.now())[:-7]
            ahom.get_homologa_idlocreci_destino(idloc2, reci2)
            ahom.upd_homologa(ahom.dep2, ahom.prov2, ahom.sec2, ahom.idloc2, ahom.dist2, ahom.zona2, ahom.reci2, ahom.departamento2, ahom.provincia2, \
                              ahom.municipio2, ahom.asiento2, ahom.nomdist2, ahom.nomzona2, ahom.recinto2, ahom.direccion2, ahom.circun2, ahom.idtipocircun2, \
                              ahom.tipocircun2, ahom.idtiporecinto2, ahom.tiporecinto2, ahom.latitud2, ahom.longitud2, f_actual, usr, ahom.idhom)
        else: #recinto para asignar
            f_ingreso = str(datetime.datetime.now())[:-7]
            f_actual = str(datetime.datetime.now())[:-7]
            ahom.get_homologa_idlocreci_origen(idloc, reci)
            ahom.get_homologa_idlocreci_destino(idloc2, reci2)
            ahom.add_homologa(ahom.dep, ahom.prov, ahom.sec, ahom.idloc, ahom.dist, ahom.zona, ahom.reci, ahom.departamento, ahom.provincia, ahom.municipio, \
                              ahom.asiento, ahom.nomdist, ahom.nomzona, ahom.recinto, ahom.direccion, ahom.circun, ahom.idtipocircun, ahom.tipocircun, \
                              ahom.idtiporecinto, ahom.tiporecinto, ahom.latitud, ahom.longitud, ahom.doc, ahom.doc1, ahom.dep2, ahom.prov2, ahom.sec2, \
                              ahom.idloc2, ahom.dist2, ahom.zona2, ahom.reci2, ahom.departamento2, ahom.provincia2, ahom.municipio2, ahom.asiento2, ahom.nomdist2, \
                              ahom.nomzona2, ahom.recinto2, ahom.direccion2, ahom.circun2, ahom.idtipocircun2, ahom.tipocircun2, ahom.idtiporecinto2, ahom.tiporecinto2, \
                              ahom.latitud2, ahom.longitud2, f_ingreso, f_actual, usr)

        rows = ahom.get_homologa_all(usrdep, inicio, final)
        return render_template('homologa_list.html', homologas=rows, load=True, ban=True, inicio=inicio, final=final, puede_adicionar='Homologa - Adición' in permisos_usr, \
                                puede_editar='Homologa - Edición' in permisos_usr
                              )  # render a template 
    else: # Viene de <homologa_list>
        return render_template('asigna_homologa.html', inicio=inicio, final=final, load=False, ban=True)

""" Final de Asignar Homologaciones """

""" Inicio de Listar Homologaciones """

@app.route('/homologacion_list', methods=['GET', 'POST'])
@login_required
def homologacion_list():
    ''' Solo listado/Reporte homologaciones '''
    ahomo = homo.Homologacion(cxms)
    if request.method == 'POST':
        inicio = request.form['inicio']
        final = request.form['final']
    else:
        inicio = '00-00-0000'
        final = '00-00-0000'
    rows = ahomo.get_homologacion_all(usrdep, inicio, final)
    rowj = ahomo.get_homojurisd_all(usrdep, inicio, final)
    if rows:
        if rowj:
            if 'Homologa - Consulta' in permisos_usr:    # tiene pemisos asignados
                return render_template('homologacion_list.html', homologaciones=rows, homojurisds=rowj, load=True, ban=True, \
                                        inicio=inicio, final=final, puede_consultar='Homologa - Consulta' in permisos_usr)  # render a template
            else:
                return render_template('msg.html', l1='Sin permisos asignados !!')
        else:
            if 'Homologa - Consulta' in permisos_usr:    # tiene pemisos asignados
                return render_template('homologacion_list.html', homologaciones=rows, load=True, ban=True, \
                                        inicio=inicio, final=final, puede_consultar='Homologa - Consulta' in permisos_usr)  # render a template
            else:
                return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        if rowj:
            if 'Homologa - Consulta' in permisos_usr:    # tiene pemisos asignados
                return render_template('homologacion_list.html', homojurisds=rowj, load=True, ban=True, \
                                        inicio=inicio, final=final, puede_consultar='Homologa - Consulta' in permisos_usr)  # render a template
            else:
                return render_template('msg.html', l1='Sin permisos asignados !!')
        else:
            return render_template('homologacion_list.html', puede_consultar='Homologa - Consulta' in permisos_usr)


@app.route('/homologacion/<idhomo>/<inicio>/<final>', methods=['GET', 'POST'])
@login_required
def homologacion(idhomo, inicio, final):
    ahomo = homo.Homologacion(cxms)
    ahomo.get_homologacion_idhom(idhomo);
    return render_template('homologacion.html', ahomo=ahomo, inicio=inicio, final=final, load=True, ban=True)


@app.route('/homojurisd/<idhomo>/<inicio>/<final>', methods=['GET', 'POST'])
@login_required
def homojurisd(idhomo, inicio, final):
    ahomo = homo.Homologacion(cxms)
    ahomo.get_homojurisd_idhom(idhomo);
    return render_template('homojurisd.html', ahomo=ahomo, inicio=inicio, final=final, load=True, ban=True)


@app.route('/get_hom_all', methods=['GET', 'POST'])
def get_hom_all():
    ahomo = homo.Homologacion(cxms)
    idhom = request.args.get('idhom')
    rows = ahomo.get_hom_all(idhom)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_homjurisd_all', methods=['GET', 'POST'])
def get_homjurisd_all():
    ahomo = homo.Homologacion(cxms)
    idhom = request.args.get('idhom')
    rows = ahomo.get_homjurisd_all(idhom)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/homologacion_pdf', methods=['GET', 'POST'])
def homologacion_pdf():
    new = 2
    rh = hpdf.HomologacionPDF(cxms)
    if request.form['inicio'] == "":
        inicio = ''
    else:
        inicio = request.form['inicio']

    if request.form['final'] == "":
        final = ''
    else:
        final = request.form['final']    
    rows = rh.reporte_consulta_h(usrdep, inicio, final)
    if rows:
        webbrowser.open(app.config['REPORTE_PDF'], new=new)
        print('PDF Generado')
        return render_template('homologacion_list.html', homologaciones=rows, load=True, ban=True, inicio=inicio, final=final, puede_adicionar='Homologa - Adición' in permisos_usr)  # render a template
    else:
        return ('PDF No Generado')

""" Final de Listar Homologaciones """
""" Inicio de Actualizacion de Jurisdiccion """

@app.route('/jurisdiccion_list', methods=['GET', 'POST'])
@login_required
def jurisdiccion_list():
    ju = jur.Jurisdiccion(cxms)
    rows = ju.get_jurisdiccion_all(usrdep)
    if rows:
        if 'Jurisdicción - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('jurisdiccion_list.html', jurisdicciones=rows, puede_adicionar='Jurisdicción - Adición' in permisos_usr, \
                                    puede_editar='Jurisdicción - Edición' in permisos_usr
                                  )# render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin Recintos...')


@app.route('/jurisdiccion/<reci>/<idloc>', methods=['GET', 'POST'])
@login_required
def jurisdiccion(reci, idloc):
    ju = jur.Jurisdiccion(cxms)
    rces = recies.Reciespeciales(cxms)
    d = docu.Documentos(cxms)
    error = None
    
    if request.method == 'POST':
        f_ingreso = str(datetime.datetime.now())[:-7]
        f_actual = str(datetime.datetime.now())[:-7]
        idloc = request.form['idloc']
        reci = request.form['idlocreci']
        idloc2 = request.form['idloc1']
        reci2 = request.form['idlocreci']
        idzona = request.form['zonad']
        idocact = request.form['docact']
        ju.get_jurisdiccion_idlocreci_origen(idloc, reci)
        ju.get_zonadist_idloc2(idloc2, idzona)
        ju.get_asiento_idloc2(idloc2)
        ju.get_jurisdiccion_idlocreci_destino(idloc, reci)

        if idloc != idloc2 and ju.get_verifica_dupli(idloc2, reci):
            nextid = ju.get_next_idreci(idloc2)
            ju.add_jurisdiccion(ju.dep, ju.prov, ju.sec, ju.idloc, ju.dist, ju.zona, ju.reci, ju.departamento, ju.provincia, ju.municipio, \
                                ju.asiento, ju.nomdist, ju.nomzona, ju.recinto, ju.direccion, ju.circun, ju.idtipocircun, ju.tipocircun, \
                                ju.idtiporecinto, ju.tiporecinto, ju.latitud, ju.longitud, idocact, ju.doc1, ju.dep2, ju.prov2, ju.sec2, \
                                idloc2, ju.dist2, ju.zona2, nextid, ju.departamento2, ju.provincia2, ju.municipio2, ju.asiento2, ju.nomdist2, \
                                ju.nomzona2, ju.recinto2, ju.direccion2, ju.circun2, ju.idtipocircun2, ju.tipocircun2, ju.idtiporecinto2, \
                                ju.tiporecinto2, ju.latitud2, ju.longitud2, f_ingreso, f_actual, usr)
            ju.upd_recinto_jurireci(idloc, reci, nextid, idloc2, idzona, idocact, usr)
        else:
            ju.add_jurisdiccion(ju.dep, ju.prov, ju.sec, ju.idloc, ju.dist, ju.zona, ju.reci, ju.departamento, ju.provincia, ju.municipio, \
                                ju.asiento, ju.nomdist, ju.nomzona, ju.recinto, ju.direccion, ju.circun, ju.idtipocircun, ju.tipocircun, \
                                ju.idtiporecinto, ju.tiporecinto, ju.latitud, ju.longitud, idocact, ju.doc1, ju.dep2, ju.prov2, ju.sec2, \
                                idloc2, ju.dist2, ju.zona2, reci2, ju.departamento2, ju.provincia2, ju.municipio2, ju.asiento2, ju.nomdist2, \
                                ju.nomzona2, ju.recinto2, ju.direccion2, ju.circun2, ju.idtipocircun2, ju.tipocircun2, ju.idtiporecinto2, \
                                ju.tiporecinto2, ju.latitud2, ju.longitud2, f_ingreso, f_actual, usr)
            ju.upd_recinto_juri(idloc, reci, idloc2, idzona, idocact, usr)

        rows = ju.get_jurisdiccion_all(usrdep)
        return render_template('jurisdiccion_list.html', jurisdicciones=rows, puede_adicionar='Jurisdicción - Adición' in permisos_usr, \
                                puede_editar='Jurisdicción - Edición' in permisos_usr
                              )# render a template
    else:
        dptos=rces.get_depaespeciales_all(usrdep)
        provincias=rces.get_provespeciales_all(usrdep)
        municipios=rces.get_muniespeciales_all(usrdep)
        if ju.get_jurisdiccion_idlocreci(reci, idloc):
            rows = ju.get_loc_estado_hab(usrdep)
            zonasd = ju.get_zonasd_all(usrdep)

        if ju.get_jurisdiccion_idloc(idloc, reci): # Verifica si ya se asigno el recinto a otro asiento
            return render_template('jurisdiccion.html', ju=ju, asientos=rows, zonasd=zonasd, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), dptos=dptos, provincias=provincias, municipios=municipios, load=True, titulo='Recinto a Modificar Jurisdicción', boton='Modificar')
        else:#se realiza la asignacion del recinto a otro asiento
            return render_template('jurisdiccion.html', ju=ju, asientos=rows, zonasd=zonasd, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), dptos=dptos, provincias=provincias, municipios=municipios, load=True, titulo='Recinto a Actualizar Jurisdicción', boton='Asignar')


@app.route('/jurisdiccion_m', methods=['GET', 'POST'])
@login_required
def jurisdiccion_m():
    ju = jur.Jurisdiccion(cxms)
    rces = recies.Reciespeciales(cxms)
    error = None
    
    if request.method == 'POST':
        f_actual = str(datetime.datetime.now())[:-7]
        idloc = request.form['idloc']
        reci = request.form['idlocreci']
        idloc2 = request.form['idloc1']
        reci2 = request.form['idlocreci']
        idzona = request.form['zonad']
        idocact = request.form['docact']
        idjurisd = request.form['idjurisd']
        ju.get_zonadist_idloc2(idloc2, idzona)
        ju.get_asiento_idloc2(idloc2)
        ju.get_jurisdiccion_idlocreci_destino(idloc, reci)

        if idloc != idloc2 and ju.get_verifica_dupli(idloc2, reci):
            nextid = ju.get_next_idreci(idloc2)
            ju.upd_jurisdiccion(idocact, ju.dep2, ju.prov2, ju.sec2, idloc2, ju.dist2, ju.zona2, nextid, ju.departamento2, \
                                ju.provincia2, ju.municipio2, ju.asiento2, ju.nomdist2, ju.nomzona2, ju.recinto2, \
                                ju.direccion2, ju.circun2, ju.idtipocircun2, ju.tipocircun2, ju.idtiporecinto2, \
                                ju.tiporecinto2, ju.latitud2, ju.longitud2, f_actual, usr, idjurisd)
            ju.upd_recinto_jurireci(idloc, reci, nextid, idloc2, idzona, idocact, usr)
        else:
            ju.upd_jurisdiccion(idocact, ju.dep2, ju.prov2, ju.sec2, idloc2, ju.dist2, ju.zona2, reci2, ju.departamento2, \
                                ju.provincia2, ju.municipio2, ju.asiento2, ju.nomdist2, ju.nomzona2, ju.recinto2, \
                                ju.direccion2, ju.circun2, ju.idtipocircun2, ju.tipocircun2, ju.idtiporecinto2, \
                                ju.tiporecinto2, ju.latitud2, ju.longitud2, f_actual, usr, idjurisd)
            ju.upd_recinto_juri(idloc, reci, idloc2, idzona, idocact, usr)

        rows = ju.get_jurisdiccion_all(usrdep)
        return render_template('jurisdiccion_list.html', jurisdicciones=rows, puede_adicionar='Jurisdicción - Adición' in permisos_usr, \
                                puede_editar='Jurisdicción - Edición' in permisos_usr
                              )# render a template


@app.route('/get_asijuri_all', methods=['GET', 'POST'])
@login_required
def get_asijuri_all():
    ju = jur.Jurisdiccion(cxms)
    dp = request.args.get('dp')
    pr = request.args.get('pr')
    mu = request.args.get('mu')
    rows = ju.get_asijuri_all(dp, pr, mu)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_zondist_all', methods=['GET', 'POST'])
@login_required
def get_zondist_all():
    ju = jur.Jurisdiccion(cxms)
    idloc = request.args.get('as')
    rows = ju.get_zondist_all(idloc)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


""" Inicio de Actualizacion de Jurisd_asi """
@app.route('/jurisd_asi_list', methods=['GET', 'POST'])
@login_required
def jurisd_asi_list():
    ja = jua.JurisdAsi(cxms)
    rows = ja.get_jurisd_asi_all(usrdep)
    if rows:
        if 'Jurisd_asi - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('jurisd_asi_list.html', jurisd_asis=rows, puede_adicionar='Jurisd_asi - Adición' in permisos_usr, \
                                    puede_editar='Jurisd_asi - Edición' in permisos_usr
                                  )  # render a template
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin Asientos...')
        return render_template('jurisd_asi_list.html', puede_adicionar='Juriss_asi - Adición' in permisos_usr, \
                                puede_editar='Jurisd_asi - Edición' in permisos_usr
                              )  # render a template


@app.route('/jurisd_asi/<idloc>', methods=['GET', 'POST'])
@login_required
def jurisd_asi(idloc):
    ''' Actualización jurisdicción de asientos '''

    ja = jua.JurisdAsi(cxms)
    rces = recies.Reciespeciales(cxms)
    d = docu.Documentos(cxms)
    error = None
    
    if request.method == 'POST':
        f_ingreso = str(datetime.datetime.now())[:-7]
        f_actual = str(datetime.datetime.now())[:-7]
        dep2 = request.form['deploc']
        prov2 = request.form['provloc']
        sec2 = request.form['secloc']
        ja.get_dpto(dep2)
        departamento2 = ja.nomdep
        ja.get_prov(dep2, prov2)
        provincia2 = ja.nomprov
        ja.get_sec(dep2, prov2, sec2)
        municipio2 = ja.nomsec
        circun = request.form['circu']
        zonade = request.form['zonade']
        idocact = request.form['docact']
        ja.get_zonadist_idloc(zonade, circun)
        if ja.add_llenado_recintos(idloc, dep2, prov2, sec2, departamento2, provincia2, municipio2, ja.dist, ja.zona, ja.nomdist, \
                                   ja.nomzona, ja.circun, f_ingreso, f_actual, usr, idocact):
            #Actualiza el asiento y sus recintos
            ja.upd_asiento_juriasi(idloc, dep2, prov2, sec2, idocact, usr)
            ja.upd_recinto_juriasi(idloc, ja.zona)
            ja.verifica_circun(idloc)
            if ja.circun_a != ja.circun:
                ja.upd_dist_juriasi_usr(idloc, ja.dist, ja.circun, usr)
            else:
                ja.upd_dist_juriasi(idloc, ja.dist, ja.circun)
        else:
            flash("El Asiento No Tiene Recintos", 'alert-warning')
            dptos=rces.get_depaespeciales_all(usrdep)
            provincias=rces.get_provespeciales_all(usrdep)
            municipios=rces.get_muniespeciales_all(usrdep)
            if ja.get_jurisd_asi_idloc(idloc):
                rows = ja.get_circuns_all(usrdep)
                zonasd = ja.get_zonasd_all(usrdep)
            
            if ja.get_jurisd_asi_idloc_idjurisd(idloc): # Modificar Asiento
                return render_template('jurisd_asi.html', ja=ja, circuns=rows, zonasd=zonasd, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), dptos=dptos, provincias=provincias, municipios=municipios, load=True, ban=True, titulo='Asiento a Modificar Jurisdicción', boton='Modificar')
            else:
                return render_template('jurisd_asi.html', ja=ja, circuns=rows, zonasd=zonasd, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), dptos=dptos, provincias=provincias, municipios=municipios, load=True, ban=False, titulo='Asiento a Actualizar Jurisdicción', boton='Asignar')
    else:
        dptos=rces.get_depaespeciales_all(usrdep)
        provincias=rces.get_provespeciales_all(usrdep)
        municipios=rces.get_muniespeciales_all(usrdep)
        if ja.get_jurisd_asi_idloc(idloc):
            rows = ja.get_circuns_all(usrdep)
            zonasd = ja.get_zonasd_all(usrdep)
        
        if ja.get_jurisd_asi_idloc_idjurisd(idloc): # LISTA
            return render_template('jurisd_asi.html', ja=ja, circuns=rows, zonasd=zonasd, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), dptos=dptos, provincias=provincias, municipios=municipios, load=True, ban=True, titulo='Asiento a Modificar Jurisdicción', boton='Modificar')
        else:
            return render_template('jurisd_asi.html', ja=ja, circuns=rows, zonasd=zonasd, tpdfsA=d.get_tipo_documentos_pdfA(usrdep), dptos=dptos, provincias=provincias, municipios=municipios, load=True, ban=False, titulo='Asiento a Actualizar Jurisdicción', boton='Asignar')    

    rows = ja.get_jurisd_asi_all(usrdep)
    return render_template('jurisd_asi_list.html', jurisd_asis=rows, puede_adicionar='Jurisd_asi - Adición' in permisos_usr, \
                            puede_editar='Jurisd_asi - Edición' in permisos_usr
                          )  # render a template


@app.route('/jurisd_asi_m/<idloc>', methods=['GET', 'POST'])
@login_required
def jurisd_asi_m(idloc):
    ja = jua.JurisdAsi(cxms)
    rces = recies.Reciespeciales(cxms)
    error = None
    
    if request.method == 'POST':
        f_actual = str(datetime.datetime.now())[:-7]
        dep2 = request.form['deploc']
        prov2 = request.form['provloc']
        sec2 = request.form['secloc']
        ja.get_dpto(dep2)
        departamento2 = ja.nomdep
        ja.get_prov(dep2, prov2)
        provincia2 = ja.nomprov
        ja.get_sec(dep2, prov2, sec2)
        municipio2 = ja.nomsec
        circun = request.form['circu']
        zonade = request.form['zonade']
        idocact = request.form['docact']
        ja.get_zonadist_idloc(zonade, circun)
        ja.upd_llenado_recintos(idloc, dep2, prov2, sec2, departamento2, provincia2, municipio2, ja.dist, ja.zona, ja.nomdist, \
                            ja.nomzona, ja.circun, f_actual, usr, idocact)
        #Actualiza el asiento y sus recintos
        ja.upd_asiento_juriasi(idloc, dep2, prov2, sec2, idocact, usr)
        ja.upd_recinto_juriasi(idloc, ja.zona)
        ja.verifica_circun(idloc)
        if ja.circun_a != ja.circun:
            ja.upd_dist_juriasi_usr(idloc, ja.dist, ja.circun, usr)
        else:
            ja.upd_dist_juriasi(idloc, ja.dist, ja.circun)

    rows = ja.get_jurisd_asi_all(usrdep)
    return render_template('jurisd_asi_list.html', jurisd_asis=rows, puede_adicionar='Jurisd_asi - Adición' in permisos_usr, \
                            puede_editar='Jurisd_asi - Edición' in permisos_usr
                          )  # render a template


@app.route('/get_circuns_dps', methods=['GET', 'POST'])
@login_required
def get_circuns_dps():
    ja = jua.JurisdAsi(cxms)
    dp = request.args.get('dp')
    pr = request.args.get('pr')
    mu = request.args.get('mu')
    rows = ja.get_circuns_dps(dp, pr, mu)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_zonas_dps', methods=['GET', 'POST'])
@login_required
def get_zonas_dps():
    ja = jua.JurisdAsi(cxms)
    dp = request.args.get('dp')
    pr = request.args.get('pr')
    mu = request.args.get('mu')
    id_loc = request.args.get('id_loc')
    rows = ja.get_zonas_dps(dp, pr, mu, id_loc)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)

""" Final de Actualizacion de Jurisd_asi """
""" Final de Actualizacion de Jurisdiccion """


""" Inicio Sincronizacion """
@app.route('/sincro_asi_list', methods=['GET', 'POST'])
@login_required
def sincro_asi_list():
    s = sin.LatLong(cxpg)
    a = asi.Asientos(cxms)
    g = ger.Gerencial(cxms)
    if request.method == 'POST':
        s.del_geo_asiento()
        rows = a.get_loc_nal_dep(0) #  0 nal
        rowas_n = g.get_gerencial_asi("00-00-0000", "00-00-0000", 0, 0, '1')
        rowas_m = g.get_gerencial_asi("00-00-0000", "00-00-0000", 0, 0, '2')
        rowas_s = g.get_gerencial_asi("00-00-0000", "00-00-0000", 0, 0, '3')
        for asie in rows:
           if asie[15] is None or asie[16] is None:
               latitud = -20.118403
               longitud = -67.540008
           else:
               latitud = asie[15]
               longitud = asie[16]
                          
           situacion = 'Antiguo'       
           s.get_geos(latitud, longitud)
           if rowas_n != False:
               for rowa_n in rowas_n:
                    if rowa_n[19] == asie[6]:
                        situacion = 'Nuevo'

           if rowas_m != False:
               for rowa_m in rowas_m:
                    if rowa_m[34] == asie[6]:
                        situacion = 'Modificado'

           if rowas_s != False:
               for rowa_s in rowas_s:
                    if rowa_s[17] == asie[6]:
                        situacion = 'Suprimido' 

           s.add_geo_asiento(asie[0], asie[1], asie[2], asie[3], asie[4], asie[5], asie[6], asie[7], asie[8], asie[9], asie[10], asie[11], asie[12], \
                             asie[13], asie[14], latitud, longitud, asie[17], s.geom, asie[18], asie[19], asie[20], situacion)

        return render_template('sincro_asi.html', titulo = 'Asientos Sincronizado', puede_consultar='Sincronizado - Consulta' in permisos_usr)# render a template
    else:
        return render_template('sincro_asi.html', titulo = 'Sincronizar Asientos', puede_consultar='Sincronizado - Consulta' in permisos_usr)


@app.route('/sincro_reci_list', methods=['GET', 'POST'])
@login_required
def sincro_reci_list():
    s = sin.LatLong(cxpg)
    rc = recintos.Recintos(cxms)
    g = ger.Gerencial(cxms)
    cont = 0
    if request.method == 'POST':
        s.del_geo_recinto()
        rows = rc.get_recintos_all1(0)
        rowas_n = g.get_gerencial_reci("00-00-0000", "00-00-0000", 0, 0, '1')
        rowas_m = g.get_gerencial_reci("00-00-0000", "00-00-0000", 0, 0, '2')
        rowas_s = g.get_gerencial_reci("00-00-0000", "00-00-0000", 0, 0, '3')
        for reci in rows:
            if reci[22] is None or reci[23] is None:
                latitud = -20.118403
                longitud = -67.540008
            else:
                latitud = reci[22]
                longitud = reci[23]

            situacion = 'Antiguo'
            cont = cont + 1
            s.get_geos(latitud, longitud)
            if rowas_n != False:
                for rowa_n in rowas_n:
                    if rowa_n[7] == reci[6] and rowa_n[9] == reci[8]: 
                        situacion = 'Nuevo'

            if rowas_m != False:
                for rowa_m in rowas_m:
                    if rowa_m[7] == reci[6] and rowa_m[9] == reci[8]:
                        situacion = 'Modificado'

            if rowas_s != False:
                for rowa_s in rowas_s:
                    if rowa_s[7] == reci[6] and rowa_s[9] == reci[8]:
                        situacion = 'Suprimido'

            s.add_geo_recinto(cont, reci[0], reci[1], reci[2], reci[3], reci[4], reci[5], reci[6], reci[7], reci[8], reci[9], reci[10], reci[11], reci[12], \
                             reci[13], reci[14], reci[15], reci[16], reci[17], reci[18], reci[19], reci[20], reci[21], latitud, longitud, s.geom, reci[24], \
                             reci[25], reci[26], situacion)

        return render_template('sincro_reci.html', titulo = 'Recintos Sincronizado', puede_consultar='Sincronizado - Consulta' in permisos_usr)# render a template
    else:
        return render_template('sincro_reci.html', titulo = 'Sincronizar Recintos', puede_consultar='Sincronizado - Consulta' in permisos_usr)


@app.route('/paises_list', methods=['GET', 'POST'])
@login_required
def paises_list():
    s = paises.Pais(cxms)
    rows = s.get_paises_all(usrdep)

    if rows:
        if 'Paises - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('paises_list.html', paises=rows, puede_adicionar='Paises - Adición' in permisos_usr, \
                                   puede_editar='Paises - Edición' in permisos_usr
                                  )  # render a template
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
                return render_template('paises_list.html', paises=rows, puede_adicionar='Paises - Adición' in permisos_usr, puede_editar=p)  # render a template
        else: # Es Edit
            s.upd_pais(pais_id, request.form['Pais'], request.form['NomPais'], request.form['Nal'], request.form['Estado'],
                       request.form['codInter'], request.form['codInterISO3166'], str(request.form['fecharegistro'])[:-7],
                       fa, usr)

            rows = s.get_paises_all(usrdep)
            return render_template('paises_list.html', paises=rows, puede_adicionar='Paises - Adición' in permisos_usr, puede_editar=p)  # render a template
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
        if 'Departamentos - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('deptos_list.html', deptos=rows, puede_adicionar='Departamentos - Adición' in permisos_usr, \
                                    puede_editar='Departamentos - Edición' in permisos_usr
                                  )# render a template
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
                s.add_depto(nextid, request.form['nomDep'], request.form['diputados'], request.form['diputadosUninominales'], request.form['pais'], request.form['descNivelId'], \
                            request.form['fechaIngreso'][:-7], fa, usr)

                rows = s.get_deptos_all(usrdep)
                return render_template('deptos_list.html', deptos=rows, puede_adicionar='Departamentos - Adición' in permisos_usr, puede_editar=p)  # render a template
        else: # Es Edit
            s.upd_depto(dep_id, request.form['nomDep'], request.form['diputados'], request.form['diputadosUninominales'], request.form['pais'], request.form['descNivelId'], fa, usr)
            rows = s.get_deptos_all(usrdep)
            return render_template('deptos_list.html', deptos=rows, puede_adicionar='Departamentos - Adición' in permisos_usr, puede_editar=p)  # render a template
    else: # Viene de <asientos_list>
        if dep_id != '0':  # EDIT
            if s.get_depto_iddep(dep_id) == True:
                if s.fechaAct == None:
                    s.fechaAct = str(datetime.datetime.now())[:-7]
                if s.usuario == None:
                    s.usuario = usr
                return render_template('deptosABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de Departamentos', tpaises=s.get_combo_paises(usrdep), tdescNivel=s.get_combo_desc_nivel(usrdep),puede_editar=p)
    # New
    return render_template('deptosABC.html', error=error, s=s, load=False, titulo='Registro de Nuevo Departamento', tpaises=s.get_combo_paises(usrdep), tdescNivel=s.get_combo_desc_nivel(usrdep), puede_editar=p)


@app.route('/get_desc_nivel_all', methods=['GET', 'POST'])
@login_required
def get_desc_nivel_all():
    s = deptoss.Departamento(cxms)
    sgrupo = request.args.get('sgrupo')
    rows = s.get_desc_nivel_all(sgrupo)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/provs_list', methods=['GET', 'POST'])
@login_required
def provs_list():
    s = provs.Prov(cxms)
    rows = s.get_provs_all(usrdep)
    if rows:
        if 'Provincias - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('provs_list.html', listaProvincias=rows, puede_adicionar='Provincias - Adición' in permisos_usr, \
                                    puede_editar='Provincias - Edición' in permisos_usr
                                  )  # render a template
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
                return render_template('provs_list.html', listaProvincias=rows, puede_adicionar='Provincias - Adición' in permisos_usr, puede_editar=p)  # render a template
        else: # Es Edit
            if request.form['idpais']!=request.form['pais']:
                if request.form['depto']!=dep_id:
                    s.upd_prov_1(request.form['depto'], dep_id, prov_id, request.form['NomProv'], request.form['codprov'], request.form['descNivelId'],fa, usr)
                else:
                    s.upd_prov(dep_id, prov_id, request.form['NomProv'], request.form['codprov'], request.form['descNivelId'],fa, usr)
            else:
                if request.form['depto']!=dep_id:
                    s.upd_prov_1(request.form['depto'], dep_id, prov_id, request.form['NomProv'], request.form['codprov'], request.form['descNivelId'],fa, usr)
                else:
                    s.upd_prov(dep_id, prov_id, request.form['NomProv'], request.form['codprov'], request.form['descNivelId'],fa, usr)

            rows = s.get_provs_all(usrdep)
            return render_template('provs_list.html', listaProvincias=rows, puede_adicionar='Provincias - Adición' in permisos_usr, puede_editar=p)  # render a template
    else: # Viene de <asientos_list>
        if dep_id != '0' and prov_id != '0':  # EDIT
            if s.get_provs_id(dep_id, prov_id) == True:
                if s.fechaAct == None:
                    s.fechaAct = str(datetime.datetime.now())[:-7]
                if s.usuario == None:
                    s.usuario = usr

                return render_template('provsABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de Provincias', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tdescNivel=s.get_combo_desc_nivel(usrdep), puede_editar=p)
    # New
    return render_template('provsABC.html', error=error, s=s, load=False, titulo='Registro de Nueva Provincia', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tdescNivel=s.get_combo_desc_nivel(usrdep), puede_editar=p)


@app.route('/get_desc_nivel_prov_all', methods=['GET', 'POST'])
@login_required
def get_desc_nivel_prov_all():
    sgrupo = request.args.get('sgrupo')
    cxms2 = dbcn.get_db_ms()
    s = provs.Prov(cxms2)
    rows = s.get_desc_nivel_prov_all(sgrupo)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_deptos_prov_all', methods=['GET', 'POST'])
def get_deptos_prov_all():
    sgrupo = request.args.get('sgrupo')
    cxms2 = dbcn.get_db_ms()
    s = provs.Prov(cxms2)
    rows = s.get_deptos_prov_all(sgrupo)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_departamentos_all', methods=['GET', 'POST'])
def get_departamentos_all():
    cxms2 = dbcn.get_db_ms()
    s = rep.Reportes(cxms2)
    rows = s.get_departamentos_all(usrdep)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)
    cxms2.close()


@app.route('/mun_list', methods=['GET', 'POST'])
@login_required
def mun_list():
    s = muns.Municipio(cxms)
    rows = s.get_mun_all(usrdep)
    if rows:
        if 'Municipios - Consulta' in permisos_usr:    # tiene pemisos asignados
            return render_template('mun_list.html', municipios=rows, puede_adicionar='Municipios - Adición' in permisos_usr, \
                                    puede_editar='Municipios - Edición' in permisos_usr
                                  )# render a template
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
            return render_template('mun_list.html', municipios=rows, puede_adicionar='Municipios - Adición' in permisos_usr, puede_editar=p)  # render a template
        else: # Es Edit
            if request.form['idpais']!=request.form['pais']:
                if request.form['depto']!=dep_id:
                    if request.form['prov']!=prov_id:
                        s.upd_mun_3(request.form['depto'], request.form['prov'], dep_id, prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)
                    else:
                        s.upd_mun_2(request.form['depto'], dep_id, prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)
                else:
                    if request.form['prov']!=prov_id:
                        s.upd_mun_1(dep_id, request.form['prov'], prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)
                    else:
                        s.upd_mun(dep_id, prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)
            else:
                if request.form['depto']!=dep_id:
                    if request.form['prov']!=prov_id:
                        s.upd_mun_3(request.form['depto'], request.form['prov'], dep_id, prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)
                    else:
                        s.upd_mun_2(request.form['depto'], dep_id, prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)
                else:
                    if request.form['prov']!=prov_id:
                        s.upd_mun_1(dep_id, request.form['prov'], prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)
                    else:
                        s.upd_mun(dep_id, prov_id, mun_id, request.form['numConceSec'], request.form['nomSec'], request.form['descNivelId'], fa, usr)

            rows = s.get_mun_all(usrdep)
            return render_template('mun_list.html', municipios=rows, puede_adicionar='Municipios - Adición' in permisos_usr, puede_editar=p)  # render a template
    else: # Viene de <asientos_list>
        if dep_id != '0' and prov_id != '0' and mun_id != '0': # EDIT
            if s.get_mun_id(dep_id, prov_id, mun_id) == True:
                if s.fechaAct == None:
                    s.fechaAct = str(datetime.datetime.now())[:-7]
                if s.usuario == None:
                    s.usuario = usr
                return render_template('munABC.html', error=error, s=s, load=True, titulo='Edicion de Datos de Municipios', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tprovs=s.get_combo_prov(dep_id,prov_id), tdescNivel=s.get_combo_desc_nivel(usrdep), puede_editar=p)
    # New
    return render_template('munABC.html', error=error, s=s, load=False, titulo='Registro de Nuevo Municipio', tpaises=s.get_combo_paises(usrdep), tdeptos=s.get_combo_deptos(usrdep), tprovs=s.get_combo_prov_new(usrdep), tdescNivel=s.get_combo_desc_nivel(usrdep), puede_adicionar=p)


@app.route('/get_desc_nivel_mun_all', methods=['GET', 'POST'])
@login_required
def get_desc_nivel_mun_all():
    s = muns.Municipio(cxms)
    sgrupo = request.args.get('sgrupo')
    rows = s.get_desc_nivel_mun_all(sgrupo)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/get_provs_all', methods=['GET', 'POST'])
def get_provs_all():
    s = muns.Municipio(cxms)
    sgrupo = request.args.get('sgrupo')
    rows = s.get_provs_all(sgrupo)
    if rows:
        return jsonify(rows)
    else:
        return jsonify(0)


@app.route('/bitacora_list', methods=['GET', 'POST'])
@login_required
def bitacora_list():
    """ Modulo log de Transacciones """

    if 'Historial' not in permisos_usr:    # No tiene pemisos asignados
        return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        s = bitacoras.Bitacora(cxms)
        if request.method == 'POST':
            if request.form['limpiar'] == 'limpiando':
                inicio = '00-00-0000'
                final = '00-00-0000'
                usuario = 0
                rows = s.get_bitacora_1000(usrdep)
                if rows:
                    return render_template('bitacora_list.html', bitacoras=rows, usuarios=s.get_usuarios(), load=True, inicio=inicio, final=final, usuario=usuario)  # render a template
                else:
                    print ('Sin registros en Historial...')
                    return render_template('bitacora_list.html', usuarios=s.get_usuarios(), load=True, inicio=inicio, final=final, usuario=usuario)
            else:
                if request.form['inicio'] == "":
                    inicio = '00-00-0000'
                else:
                    inicio = request.form['inicio']

                if request.form['final'] == "":
                    final = '00-00-0000'
                else:
                    final = request.form['final']

                if request.form['usuario'] == '':    
                    usuario = 0
                else:
                    usuario = request.form['usuario']

                rows = s.get_bitacora_all(inicio, final, usuario)

                if rows:
                    return render_template('bitacora_list.html', bitacoras=rows, usuarios=s.get_usuarios(), load=True, inicio=inicio, final=final, usuario=usuario)  # render a template
                else:
                    print ('Sin registros en Historial...')
                    return render_template('bitacora_list.html', usuarios=s.get_usuarios(), load=True, inicio=inicio, final=final, usuario=usuario)
        else:
            inicio = '00-00-0000'
            final = '00-00-0000'
            usuario = 0
            rows = s.get_bitacora_1000(usrdep)
            if rows:
                return render_template('bitacora_list.html', bitacoras=rows, usuarios=s.get_usuarios(), load=True, inicio=inicio, final=final, usuario=usuario, puede_adicionar='Bitacoras - Adición' in permisos_usr)  # render a template
            else:
                print ('Sin registros en Historial...')
                return render_template('bitacora_list.html', usuarios=s.get_usuarios(), load=True, inicio=inicio, final=final, usuario=usuario, puede_adicionar='Bitacoras - Adición' in permisos_usr)


@app.route('/grupo_list', methods=['GET', 'POST'])
@login_required
def grupo_list():
    s = clas_grupo.Grupo(cxms)
    rows = s.get_clas_grupos_all()
    if rows:
        if ('Grupos - Consulta' in permisos_usr):   
            return render_template('grupo_list.html', clas_grup=rows, \
                                   puede_adicionar='Grupos - Adición' in permisos_usr, \
                                   puede_editar='Grupos - Edición' in permisos_usr, \
                                   puede_eliminar='Grupos - Eliminación' in permisos_usr, \
                                   puede_consultar='Grupos - Consulta' in permisos_usr \
                                  )  
        else:
            return render_template('msg.html', l1='Sin permisos asignados !!')
    else:
        print ('Sin Grupos...')


@app.route('/grupo/<grupo_id>', methods=['GET', 'POST'])
@login_required
def grupo(grupo_id):
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
                return redirect(url_for('grupo_list'))
        else: # Es Edit
            s.upd_grupo(grupo_id, request.form['descripcion'])
            return redirect(url_for('grupo_list'))
    else: # Viene de <grupos_list>
        if grupo_id != '0':  # EDIT
            if s.get_clas_grupo_idclasGrup(grupo_id) == True:
                return render_template('grupo.html', error=error, \
                                       s=s, load=True, \
                                       titulo='Edición de Grupo', 
                                       puede_editar=p)
    # New
    return render_template('grupo.html', error=error, s=s, load=False, titulo='Registro de Nuevo grupo', puede_editar=p)


@app.route('/grupo_del/<grupo_id>', methods=['GET', 'POST'])
@login_required
def grupo_del(grupo_id):
    g = clas_grupo.Grupo(cxms)
    g.del_grupo(grupo_id)

    return redirect(url_for('grupo_list'))


@app.route('/clas_list/<grupo_id>', methods=['GET', 'POST'])
@login_required
def clas_list(grupo_id):
    s = clasificadores.Clasificador(cxms)
    if grupo_id != '0':  
            if s.get_clas_idclas(grupo_id) != False:
                rows = s.get_clas_idclas(grupo_id)
                if not rows:
                    return render_template('clas_new.html', grupo_id=grupo_id)  # render a template
                else:
                    if ('Clasificadores - Consulta' in permisos_usr):    # tiene pemisos asignados
                        return render_template('clas_list.html', clasificadores=rows, \
                                               puede_adicionar='Clasificadores - Adición' in permisos_usr, \
                                               puede_editar='Clasificadores - Edición' in permisos_usr, \
                                               puede_eliminar='Clasificadores - Eliminación' in permisos_usr, \
                                               puede_consultar='Clasificadores - Consulta' in permisos_usr, \
                                              )
                    else:
                        print('sin permisos')
                        return render_template('msg.html', l1='Sin permisos asignados !!')
            else:
                print('Sin grupo...')


@app.route('/clas_new/<grupo_id>', methods=['GET', 'POST'])
@login_required
def clas_new(grupo_id):
    s = clasificadores.Clasificador(cxms)
    if grupo_id != '0':  # EDIT
            if s.get_clas_idclas(grupo_id) != False:
                rows = s.get_clas_idclas(grupo_id)
    else:
        print('Nuevo...')


@app.route('/clas_del/<clasif_id>/<grupo_id>', methods=['GET', 'POST'])
@login_required
def clas_del(clasif_id, grupo_id):
    c = clasificadores.Clasificador(cxms)
    c.del_clas(int(clasif_id))
    return redirect(url_for('clas_list', grupo_id=grupo_id))


@app.route('/clas/<clas_id>/<clas_grup_id>', methods=['GET', 'POST'])
@login_required
def clas(clas_id, clas_grup_id):
    s = clasificadores.Clasificador(cxms)
    error = None
    p = ('clasificadores - Edición' in permisos_usr)  # t/f
    if request.method == 'POST':
        if clas_id == '0':  # es NEW
            if False:   # valida si neces POST
                print('msg-err')
            else:
                nextid = s.get_next_idclas()
                s.add_clas(nextid, request.form['descripcion'], clas_grup_id,request.form['subgrupo'])
                return redirect(url_for('clas_list', grupo_id=clas_grup_id))
        else: # Es Edit
            s.upd_clas(clas_id, request.form['descripcion'],request.form['subgrupo'])
            #return redirect(url_for('clas_list', grupo_id=clas_grup_id))
            rows = s.get_clas_idclas(request.form['grupo'])
            return render_template('clas_list.html', clasificadores=rows, \
                                   puede_adicionar='Clasificadores - Adición' in permisos_usr, \
                                   puede_editar='Clasificadores - Edición' in permisos_usr, \
                                   puede_eliminar='Clasificadores - Eliminación' in permisos_usr, \
                                   puede_consultar='Clasificadores - Consulta' in permisos_usr, \
                                  )
    else: # Viene de <asientos_list>
        if clas_id != '0':  # EDIT
            if s.get_clas_id(clas_id) == True:
                return render_template('clas.html', error=error, s=s, load=True, titulo='Edicion de Datos de clasificadores', puede_editar=p)
    # New
    return render_template('clas.html', error=error, s=s, load=False, titulo='Registro de Nuevo clasificador', puede_editar=p)


@app.route('/recinto_img/<idloc>/<reci>/<string:nomreci>', methods=['GET', 'POST'])
@login_required
def recinto_img(idloc, reci, nomreci):
    ''' Gestiona imágenes Recintos - Uninominales '''

    i = clasif_get.ClasifGet(cxms)  # conecta a la BD
    li = reci_img.ReciImg(cxms)

    with_img = li.get_reci_imgs(idloc, reci)  # False or rows-img

    error = None

    if request.method == 'POST':
        img_ids_ = request.form.getlist('imgsa[]')  # options img for Recinto
        img_ids = list(img_ids_[0].split(","))      # list ok

        uploaded_files = request.files.getlist("filelist")

        for n in range(len(img_ids)):
            f  = uploaded_files[n]
            if f.filename != '':
                securef = secure_filename(f.filename)
                fpath = os.path.join(app.config['IMG_RECINTOS'], securef)
                arch, ext = os.path.splitext(fpath)
                name_to_save = str(idloc).zfill(5) + "_" + str(reci).zfill(5) + "_" + str(img_ids[n]).zfill(2) + ext
                fpath_destino = os.path.join(app.config['IMG_RECINTOS'], name_to_save)   # loc_img.ruta

                if li.exist_img_reci(idloc, reci, img_ids[n]):   # si upd img
                    file_to_del = li.get_name_file_img_reci(idloc, reci, img_ids[n]) # referencia en bd 
                    os.remove(file_to_del[1:]) # borra arch. de HD
                    li.upd_reci_img(idloc, img_ids[n], reci, fpath_destino, datetime.datetime.now(), usr) # upd de bd
                else: # new
                    li.add_reci_img(idloc, img_ids[n], reci, fpath_destino, datetime.datetime.now(), usr)

                f.save(os.path.join('.' + app.config['IMG_RECINTOS'], securef))
                resize_save_file1(fpath, name_to_save, (1024, 768))

                os.remove(fpath[1:])   # arch. fuente 

        return redirect(url_for('recintos_list'))

    else:
        if with_img:  # Edit
            return render_template('recinto_img_upd.html', rows=i.get_descripcion(14), nomloc=nomreci,
                                puede_editar='Recintos - Edición' in permisos_usr,
                                imgs_loaded=with_img)
        else:  # New
            return render_template('recinto_img.html', rows=i.get_descripcion(14), nomloc=nomreci,
                                puede_editar='Recintos - Edición' in permisos_usr)


@app.route('/reciespe_img/<idloc>/<reci>/<string:nomreci>', methods=['GET', 'POST'])
@login_required
def reciespe_img(idloc, reci, nomreci):
    ''' Gestiona imágenes Recintos - Especiales (Indígenas) '''

    i = clasif_get.ClasifGet(cxms)  # conecta a la BD
    li = reci_img.ReciImg(cxms)

    with_img = li.get_reci_imgs(idloc, reci)  # False or rows-img

    error = None

    if request.method == 'POST':
        img_ids_ = request.form.getlist('imgsa[]')  # options img for Asiento
        img_ids = list(img_ids_[0].split(","))      # list ok

        uploaded_files = request.files.getlist("filelist")

        for n in range(len(img_ids)):
            f  = uploaded_files[n]
            if f.filename != '':
                securef = secure_filename(f.filename)
                fpath = os.path.join(app.config['IMG_RECINTOS'], securef)
                arch, ext = os.path.splitext(fpath)
                name_to_save = str(idloc).zfill(5) + "_" + str(reci).zfill(5) + "_" + str(img_ids[n]).zfill(2) + ext
                fpath_destino = os.path.join(app.config['IMG_RECINTOS'], name_to_save)   # loc_img.ruta

                if li.exist_img_reci(idloc, reci, img_ids[n]):   # si upd img
                    file_to_del = li.get_name_file_img_reci(idloc, reci, img_ids[n]) # referencia en bd 
                    os.remove(file_to_del[1:]) # borra arch. de HD
                    li.upd_reci_img(idloc, img_ids[n], reci, fpath_destino, datetime.datetime.now(), usr) # upd de bd
                else: # new
                    li.add_reci_img(idloc, img_ids[n], reci, fpath_destino, datetime.datetime.now(), usr)

                f.save(os.path.join('.' + app.config['IMG_RECINTOS'], securef))
                resize_save_file1(fpath, name_to_save, (1024, 768))

                os.remove(fpath[1:])   # arch. fuente 

        return redirect(url_for('reci_espec_list'))
    else:
        if with_img:  # Edit
            return render_template('reciespe_img_upd.html', rows=i.get_descripcion(14), nomloc=nomreci,
                                puede_editar='Especiales - Edición' in permisos_usr,
                                imgs_loaded=with_img)
        else:  # New
            return render_template('reciespe_img.html', rows=i.get_descripcion(14), nomloc=nomreci,
                                puede_editar='Especiales - Edición' in permisos_usr)


#def resize_save_file(in_file, out_file, size, ruta_img):
def resize_save_file(in_file, out_file, size):
    with open('.' + in_file, 'rb') as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)

    #image.save('.' + ruta_img, out_file)
    #image.save('.' + os.path.join(app.config['IMG_RECINTOS'], out_file))
    image.save('.' + os.path.join(app.config['IMG_ASIENTOS'], out_file))
    image.close()
    #return(out_file)


def resize_save_file1(in_file, out_file, size):
    with open('.' + in_file, 'rb') as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)

    #image.save('.' + ruta_img, out_file)
    #image.save('.' + os.path.join(app.config['IMG_RECINTOS'], out_file))
    image.save('.' + os.path.join(app.config['IMG_RECINTOS'], out_file))
    image.close()
    #return(out_file)


@app.route('/reportes', methods=['GET', 'POST'])
@login_required
def reportes():
    r = rep.Reportes(cxms)
    if 'Reportes - Consulta' in permisos_usr:
        return render_template('reportes.html', asientos=r.get_rep_asientos_all(usrdep), recintos=r.get_rep_recintos_all(usrdep), 
                                homologaciones=r.get_rep_homologacion_all(usrdep), homojurisds=r.get_rep_homojurisd_all(usrdep),
                                jurisdicciones=r.get_rep_jurisdiccion_all(usrdep), transacciones=r.get_rep_logtransaccion_all(usrdep), 
                                extasientos=r.get_rep_ext_asie_all(), extrecintos=r.get_rep_ext_reci_all(), 
                                puede_consultar='Reportes - Consulta' in permisos_usr)
    else:
        return render_template('reportes.html', puede_consultar='Reportes - Consulta' in permisos_usr)


@app.route('/rep_loc_habil', methods=['GET', 'POST'])
@login_required
def rep_loc_habil():
    r = rep.Reportes(cxms)
    if 'Reportes - Consulta' in permisos_usr:
        return render_template('rep_loc_habil.html', asientos=r.view_geoasientos_nacional_ant(usrdep))
    else:
        return render_template('home.html')


@app.route('/rep_reci_habil', methods=['GET', 'POST'])
@login_required
def rep_reci_habil():
    r = rep.Reportes(cxms)
    if 'Reportes - Consulta' in permisos_usr:
        return render_template('rep_reci_habil.html', recintos=r.view_georecintos_nacional_ant(usrdep))
    else:
        return render_template('home.html')


@app.route('/rep_loc_proc', methods=['GET', 'POST'])
@login_required
def rep_loc_proc():
    ''' vista: v_loc_nal_all de bd en proceso '''
    r = rep.Reportes(cxms)
    if 'Reportes - Consulta' in permisos_usr:
        return render_template('rep_loc_proc.html', locs=r.v_loc_nal_all(usrdep))
    else:
        return render_template('home.html')


@app.route('/rep_reci_proc', methods=['GET', 'POST'])
@login_required
def rep_reci_proc():
    ''' vista: ...  de v_reci_nal_all de bd en proceso '''
    r = rep.Reportes(cxms)
    if 'Reportes - Consulta' in permisos_usr:
        return render_template('rep_reci_proc.html', recintos=r.v_reci_nal_all(usrdep))
    else:
        return render_template('home.html')


@app.route('/gerencial_asi', methods=['GET', 'POST'])
@login_required
def gerencial_asi():
    g = ger.Gerencial(cxms)
    if 'Gerencial - Consulta' not in permisos_usr:
        return render_template('gerencial.html', puede_consultar='Gerencial - Consulta' in permisos_usr)
    else:
        if request.method == 'POST':
            if request.form['limpiar'] == 'limpiando':
                inicio = '00-00-0000'
                final = '00-00-0000'
                depto = 0
                usuario = 0
                accion = 0
                return render_template('gerencial.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=False, puede_consultar='Gerencial - Consulta' in permisos_usr)
            else:
                if request.form['inicio'] == "":
                    inicio = '00-00-0000'
                else:
                    inicio = request.form['inicio']

                if request.form['final'] == "":
                    final = '00-00-0000'
                else:
                    final = request.form['final']

                if request.form['dep'] != '0':
                    depto = usrdep
                else:
                    if request.form['depto'] == 'Seleccionar':
                        depto = 0
                    else:
                        depto = request.form['depto']

                if request.form['usua'] != '0':
                    usuario = current_user.usuario
                else:
                    if request.form['usuario'] == 'Seleccionar':    
                        usuario = 0
                    else:
                        user = request.form['usuario']
                        g.id_usuario(user)
                        usuario = g.usuario

                if request.form['accion'] == 0:    
                    accion = 0
                else:
                    accion = request.form['accion']

                rows = g.get_gerencial_asi(inicio, final, depto, usuario, accion)
                if rows:
                    return render_template('gerencial.html', asientos=rows, dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=True, inicio=inicio, final=final, depa=depto, us=usuario, accion=accion)  # render a template
                else:
                    print ('Sin registros en Asientos...')
                    return render_template('gerencial.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=False, inicio=inicio, final=final, depa=depto, us=usuario, accion=accion)
        else:
            inicio = '00-00-0000'
            final = '00-00-0000'
            depto = 0
            usuario = 0
            accion = 0 
            return render_template('gerencial.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=False, puede_consultar='Gerencial - Consulta' in permisos_usr)


@app.route('/gerencial_reci', methods=['GET', 'POST'])
@login_required
def gerencial_reci():
    g = ger.Gerencial(cxms)
    if 'Gerencial - Consulta' not in permisos_usr:
        return render_template('gerencial_reci.html', puede_consultar='Gerencial - Consulta' in permisos_usr)
    else:
        if request.method == 'POST':
            if request.form['accion'] == '0':    
                #return render_template('gerencial_reci.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=False, puede_consultar='Gerencial - Consulta' in permisos_usr)
                return render_template('gerencial_reci.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(),
                                       load=False, puede_consultar='Gerencial - Consulta' in permisos_usr,
                                       error = 'Previamente debe seleccionar la opción LISTADO DE CAMBIOS')
            else:
                accion = request.form['accion']

            if request.form['limpiar'] == 'limpiando':
                inicio = '00-00-0000'
                final = '00-00-0000'
                depto = 0
                usuario = 0
                accion = 0
                return render_template('gerencial_reci.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=False, puede_consultar='Gerencial - Consulta' in permisos_usr)
            else:
                if request.form['inicio'] == "":
                    inicio = '00-00-0000'
                else:
                    inicio = request.form['inicio']

                if request.form['final'] == "":
                    final = '00-00-0000'
                else:
                    final = request.form['final']

                if request.form['dep'] != '0':
                    depto = usrdep
                else:
                    if request.form['depto'] == 'Seleccionar':    
                        depto = 0
                    else:
                        depto = request.form['depto']

                if request.form['usua'] != '0':
                    usuario = current_user.usuario
                else:
                    if request.form['usuario'] == 'Seleccionar':    
                        usuario = 0
                    else:
                        user = request.form['usuario']
                        g.id_usuario(user)
                        usuario = g.usuario

                rows = g.get_gerencial_reci(inicio, final, depto, usuario, accion)
                if rows:
                    return render_template('gerencial_reci.html', recintos=rows, dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=True, inicio=inicio, final=final, depa=depto, us=usuario, accion=accion)  # render a template
                else:
                    return render_template('gerencial_reci.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=False, inicio=inicio, final=final, depa=depto, us=usuario, accion=accion)
        else:
            inicio = '00-00-0000'
            final = '00-00-0000'
            depto = 0
            usuario = 0
            accion = 0 
            return render_template('gerencial_reci.html', dptos=g.get_deptos_all(), usuarios=g.get_usuarios(), load=False, puede_consultar='Gerencial - Consulta' in permisos_usr)


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)

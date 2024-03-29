# Operaciones usuarios

class Usuarios:
    id = 0
    usuario = ''
    nombre = ''
    apellidos = ''
    email = ''
    password = ''
    dep = 0
    authenticated = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def add_usuario(self, usuario, nombre, apellidos, email, password, dep, authenticated, tusr):
        new_usuario = usuario, nombre, apellidos, email, password, dep, authenticated, tusr
        s = "insert into usuarios (usuario, nombre, apellidos, email, password, dep, authenticated, tipo_usr) values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_usuario)
        self.cx.commit()
        print("adicionado...")

    def get_usuario(self, usrtxt):
        s = "select * from usuarios where usuario = %s"
        self.cur.execute(s, usrtxt)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.id = row[0]
            self.usuario = row[1]
            self.nombre = row[2]
            self.apellidos = row[3]
            self.email = row[4]
            self.password = row[5]
            self.dep = row[6]
            self.authenticated = row[7]
            self.tipo_usr = row[8]
            return True

    def get_usuario_id(self, id):
        s = "select * from usuarios where id = %d"
        self.cur.execute(s, id)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.usuario = row[1]
            self.nombre = row[2]
            self.apellidos = row[3]
            self.email = row[4]
            self.password = row[5]
            self.dep = row[6]
            self.authenticated = row[7]
            self.tipo_usr = row[8]
            return True

    def get_usuario_usr(self, usr):
        s = "select * from usuarios where usuario = %s"
        self.cur.execute(s, usr)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.usuario = row[1]
            self.nombre = row[2]
            self.apellidos = row[3]
            self.email = row[4]
            self.password = row[5]
            self.dep = row[6]
            self.authenticated = row[7]
            self.tipo_usr = row[8]
            return True

    def get_usuarios(self):
        s = "select * from usuarios order by usuario"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
        '''
        if  rows == None:
            return False
        else:
            return rows
        '''

    def del_usuario(self, id):
        s = "delete from usuarios where id = %d"
        try:
            self.cur.execute(s, id)
            self.cx.commit()
            print('Usuario eliminado')
        except:
             print("Error --DEL-- usuario...")

    def upd_usuario(self, id, nombre, apellidos, email, dep, authenticated, tusr):
        upd_usuario = (nombre, apellidos, email, dep, authenticated, tusr, id)
        s = "update usuarios " + \
            " set nombre= %s, apellidos= %s, email= %s, dep= %d, authenticated= %d, tipo_usr= %d " + \
            " where id = %d"
        try:
            self.cur.execute(s, upd_usuario)
            self.cx.commit()
            print('Usuario actualizado')
        except:
            print("Error --UPD-- usuario...")

    def upd_pwd_usuario(self, usuario, password):
        upd_usuario = (password, usuario)
        s = "update usuarios " + \
            " set password= %s "  + \
            " where usuario = %s"
        try:
            self.cur.execute(s, upd_usuario)
            self.cx.commit()
            print('Password actualizado')
        except:
            print("Error --UPD-- password usuario...")

    def get_permisos(self, usuario_id):
        """ Retorna list con permisos asignados a usuario """
        s = "select b.modulo " + \
	    "from permisos a, modulos b " + \
	    "where a.modulo_id = b.id  and a.usuario_id = %d "
        try:
            self.cur.execute(s, usuario_id)
            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                permisos = []
                for p in rows:
                    permisos.append(p[0])
                return permisos
        except Exception as e:
            print('Error -get_permisos-')
            print(e)

    def get_permisos_name(self, usuario):
        """ Retorna list con permisos asignados a usuario """
        s = "select b.modulo " + \
	    "from permisos a, modulos b, usuarios c " + \
	    "where a.modulo_id = b.id  and a.usuario_id = c.id and c.usuario=%s "
        try:
            self.cur.execute(s, usuario)
            rows = self.cur.fetchall()
            permisos = []
            if rows:
                for p in rows:
                    permisos.append(p[0])
            return permisos
        except Exception as e:
            print('Error -get_permisos_name-')
            print(e)


    def get_tipo_usuario(self):
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=16"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_id(self):
        """return the email address to satisfy Flask-Login's requirements."""
        #return self.email
        return str(self.usuario)

    def is_active(self):
        """True, as all users are active."""
        return True


    def is_authenticated(self):
        """Return True if the user is authenticated."""
        if (self.authenticated==1):
            return True
        else:
            return False

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False

    def __str__(self):
        return self.nombre + ' ' + self.apellidos


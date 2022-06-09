# Operaciones permisos

class Permisos:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_permisos_de_usuario(self, id):
        s = "select b.id, b.modulo from permisos a, modulos b where b.id= a.modulo_id and a.usuario_id = %d order by a.modulo_id"
        self.cur.execute(s, id)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def reset_permisos_de_usuario(self, id):
        s = "delete from permisos where  usuario_id = %d"
        self.cur.execute(s, id)
        self.cx.commit()


    def get_modulos(self):
        s = "select * from modulos order by id"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_modulos_sin_asignar(self, id):
        s = "select * from modulos where id not in (select modulo_id from permisos where usuario_id= %d)"
        self.cur.execute(s, id)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def save_permisos_txt(self, usuario_id, txt):
        asignados = list(txt.split("|"))

        for modulo_id in asignados:
            new_permiso = usuario_id, modulo_id
            s = "insert into permisos (usuario_id, modulo_id) values " + \
                " (%s, %s) "
            self.cur.execute(s, new_permiso)
        self.cx.commit()


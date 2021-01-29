# Operaciones usuarios

class Grupo:
    idClasifGrupo = 0
    Descripcion = ''
    
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()
    
    def get_clas_grupos_all(self, usrdep):

        s = "SELECT idClasifGrupo, descripcion FROM [GeografiaElectoral_app].[dbo].[clasifGrupo]"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_clas_grupo_idclasGrup(self, idClasifGrupo):
        s = "SELECT idClasifGrupo, descripcion " + \
                "from [GeografiaElectoral_app].[dbo].[clasifGrupo] where idClasifGrupo = %d "
        self.cur.execute(s, idClasifGrupo)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idClasifGrupo = row[0]
            self.Descripcion = row[1]
            return True

    def add_clas_grupo(self, idClasifGrupo, Descripcion):
        new_clas_grupo = idClasifGrupo, Descripcion
        s = "insert into GeografiaElectoral_app.dbo.clasifGrupo (idClasifGrupo, Descripcion) values " + \
            " (%s, %s) "
        self.cur.execute(s, new_clas_grupo)
        self.cx.commit()
        print("adicionado...grupo")

    def upd_grupo(self, idClasifGrupo, Descripcion):
        new_clas_grupo = Descripcion, idClasifGrupo
        s = "update [GeografiaElectoral_app].[dbo].[clasifGrupo]" + \
            " set Descripcion= %s" + \
            " where [GeografiaElectoral_app].[dbo].[clasifGrupo].idClasifGrupo = %d"
        try:
            self.cur.execute(s, new_clas_grupo)
            self.cx.commit()
            print('grupo actualizado')
        except Exception as e:
            print("Error - actualización de grupo")
            print(e)
    
    def get_next_idgrupo(self):
        self.cur.execute("select  max(GeografiaElectoral_app.dbo.clasifGrupo.idClasifGrupo) + 1  from GeografiaElectoral_app.dbo.clasifGrupo")
        row = self.cur.fetchone()
        return row[0]

    
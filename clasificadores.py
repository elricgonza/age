# Operaciones usuarios

class Clasificador:
    idClasif = 0
    descripcion = ''
    clasifGrupoId = 0
    clasifSubGrupo = ''
    
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()
    
    def get_clas_all(self, usrdep):

        s = "SELECT    GeografiaElectoral_app.dbo.clasif.idClasif, GeografiaElectoral_app.dbo.clasifGrupo.descripcion AS Grupo, GeografiaElectoral_app.dbo.clasif.descripcion AS Descripcion " + \
            "FROM GeografiaElectoral_app.dbo.clasif INNER JOIN GeografiaElectoral_app.dbo.clasifGrupo ON GeografiaElectoral_app.dbo.clasif.clasifGrupoId = GeografiaElectoral_app.dbo.clasifGrupo.idClasifGrupo "
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_clas_idclas(self, clasifGrupoId):
        s = "SELECT idClasif,descripcion,clasifGrupoId,clasifSubGrupo FROM [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId = %d" 
        self.cur.execute(s, clasifGrupoId)
        row = self.cur.fetchall()
        if  self.cur.rowcount == 0:
            print('filas vacias')
            return row
        else:
            print('filas llenas')
            return row

    def get_clas_id(self, idClasif):
        s = "SELECT  idClasif,descripcion,clasifGrupoId,clasifSubGrupo  " + \
                "from [GeografiaElectoral_app].[dbo].[clasif] where idClasif = %d "
        self.cur.execute(s, idClasif)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idClasif = row[0]
            self.descripcion = row[1]
            self.clasifGrupoId = row[2]
            self.clasifSubGrupo = row[3]

            return True

    def add_clas(self, idClasif,descripcion,clasifGrupoId,clasifSubGrupo):
        new_clas = idClasif,descripcion,clasifGrupoId,clasifSubGrupo
        s = "insert into GeografiaElectoral_app.dbo.clasif (idClasif,descripcion,clasifGrupoId,clasifSubGrupo) values (%s, %s, %s, %s)"
        self.cur.execute(s, new_clas)
        self.cx.commit()
        print("adicionado...grupo")
                       


    def upd_clas(self, idClasif,descripcion,clasifSubGrupo):
        new_clas = descripcion,clasifSubGrupo,idClasif
        s = "update GeografiaElectoral_app.dbo.clasif " + \
            "set descripcion= %s, clasifSubGrupo= %s " + \
            "where GeografiaElectoral_app.dbo.clasif.idClasif = %d"
        try:
            self.cur.execute(s, new_clas)
            self.cx.commit()
            print('clasificador actualizado')
        except Exception as e:
            print("Error - actualización de clasificador")
            print(e)
    

    def del_clas(self, id):
        '''Elimina clasificador '''

        s = "delete from GeografiaElectoral_app.dbo.clasif where idClasif = %d"
        try:
            self.cur.execute(s, id)
            self.cx.commit()
            print('Clasificador eliminado')
        except Exception as e:
             print("Error --DEL--clasificador ...")
             print(e)


    def get_next_idclas(self):
        self.cur.execute("select max(GeografiaElectoral_app.dbo.clasif.idClasif) + 1 from GeografiaElectoral_app.dbo.clasif")
        row = self.cur.fetchone()
        return row[0]

    

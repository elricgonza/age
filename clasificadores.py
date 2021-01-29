# Operaciones usuarios

class Clasificador:
    idClasif = 0
    descripcion = ''
    subgrupo = ''
    clasifGrupoId = 0
    
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
        s = "SELECT idClasif,descripcion,subgrupo,clasifGrupoId FROM [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId = %d" 
        self.cur.execute(s, clasifGrupoId)
        row = self.cur.fetchall()
        if  self.cur.rowcount == 0:
            print('filas vacias')
            return row
        else:
            print('filas llenas')
            return row

    def get_clas_id(self, idClasif):
        s = "SELECT  idClasif,descripcion,subgrupo,clasifGrupoId  " + \
                "from [GeografiaElectoral_app].[dbo].[clasif] where idClasif = %d "
        self.cur.execute(s, idClasif)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idClasif = row[0]
            self.descripcion = row[1]
            self.subgrupo = row[2]
            self.clasifGrupoId = row[3]
            return True

    def add_clas(self, idClasif,descripcion,subgrupo,clasifGrupoId):
        new_clas = idClasif,descripcion,subgrupo,clasifGrupoId
        print('INSERT CLASIF AD')
        print(new_clas)
        s = "insert into GeografiaElectoral_app.dbo.clasif (idClasif,descripcion,subgrupo,clasifGrupoId) values (%s, %s, %s, %s)"
        self.cur.execute(s, new_clas)
        self.cx.commit()
        print("adicionado...grupo")
                       


    def upd_clas(self, idClasif,descripcion,subgrupo):
        new_clas = descripcion,subgrupo,idClasif
        print('NEW CLASS')
        print(new_clas)
        s = "update GeografiaElectoral_app.dbo.clasif " + \
            "set descripcion= %s, subgrupo= %s " + \
            "where GeografiaElectoral_app.dbo.clasif.idClasif = %d"
        try:
            self.cur.execute(s, new_clas)
            self.cx.commit()
            print('clasificador actualizado')
        except Exception as e:
            print("Error - actualización de clasificador")
            print(e)
    
    def get_next_idclas(self):
        self.cur.execute("select max(GeografiaElectoral_app.dbo.clasif.idClasif) + 1 from GeografiaElectoral_app.dbo.clasif")
        row = self.cur.fetchone()
        return row[0]

    
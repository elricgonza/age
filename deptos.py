# Operaciones Departamentos

class Departamento:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_deptos(self, usrdep):
            s = "select Dep, NomDep from [GeografiaElectoral_app].[dbo].[DEP]"
            if usrdep != 0 :
                s = s + " where Dep = %d "
                self.cur.execute(s, usrdep)
            else:
                s = s + " order by Dep"
                self.cur.execute(s)

            rows = self.cur.fetchall()
            return rows


    def get_deptos_all(self, usrdep):
            s = "SELECT DEP.Dep, PAIS.IdPais, PAIS.NomPais, DEP.NomDep " + \
                "FROM  [GeografiaElectoral_app].[dbo].[DEP] INNER JOIN [GeografiaElectoral_app].[dbo].[PAIS] ON  " + \
                "[GeografiaElectoral_app].[dbo].[DEP].IdPais = [GeografiaElectoral_app].[dbo].[PAIS].IdPais"
            self.cur.execute(s)
            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_depto_iddep(self, Dep):
        s = "select Dep, NomDep, Diputados, DiputadosUninominales, IdPais, fechaIngreso, fechaAct, usuario, descNivelId " + \
                " from [GeografiaElectoral_app].[dbo].[DEP] where Dep = %d "
        self.cur.execute(s, Dep)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dep = row[0]
            self.nomDep = row[1]
            self.diputados = row[2]
            self.diputadosUninominales = row[3]
            self.idPais = row[4]
            self.fechaIngreso = row[5]
            self.fechaAct = row[6]
            self.usuario = row[7]
            self.descNivelId = row[8]

            return True

    def add_depto(self, Dep, NomDep, Diputados, DiputadosUninominales, IdPais, descNivelId, fechaIngreso, fechaAct, usuario):
        new_depto = Dep, NomDep, Diputados, DiputadosUninominales, IdPais, descNivelId, fechaIngreso, fechaAct, usuario
        s = "insert into GeografiaElectoral_app.dbo.Dep (Dep, NomDep, Diputados, DiputadosUninominales, IdPais, descNivelId, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        self.cur.execute(s, new_depto)
        self.cx.commit()

    def upd_depto(self, dep, nomDep, diputados, diputadosUninominales, idPais, descNivelId, fechaAct, usuario):
        new_depto = nomDep, diputados, diputadosUninominales, idPais, descNivelId, fechaAct, usuario,  dep
        s = "update [GeografiaElectoral_app].[dbo].[DEP]" + \
            " set NomDep= %s, Diputados= %s, DiputadosUninominales= %s, IdPais= %s, " + \
            " descNivelId= %s, fechaAct= %s, usuario= %s " + \
            " where [GeografiaElectoral_app].[dbo].[DEP].Dep = %d"
        try:
            self.cur.execute(s, new_depto)
            self.cx.commit()
            print('depto actualizado')
        except Exception as e:
            print("Error - actualización de depto")
            print(e)
    
    def get_next_iddep(self):
        self.cur.execute("select max(Dep) + 1 from GeografiaElectoral_app.dbo.dep")
        row = self.cur.fetchone()
        return row[0]

    def get_combo_paises(self, usrdep):
        s = "select IdPais, NomPais from GeografiaElectoral_app.dbo.PAIS where Estado = 1 order by NomPais;"             
        self.cur.execute(s) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows    

    def get_combo_desc_nivel(self, usrdep):
        s = "SELECT idClasif, descripcion, clasifSubGrupo FROM [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=15"             
        self.cur.execute(s) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_desc_nivel_all(self, sgrupo):
        s = "SELECT idClasif, descripcion FROM [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=15 and clasifSubGrupo=%d"             
        self.cur.execute(s, sgrupo) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows 


    def get_deptos_nal(self):
        ''' Retorna cod y nombre de deptos nacional '''
        s = "select dep, nomdep from [GeografiaElectoral_app].[dbo].[dep] where dep < 10 order by dep "
        self.cur.execute(s)
        return self.cur.fetchall()

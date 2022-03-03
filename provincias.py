# Operaciones provincias

class Prov:
    DepProv = 0
    Prov = 0
    NomProv = ''
    codprov = 0
    fechaIngreso = ''
    fechaAct = ''
    usuario = ''
    DescNivelId = ''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()
    
    def get_provs_all(self, usrdep):
            s = "select pa.NomPais, d.NomDep, p.DepProv, p.Prov, p.NomProv from [GeografiaElectoral_app].[dbo].[PROV] p" + \
                " inner join [GeografiaElectoral_app].[dbo].[DEP] d on p.DepProv=d.Dep" + \
                " inner join [GeografiaElectoral_app].[dbo].[PAIS] pa on d.IdPais=pa.IdPais"
            self.cur.execute(s)
            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_provs_id(self, iddepprov, idprov):
        varAux = iddepprov, idprov
        s = "select pa.IdPais, p.DepProv, p.Prov, p.NomProv, p.codprov, p.fechaIngreso, p.fechaAct, p.usuario, p.descNivelId" + \
            " from [GeografiaElectoral_app].[dbo].[PROV] p inner join [GeografiaElectoral_app].[dbo].[DEP] d" + \
            " on p.DepProv=d.Dep inner join [GeografiaElectoral_app].[dbo].[PAIS] pa on d.IdPais=pa.IdPais" + \
            " where p.DepProv = %d  and p.prov = %d"
        self.cur.execute(s, varAux)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.IdPais = row[0]
            self.DepProv = row[1]
            self.Prov = row[2]
            self.NomProv = row[3]
            self.codprov = row[4]
            self.fechaingreso = row[5]
            self.fechaactual = row[6]
            self.usuario = row[7]
            self.descNivelId = row[8]
            return True

    def add_prov(self, depto, Prov, NomProv, codprov, descNivelId, fechaIngreso, fechaAct, usuario):
        new_prov = depto, Prov, NomProv, codprov, descNivelId,fechaIngreso, fechaAct, usuario
        s = "insert into GeografiaElectoral_app.dbo.prov(DepProv, Prov, NomProv, codprov, descNivelId, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_prov)
        self.cx.commit()
        print("adicionado...Provincias")

    def upd_prov(self, DepProv, Prov, NomProv, codprov, descNivelId, fechaAct, usuario):
        new_prov = NomProv, codprov, descNivelId, fechaAct, usuario, DepProv, Prov
        s = "update [GeografiaElectoral_app].[dbo].[PROV]" + \
            " set NomProv= %s, codprov= %s, descNivelId=%s, " + \
            " fechaAct= %s, usuario= %s " + \
            " where [GeografiaElectoral_app].[dbo].[PROV].DepProv = %d and " + \
            "  [GeografiaElectoral_app].[dbo].[PROV].Prov = %d "
        try:
            self.cur.execute(s, new_prov)
            self.cx.commit()
            print('provincia actualizado')
        except Exception as e:
            print("Error - actualización de provincia")
            print(e)
    
    def get_next_idprov(self, depto_id):
        self.cur.execute("select max(prov) + 1 from GeografiaElectoral_app.dbo.prov where DepProv=%d", depto_id)
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

    def get_combo_deptos(self, usrdep):
        s = "SELECT Dep, NomDep, IdPais FROM [GeografiaElectoral_app].[dbo].[DEP] order by IdPais;"             
        self.cur.execute(s) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows   
 
    def get_depto_idPais(self, Dep):
        s = "select Dep, NomDep, Diputados, DiputadosUninominales, IdPais, fechaIngreso, fechaAct, usuario " + \
                " from [GeografiaElectoral_app].[dbo].[DEP] where IdPais = %d "
        self.cur.execute(s, Dep)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dep = row[0]
            self.nomDep = row[1]
        return True

    def get_combo_desc_nivel(self, usrdep):
        s = "SELECT idClasif, descripcion, clasifSubGrupo FROM [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=15"             
        self.cur.execute(s) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_desc_nivel_prov_all(self, sgrupo):
        s = "SELECT idClasif, descripcion FROM [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=15 and clasifSubGrupo=%d"             
        self.cur.execute(s, sgrupo) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
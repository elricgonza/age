# Operaciones SECCIONES

class Municipio:
    DepSec = 0
    ProvSec = 0
    Sec = 0
    NumConceSec = 0
    NomSec = ''
    CircunSec = 0
    CodProv = 0
    CodSecc = 0
    fechaIngreso = ''
    fechaAct = ''
    usuario = ''
    DescNivelId = ''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()
    
    def get_mun_all(self, usrdep):
        s = "SELECT pa.IdPais, d.Dep, p.prov, s.Sec, pa.NomPais, d.NomDep, p.NomProv, s.NomSec " + \
            "from [GeografiaElectoral_app].[dbo].[SEC] s " + \
            "inner join [GeografiaElectoral_app].[dbo].[PROV] p on s.ProvSec=p.Prov " + \
            "inner join [GeografiaElectoral_app].[dbo].[DEP] d on d.Dep=p.DepProv and d.Dep=s.DepSec " + \
            "inner join [GeografiaElectoral_app].[dbo].[PAIS] pa on pa.IdPais=d.IdPais"
            
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_mun_id(self, idDepSec, idProvSec, idSec):
        varAux = idDepSec, idProvSec, idSec
        s = "SELECT pa.IdPais, s.DepSec, s.ProvSec, s.Sec, s.NumConceSec, s.NomSec, s.CircunSec, s.CodProv, s.CodSecc, s.fechaIngreso, s.fechaAct, s.usuario, s.descNivelId " + \
            "FROM [GeografiaElectoral_app].[dbo].[SEC] AS s INNER JOIN [GeografiaElectoral_app].[dbo].[DEP] AS d " + \
            "ON s.DepSec = d.Dep INNER JOIN [GeografiaElectoral_app].[dbo].[PAIS] AS pa ON d.IdPais = pa.IdPais " + \
            "WHERE(s.DepSec = %d) AND (s.ProvSec = %d) AND (s.Sec = %d)"
        
        self.cur.execute(s, varAux)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.IdPais = row[0]
            self.DepSec = row[1]
            self.ProvSec = row[2]
            self.Sec = row[3]
            self.NumConceSec = row[4]            
            self.NomSec = row[5]
            self.CircunSec = row[6]
            self.CodProv = row[7]
            self.CodSecc = row[8]

            self.fechaIngreso = row[9]
            self.fechaAct = row[10]
            self.usuario = row[11]
            self.descNivelId = row[12]
            return True

    def add_mun(self, DepSec, ProvSec, Sec, NumConceSec, NomSec,descNivelId, fechaIngreso, fechaAct, usuario):
        new_mun =  DepSec, ProvSec, Sec, NumConceSec, NomSec, descNivelId, fechaIngreso, fechaAct, usuario
        s = "insert into GeografiaElectoral_app.dbo.sec(DepSec, ProvSec, Sec, NumConceSec, NomSec, descNivelId,fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s,%s, %s, %s) "
        self.cur.execute(s, new_mun)
        self.cx.commit()
        print("adicionado...municipio")

    def upd_mun(self, DepSec, ProvSec, Sec, NumConceSec, NomSec, descNivelId, fechaAct, usuario):
        new_mun = NumConceSec, NomSec, descNivelId, fechaAct, usuario, DepSec, ProvSec, Sec
        s = "update [GeografiaElectoral_app].[dbo].[SEC]" + \
            " set NumConceSec= %s, NomSec= %s, descNivelId= %s, " + \
            " fechaAct= %s, usuario= %s " + \
            " where [GeografiaElectoral_app].[dbo].[SEC].DepSec = %d and " + \
            " [GeografiaElectoral_app].[dbo].[SEC].ProvSec = %d and " + \
            " [GeografiaElectoral_app].[dbo].[SEC].Sec = %d"
        try:
            self.cur.execute(s, new_mun)
            self.cx.commit()
            print('municipio actualizado')
        except Exception as e:
            print("Error - actualización de municipio")
            print(e)
    
    def get_next_idmun(self, depto, prov):
        new_mun = depto, prov
        s = "select max(sec) + 1 from GeografiaElectoral_app.dbo.sec where DepSec=%d and ProvSec=%d"
        self.cur.execute(s, new_mun)
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
    
    def get_combo_prov_new(self, usrdep):
        s = "SELECT Prov, NomProv, DepProv FROM [GeografiaElectoral_app].[dbo].[PROV] order by DepProv;"             
        self.cur.execute(s) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_combo_prov(self, DepSec, ProvSec):
        new_prov = DepSec, ProvSec
        s = "SELECT Prov, NomProv, DepProv FROM [GeografiaElectoral_app].[dbo].[PROV] where [GeografiaElectoral_app].[dbo].[PROV].DepProv = %s and [GeografiaElectoral_app].[dbo].[PROV].Prov = %s;"      
        self.cur.execute(s,new_prov) 
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

    def get_desc_nivel_mun_all(self, sgrupo):
        s = "SELECT idClasif, descripcion FROM [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=15 and clasifSubGrupo=%d"             
        self.cur.execute(s, sgrupo) 
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows 
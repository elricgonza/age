# Operaciones asientos

class Zonas:
    idlocreci=0
    reci=0
    nomreci=''
    idloc=0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_zonas_all(self, usrdep):        
        s = "select d.IdLocDist, l.NomLoc, d.Dist, d.CircunDist, d.NomDist from [GeografiaElectoral_app].[dbo].[DIST] d " + \
            "left join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=d.IdLocDist "
        if usrdep != 0 :
            s = s + " where l.DepLoc = %d order by d.IdLocDist, d.Dist"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by d.IdLocDist, d.Dist"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_next_zona(self, idloc):
        s = "select max(zona) + 1 from GeografiaElectoral_app.dbo.zona where IdLocZona = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]


    def get_next_dist(self, idloc):
        s = "select max(dist) + 1 from GeografiaElectoral_app.dbo.dist where IdLocDist = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]


    def add_zona(self, idloczona, zona, nomzona, distzona, fecharegistro, usuario, fechaingreso):
        new_zona = idloczona, zona, nomzona, distzona, fecharegistro, usuario, fechaingreso
        s = "insert into GeografiaElectoral_app.dbo.zona (IdLocZona, Zona, NomZona, DistZona, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_zona)
        self.cx.commit()
        print("adicionado...")


    def add_dist(self, idlocdist, dist, circundist, nomdist, fecharegistro, usuario, fechaingreso):
        new_dist = idlocdist, dist, circundist, nomdist, fecharegistro, usuario, fechaingreso
        s = "insert into GeografiaElectoral_app.dbo.dist (IdLocDist, Dist, CircunDist, NomDist, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_dist)
        self.cx.commit()
        print("adicionado...")
    

    def upd_zona(self, idloczona, idzona, nomzona, fa, usuario):        
        upd_zona = (idloczona, nomzona, fa, usuario, idzona)   
        s = "update GeografiaElectoral_app.dbo.zona " + \
            " set IdLocZona = %d, NomZona = %s, fechaAct = %s, usuario = %s" + \
            " where Zona = %d"
        try:
            self.cur.execute(s, upd_zona)
            self.cx.commit()
            print('Zona actualizada')
        except:
            print("Error --UPD-- Zona...")


    def upd_dist(self, idlocdist, iddist, circundist, nomdist, fa, usuario):        
        upd_dist = (circundist, nomdist, fa, usuario, idlocdist, iddist) 
        s = "update GeografiaElectoral_app.dbo.dist set CircunDist = %s, NomDist = %s, fechaAct = %s, usuario = %s" + \
            " where IdLocDist = %d and Dist = %d"
        try:
            self.cur.execute(s, upd_dist)
            self.cx.commit()
            print('Distrito actualizado')
        except:
            print("Error --UPD-- Distrito...")


    def get_zonadist_idloc(self, idloc, iddist):
        up_zonadist = idloc, iddist
        s = "select l.IdLoc, l.NomLoc, d.Dist, d.CircunDist, d.NomDist, d.fechaIngreso, d.fechaAct, d.usuario " + \
            "from [GeografiaElectoral_app].[dbo].[DIST] d " + \
            "left join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=d.IdLocDist " + \
            "where d.IdLocDist= %d and d.Dist= %d"
        self.cur.execute(s, up_zonadist)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.nomloc = row[1]
            self.dist = row[2]
            self.circundist = row[3]
            self.nomdist = row[4]
            self.fechaIngreso = row[5]
            self.fechaAct = row[6]
            self.usuario = row[7]
            return True


    def asientoz(self, azona):
        s = "select IdLoc, NomLoc from [GeografiaElectoral_app].[dbo].[LOC]" + \
            "where IdLoc= %d"
        self.cur.execute(s, azona)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.nomloc = row[1]
            return True

    def get_nomdist(self, idloc, nomdist):
        con = idloc, nomdist
        s = "select NomDist from [GeografiaElectoral_app].[dbo].[DIST]" + \
            "where IdLocDist= %d and Dist= %d"
        self.cur.execute(s, con)
        row = self.cur.fetchone()
        return row[0]

    def get_ultimodist(self, idloc):
        s = "select max(dist) from GeografiaElectoral_app.dbo.dist where IdLocDist = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]

    

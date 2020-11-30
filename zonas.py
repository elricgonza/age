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
        s = "select z.IdLocZona, l.NomLoc, z.Zona, z.NomZona, d.Dist, d.CircunDist, d.NomDist from [GeografiaElectoral_app].[dbo].[ZONA] z " + \
            "inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist " + \
            "left join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
        if usrdep != 0 :
            s = s + " where l.DepLoc = %d order by z.Zona"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by z.Zona"
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
        upd_dist = (idlocdist, circundist, nomdist, fa, usuario, iddist) 
        s = "update GeografiaElectoral_app.dbo.dist set IdLocDist = %d, CircunDist = %s, NomDist = %s, fechaAct = %s, usuario = %s" + \
            " where Dist = %d"
        try:
            self.cur.execute(s, upd_dist)
            self.cx.commit()
            print('Distrito actualizado')
        except:
            print("Error --UPD-- Distrito...")


    def get_zonadist_idloc(self, idloc, idzona, iddist):
        up_zonadist = idloc, idzona, idloc, iddist
        s = "select z.IdLocZona, l.NomLoc, z.Zona, z.NomZona, d.Dist, d.CircunDist, d.NomDist, z.fechaIngreso, z.fechaAct, z.usuario " + \
            "from [GeografiaElectoral_app].[dbo].[ZONA] z " + \
            "inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist " + \
            "left join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist " + \
            "where z.IdLocZona= %d and z.Zona= %d and d.IdLocDist= %d and d.Dist= %d"
        self.cur.execute(s, up_zonadist)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.nomloc = row[1]
            self.zona = row[2]
            self.nomzona = row[3]
            self.dist = row[4]
            self.circundist = row[5]
            self.nomdist = row[6]
            self.fechaIngreso = row[7]
            self.fechaAct = row[8]
            self.usuario = row[9]
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

    
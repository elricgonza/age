# Operaciones asientos

class Zon:
    idlocreci=0
    reci=0
    nomreci=''
    idloc=0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_zon_all(self, usrdep):        
        s = "select l.IdLoc, r.Reci, z.NomZona, d.Dist, d.NomDist, d.CircunDist, z.Zona from [GeografiaElectoral_app].[dbo].[RECI] r" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on r.IdLocReci=l.IdLoc" + \
            " left join [GeografiaElectoral_app].[dbo].[ZONA] z on r.IdLocReci= z.IdLocZona and r.ZonaReci = z.Zona" + \
            " left join [GeografiaElectoral_app].[dbo].[DIST] d on r.IdLocReci= d.IdLocDist and z.DistZona = d.Dist"
        if usrdep != 0 :
            s = s + " where r.estado in (1, 2, 79, 80) and l.DepLoc = %d order by l.IdLoc, l.NomLoc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where r.estado in (1, 2, 79, 80) order by l.IdLoc, l.NomLoc"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_zon_idloc(self, idloczona, idzon):
        up_zonadist = idloczona, idzon
        s = "select l.IdLoc, l.NomLoc, z.Zona, z.NomZona, z.DistZona, z.fechaIngreso, z.fechaAct, z.usuario, d.CircunDist" + \
            " from [GeografiaElectoral_app].[dbo].[RECI] r" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on r.IdLocReci=l.IdLoc" + \
            " left join [GeografiaElectoral_app].[dbo].[ZONA] z on r.IdLocReci= z.IdLocZona and r.ZonaReci = z.Zona" + \
            " left join [GeografiaElectoral_app].[dbo].[DIST] d on r.IdLocReci= d.IdLocDist and z.DistZona = d.Dist" + \
            " where z.IdLocZona= %d and z.Zona= %d"
        self.cur.execute(s, up_zonadist)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.nomloc = row[1]
            self.idzon = row[2]
            self.nomzona = row[3]
            self.distzona = row[4]
            self.fechaIngreso = row[5]
            self.fechaAct = row[6]
            self.usuario = row[7]
            self.circundist = row[8]
            return True

    def get_next_zon(self, idloc):
        s = "select isnull(max(zona), 0)+1 from GeografiaElectoral_app.dbo.zona where IdLocZona = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]
    
    def add_zon(self, idloczona, zona, nomzona, distzona, fecharegistro, usuario, fechaingreso):
        new_zona = idloczona, zona, nomzona, distzona, fecharegistro, usuario, fechaingreso
        s = "insert into GeografiaElectoral_app.dbo.zona (IdLocZona, Zona, NomZona, DistZona, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_zona)
        self.cx.commit()
        print("adicionado...")

    def upd_zon(self, idloczona, idzona, nomzona, distzona, fa, usuario):      
        upd_zona = (nomzona, distzona, fa, usuario, idloczona, idzona)   
        s = "update GeografiaElectoral_app.dbo.zona " + \
            " set NomZona = %s, DistZona = %s, fechaAct = %s, usuario = %s" + \
            " where IdLocZona = %d and Zona = %d"
        try:
            self.cur.execute(s, upd_zona)
            self.cx.commit()
            print('Zona actualizada')
        except:
            print("Error --UPD-- Zona...")

    def get_circundist(self, idloc, circd):        
        s = "select CircunDist, NombreRecinto from [bdge].[dbo].[GeoRecintos_all] where idEstado in (1, 2, 79, 80) and IdLoc = %d" + \
            " and CircunDist = %d order by Dist"
        consulta = idloc, circd
        self.cur.execute(s, consulta)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

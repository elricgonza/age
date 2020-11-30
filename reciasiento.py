# Operaciones asientos

class Reciasiento:
    deploc = 0
    provloc = 0
    secloc = 0
    nomloc = ""

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_asientos_all(self, usrdep):        
        s = "select DepLoc, ProvLoc, SecLoc, IdLoc, NomLoc from [GeografiaElectoral_app].[dbo].[LOC]"
        if usrdep != 0 :
            s = s + " where DepLoc = %d order by NomLoc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by NomLoc"
            print(s)
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_zonas_all(self, usrdep):        
        s = "select z.IdLocZona, z.Zona, z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
        if usrdep != 0 :
            s = s + " where l.DepLoc = %d order by z.NomZona"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by z.NomZona"
            print(s)
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    
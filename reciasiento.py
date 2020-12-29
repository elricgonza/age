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
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_asientos_all1(self, usrdep, dep, prov, secc):        
        s = "select DepLoc, ProvLoc, SecLoc, IdLoc, NomLoc from [GeografiaElectoral_app].[dbo].[LOC]"
        if usrdep != 0 :
            asie = dep, prov, secc, usrdep
            s = s + " where DepLoc = %d and ProvLoc = %d and SecLoc = %d and DepLoc = %d and TipoLocLoc in (2, 3) order by NomLoc"
            self.cur.execute(s, asie)
        else:
            asie = dep, prov, secc
            s = s + " where DepLoc = %d and ProvLoc = %d and SecLoc = %d and TipoLocLoc in (2, 3) order by NomLoc"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_asientos_all2(self, usrdep, dep, prov, secc):        
        s = "select DepLoc, ProvLoc, SecLoc, IdLoc, NomLoc from [GeografiaElectoral_app].[dbo].[LOC]"
        if usrdep != 0 :
            asie = dep, prov, secc, usrdep
            s = s + " where DepLoc = %d and ProvLoc = %d and SecLoc = %d and DepLoc = %d order by NomLoc"
            self.cur.execute(s, asie)
        else:
            asie = dep, prov, secc
            s = s + " where DepLoc = %d and ProvLoc = %d and SecLoc = %d order by NomLoc"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_zonas_all(self, usrdep):        
        s = "select l.IdLoc, z.Zona, z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
        if usrdep != 0 :
            s = s + " where l.DepLoc = %d order by z.NomZona"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by z.NomZona"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_zonas_all1(self, usrdep, idloc, circun):        
        s = "select l.IdLoc, z.Zona, z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
        if usrdep != 0 :
            zon = idloc, usrdep
            s = s + " where l.Idloc = %d and l.DepLoc = %d order by z.NomZona"
            self.cur.execute(s, zon)
        else:
            zon = idloc
            s = s + " where l.Idloc = %d order by z.NomZona"
            self.cur.execute(s, zon)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_distritos_all(self, circun, idlocreci):        
        s = "select IdLocDist, Dist, CircunDist, NomDist from [GeografiaElectoral_app].[dbo].[DIST] where CircunDist = %d and IdLocDist = %d order by Dist"
        consulta = circun, idlocreci
        self.cur.execute(s, consulta)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_geoesp_all(self, lat, long):
        s = "select l.IdLoc, l.DepLoc, d.NomDep, l.ProvLoc, p.NomProv, l.SecLoc, s.NomSec, c.Circun" + \
            " from GeografiaElectoral_app.dbo.LOC l" + \
            " left join GeografiaElectoral_app.dbo.DEP d on l.DepLoc=d.Dep" + \
            " left join GeografiaElectoral_app.dbo.PROV p on l.ProvLoc=p.Prov and l.DepLoc=p.DepProv" + \
            " left join GeografiaElectoral_app.dbo.SEC s on l.SecLoc=s.Sec and l.ProvLoc=s.ProvSec and l.DepLoc=s.DepSec" + \
            " left join GeografiaElectoral_app.dbo.ZONA z on l.IdLoc=z.IdLocZona" + \
            " left join GeografiaElectoral_app.dbo.DIST di on l.IdLoc=di.IdLocDist and z.DistZona=di.Dist" + \
            " left join GeografiaElectoral_app.dbo.Circun c on l.DepLoc=c.DepCircun and di.CircunDist=c.Circun" + \
            " where l.latitud = %s and l.longitud = %s" + \
            " group by l.IdLoc, l.DepLoc, d.NomDep, l.ProvLoc, p.NomProv, l.SecLoc, s.NomSec, c.Circun"
        coord = lat, long
        self.cur.execute(s, coord)
        row = self.cur.fetchone()
        if row == None:
            return False
        else:
            self.dep = row[1]
            self.departamento = row[2]
            self.prov = row[3]
            self.provincia = row[4]
            self.sec = row[5]
            self.municipio = row[6]
            self.nrocircun = row[7]
            return True

    def get_pueblos_all(self, dep):      
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifSubGrupoId = %s order by descripcion"
        self.cur.execute(s, dep)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    
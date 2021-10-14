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
        s = "select Dep, Prov, Sec, IdLoc, AsientoElectoral from [bdge].[dbo].[GeoAsientos_Nacional_all]"
        if usrdep != 0 :
            s = s + " where Dep = %d order by AsientoElectoral"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by AsientoElectoral"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_asientos_all1(self, usrdep, dep, prov, secc):
        s = "select Dep, Prov, Sec, IdLoc, AsientoElectoral from [bdge].[dbo].[GeoAsientos_Nacional_all]"
        if usrdep != 0 :
            asie = dep, prov, secc, usrdep
            s = s + " where Dep = %d and Prov = %d and Sec = %d and Dep = %d and idclasif in (16, 17, 75, 76) order by AsientoElectoral"
            self.cur.execute(s, asie)
        else:
            asie = dep, prov, secc
            s = s + " where Dep = %d and Prov = %d and Sec = %d and idclasif in (16, 17, 75, 76) order by AsientoElectoral"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_asientos_all2(self, usrdep, dep, prov, secc):        
        s = "select Dep, Prov, Sec, IdLoc, AsientoElectoral from [bdge].[dbo].[GeoAsientos_Nacional_all]"
        if usrdep != 0 :
            asie = dep, prov, secc, usrdep
            s = s + " where Dep = %d and Prov = %d and Sec = %d and Dep = %d and idclasif in (16, 17, 75, 76) order by AsientoElectoral"
            self.cur.execute(s, asie)
        else:
            asie = dep, prov, secc
            s = s + " where Dep = %d and Prov = %d and Sec = %d and idclasif in (16, 17, 75, 76) order by AsientoElectoral"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_zonas_all(self, usrdep):        
        s = "select l.IdLoc, z.Zona, z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " inner join [GeografiaElectoral_app].[dbo].[GeoAsientos_Nacional] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
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
        s = "select l.IdLoc, z.Zona, z.NomZona, d.NomDist, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " inner join [GeografiaElectoral_app].[dbo].[GeoAsientos_Nacional] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
        if usrdep != 0 :
            zon = idloc, circun, usrdep
            s = s + " where l.Idloc = %d and (d.CircunDist = %d) and l.DepLoc = %d order by z.NomZona"
            self.cur.execute(s, zon)
        else:
            zon = idloc, circun
            s = s + " where l.Idloc = %d and (d.CircunDist = %d) order by z.NomZona"
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

    def get_distritos_all1(self, idloc):        
        s = "select IdLocDist, Dist, CircunDist, NomDist from [GeografiaElectoral_app].[dbo].[DIST] where IdLocDist = %d order by Dist"
        consulta = idloc
        self.cur.execute(s, consulta)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_pueblos_all(self, dep):      
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifSubGrupo = %s order by descripcion"
        self.cur.execute(s, dep)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
 
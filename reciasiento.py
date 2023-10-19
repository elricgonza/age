# Operaciones asientos

class Reciasiento:
    deploc = 0
    provloc = 0
    secloc = 0
    nomloc = ""


    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_loc_all(self, usrdep):
        ''' Obtiene datos bàsicos de asiento para - recintos '''
        s = "select Dep, Prov, Sec, IdLoc, nomloc as AsientoElectoral from [bdge].[dbo].[v_loc_nal_all]"
        if usrdep != 0 :
            s = s + " where Dep = %d order by AsientoElectoral"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by AsientoElectoral"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        return rows


    def get_asientos_all1(self, usrdep, dep, prov, secc):
        ''' Obtiene asientos con ESTADO habilitado/rehabilitado TED y TSE y TipoCircun ESPECIAL (actualizado query) '''

        s = "select Dep, Prov, Sec, IdLoc, nomLoc as AsientoElectoral from [bdge].[dbo].[v_loc_nal_all]"
        if usrdep != 0 :
            asie = dep, prov, secc, usrdep
            s = s + " where Dep = %d and Prov = %d and Sec = %d and estado in (16, 17, 75, 76) and tipoLocLoc = 68 order by AsientoElectoral"
            self.cur.execute(s, asie)
        else:
            asie = dep, prov, secc
            s = s + " where Dep = %d and Prov = %d and Sec = %d and estado in (16, 17, 75, 76) and tipoLocLoc = 68 order by AsientoElectoral"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        return rows


    def get_asientos_all2(self, usrdep, dep, prov, secc):
        ''' Obtiene asientos con ESTADO habilitado/rehabilitado TED y TSE y TipoCircun UNINOM y MIXTO (actualizado query) '''

        s = "select Dep, Prov, Sec, IdLoc, nomLoc as AsientoElectoral from [bdge].[dbo].[v_loc_nal_all]"
        if usrdep != 0 :
            asie = dep, prov, secc, usrdep
            s = s + " where Dep = %d and Prov = %d and Sec = %d and estado in (16, 17, 75, 76) and tipoLocLoc in (67, 69) order by AsientoElectoral"
            self.cur.execute(s, asie)
        else:
            asie = dep, prov, secc
            s = s + " where Dep = %d and Prov = %d and Sec = %d and estado  in (16, 17, 75, 76) and tipoLocLoc in (67, 69) order by AsientoElectoral"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        return rows


    def get_asientos_all4(self, usrdep, dep, prov, secc):
        ''' Obtiene asientos con ESTADO habilitado/rehabilitado TED y TSE y TipoCircun UNINOM, ESPECIAL y MIXTO (actualizado query) '''

        s = "select Dep, Prov, Sec, IdLoc, nomLoc as AsientoElectoral from [bdge].[dbo].[v_loc_nal_all]"
        if usrdep != 0 :
            asie = dep, prov, secc, usrdep
            s = s + " where Dep = %d and Prov = %d and Sec = %d and estado in (16, 17, 75, 76) and tipoLocLoc in (67, 68, 69) order by AsientoElectoral"
            self.cur.execute(s, asie)
        else:
            asie = dep, prov, secc
            s = s + " where Dep = %d and Prov = %d and Sec = %d and estado in (16, 17, 75, 76) and tipoLocLoc in (67, 68, 69) order by AsientoElectoral"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        return rows


    def get_asientos_all3(self, usrdep, pa, dep, prov, secc):
        s = "select IdPais, Dep, Prov, Sec, IdLoc, NomLoc from [bdge].[dbo].[GeoAsientos_Exterior_all]"
        if usrdep != 0 :
            asie = pa, dep, prov, secc, usrdep
            s = s + " where IdPais = %d and Dep = %d and Prov = %d and Sec = %d and Dep = %d and idEstado in (75, 76) order by NomLoc"
            self.cur.execute(s, asie)
        else:
            asie = pa, dep, prov, secc
            s = s + " where IdPais = %d and Dep = %d and Prov = %d and Sec = %d and idEstado in (75, 76) order by NomLoc"
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_asiento_one(self, usrdep, idloc):
        ''' Invocado por ajax getJSON - Obtiene asiento por idLoc y dep de usuario (query actualizado) '''

        s = "select Dep, Prov, Sec, IdLoc, nomLoc as AsientoElectoral from [bdge].[dbo].[v_loc_nal_all]"
        if usrdep != 0 :
            asie = idloc, usrdep
            s = s + " where IdLoc = %d and Dep = %d "
            self.cur.execute(s, asie)
        else:
            asie = idloc
            s = s + " where IdLoc = %d "
            self.cur.execute(s, asie)

        rows = self.cur.fetchall()
        return rows


    def get_zonas_all(self, usrdep):
        s = "select l.IdLoc, z.Zona, z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " inner join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
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
            " inner join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
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


    def get_zonas_all2(self, usrdep, idloc):
        s = "select l.IdLoc, z.Zona, z.NomZona, d.NomDist from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " inner join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
        if usrdep != 0 :
            zon = idloc
            s = s + " where l.Idloc = %d order by z.NomZona"
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


    def get_distritos_all1(self, idloc):
        s = "select IdLocDist, Dist, CircunDist, NomDist from [GeografiaElectoral_app].[dbo].[DIST] where IdLocDist = %d order by Dist"
        consulta = idloc
        self.cur.execute(s, consulta)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_distritos_all2(self, idlocreci):
        s = "select IdLocDist, Dist, NomDist from [GeografiaElectoral_app].[dbo].[DIST] where IdLocDist = %d order by Dist"
        consulta = idlocreci
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

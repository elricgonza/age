# Operaciones asientos

class Jurisd_asi:
    idlocreci=0
    reci=0
    nomreci=''
    estado=0
    fechaAct=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_jurisd_asi_all(self, usrdep):        
        s = "select a.IdLoc, a.NomDep as Departamento, a.NomProv as Provincia, a.NombreMunicipio as Municipio, "  + \
            "a.AsientoElectoral as Asiento, a.TipoCircunscripcion, a.DEP, a.PROV, a.SEC, a.Estado, j.idLoc, j.origen" + \
            " from [bdge].[dbo].[GeoAsientos_Nacional_all] a" + \
            " left join [bdge].[dbo].[actJurisd] j on a.IdLoc=j.idLoc"
        if usrdep != 0 :
            s = s + " where a.DEP = %d group by a.IdLoc, a.NomDep, a.NomProv, a.NombreMunicipio, "  + \
                    "a.AsientoElectoral, a.TipoCircunscripcion, a.DEP, a.PROV, a.SEC, a.Estado, j.idLoc, j.origen order by a.prov, a.sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " group by a.IdLoc, a.NomDep, a.NomProv, a.NombreMunicipio, "  + \
                    "a.AsientoElectoral, a.TipoCircunscripcion, a.DEP, a.PROV, a.SEC, a.Estado, j.idLoc, j.origen order by a.DEP, a.PROV, a.SEC"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    
    def get_jurisd_asi_idloc(self, idloc):
        s = "select a.IdLoc, a.DepLoc, a.ProvLoc, a.SecLoc, a.NomLoc," + \
            "a.PoblacionLoc, a.PoblacionElecLoc, a.FechaCensoLoc, a.TipoLocLoc, a.fechaBaseLegLoc," + \
            "a.MarcaLoc, a.latitud, a.longitud, a.estado, a.circunConsulado," + \
            "b.NomDep as _departamento, c.NomProv as _provincia, d.NomSec as _municipio, e.NombreTipoLocLoc as _tipo_circun," + \
            "a.etapa, a.doc_idA, a.obsUbicacion, a.doc_idRN, a.obs, a.fechaIngreso, a.fechaAct, a.usuario " + \
            "from [GeografiaElectoral_app].[dbo].[LOC] a" + \
            "        left join [GeografiaElectoral_app].[dbo].[DEP] b on a.DepLoc= b.Dep " + \
            "        left join [GeografiaElectoral_app].[dbo].[PROV] c on a.DepLoc= c.DepProv and a.ProvLoc= c.Prov" + \
            "        left join [GeografiaElectoral_app].[dbo].[SEC] d on a.DepLoc= d.DepSec and a.ProvLoc= d.ProvSec and a.SecLoc= d.Sec" + \
            "        left join [GeografiaElectoral_app].[dbo].[clTipoLocLoc] e on a.TipoLocLoc = e.Tipolocloc" + \
            " where a.idloc = %d "

        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.deploc = row[1]
            self.provloc = row[2]
            self.secloc = row[3]
            self.nomloc = row[4]

            self.poblacionloc = row[5]
            self.poblacionelecloc = row[6]
            self.fechacensoloc = row[7]
            self.tipolocloc = row[8]
            self.fechabaselegloc = row[9]

            self.marcaloc = row[10]
            self.latitud = row[11]
            self.longitud = row[12]
            self.estado = row[13]
            self.circunconsulado = row[14]
            self._departamento = row[15]
            self._provincia = row[16]
            self._municipio = row[17]
            self._tipo_circun = row[18]

            self.etapa = row[19]
            self.doc_idA = row[20]
            self.obsUbicacion = row[21]
            self.doc_idRN = row[22]
            self.obs = row[23]
            self.fechaIngreso = row[24]
            self.fechaAct = row[25]
            self.usuario = row[26]
            return True

    def get_circuns_all(self, usrdep):        
        s = "select a.DepLoc, a.ProvLoc, a.SecLoc, d.CircunDist from GeografiaElectoral_app.dbo.LOC a " + \
            "inner join GeografiaElectoral_app.dbo.ZONA z on a.IdLoc=z.IdLocZona " + \
            "inner join GeografiaElectoral_app.dbo.DIST d on a.IdLoc=d.IdLocDist and z.IdLocZona=d.IdLocDist and z.DistZona=d.Dist"
        if usrdep != 0:
            s = s + " where a.DepLoc = %d group by a.DepLoc, a.ProvLoc, a.SecLoc, d.CircunDist order by d.CircunDist"
            self.cur.execute(s, usrdep)
        else:
            s = s + " group by a.DepLoc, a.ProvLoc, a.SecLoc, d.CircunDist order by d.CircunDist"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_circuns_dps(self, dp, pr, mu):        
        s = "select a.DepLoc, a.ProvLoc, a.SecLoc, d.CircunDist from GeografiaElectoral_app.dbo.LOC a " + \
            "inner join GeografiaElectoral_app.dbo.ZONA z on a.IdLoc=z.IdLocZona " + \
            "inner join GeografiaElectoral_app.dbo.DIST d on a.IdLoc=d.IdLocDist and z.IdLocZona=d.IdLocDist and z.DistZona=d.Dist " + \
            "where a.DepLoc=%d and a.ProvLoc=%d and a.SecLoc=%d group by a.DepLoc, a.ProvLoc, a.SecLoc, d.CircunDist order by d.CircunDist"
        lista = dp, pr, mu    
        self.cur.execute(s, lista)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_zonas_dps(self, dp, pr, mu, ci):  
        s = "select d.Dist, z.Zona, z.NomZona, d.CircunDist from GeografiaElectoral_app.dbo.DIST d " + \
            "inner join GeografiaElectoral_app.dbo.ZONA z on d.Dist=z.DistZona " + \
            "inner join GeografiaElectoral_app.dbo.LOC a on d.IdLocDist=a.IdLoc and z.IdLocZona=a.IdLoc " + \
            "where d.IdLocDist=z.IdLocZona and d.CircunDist=%d and a.DepLoc=%d and a.ProvLoc=%d and a.SecLoc=%d " + \
            "group by d.Dist, z.Zona, z.NomZona, d.CircunDist order by z.NomZona"
        lista = ci, dp, pr, mu    
        self.cur.execute(s, lista)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_zonadist_idloc(self, zonade, circun):
        s = "Select d.Dist, z.Zona, d.NomDist, z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z, " + \
            "[GeografiaElectoral_app].[dbo].[DIST] d where z.DistZona=d.Dist and z.IdLocZona = d.IdLocDist " + \
            "and d.CircunDist=%d and z.Zona=%d group by d.Dist, z.Zona, d.NomDist, z.NomZona, d.CircunDist"
        lista= circun, zonade        
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dist = row[0]
            self.zona = row[1]
            self.nomdist = row[2]
            self.nomzona = row[3]
            self.circun = row[4]
            return True

    def get_dpto(self, dep):
        s = "Select NomDep from [GeografiaElectoral_app].[dbo].[DEP] where Dep = %d"        
        self.cur.execute(s, dep)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.nomdep = row[0]
            return True

    def get_prov(self, dep, prov):
        s = "Select NomProv from [GeografiaElectoral_app].[dbo].[PROV] where DepProv = %d and Prov = %d"
        lista = dep, prov
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.nomprov = row[0]
            return True

    def get_sec(self, dep, prov, sec):
        s = "Select NomSec from [GeografiaElectoral_app].[dbo].[SEC] where DepSec = %d and ProvSec = %d and Sec = %d"
        lista = dep, prov, sec  
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.nomsec = row[0]
            return True

    def add_llenado_recintos(self, idloc, dep2, prov2, sec2, departamento2, provincia2, municipio2, dist, zona, \
                         nomdist, nomzona, circun, f_ingreso, f_actual, usr, idocact):
        s = "Select Dep, Prov, Sec, IdLoc, Dist, Zona, Reci, NomDep, NomProv, NombreMunicipio, AsientoElectoral, NomDist, NomZona," + \
            " NombreRecinto, Direccion, CircunDist, TipoLocLoc, TipoCircunscripcion, idTipoRecinto, TipoRecinto, latitud, longitud, doc_idA, doc_idAF" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where IdLocReci = %d"
        self.cur.execute(s, idloc)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            for recinto in rows:
                new_jurisd_asi = recinto[0], recinto[1], recinto[2], recinto[3], recinto[4], recinto[5], recinto[6], recinto[7], \
                recinto[8], recinto[9], recinto[10], recinto[11], recinto[12], recinto[13], recinto[14], recinto[15], recinto[16], \
                recinto[17], recinto[18], recinto[19], recinto[20], recinto[21], idocact, recinto[23], dep2, prov2, sec2, recinto[3], \
                dist, zona, recinto[6], departamento2, provincia2, municipio2, recinto[10], nomdist, nomzona, recinto[13], \
                recinto[14], circun, recinto[16], recinto[17], recinto[18], recinto[19], recinto[20], recinto[21], 0, f_ingreso, f_actual, usr, 'A'
                s = "insert into bdge.dbo.actJurisd (dep, prov, sec, idloc, dist, zona, reci, nomDep, nomProv, nomSec, nomLoc," + \
                    " nomDist, nomZona, nomReci, direccion, circun, idTipoCircun, tipoCircun, idTipoRecinto, tipoRecinto," + \
                    " latitud, longitud, doc, doc1, dep2, prov2, sec2, idloc2, dist2, zona2, reci2, nomDep2, nomProv2," + \
                    " nomSec2, nomLoc2, nomDist2, nomZona2, nomReci2, direccion2, circun2, idTipoCircun2, tipoCircun2," + \
                    " idTipoRecinto2, tipoRecinto2, latitud2, longitud2, cerrado, fechaIngreso, fechaAct, usuario, origen) VALUES" + \
                    " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," + \
                    " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                self.cur.execute(s, new_jurisd_asi)
                self.cx.commit()

            return True

    def upd_llenado_recintos(self, idloc, dep2, prov2, sec2, departamento2, provincia2, municipio2, dist, zona, \
                         nomdist, nomzona, circun, f_actual, usr, idocact):
        s = "Select id from actJurisd where idLoc = %s"  
        self.cur.execute(s, idloc)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            for recinto in rows:
                upd_jurisd_asi = idocact, dep2, prov2, sec2, dist, zona, departamento2, provincia2, municipio2, nomdist, nomzona, \
                                 circun, f_actual, usr, recinto[0]
                s = "update bdge.dbo.actJurisd" + \
                    " set doc = %s, dep2 = %s, prov2 = %s, sec2 = %s, dist2 = %s, zona2 = %s, nomDep2 = %s," + \
                    " nomProv2 = %s, nomSec2 = %s, nomDist2 = %s, nomZona2 = %s," + \
                    " circun2 = %s, fechaAct = %s, usuario = %s" + \
                    " where id = %d"
                self.cur.execute(s, upd_jurisd_asi)
                self.cx.commit()

            return True

    def upd_asiento_juriasi(self, idloc, dep, prov, sec, idocact):
        asiento = dep, prov, sec, idocact, idloc
        s = "update GeografiaElectoral_app.dbo.LOC" + \
            " set DepLoc= %s, ProvLoc=%s, SecLoc = %s, doc_idA = %s where IdLoc = %s"
        try:
            self.cur.execute(s, asiento)
            self.cx.commit()
            print('Asiento actualizado')
        except Exception as e:
            print("Error - actualización de Asiento...")

    def upd_recinto_juriasi(self, idloc, zona):
        recinto = zona, idloc
        s = "update GeografiaElectoral_app.dbo.RECI" + \
            " set ZonaReci = %s where IdLocReci = %s"
        try:
            self.cur.execute(s, recinto)
            self.cx.commit()
            print('Recinto actualizado')
        except Exception as e:
            print("Error - actualización de Recinto...")    
    
    def get_jurisd_asi_idloc_idjurisd(self, idloc):        
        s = "select bdge.dbo.actJurisd.idLoc, bdge.dbo.actJurisd.circun2, bdge.dbo.actJurisd.zona2, bdge.dbo.actJurisd.dist2 from bdge.dbo.GeoAsientos_Nacional_all" + \
            " left join bdge.dbo.actJurisd on bdge.dbo.GeoAsientos_Nacional_all.IdLoc=bdge.dbo.actJurisd.idLoc" + \
            " where bdge.dbo.actJurisd.idLoc=%d group by bdge.dbo.actJurisd.idLoc, bdge.dbo.actJurisd.circun2, bdge.dbo.actJurisd.zona2, bdge.dbo.actJurisd.dist2"    
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.circ = row[1]
            self.idzona = row[2]
            self.dist = row[3]
            return True

    def get_zonasd_all(self, usrdep):        
        s = "Select d.Dist, z.Zona, z.NomZona, d.CircunDist, a.DepLoc, a.ProvLoc, a.SecLoc from [GeografiaElectoral_app].[dbo].[ZONA] z, " + \
            "[GeografiaElectoral_app].[dbo].[DIST] d, [GeografiaElectoral_app].[dbo].[LOC] a"
        if usrdep != 0:
            s = s + " where z.DistZona=d.Dist and a.IdLoc=z.IdLocZona and a.IdLoc=d.IdLocDist and a.DepLoc = %d order by z.NomZona"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where z.DistZona=d.Dist and a.IdLoc=z.IdLocZona and a.IdLoc=d.IdLocDist order by z.NomZona"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
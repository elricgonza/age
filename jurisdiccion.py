# Operaciones asientos

class Jurisdiccion:
    idlocreci=0
    reci=0
    nomreci=''
    estado=0
    fechaAct=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_jurisdiccion_all(self, usrdep):        
        s = "Select [bdge].[dbo].[GeoRecintos_all].IdLocReci, [bdge].[dbo].[GeoRecintos_all].Reci, [bdge].[dbo].[GeoRecintos_all].NomDep" + \
            " as Departamento, [bdge].[dbo].[GeoRecintos_all].NomProv as Provincia, [bdge].[dbo].[GeoRecintos_all].NombreMunicipio as Municipio," + \
            " [bdge].[dbo].[GeoRecintos_all].NombreRecinto, [bdge].[dbo].[GeoRecintos_all].TipoCircunscripcion, [bdge].[dbo].[GeoRecintos_all].DEP," + \
            " [bdge].[dbo].[GeoRecintos_all].PROV, [bdge].[dbo].[GeoRecintos_all].SEC," + \
            " [bdge].[dbo].[GeoRecintos_all].Estado, [bdge].[dbo].[actJurisd].idloc2, [bdge].[dbo].[actJurisd].reci2" + \
            " from [bdge].[dbo].[GeoRecintos_all] left join [bdge].[dbo].[actJurisd] on [bdge].[dbo].[GeoRecintos_all].IdLoc=[bdge].[dbo].[actJurisd].idloc2" + \
            " and [bdge].[dbo].[GeoRecintos_all].Reci=[bdge].[dbo].[actJurisd].reci2"
        if usrdep != 0 :
            s = s + " where [bdge].[dbo].[GeoRecintos_all].TipoLocLoc in (67, 69) and [bdge].[dbo].[GeoRecintos_all].DEP = %d order by [bdge].[dbo].[GeoRecintos_all].prov, [bdge].[dbo].[GeoRecintos_all].sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where [bdge].[dbo].[GeoRecintos_all].TipoLocLoc in (67, 69) order by [bdge].[dbo].[GeoRecintos_all].Dep, [bdge].[dbo].[GeoRecintos_all].Prov, [bdge].[dbo].[GeoRecintos_all].Sec"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_jurisdiccion_idloc(self, idloc, reci):        
        s = "select bdge.dbo.actJurisd.id, bdge.dbo.actJurisd.idLoc2, bdge.dbo.actJurisd.reci2" + \
            " from bdge.dbo.GeoRecintos_all left join bdge.dbo.actJurisd on bdge.dbo.GeoRecintos_all.IdLoc=bdge.dbo.actJurisd.idloc2" + \
            " and bdge.dbo.GeoRecintos_all.Reci=bdge.dbo.actJurisd.reci2" + \
            " where bdge.dbo.actJurisd.idLoc2=%d and bdge.dbo.GeoRecintos_all.Reci=%d"
        lista = idloc, reci    
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idjurisd = row[0]
            self.idloc = row[1]
            self.reci = row[2]
            return True

    def get_jurisdiccion_idlocreci(self, idreci, idlocreci):
        s = "select a.IdLocReci, a.Reci, g.CircunDist, b.DepLoc, c.NomDep, b.ProvLoc, " + \
            "d.NomProv, b.SecLoc, e.NomSec, a.NomReci, a.ZonaReci, a.MaxMesasReci, " + \
            "a.Direccion, a.latitud, a.longitud, a.estado, a.tipoRecinto, " + \
            "a.codRue, a.codRueEdif, a.depend, a.cantPisos, a.fechaIngreso, a.fechaAct, a.usuario, " + \
            "a.etapa, a.doc_idA, a.doc_idAF, h.ruta as rutaA, i.ruta as rutaAF, b.NomLoc, g.NomDist, f.NomZona, f.Zona " + \
            "from [GeografiaElectoral_app].[dbo].[RECI] a " + \
            "inner join [GeografiaElectoral_app].[dbo].[LOC] b on a.IdLocReci=b.IdLoc " + \
            "inner join [GeografiaElectoral_app].[dbo].[DEP] c on b.DepLoc=c.Dep " + \
            "inner join [GeografiaElectoral_app].[dbo].[PROV] d on b.ProvLoc=d.Prov and b.DepLoc=d.DepProv " + \
            "inner join [GeografiaElectoral_app].[dbo].[SEC] e on b.SecLoc=e.Sec and b.DepLoc=e.DepSec and b.ProvLoc=e.ProvSec " + \
            "inner join [GeografiaElectoral_app].[dbo].[ZONA] f on a.IdLocReci=f.IdLocZona and a.ZonaReci=f.Zona " + \
            "inner join [GeografiaElectoral_app].[dbo].[DIST] g on f.IdLocZona=g.IdLocDist and f.DistZona=g.Dist " + \
            "left join [bdge].[dbo].[doc] h on a.doc_idA=h.id " + \
            "left join [bdge].[dbo].[doc] i on a.doc_idAF=i.id " + \
            "where a.IdLocReci = %d and a.Reci = %d"
        mod_recinto = idlocreci, idreci
        self.cur.execute(s, mod_recinto)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.reci = row[1]
            self.circundist = row[2]
            self.deploc = row[3]
            self.nomdep = row[4]
            self.provloc = row[5]
            self.nomprov = row[6]
            self.secloc = row[7]
            self.nomsec = row[8]
            self.nomreci = row[9]
            self.zonareci = row[10]
            self.maxmesasreci = row[11]
            self.direccion = row[12]
            self.latitud = row[13]
            self.longitud = row[14]
            self.estado = row[15]
            self.tiporecinto = row[16]
            self.codrue = row[17]
            self.codrueedif = row[18]
            self.depend = row[19]
            self.cantpisos = row[20]
            self.fechaIngreso = row[21]
            self.fechaAct = row[22]
            self.usuario = row[23]
            self.etapa = row[24]
            self.doc_idA = row[25]
            self.doc_idAF = row[26]
            self.rutaA = row[27]
            self.rutaAF = row[28]
            self.nomloc = row[29]
            self.nomdist = row[30]
            self.nomzona = row[31]
            self.idzona = row[32]
            return True
    
    def get_asientos_all(self, usrdep):        
        s = "select distinct IdLoc, AsientoElectoral, Dep, Prov, Sec, CircunDist" + \
        " from [bdge].[dbo].[GeoAsientos_Nacional_Juri_all]"
        if usrdep != 0:
            s = s + " where Dep = %d and estado in (16, 17, 75, 76) order by AsientoElectoral"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where estado in (16, 17, 75, 76) order by AsientoElectoral"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_zonasd_all(self, usrdep):        
        s = "Select d.Dist, z.Zona, z.NomZona, d.CircunDist, a.IdLoc from [GeografiaElectoral_app].[dbo].[ZONA] z, " + \
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

    def get_asijuri_all(self, dp, pr, mu):
        s = "select distinct IdLoc, AsientoElectoral, Dep, Prov, Sec, CircunDist" + \
            " from [bdge].[dbo].[GeoAsientos_Nacional_Juri_all]" + \
            " where Dep = %d and Prov = %d and Sec = %d and estado in (16, 17, 75, 76) order by AsientoElectoral"
        lista = dp, pr, mu    
        self.cur.execute(s, lista)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_zondist_all(self, idloc):
        s = "Select d.Dist, z.Zona,z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z, " + \
            "[GeografiaElectoral_app].[dbo].[DIST] d where z.DistZona=d.Dist and z.IdLocZona = %d and d.IdLocDist= %d"
        lista = idloc, idloc    
        self.cur.execute(s, lista)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_valida_reci(self, idloc, reci):
        s = "Select idloc2, reci2 from [bdge].[dbo].[actJurisd] where idloc2=%d and reci2 = %d"
        lista = idloc, reci    
        self.cur.execute(s, lista)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_verifica_dupli(self, idloc, reci):
        s = "Select IdLocReci, Reci from [GeografiaElectoral_app].[dbo].[RECI] where IdLocReci=%d and Reci=%d"
        lista = idloc, reci    
        self.cur.execute(s, lista)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_jurisdiccion_idlocreci_origen(self, idloc, reci):
        s = "Select Dep, Prov, Sec, IdLoc, Dist, Zona, Reci, NomDep, NomProv, NombreMunicipio, AsientoElectoral, NomDist, NomZona," + \
            " NombreRecinto, Direccion, CircunDist, TipoLocLoc, TipoCircunscripcion, idTipoRecinto, TipoRecinto, latitud, longitud, doc_idA, doc_idAF" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where IdLocReci = %d and Reci = %d"
        lista = idloc, reci    
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dep = row[0]
            self.prov = row[1]
            self.sec = row[2]
            self.idloc = row[3]
            self.dist = row[4]
            self.zona = row[5]
            self.reci = row[6]
            self.departamento = row[7]
            self.provincia = row[8]
            self.municipio = row[9]
            self.asiento = row[10]
            self.nomdist = row[11]
            self.nomzona = row[12]
            self.recinto = row[13]
            self.direccion = row[14]
            self.circun = row[15]
            self.idtipocircun = row[16]
            self.tipocircun = row[17]
            self.idtiporecinto = row[18]
            self.tiporecinto = row[19]
            self.latitud = row[20]
            self.longitud = row[21]
            self.doc = row[22]
            self.doc1 = row[23]
            return True

    def get_zonadist_idloc2(self, idloc, idzona):
        s = "Select d.Dist, z.Zona, d.NomDist, z.NomZona, d.CircunDist from [GeografiaElectoral_app].[dbo].[ZONA] z, " + \
            "[GeografiaElectoral_app].[dbo].[DIST] d where z.DistZona=d.Dist and z.IdLocZona = %d and d.IdLocDist= %d " +\
            "and z.Zona = %d"
        lista= idloc, idloc, idzona        
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dist2 = row[0]
            self.zona2 = row[1]
            self.nomdist2 = row[2]
            self.nomzona2 = row[3]
            self.circun2 = row[4]
            return True

    def get_asiento_idloc2(self, idloc):
        s = "Select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, tipocircun, TipoCircunscripcion " + \
            "from [bdge].[dbo].[GeoAsientos_Nacional_all] where IdLoc = %d"   
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dep2 = row[0]
            self.prov2 = row[1]
            self.sec2 = row[2]
            self.departamento2 = row[3]
            self.provincia2 = row[4]
            self.municipio2 = row[5]
            self.asiento2 = row[6]
            self.idtipocircun2 = row[7]
            self.tipocircun2 = row[8]
            return True

    def get_jurisdiccion_idlocreci_destino(self, idloc, reci):
        s = "Select NombreRecinto, Direccion, idTipoRecinto, TipoRecinto, latitud, longitud" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where IdLocReci = %d and Reci = %d"
        lista = idloc, reci    
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.recinto2 = row[0]
            self.direccion2 = row[1]
            self.idtiporecinto2 = row[2]
            self.tiporecinto2 = row[3]
            self.latitud2 = row[4]
            self.longitud2 = row[5]
            return True

    def add_jurisdiccion(self, dep, prov, sec, idloc, dist, zona, reci, departamento, provincia, municipio, \
                     asiento, nomdist, nomzona, recinto, direccion, circun, idtipocircun, tipocircun, \
                     idtiporecinto, tiporecinto, latitud, longitud, doc, doc1, dep2, prov2, sec2, \
                     idloc2, dist2, zona2, reci2, departamento2, provincia2, municipio2, asiento2, nomdist2, \
                     nomzona2, recinto2, direccion2, circun2, idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, \
                     latitud2, longitud2, f_ingreso, f_actual, usr):
        new_jurisd = dep, prov, sec, idloc, dist, zona, reci, departamento, provincia, municipio, \
            asiento, nomdist, nomzona, recinto, direccion, circun, idtipocircun, tipocircun, \
            idtiporecinto, tiporecinto, latitud, longitud, doc, doc1, dep2, prov2, sec2, idloc2, dist2, \
            zona2, reci2, departamento2, provincia2, municipio2, asiento2, nomdist2, nomzona2, recinto2, \
            direccion2, circun2, idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, latitud2, \
            longitud2, 0, f_ingreso, f_actual, usr, 'R'
        s = "insert into bdge.dbo.actJurisd (dep, prov, sec, idloc, dist, zona, reci, nomDep, nomProv, nomSec, nomLoc," + \
            " nomDist, nomZona, nomReci, direccion, circun, idTipoCircun, tipoCircun, idTipoRecinto, tipoRecinto," + \
            " latitud, longitud, doc, doc1, dep2, prov2, sec2, idloc2, dist2, zona2, reci2, nomDep2, nomProv2," + \
            " nomSec2, nomLoc2, nomDist2, nomZona2, nomReci2, direccion2, circun2, idTipoCircun2, tipoCircun2," + \
            " idTipoRecinto2, tipoRecinto2, latitud2, longitud2, cerrado, fechaIngreso, fechaAct, usuario, origen) VALUES" + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," + \
            " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_jurisd)
            self.cx.commit()
            print("jurisdiccion adicionado...") 
        except:
            print("Error - actualización de jurisdiccion...")

    def upd_jurisdiccion(self, idocact, dep2, prov2, sec2, idloc2, dist2, zona2, reci2, departamento2, \
                     provincia2, municipio2, asiento2, nomdist2, nomzona2, recinto2, direccion2, \
                     circun2, idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, \
                     latitud2, longitud2, f_actual, usr, idjurisd):
        upd_jurisd = idocact, dep2, prov2, sec2, idloc2, dist2, zona2, reci2, departamento2, \
            provincia2, municipio2, asiento2, nomdist2, nomzona2, recinto2, direccion2, circun2, \
            idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, latitud2, \
            longitud2, f_actual, usr, idjurisd
        s = "update bdge.dbo.actJurisd" + \
            " set doc = %s, dep2 = %s, prov2 = %s, sec2 = %s, idLoc2 = %s, dist2 = %s, zona2 = %s, reci2 = %s, nomDep2 = %s," + \
            " nomProv2 = %s, nomSec2 = %s, nomLoc2 = %s, nomDist2 = %s, nomZona2 = %s, nomReci2 = %s, direccion2 = %s," + \
            " circun2 = %s, idTipoCircun2 = %s, tipoCircun2 = %s, idTipoRecinto2 = %s, tipoRecinto2 = %s, latitud2 = %s, longitud2 = %s," + \
            " fechaAct = %s, usuario = %s" + \
            " where id = %d"
        try:
            self.cur.execute(s, upd_jurisd)
            self.cx.commit()
            print('Jurisdiccion actualizado')
        except Exception as e:
            print("Error - actualización de Jurisdiccion...")

    def upd_recinto_jurireci(self, idlocreci, reci, reci2, idloc2, zonareci, idocact):
        recinto = idloc2, zonareci, reci2, idocact, idlocreci, reci
        s = "update GeografiaElectoral_app.dbo.reci" + \
            " set IdLocReci= %s, ZonaReci= %s, Reci=%s, doc_idA=%s where IdLocReci = %s and Reci = %s"
        try:
            self.cur.execute(s, recinto)
            self.cx.commit()
            print('Recinto actualizado')
        except Exception as e:
            print("Error - actualización de Recinto...")

    def upd_recinto_juri(self, idlocreci, reci, idloc2, zonareci, idocact):
        recinto = idloc2, zonareci, idocact, idlocreci, reci
        s = "update GeografiaElectoral_app.dbo.reci" + \
            " set IdLocReci= %s, ZonaReci= %s, doc_idA=%s where IdLocReci = %s and Reci = %s"
        try:
            self.cur.execute(s, recinto)
            self.cx.commit()
            print('Recinto actualizado')
        except Exception as e:
            print("Error - actualización de Recinto...")

    def get_next_idreci(self, idloc, reci):
        lista = idloc, reci
        self.cur.execute("select max(Reci) + 1 from GeografiaElectoral_app.dbo.RECI where IdLocReci=%d and Reci=%d", lista)
        row = self.cur.fetchone()
        return row[0]

# Operaciones asientos

class Homologa:
    idlocreci=0
    reci=0
    nomreci=''
    estado=0
    fechaAct=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_homologa_all(self, usrdep, inicio, final):
        if inicio == "00-00-0000" and final == "00-00-0000":
            return False
        else:
            s = "select a.IdLoc, a.reci, a.NomDep, a.NomLoc, a.NomReci, a.desEstado, " + \
                    "h.idLoc2, h.reci2, h.nomReci2, a.desUrbanoRural " + \
                "from bdge.dbo.v_reci_nal_all a " + \
                "left join bdge.dbo.hom h on a.IdLoc = h.idLoc and a.Reci = h.reci"
            if usrdep != 0 :
                lista = usrdep, inicio, final
                # suspendidos/suprimidos 
                s = s + " where Estado in (4, 5, 82, 83) and a.DEP = %d and Convert(CHAR(10),a.fechaAct,23) between %d and %d order by a.prov, a.sec"
                self.cur.execute(s, lista)
            else:
                lista = inicio, final
                s = s + " where Estado in (4, 5, 82, 83)  and Convert(CHAR(10),a.fechaAct,23) between %d and %d order by a.Dep, a.Prov, a.Sec"
                self.cur.execute(s, lista)

            rows = self.cur.fetchall()
            return rows


    def get_homologa_idloc(self, idlocreci):   
        s = "Select IdLocReci, Reci, NomDep as Departamento, AsientoElectoral, NombreRecinto, Estado, idloc2, reci2, nomreci2" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]"    
        if usrdep != 0 :
            lista = usrdep, inicio, final
            s = s + " where  DEP = %d and Convert(CHAR(10),fechaAct,23) between %d and %d order by prov, sec"
            self.cur.execute(s, lista)
        else:
            lista = inicio, final
            s = s + " where Convert(CHAR(10),fechaAct,23) between %d and %d order by Dep, Prov, Sec"
            self.cur.execute(s, lista)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_homologa_idlocreci(self, idreci, idlocreci):
        s = "Select IdLocReci, Reci, NomDep as Departamento, AsientoElectoral, NombreRecinto, Estado, CircunDist, Dep, Prov, Sec" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in (4, 5, 82, 83) and IdLocReci = %d and Reci = %d"
        lista = idlocreci, idreci    
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idlocreci = row[0]
            self.idreci = row[1]
            self.departamento = row[2]
            self.asiento = row[3]
            self.recinto = row[4]
            self.estado = row[5]
            self.circun = row[6]
            self.dep = row[7]
            self.prov = row[8]
            self.sec = row[9]
            return True

    def ver_homologa_idlocreci(self, idreci, idlocreci, idlocdes):
        if idlocdes != 0:
            if idlocdes == idlocreci:
                    idlocdes=idlocreci
        else:
            idlocdes = idlocreci

        s = "Select idLoc2, reci2 from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in (4, 5, 82, 83) and IdLocReci = %d and Reci = %d and idLoc2 = %d"
        lista = idlocreci, idreci, idlocdes    
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc2 = row[0]
            self.reci2 = row[1]
            return True

    def verificar_homologa_idlocreci(self, idloc, reci, idloc2, reci2):
        s = "Select id from [bdge].[dbo].[hom]" + \
            " where idLoc = %d and reci = %d and idLoc2 = %d and reci2 = %d"
        lista = idloc, reci, idloc2, reci2    
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idhom = row[0]
            return True

    def get_homologa_idlocreci_origen(self, idloc, reci):
        s = "Select Dep, Prov, Sec, IdLoc, Dist, Zona, Reci, NomDep, NomProv, NombreMunicipio, AsientoElectoral, NomDist, NomZona, NombreRecinto," + \
            " Direccion, CircunDist, TipoLocLoc, TipoCircunscripcion, idTipoRecinto, TipoRecinto, latitud, longitud, doc_idA, doc_idAF" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in (4, 5, 82, 83) and IdLocReci = %d and Reci = %d"
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

    def get_homologa_idlocreci_destino(self, idloc2, reci2):
        s = "Select Dep, Prov, Sec, IdLoc, Dist, Zona, Reci, NomDep, NomProv, NombreMunicipio, AsientoElectoral, NomDist, NomZona, NombreRecinto," + \
            " Direccion, CircunDist, TipoLocLoc, TipoCircunscripcion, idTipoRecinto, TipoRecinto, latitud, longitud" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in (1, 2, 3, 6, 79, 80, 81, 84) and IdLocReci = %d and Reci = %d"
        lista = idloc2, reci2    
        self.cur.execute(s, lista)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dep2 = row[0]
            self.prov2 = row[1]
            self.sec2 = row[2]
            self.idloc2 = row[3]
            self.dist2 = row[4]
            self.zona2 = row[5]
            self.reci2 = row[6]
            self.departamento2 = row[7]
            self.provincia2 = row[8]
            self.municipio2 = row[9]
            self.asiento2 = row[10]
            self.nomdist2 = row[11]
            self.nomzona2 = row[12]
            self.recinto2 = row[13]
            self.direccion2 = row[14]
            self.circun2 = row[15]
            self.idtipocircun2 = row[16]
            self.tipocircun2 = row[17]
            self.idtiporecinto2 = row[18]
            self.tiporecinto2 = row[19]
            self.latitud2 = row[20]
            self.longitud2 = row[21]
            return True

    def add_homologa(self, dep, prov, sec, idloc, dist, zona, reci, departamento, provincia, municipio, \
                     asiento, nomdist, nomzona, recinto, direccion, circun, idtipocircun, tipocircun, \
                     idtiporecinto, tiporecinto, latitud, longitud, doc, doc1, dep2, prov2, sec2, \
                     idloc2, dist2, zona2, reci2, departamento2, provincia2, municipio2, asiento2, nomdist2, \
                     nomzona2, recinto2, direccion2, circun2, idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, \
                     latitud2, longitud2, f_ingreso, f_actual, usr):
        new_homologa = dep, prov, sec, idloc, dist, zona, reci, departamento, provincia, municipio, \
            asiento, nomdist, nomzona, recinto, direccion, circun, idtipocircun, tipocircun, \
            idtiporecinto, tiporecinto, latitud, longitud, doc, doc1, dep2, prov2, sec2, idloc2, dist2, \
            zona2, reci2, departamento2, provincia2, municipio2, asiento2, nomdist2, nomzona2, recinto2, \
            direccion2, circun2, idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, latitud2, \
            longitud2, 0, f_ingreso, f_actual, usr
        s = "insert into bdge.dbo.hom (dep, prov, sec, idloc, dist, zona, reci, nomDep, nomProv, nomSec, nomLoc," + \
            " nomDist, nomZona, nomReci, direccion, circun, idTipoCircun, tipoCircun, idTipoRecinto, tipoRecinto," + \
            " latitud, longitud, doc, doc1, dep2, prov2, sec2, idloc2, dist2, zona2, reci2, nomDep2, nomProv2," + \
            " nomSec2, nomLoc2, nomDist2, nomZona2, nomReci2, direccion2, circun2, idTipoCircun2, tipoCircun2," + \
            " idTipoRecinto2, tipoRecinto2, latitud2, longitud2, cerrado, fechaIngreso, fechaAct, usuario) VALUES" + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," + \
            " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_homologa)
            self.cx.commit()
            print("homologa adicionado...") 
        except:
            print("Error - actualización de homologa...")

    def upd_homologa(self, dep2, prov2, sec2, idloc2, dist2, zona2, reci2, departamento2, provincia2, municipio2, asiento2, nomdist2, \
                     nomzona2, recinto2, direccion2, circun2, idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, latitud2, longitud2, \
                     f_actual, usr, idhom):
        upd_homologa = dep2, prov2, sec2, idloc2, dist2, zona2, reci2, departamento2, provincia2, municipio2, asiento2, nomdist2, nomzona2, \
            recinto2, direccion2, circun2, idtipocircun2, tipocircun2, idtiporecinto2, tiporecinto2, latitud2, longitud2, f_actual, usr, idhom
        s = "update bdge.dbo.hom" + \
            " set dep2 = %s, prov2 = %s, sec2 = %s, idLoc2 = %s, dist2 = %s, zona2 = %s, reci2 = %s, nomDep2 = %s," + \
            " nomProv2 = %s, nomSec2 = %s, nomLoc2 = %s, nomDist2 = %s, nomZona2 = %s, nomReci2 = %s, direccion2 = %s," + \
            " circun2 = %s, idTipoCircun2 = %s, tipoCircun2 = %s, idTipoRecinto2 = %s, tipoRecinto2 = %s, latitud2 = %s, longitud2 = %s," + \
            " fechaAct = %s, usuario = %s" + \
            " where id = %d"
        try:
            self.cur.execute(s, upd_homologa)
            self.cx.commit()
            print('Homologa actualizado')
        except Exception as e:
            print("Error - actualización de Homologa...")        


    def get_recintos_idloc(self, idlocreci, circun):
        s = "select IdLoc, Reci, NomReci, NomZona, NomDist, CircunDist, Direccion" + \
            " from [bdge].[dbo].[v_reci_nal_all]" + \
            " where IdLoc = %d and CircunDist = %d and estado in (1, 2, 79, 80)"
        circuns = idlocreci, circun    
        self.cur.execute(s, circuns)
        rows = self.cur.fetchall()
        return rows


    def get_recintos_circun(self, dep, prov, sec, circun):
        s = "select IdLoc, Reci, NomReci, NomZona, NomDist, CircunDist, Direccion" + \
            " from [bdge].[dbo].[v_reci_nal_all]" + \
            " where Dep = %d and Prov = %d and Sec = %d and CircunDist = %d and estado in (1, 2, 79, 80)"
        circuns = dep, prov, sec, circun    
        self.cur.execute(s, circuns)
        rows = self.cur.fetchall()
        return rows


    def get_recintos_dep(self, dep):
        ''' Obtiene recintos destino para casos excepcionales (cualquier recinto del dep) '''

        s = "select IdLoc, Reci, NomReci, NomZona, NomDist, CircunDist, Direccion" + \
            " from [bdge].[dbo].[v_reci_nal_all]" + \
            " where Dep = %d  and estado in (1, 2, 79, 80)"
        self.cur.execute(s, dep)
        rows = self.cur.fetchall()
        return rows


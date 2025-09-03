# Homologaciones

class Homologa:
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_homologa_all(self, usrdep, inicio, final):
        '''  '''
        if inicio == "00-00-0000" and final == "00-00-0000":
            return False
        else:
            susp_supr = " (4, 5, 82, 83) "

            s = "Select IdLocReci, Reci, NomDep as Departamento, AsientoElectoral, NombreRecinto, Estado, idloc2, reci2, nomreci2, Area" + \
                " from [bdge].[dbo].[GeoRecintos_Hom_all]"
            if usrdep != 0 :
                lista = usrdep, inicio, final
                # suspendidos/suprimidos 
                s = s + " where idEstado in " + susp_supr + " and DEP = %d and Convert(CHAR(10),fechaAct,23) between %d and %d order by prov, sec"
                self.cur.execute(s, lista)
            else:
                lista = inicio, final
                s = s + " where idEstado in " + susp_supr + " and Convert(CHAR(10),fechaAct,23) between %d and %d order by Dep, Prov, Sec"
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
        susp_supr = " (4, 5, 82, 83) "
        s = "Select IdLocReci, Reci, NomDep as Departamento, AsientoElectoral, NombreRecinto, Estado, nroCircun, Dep, Prov, Sec" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in " + susp_supr + " and IdLocReci = %d and Reci = %d"
        t = idlocreci, idreci
        self.cur.execute(s, t)
        row = self.cur.fetchone()
        if  row:
            self.idlocreci = row[0]
            self.idreci = row[1]
            self.departamento = row[2]
            self.asiento = row[3]
            self.recinto = row[4]
            self.estado = row[5]
            self.circun = row[6] #nroCircun
            self.dep = row[7]
            self.prov = row[8]
            self.sec = row[9]


    def si_ya_homologado(self, idlocreci, idreci, idlocdes):
        ''' Determina con idlocdes - si existe idlocdes '''

        ''' rayado elim
        if idlocdes != 0:
            if idlocdes == idlocreci:
                    idlocdes=idlocreci
        else:
            idlocdes = idlocreci
        '''
        if idlocdes == 0:
            idlocdes = idlocreci

        susp_supr = " (4, 5, 82, 83) "

        s = "Select idLoc2, reci2 from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in " + susp_supr + " and IdLocReci = %d and Reci = %d and idLoc2 = %d"
        t = idlocreci, idreci, idlocdes
        self.cur.execute(s, t)
        row = self.cur.fetchone()
        if  row:
            self.idloc2 = row[0]
            self.reci2 = row[1]
        return row


    def existe_homologacion(self, idloc, reci, idloc2, reci2):
        s = "Select id from [bdge].[dbo].[hom]" + \
            " where idLoc = %d and reci = %d and idLoc2 = %d and reci2 = %d"
        t = idloc, reci, idloc2, reci2
        self.cur.execute(s, t)
        row = self.cur.fetchone()
        if row:
            self.idhom = row[0]
            return True


    def get_homologa_idlocreci_origen(self, idloc, reci):
        ''' Existe origen '''

        susp_supr = " (4, 5, 82, 83) "
        s = "Select Dep, Prov, Sec, IdLoc, Dist, Zona, Reci, NomDep, NomProv, NombreMunicipio, AsientoElectoral, NomDist, NomZona, NombreRecinto," + \
            " Direccion, NroCircun, TipoLocLoc, TipoCircunscripcion, idTipoRecinto, TipoRecinto, latitud, longitud, doc_idA, doc_idAF" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in " + susp_supr + " and IdLocReci = %d and Reci = %d"
        t = idloc, reci
        self.cur.execute(s, t)
        row = self.cur.fetchone()
        if  row:
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
            self.circun = row[15] #NroCircun
            self.idtipocircun = row[16]
            self.tipocircun = row[17]
            self.idtiporecinto = row[18]
            self.tiporecinto = row[19]
            self.latitud = row[20]
            self.longitud = row[21]
            self.doc = row[22]
            self.doc1 = row[23]


    def get_homologa_idlocreci_destino(self, idloc2, reci2):
        ''' Existe destino '''
        # destino - excepto suspendidos y suprimidos

        s = "Select Dep, Prov, Sec, IdLoc, Dist, Zona, Reci, NomDep, NomProv, NombreMunicipio, AsientoElectoral, NomDist, NomZona, NombreRecinto," + \
            " Direccion, NroCircun, TipoLocLoc, TipoCircunscripcion, idTipoRecinto, TipoRecinto, latitud, longitud" + \
            " from [bdge].[dbo].[GeoRecintos_Hom_all]" + \
            " where idEstado in (1, 2, 3, 6, 79, 80, 81, 84) and IdLocReci = %d and Reci = %d"
        t = idloc2, reci2
        self.cur.execute(s, t)
        row = self.cur.fetchone()
        if  row:
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
            self.recinto2 = row[13] #NroCircun
            self.direccion2 = row[14]
            self.circun2 = row[15]
            self.idtipocircun2 = row[16]
            self.tipocircun2 = row[17]
            self.idtiporecinto2 = row[18]
            self.tiporecinto2 = row[19]
            self.latitud2 = row[20]
            self.longitud2 = row[21]


    def add_homologa(self, *hom):
        new_hom = hom[0]
        s = "insert into bdge.dbo.hom (dep, prov, sec, idloc, dist, zona, reci, nomDep, nomProv, nomSec, nomLoc," + \
            " nomDist, nomZona, nomReci, direccion, circun, idTipoCircun, tipoCircun, idTipoRecinto, tipoRecinto," + \
            " latitud, longitud, doc, doc1, dep2, prov2, sec2, idloc2, dist2, zona2, reci2, nomDep2, nomProv2," + \
            " nomSec2, nomLoc2, nomDist2, nomZona2, nomReci2, direccion2, circun2, idTipoCircun2, tipoCircun2," + \
            " idTipoRecinto2, tipoRecinto2, latitud2, longitud2, cerrado, fechaIngreso, fechaAct, usuario) VALUES" + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," + \
            " %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_hom)
            self.cx.commit()
            print("Homologación adicionada...")
        except:
            print("Error - Adición de homologación...")


    def upd_homologa(self, *hom):
        upd_hom = hom
        s = "update bdge.dbo.hom" + \
            " set dep2 = %s, prov2 = %s, sec2 = %s, idLoc2 = %s, dist2 = %s, zona2 = %s, reci2 = %s, nomDep2 = %s," + \
            " nomProv2 = %s, nomSec2 = %s, nomLoc2 = %s, nomDist2 = %s, nomZona2 = %s, nomReci2 = %s, direccion2 = %s," + \
            " circun2 = %s, idTipoCircun2 = %s, tipoCircun2 = %s, idTipoRecinto2 = %s, tipoRecinto2 = %s, latitud2 = %s, longitud2 = %s," + \
            " fechaAct = %s, usuario = %s" + \
            " where id = %d"
        try:
            self.cur.execute(s, upd_hom)
            self.cx.commit()
            print('Homologación actualizada')
        except Exception as e:
            print("Error - Actualización de Homologación...")


    def get_recintos_idloc_cir(self, idlocreci, circun):
        ''' Recintos destino para asignar homolog. si urb en asiento y misma circun '''
        # hab/rehab TED TSE - (1,2,79,80)

        s = "select IdLoc, Reci, NomReci, NomZona, NomDist, NroCircun, Direccion" + \
            " from [bdge].[dbo].[v_reci_nal_all]" + \
            " where IdLoc = %d and NroCircun = %d and estado in (1, 2, 79, 80)"
        t = idlocreci, circun
        self.cur.execute(s, t)
        rows = self.cur.fetchall()
        return rows


    def get_recintos_circun(self, dep, prov, sec, circun):
        ''' Recintos destino para asignar homolog. '''
        # hab/rehab TED TSE - (1,2,79,80)

        s = "select IdLoc, Reci, NomReci, NomZona, NomDist, NroCircun, Direccion" + \
            " from [bdge].[dbo].[v_reci_nal_all]" + \
            " where Dep = %d and Prov = %d and Sec = %d and NroCircun = %d and estado in (1, 2, 79, 80)"
        t = dep, prov, sec, circun
        self.cur.execute(s, t)
        rows = self.cur.fetchall()
        return rows


    def get_recintos_dep(self, dep):
        ''' Obtiene recintos destino para casos excepcionales (cualquier recinto del dep) '''

        # hab/rehab TED TSE - (1,2,79,80)
        s = "select IdLoc, Reci, NomReci, NomZona, NomDist, NroCircun, Direccion" + \
            " from [bdge].[dbo].[v_reci_nal_all]" + \
            " where Dep = %d  and estado in (1, 2, 79, 80)"
        self.cur.execute(s, dep)
        rows = self.cur.fetchall()
        return rows

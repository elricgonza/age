# Operaciones asientos

class Asientos:
    idloc = 0
    deploc = 0
    provloc = 0
    secloc = 0
    nomloc = ""
    poblacionloc = 0
    poblacionelecloc = 0
    fechacensoloc = ''
    tipolocloc = ''
    fechabaselegloc = ''
    marcaloc = ''
    latitud = 0
    longitud = 0
    estado = 0
    circunconsulado = ''

    etapa = 0
    obsUbicacion = ''
    obs = ''
    doc_idA = 0
    docRspNal = 0
    fechaIngreso = ''
    fechaAct = ''
    usuario = ''

    _departamento = ''
    _provincia = ''
    _municipio = ''
    _tipo_circun = ''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_asientos_all(self, usrdep):        
        s = "select IdLoc, NomDep as Departamento, NomProv as Provincia, NombreMunicipio as Municipio," + \
            " AsientoElectoral as Asiento, tipoCircunscripcion, DEP, PROV, SEC, Estado" + \
            " from [bdge].[dbo].[GeoAsientos_Nacional_all]"
        if usrdep != 0 :
            s = s + " where DEP = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DEP, PROV, SEC"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_asiento_idloc(self, idloc):
        s = "select a.IdLoc, a.DepLoc, a.ProvLoc, a.SecLoc, a.NomLoc," + \
            " a.PoblacionLoc, a.PoblacionElecLoc, Convert(CHAR(10),a.FechaCensoLoc,23), a.TipoLocLoc, a.fechaBaseLegLoc," + \
            " a.MarcaLoc, a.latitud, a.longitud, a.estado, a.circunConsulado," + \
            " b.NomDep as _departamento, c.NomProv as _provincia, d.NomSec as _municipio, e.descripcion as TipoCircunscripcion," + \
            " a.etapa, a.doc_idA, a.obsUbicacion, a.doc_idRN, a.obs, a.fechaIngreso, a.fechaAct, a.usuario," + \
            " g.ruta as rutaA, h.ruta as rutaRN, b.IdPais, a.doc_idAF, i.ruta as rutaAF, f.idClasif as urural" + \
            " from [GeografiaElectoral_app].[dbo].[LOC] a" + \
            " left join [GeografiaElectoral_app].[dbo].[DEP] b on a.DepLoc= b.Dep" + \
            " left join [GeografiaElectoral_app].[dbo].[PROV] c on a.DepLoc= c.DepProv and a.ProvLoc= c.Prov" + \
            " left join [GeografiaElectoral_app].[dbo].[SEC] d on a.DepLoc= d.DepSec and a.ProvLoc= d.ProvSec and a.SecLoc= d.Sec" + \
            " left join [GeografiaElectoral_app].[dbo].[clasif] e on a.TipoLocLoc = e.idClasif" + \
            " left join [GeografiaElectoral_app].[dbo].[clasif] f on a.urbanoRural = f.idClasif and f.clasifGrupoId=4" + \
            " left join [bdge].[dbo].[doc] g on a.doc_idA=g.id" + \
            " left join [bdge].[dbo].[doc] h on a.doc_idRN=h.id" + \
            " left join [bdge].[dbo].[doc] i on a.doc_idAF=i.id" + \
            " where a.idloc = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        if row:
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
            self.rutaA = row[27]
            self.rutaRN = row[28]
            self.idpais = row[29]
            self.doc_idAF = row[30]
            self.rutaAF = row[31]
            self.urural = row[32]
        return row

    
    def add_asiento(self, idloc, deploc, provloc, \
                    secloc, nomloc, poblacionloc, \
                    poblacionelecloc, fechacensoloc, tipolocloc, \
                    latitud, longitud, \
                    estado, circunconsulado, etapa, obsUbicacion, \
                    obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal, docActF, urural):

        new_asiento = idloc, deploc, provloc, secloc, 0, \
            0, nomloc, poblacionloc, poblacionelecloc, fechacensoloc, \
            tipolocloc, '2007-01-01', '', 1, '', \
            '', 0, 0, 0, 0, \
            0, latitud, longitud, estado, circunconsulado, etapa, obsUbicacion, \
            obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal, docActF, urural

        s = "insert into GeografiaElectoral_app.dbo.loc (idloc, deploc, provloc, secloc, loc, " + \
            " idcanloc, nomloc, poblacionloc, poblacionelecloc, fechacensoloc, " + \
            " tipolocloc, fechabaselegloc, codbaselegloc, marcaloc, escabeceracanloc, " + \
            " escabecerasecloc, codprov, codsecc, tipocircun, circun, " + \
            " estadomapa, latitud, longitud, estado, circunconsulado, etapa, obsUbicacion, obs, fechaIngreso," + \
            " fechaAct, usuario, doc_idA, doc_idRN, doc_idAF, urbanoRural) VALUES " + \
            " (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s," + \
            " %s, %s,  %s, %s, %s,  %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_asiento)
            self.cx.commit()
            print("asiento adicionado...") 
        except:
            print("Error - actualización de asiento...")
    

    def upd_asiento(self, asiento):
        '''
            NO actualiza datos de jurisdicción - dep, prov, sec
        '''

        if self.diff_old_new_asi(asiento):
            s = "update GeografiaElectoral_app.dbo.loc" + \
                " set nomloc= %s, poblacionloc= %d, " + \
                " poblacionelecloc= %s, fechacensoloc= %s, tipolocloc= %d, " + \
                " latitud= %s, longitud= %d, " + \
                " estado= %d, circunconsulado= %s, " + \
                " etapa= %d, obsUbicacion= %s, obs= %s, fechaIngreso= %s," + \
                " fechaAct= %s, usuario= %s, doc_idA= %d, doc_idRN= %d, doc_idAF= %d, urbanoRural= %d" + \
                " where idloc = %d"
            try:
                self.cur.execute(s, asiento)
                self.cx.commit()
                print('Asiento actualizado')
            except Exception as e:
                print(e)
                print("Error - actualización de Asiento...")


    def diff_old_new_asi(self, row_to_upd):
        '''
        Verif. si existe dif. en registro editado
        '''
        a = self.get_asiento_idloc(row_to_upd[19])  #19 -> idloc

        '''
        row_old = self.nomloc, self.poblacionloc, \
                self.poblacionelecloc, self.fechacensoloc, self.tipolocloc, \
                self.latitud, self.longitud, \
                self.estado, self.etapa, \
                self.obsUbicacion, self.obs, \
                self.fechaIngreso, self.fechaAct, self.usuario, self.doc_idA, self.doc_idRN,  \
                self.doc_idAF, self.urural, self.idloc

        print('old---')
        print(row_old)
        print('new---*')
        print(row_to_upd)
        '''

        vdif = False

        if self.nomloc != row_to_upd[0]:
            print('nom dif')
            vdif = True
        if self.poblacionloc != int(row_to_upd[1]):
            print('poblacionloc dif')
            vdif = True
        if self.poblacionelecloc != int(row_to_upd[2]):
            print('poblacionelecloc dif')
            vdif = True
        if (self.fechacensoloc == None and row_to_upd[3] != None):
            print('fechacensoloc- null')
            vdif = True
        if (self.tipolocloc.strip() != row_to_upd[4]):
            print('tipolocloc- dif')
            vdif = True
        if (str(self.latitud) != row_to_upd[5]):
            print('lat - dif')
            print(str(self.latitud))
            vdif = True
        if (str(self.longitud) != row_to_upd[6]):
            print('long - dif')
            vdif = True
        if (str(self.estado) != row_to_upd[7]):
            print('estado - dif')
            vdif = True
        #a.circunConsulado
        if str(self.etapa) != row_to_upd[9]:
            print('etapa - dif')
            print(self.etapa)
            print(row_to_upd[9])
            vdif = True
        if (self.obsUbicacion != row_to_upd[10]):
            print('obsUbicacion dif')
            vdif = True
        if (self.obs != row_to_upd[11]):
            print('obs dif')
            vdif = True
        #a.fechaIngreso
        #a.fechaAct
        if (self.usuario != row_to_upd[14]):
            print('usuario dif')
            vdif = True
        if (str(self.doc_idA) != row_to_upd[15]):
            print('doc_idA  dif')
            vdif = True
        if (self.doc_idRN != int(row_to_upd[16])):
            print('doc_idRN dif')
            print(str(self.doc_idRN))
            print(row_to_upd[16])
            vdif = True
        if ((self.doc_idAF) != int(row_to_upd[17])):
            print('doc_idAF dif')
            print(str(self.doc_idAF))
            print(row_to_upd[17])
            vdif = True
        if (str(self.urural) != row_to_upd[18]):
            print('urural dif')
            vdif = True

        return vdif


    def upd_asiento_ex(self, idloc, deploc, provloc, \
                    secloc, nomloc, poblacionloc, \
                    poblacionelecloc, tipolocloc, \
                    latitud, longitud, \
                    estado, circunconsulado, etapa, obsUbicacion, \
                    obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal):
        
        asiento = deploc, provloc, \
                    secloc, nomloc, poblacionloc, \
                    poblacionelecloc, tipolocloc, \
                    latitud, longitud, \
                    estado, circunconsulado, etapa, obsUbicacion, \
                    obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal, idloc
        s = "update GeografiaElectoral_app.dbo.loc" + \
            " set deploc= %d, provloc= %d, secloc= %d, nomloc= %s, poblacionloc= %d, " + \
            " poblacionelecloc= %s, tipolocloc= %d, " + \
            " latitud= %s, longitud= %d, " + \
            " estado= %d, circunconsulado= %s, " + \
            " etapa= %d, obsUbicacion= %s, obs= %s, fechaIngreso= %s," + \
            " fechaAct= %s, usuario= %s, doc_idA= %d, doc_idRN= %d" + \
            " where idloc = %d"
        try:
            self.cur.execute(s, asiento)
            self.cx.commit()
            print('Asiento actualizado')
        except Exception as e:
            print("Error - actualización de Asiento...")
            print(e)
    
    def get_next_idloc(self):
        self.cur.execute("select max(idloc) + 1 from GeografiaElectoral_app.dbo.loc")
        row = self.cur.fetchone()
        return row[0]

    def get_geo_all(self, usrdep):
        s = "select gn.IdLoc, gn.Dep, gn.NomDep, gn.Prov, gn.NomProv, gn.Sec, gn.NombreMunicipio, gn.AsientoElectoral, gn.latitud," + \
        " gn.longitud, gn.idEstado, Convert(CHAR(10),gn.fechaIngreso,23) as fecha, gn.TipoCircunscripcion"  + \
        " from [bdge].[dbo].[GeoAsientos_Nacional_all] AS gn"
        self.cur.execute(s)
        if usrdep != 0 :
            s = s + " where DEP = %d order by gn.prov, gn.sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by gn.DEP, gn.PROV, gn.SEC"
            print(s)
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_tipocircun(self):
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=7"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def __str__(self):
        return str(self.idloc) + '--' + self.nomloc
    

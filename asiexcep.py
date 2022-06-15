# Operaciones asientos

class Asi_excep:
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

    def get_asi_excep_all(self, usrdep):        
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

    def get_asi_excep_idloc(self, idloc):
        s = "select a.IdLoc, a.DepLoc, a.ProvLoc, a.SecLoc, a.NomLoc," + \
            " a.PoblacionLoc, a.PoblacionElecLoc, Convert(CHAR(10),a.FechaCensoLoc,23), a.TipoLocLoc, a.fechaBaseLegLoc," + \
            " a.MarcaLoc, a.latitud, a.longitud, a.estado, a.circunConsulado," + \
            " b.NomDep as _departamento, c.NomProv as _provincia, d.NomSec as _municipio, e.descripcion as TipoCircunscripcion," + \
            " a.etapa, a.doc_idA, a.obsUbicacion, a.doc_idRN, a.obs, a.fechaIngreso, a.fechaAct, a.usuario," + \
            " g.ruta as rutaA, h.ruta as rutaRN, b.IdPais, a.doc_idAF, i.ruta as rutaAF, f.idClasif as urural, a.doc_idAT, j.ruta as rutaAT," + \
            " a.doc_idRNT, k.ruta as rutaRNT" + \
            " from [GeografiaElectoral_app].[dbo].[LOC] a" + \
            " left join [GeografiaElectoral_app].[dbo].[DEP] b on a.DepLoc= b.Dep" + \
            " left join [GeografiaElectoral_app].[dbo].[PROV] c on a.DepLoc= c.DepProv and a.ProvLoc= c.Prov" + \
            " left join [GeografiaElectoral_app].[dbo].[SEC] d on a.DepLoc= d.DepSec and a.ProvLoc= d.ProvSec and a.SecLoc= d.Sec" + \
            " left join [GeografiaElectoral_app].[dbo].[clasif] e on a.TipoLocLoc = e.idClasif" + \
            " left join [GeografiaElectoral_app].[dbo].[clasif] f on a.urbanoRural = f.idClasif and f.clasifGrupoId=4" + \
            " left join [bdge].[dbo].[doc] g on a.doc_idA=g.id" + \
            " left join [bdge].[dbo].[doc] h on a.doc_idRN=h.id" + \
            " left join [bdge].[dbo].[doc] i on a.doc_idAF=i.id" + \
            " left join [bdge].[dbo].[doc] j on a.doc_idAT=j.id" + \
            " left join [bdge].[dbo].[doc] k on a.doc_idRNT=k.id" + \
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
            self.doc_idAT = row[33]
            self.rutaAT = row[34]
            self.doc_idRNT = row[35]
            self.rutaRNT = row[36]
        return row

    
    def add_asi_excep(self, idloc, deploc, provloc, \
                      secloc, nomloc, poblacionloc, \
                      poblacionelecloc, fechacensoloc, tipolocloc, \
                      latitud, longitud, \
                      estado, circunconsulado, etapa, obsUbicacion, \
                      obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal, docActF, urural, docActT, docRspNalT):

        new_asiento = idloc, deploc, provloc, secloc, 0, \
            0, nomloc, poblacionloc, poblacionelecloc, fechacensoloc, \
            tipolocloc, '2007-01-01', '', 1, '', \
            '', 0, 0, 0, 0, \
            0, latitud, longitud, estado, circunconsulado, etapa, obsUbicacion, \
            obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal, docActF, urural, docActT, docRspNalT

        s = "insert into GeografiaElectoral_app.dbo.loc (idloc, deploc, provloc, secloc, loc, " + \
            " idcanloc, nomloc, poblacionloc, poblacionelecloc, fechacensoloc, " + \
            " tipolocloc, fechabaselegloc, codbaselegloc, marcaloc, escabeceracanloc, " + \
            " escabecerasecloc, codprov, codsecc, tipocircun, circun, " + \
            " estadomapa, latitud, longitud, estado, circunconsulado, etapa, obsUbicacion, obs, fechaIngreso," + \
            " fechaAct, usuario, doc_idA, doc_idRN, doc_idAF, urbanoRural, doc_idAT, doc_idRNT) VALUES " + \
            " (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s," + \
            " %s, %s,  %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_asiento)
            self.cx.commit()
            print("asiento adicionado...") 
        except:
            print("Error - actualización de asiento...")
    

    def upd_asi_excep(self, asiento):
        '''
            NO actualiza datos de jurisdicción - dep, prov, sec
        '''

        if self.diff_old_new_asi(asiento):
            s = "update GeografiaElectoral_app.dbo.loc" + \
                " set deploc= %d, provloc= %d, secloc= %d, nomloc= %s, poblacionloc= %d, " + \
                " poblacionelecloc= %s, fechacensoloc= %s, tipolocloc= %d, " + \
                " latitud= %s, longitud= %d, " + \
                " estado= %d, circunconsulado= %s, " + \
                " etapa= %d, obsUbicacion= %s, obs= %s, fechaIngreso= %s," + \
                " fechaAct= %s, usuario= %s, doc_idA= %d, doc_idRN= %d, doc_idAF= %d, urbanoRural= %d, doc_idAT= %d, doc_idRNT= %d" + \
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
        a = self.get_asi_excep_idloc(row_to_upd[24])  #21 -> idloc
        vdif = False

        if self.deploc != row_to_upd[0]:
            print('dep dif')
            vdif = True
        if self.provloc != row_to_upd[1]:
            print('prov dif')
            vdif = True
        if self.secloc != row_to_upd[2]:
            print('sec dif')
            vdif = True
        if self.nomloc != row_to_upd[3]:
            print('nom dif')
            vdif = True
        if self.poblacionloc != int(row_to_upd[4]):
            print('poblacionloc dif')
            vdif = True
        if self.poblacionelecloc != int(row_to_upd[5]):
            print('poblacionelecloc dif')
            vdif = True
        if (self.fechacensoloc == None and row_to_upd[6] != None):
            print('fechacensoloc- null')
            vdif = True
        if (self.tipolocloc.strip() != row_to_upd[7]):
            print('tipolocloc- dif')
            vdif = True
        if (str(self.latitud) != row_to_upd[8]):
            print('lat - dif')
            print(str(self.latitud))
            vdif = True
        if (str(self.longitud) != row_to_upd[9]):
            print('long - dif')
            vdif = True
        if (str(self.estado) != row_to_upd[10]):
            print('estado - dif')
            vdif = True
        #a.circunConsulado
        if str(self.etapa) != row_to_upd[12]:
            print('etapa - dif')            
            vdif = True
        if (self.obsUbicacion != row_to_upd[13]):
            print('obsUbicacion dif')
            vdif = True
        if (self.obs != row_to_upd[14]):
            print('obs dif')
            vdif = True
        #a.fechaIngreso
        #a.fechaAct
        if (self.usuario != row_to_upd[17]):
            print('usuario dif')
            vdif = True
        if (str(self.doc_idA) != row_to_upd[18]):
            print('doc_idA  dif')
            vdif = True
        if (self.doc_idRN != int(row_to_upd[19])):
            print('doc_idRN dif')
            vdif = True
        if ((self.doc_idAF) != int(row_to_upd[20])):
            print('doc_idAF dif')
            vdif = True
        if (str(self.urural) != row_to_upd[21]):
            print('urural dif')
            vdif = True
        if (str(self.doc_idAT) != row_to_upd[22]):
            print('doc_idAT  dif')
            vdif = True
        if (self.doc_idRNT != int(row_to_upd[23])):
            print('doc_idRNT dif')
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

    def get_estados(self):
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=3"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_etapas(self, usrdep, usrtipo):

        if usrdep != 0 and usrtipo == 116:
            s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=8 and idClasif in (70, 71)"
        elif usrdep == 0 and usrtipo == 117:
            s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=8 and idClasif in (70, 71, 72)"
        else:
            s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=8"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_depa_excep_all(self, usrdep):        
            s = "select Dep, NomDep from [GeografiaElectoral_app].[dbo].[DEP]"
            if usrdep != 0 :
                s = s + " where Dep <= 9 and Dep = %d order by Dep"
                self.cur.execute(s, usrdep)
            else:
                s = s + " where Dep <= 9 order by Dep"
                self.cur.execute(s)

            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_prov_excep_all(self, usrdep):        
        s = "select DepProv, Prov, NomProv from [GeografiaElectoral_app].[dbo].[PROV]"
        if usrdep != 0 :
            s = s + " where DepProv = %d order by DepProv"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DepProv"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_muni_excep_all(self, usrdep):        
        s = "select DepSec, ProvSec, Sec, NomSec from [GeografiaElectoral_app].[dbo].[SEC]"
        if usrdep != 0 :
            s = s + " where DepSec = %d order by DepSec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DepSec"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def __str__(self):
        return str(self.idloc) + '--' + self.nomloc
    

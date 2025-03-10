# Operaciones recintos

class Recintos:
    idlocreci=0
    reci=0
    nomreci=''
    zonareci=0
    maxmesasreci=0
    ambientes=0
    direccion=''
    latitud=0
    longitud=0
    estado=0
    tiporecinto=0
    codrue=''
    codrueedif=''
    depend=0
    cantpisos=''
    fechaIngreso=''
    fechaAct=''
    usuario=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_reci_uninom_mixto(self, usrdep):
        '''Obtiene recintos uninominales y mixtos '''

        s = "Select IdLoc as IdLocReci, Reci, NomDep as Departamento, NomProv as Provincia, NomMun as Municipio," + \
            " NomReci as NombreRecinto, nombreTipoLocLoc as TipoCircunscripcion, DEP, PROV, SEC, desEstado as Estado, desEtapa, usuario " + \
            " from [bdge].[dbo].[v_reci_nal_all]"
        if usrdep != 0:
            s = s + " where  TipoLocLoc in (67, 69) and DEP = %d order by prov, sec"  #67 uninom, 69 mixt
            self.cur.execute(s, usrdep)
        else:
            s = s + " where  TipoLocLoc in (67, 69) order by Dep, Prov, Sec"
            self.cur.execute(s, usrdep)

        rows = self.cur.fetchall()
        return rows


    def get_recinto_idreci(self, idreci, idlocreci):
        s = "select a.IdLocReci, a.Reci, g.CircunDist, b.DepLoc, c.NomDep, b.ProvLoc, " + \
            "d.NomProv, b.SecLoc, e.NomSec, a.NomReci, a.ZonaReci, a.MaxMesasReci, " + \
            "a.Direccion, a.latitud, a.longitud, a.estado, a.tipoRecinto, " + \
            "a.codRue, a.codRueEdif, a.depend, a.cantPisos, a.fechaIngreso, a.fechaAct, a.usuario, " + \
            "a.etapa, a.doc_idA, a.doc_idAF, h.ruta as rutaA, i.ruta as rutaAF, b.NomLoc, a.ambientesDisp, a.doc_idT, j.ruta as rutaT " + \
            "from [GeografiaElectoral_app].[dbo].[RECI] a " + \
            "inner join [GeografiaElectoral_app].[dbo].[LOC] b on a.IdLocReci=b.IdLoc " + \
            "inner join [GeografiaElectoral_app].[dbo].[DEP] c on b.DepLoc=c.Dep " + \
            "inner join [GeografiaElectoral_app].[dbo].[PROV] d on b.ProvLoc=d.Prov and b.DepLoc=d.DepProv " + \
            "inner join [GeografiaElectoral_app].[dbo].[SEC] e on b.SecLoc=e.Sec and b.DepLoc=e.DepSec and b.ProvLoc=e.ProvSec " + \
            "inner join [GeografiaElectoral_app].[dbo].[ZONA] f on a.IdLocReci=f.IdLocZona and a.ZonaReci=f.Zona " + \
            "inner join [GeografiaElectoral_app].[dbo].[DIST] g on f.IdLocZona=g.IdLocDist and f.DistZona=g.Dist " + \
            "left join [bdge].[dbo].[doc] h on a.doc_idA=h.id " + \
            "left join [bdge].[dbo].[doc] i on a.doc_idAF=i.id " + \
            "left join [bdge].[dbo].[doc] j on a.doc_idT=j.id " + \
            "where a.IdLocReci = %d and a.Reci = %d"
        mod_recinto = idlocreci, idreci
        self.cur.execute(s, mod_recinto)
        row = self.cur.fetchone()
        if  row:
            self.idlocreci = row[0]
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
            self.ambientes = row[30]
            self.doc_idT = row[31]
            self.rutaT = row[32]
        return row


    def add_recinto(self, idlocreci, reci, nomreci, zonareci, \
                    maxmesasreci, direccion, latitud, longitud, \
                    estado, tiporecinto, codrue, \
                    codrueedif, depend, \
                    cantpisos, fechaIngreso, fechaAct, usuario, etapa, docAct, docActF, ambientes, docTec):

        new_recinto = idlocreci, reci, nomreci, '', '', zonareci, \
            maxmesasreci, direccion, latitud, longitud, \
            estado, tiporecinto, codrue, codrueedif, \
            depend, cantpisos, fechaIngreso, fechaAct, usuario, etapa, docAct, docActF, '0', ambientes, docTec

        s = "insert into [GeografiaElectoral_app].[dbo].[RECI] (IdLocReci, Reci, NomReci, SupReci, ApoyoReci, " + \
            " ZonaReci, MaxMesasReci, Direccion, latitud, " + \
            " longitud, estado, tipoRecinto, codRue, codRueEdif, " + \
            " depend, cantPisos, fechaIngreso, fechaAct, usuario, etapa, doc_idA, doc_idAF, nacionId, ambientesDisp, doc_idT) VALUES " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_recinto)
            self.cx.commit()
            print("recinto adicionado...") 
        except:
            print("Error - actualización de recinto...")


    def upd_recinto(self, recinto):
        if self.diff_old_new_reci(recinto):
            s = "update GeografiaElectoral_app.dbo.RECI" + \
                " set NomReci= %s, ZonaReci= %s, MaxMesasReci= %s, Direccion= %s, latitud= %s, " + \
                " longitud= %s, estado= %s, tipoRecinto= %s, codRue= %s, codRueEdif= %s, " + \
                " depend= %d, cantPisos= %s, fechaAct= %s, usuario= %s, " + \
                " etapa= %s, doc_idA= %s, doc_idAF= %s, ambientesDisp= %s, doc_idT= %s " + \
                " where IdLocReci = %s and Reci = %s"
            try:
                self.cur.execute(s, recinto)
                self.cx.commit()
                print('Recinto actualizado')
            except Exception as e:
                print("Error - actualización de Recinto...")


    def diff_old_new_reci(self, row_to_upd):
        rc = self.get_recinto_idreci(row_to_upd[20], row_to_upd[19])  #19 -> idreci, #20 -> idlocreci
        vdif = False
        if self.nomreci != row_to_upd[0]:
            #print('nom dif')
            vdif = True
        if self.zonareci != int(row_to_upd[1]):
            #print('zonareci dif')
            vdif = True
        if self.maxmesasreci != int(row_to_upd[2]):
            #print('maxmesasreci dif')
            vdif = True
        if (self.direccion != row_to_upd[3]):
            #print('direccion dif')
            vdif = True
        if (str(self.latitud) != row_to_upd[4]):
            #print('latitud dif')
            vdif = True
        if (str(self.longitud) != row_to_upd[5]):
            #print('longitud dif')
            vdif = True
        if self.estado != int(row_to_upd[6]):
            #print('estado dif')
            vdif = True
        if self.tiporecinto != int(row_to_upd[7]):
            #print('tiporecinto dif')
            vdif = True
        if self.codrue != row_to_upd[8]:
            #print('codrue dif')
            vdif = True
        if self.codrueedif != row_to_upd[9]:
            #print('codrueedit dif')
            vdif = True
        #if self.depend != int(row_to_upd[10]):
        if ((self.depend) != (0 if row_to_upd[10]=="" else int(row_to_upd[10]) )):
            #print('depend dif')
            vdif = True
        if self.cantpisos != row_to_upd[11]:
            #print('cantPisos dif')
            vdif = True
        #a.fechaAct
        '''
        if self.usuario != row_to_upd[13]:
            #print('usuario dif')
            vdif = True
        '''
        if self.etapa != int(row_to_upd[14]):
            #print('etapa dif')
            vdif = True
        #if self.doc_idA != int(row_to_upd[15]):
        if ((self.doc_idA) != (0 if row_to_upd[15]=="" else int(row_to_upd[15]) )):
            #print('doc_idA dif')
            vdif = True
        if self.doc_idAF != int(row_to_upd[16]):
            #print('doc_idAF dif')
            vdif = True
        if self.ambientes != int(row_to_upd[17]):
            #print('ambientesDisp dif')
            vdif = True
        #if self.doc_idT != int(row_to_upd[18]):
        if ((self.doc_idT) != (0 if row_to_upd[18]=="" else int(row_to_upd[18]) )):
            #print('doc_idT dif')
            vdif = True

        return vdif


    def upd_reci_noauth(self, row_to_upd):
        '''tmpauth3 valida que no se modifiquen datos no autorizados'''

        rc = self.get_recinto_idreci(row_to_upd[20], row_to_upd[19])  #19 -> idreci, #20 -> idlocreci
        vdif = False
        if self.nomreci != row_to_upd[0]:
            print('nom dif -auth3')
            vdif = True
        if self.zonareci != int(row_to_upd[1]):
            print('zonareci dif -auth3')
            vdif = True
        '''
        if self.maxmesasreci != int(row_to_upd[2]):
            print('maxmesasreci dif')
            vdif = True
        if (self.direccion != row_to_upd[3]):
            print('direccion dif')
            vdif = True
        '''
        if (str(self.latitud) != row_to_upd[4]):
            print('latitud dif -auth3')
            vdif = True
        if (str(self.longitud) != row_to_upd[5]):
            print('longitud dif -auth3')
            vdif = True
        if self.estado != int(row_to_upd[6]):
            print('estado dif -auth3')
            vdif = True
        '''
        if self.tiporecinto != int(row_to_upd[7]):
            print('tiporecinto dif')
            vdif = True
        if self.codrue != row_to_upd[8]:
            print('codrue dif')
            vdif = True
        if self.codrueedif != row_to_upd[9]:
            print('codrueedit dif')
            vdif = True
        if self.depend != int(row_to_upd[10]):
            print('depend dif')
            vdif = True
        if self.cantpisos != row_to_upd[11]:
            print('cantPisos dif')
            vdif = True
        #a.fechaAct
        if self.usuario != row_to_upd[13]:
            print('usuario dif')
            vdif = True
        '''
        if self.etapa != int(row_to_upd[14]):
            print('etapa dif -auth3')
            vdif = True
        '''
        if self.doc_idA != int(row_to_upd[15]):
            print('doc_idA dif')
            vdif = True
        if self.doc_idAF != int(row_to_upd[16]):
            print('doc_idAF dif')
            vdif = True
        if self.ambientes != int(row_to_upd[17]):
            print('ambientesDisp dif')
            vdif = True
        if self.doc_idT != int(row_to_upd[18]):
            print('doc_idT dif')
            vdif = True
        '''

        return vdif

    def get_next_reci(self):
        self.cur.execute("select max(reci) + 1 from GeografiaElectoral_app.dbo.reci")
        row = self.cur.fetchone()
        return row[0]


    def get_estados_reci(self, usrtipo):
        ''' Obtiene estados en función del tipo de usr '''

        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif]"

        if usrtipo == 116: # dep
            s = s + " where clasifGrupoId=1 and idClasif in (1, 2, 3, 4, 5, 6)" # estados TED
        else:
            s = s + " where clasifGrupoId=1"
        self.cur.execute(s)

        rows = self.cur.fetchall()
        return rows


    def get_tiporecintos(self):
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=2"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_etapas(self, usrtipo):
        ''' Obtiene etapas en función del tipo de usuario '''

        if usrtipo == 116: # dep
            s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=8 and idClasif in (70, 71)"
        elif usrtipo in (117, 118, 119, 124): # nal, adm, jefat, consulta
            s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=8"

        self.cur.execute(s)
        rows = self.cur.fetchall()
        return rows


    def get_etapas_auth(self, usrdep, usrtipo):
        #auth3tmp creado sólo para transcripción habilitar usuario transcriptor

        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=8"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_dependencias(self):
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=6"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_recintos_all1(self, usrdep):
        s = "Select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, IdLoc, AsientoElectoral, Reci, NombreRecinto, doc_act, fecha_doc_act, " + \
            "cod_dist, NomDist, cod_zona, NomZona, Direccion, CircunDist, tipoCircunscripcion, tipoRecinto, etapa, estado, latitud, longitud, fechaIngreso, " + \
            "fechaAct, usuario " + \
            "from [bdge].[dbo].[Geo_Recintos_all]"
        if usrdep != 0 :
            s = s + " where Dep = %d order by Prov, Sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by Dep, Prov, Sec"
            self.cur.execute(s, usrdep)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def __str__(self):
        return str(self.idloc) + ' - ' + str(self.reci) +  ' -- ' + self.nomloc

# Operaciones recintos - Uninominales/Especiales

class Recintos:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_reci_uninom(self, usrdep):
        '''Obtiene recintos uninominales'''

        s = "Select IdLoc as IdLocReci, Reci, NomDep as Departamento, NomProv as Provincia, NomMun as Municipio," + \
            " NomReci as NombreRecinto, TipoCircun as TipoCircunscripcion, DEP, PROV, SEC, desEstado as Estado, desEtapa, usuario " + \
            " from [bdge].[dbo].[v_reci_nal_all]"
        if usrdep != 0:
            s = s + " where (TipoCircun = 'Uninominal' or isnull(TipoCircun,'')='')  and DEP = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where (TipoCircun = 'Uninominal' or isnull(TipoCircun,'')='')  order by Dep, Prov, Sec"
            self.cur.execute(s, usrdep)

        rows = self.cur.fetchall()
        return rows


    def get_recinto_key(self, idlocreci, reci):
        s = "select a.IdLocReci, a.Reci, a.idCircun, b.DepLoc, c.NomDep, b.ProvLoc, " + \
            "d.NomProv, b.SecLoc, e.NomSec, a.NomReci, a.ZonaReci, a.MaxMesasReci, " + \
            "a.Direccion, a.latitud, a.longitud, a.estado, a.tipoRecinto, " + \
            "a.codRue, a.codRueEdif, a.depend, a.cantPisos, a.fechaIngreso, a.fechaAct, a.usuario, " + \
            "a.etapa, a.doc_idA, a.doc_idAF, h.ruta as rutaA, i.ruta as rutaAF, b.NomLoc, a.ambientesDisp, " + \
            "a.doc_idT, j.ruta as rutaT, a.obs, f.zonaGeo, g.distGeo, a.nacionId " + \
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
        key = idlocreci, reci
        self.cur.execute(s, key)
        row = self.cur.fetchone()
        if  row:
            self.idlocreci = row[0]
            self.reci = row[1]
            self.idcircun = row[2]
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
            self.obs = row[33]
            self.zonaGeo = row[34]
            self.distGeo = row[35]
            self.nacionId = row[36]
        return row


    def add_recinto(self, datos):
        s = "insert into [GeografiaElectoral_app].[dbo].[RECI] " + \
                " (IdLocReci, Reci, NomReci, ZonaReci, MaxMesasReci, " + \
                " direccion, latitud, longitud, estado, tipoRecinto, " + \
                " codRue, codRueEdif, depend, cantPisos, fechaIngreso, " + \
                " fechaAct, usuario, etapa, doc_idA, doc_idAF, " + \
                " ambientesDisp, doc_idT, idcircun, obs, nacionId) VALUES " + \
                " (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, " + \
                " %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, " + \
                " %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, datos)
            self.cx.commit()
            print("recinto adicionado...") 
            return True
        except Exception as e:
            print(e)
            print("Error - actualización de recinto...")


    def upd_recinto(self, recinto):
        if self.diff_old_new_reci(recinto):
            s = "update GeografiaElectoral_app.dbo.RECI" + \
                " set NomReci= %s, ZonaReci= %s, MaxMesasReci= %s, Direccion= %s, latitud= %s, " + \
                " longitud= %s, estado= %s, tipoRecinto= %s, codRue= %s, codRueEdif= %s, " + \
                " depend= %d, cantPisos= %s, fechaAct= %s, usuario= %s, " + \
                " etapa= %s, doc_idA= %s, doc_idAF= %s, ambientesDisp= %s, doc_idT= %s, " + \
                " obs= %s, nacionId= %s" + \
                " where IdLocReci = %s and Reci = %s"
            try:
                self.cur.execute(s, recinto)
                self.cx.commit()
                print('Recinto actualizado')
            except Exception as e:
                print(e)
                print("Error - actualización de Recinto...")


    def diff_old_new_reci(self, row_to_upd):
        #upd 21ago2025 - add obs, nacionId
        rc = self.get_recinto_key(row_to_upd[21], row_to_upd[22]) 
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

        #obs
        if self.obs.strip() != row_to_upd[19].strip():
            #print('dif...... (ambos son STR)')
            vdif = True

        if self.nacionId != row_to_upd[20]:
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


    def get_naciones(self):
        s = "select idClasif, descripcion, clasifSubGrupo from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=5"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        return rows


    def get_dependencias(self):
        s = "select idClasif, descripcion from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId=6"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_recintos_sincro(self, usrdep):
        '''Used en opc sincroniza'''

        s = '''
            select dep, prov, sec, NomDep, NomProv, NomMun, IdLoc,
            NomLoc, Reci, NomReci, rspted_cite, rspted_fecha, dist, NomDist,
            Zona, NomZona, Direccion, NroCircun, TipoCircun, desTipoRecinto, desEtapa,
            desEstado, latitud, longitud, fechaIngreso, fechaAct, usuario
            from [bdge].[dbo].[v_reci_nal_all]
        '''
        if usrdep != 0 :
            s = s + " where Dep = %d order by Prov, Sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by Dep, Prov, Sec"
            self.cur.execute(s, usrdep)

        rows = self.cur.fetchall()
        return rows


    def get_reci_espec(self, usrdep):
        ''' Obtiene recintos especiales (indígenas) 
        condic idloc not in (729, 820, 821, 2059, 2680, 2234) --asientos capitales: lpz, ea, cbba, or, tja, scz
        '''

        s = "Select IdLoc as IdLocReci, Reci, NomDep as Departamento, NomProv as Provincia, NomMun as Municipio, " + \
            " NomReci as NombreRecinto, TipoCircun as TipoCircunscripcion, DEP, PROV, SEC, desEstado as Estado, desEtapa, usuario " + \
            " from [bdge].[dbo].[v_reci_nal_all] " 
        if usrdep != 0:
            s = s + " where (TipoCircun= 'Especial' or isnull(TipoCircun,'')='') and DEP = %d and DEP not in (1,5) " + \
                " and idloc not in (729, 820, 821, 2059, 2680, 2234) " + \
                " order by Estado, prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where (TipoCircun= 'Especial' or isnull(TipoCircun,'')='') and DEP not in (1,5) " + \
                " and idloc not in (729, 820, 821, 2059, 2680, 2234) " + \
                " order by Estado, Dep, Prov, Sec"
            self.cur.execute(s, usrdep)

        rows = self.cur.fetchall()
        return rows


class RecintosExcep(Recintos):
    ''' Clase para recintos excepcionales - hereda de recintos '''

    def __init__(self, cx):
        super().__init__(cx)


    def get_reci_excep(self, usrdep):
        '''Obtiene para actualización como recintos excepcionales'''

        s = "Select IdLoc as IdLocReci, Reci, NomDep as Departamento, NomProv as Provincia, NomMun as Municipio," + \
            " NomReci as NombreRecinto, TipoCircun as TipoCircunscripcion, DEP, PROV, SEC, desEstado as Estado, desEtapa, usuario " + \
            " from [bdge].[dbo].[v_reci_nal_all]"

        if usrdep != 0:
            s = s + " where Dep = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by Dep, Prov, Sec"
            self.cur.execute(s)
        rows = self.cur.fetchall()
        return rows


    def upd_recinto_excep(self, recinto):
        '''Complementa con dato de circunscripción (idCircun)
            omite nacionId en actualización 
            hummm no neces si se habilita edit sólo en modulo uninominales

            -pendiente correcciones - justificaría sólo upd de coordenadas
            -upd de munic, prov, dep  -> cambio de jurisdicción
            -upd de circun debiera estar asociada a validación de departamento
            -si se habilita edición en grabar omitir:
                    -ZonaReci, nacionId, idCircun
                    -visualizar datos solo readonly para dep, prov, sec, circun, asiento, zona
                    -al introducir coordenadas NO actualizar dep, prov, sec dist zona
        '''

        super().get_recinto_key(recinto[22], recinto[23])  #22 -> idlocreci, #23 -> reci

        if super().diff_old_new_reci(recinto):
            s = "update GeografiaElectoral_app.dbo.RECI" + \
                " set NomReci= %s, ZonaReci= %s, MaxMesasReci= %s, Direccion= %s, latitud= %s, " + \
                " longitud= %s, estado= %s, tipoRecinto= %s, codRue= %s, codRueEdif= %s, " + \
                " depend= %d, cantPisos= %s, fechaAct= %s, usuario= %s, " + \
                " etapa= %s, doc_idA= %s, doc_idAF= %s, ambientesDisp= %s, doc_idT= %s, " + \
                " obs= %s, nacionId= %s, idCircun= %s " + \
                " where IdLocReci = %s and Reci = %s"
            try:
                self.cur.execute(s, recinto)
                self.cx.commit()
                print('Recinto Excepcional actualizado')
            except Exception as e:
                print(e)
                print("Error - actualización de Recinto Excepcional..")


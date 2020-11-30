# Operaciones asientos

class Recintos:
    idlocreci=0
    reci=0
    nomreci=''
    zonareci=0
    maxmesasreci=0
    direccion=''
    latitud=0
    longitud=0
    estado=0
    tiporecinto=0
    codrue=''
    codrueedif=''
    depend=0
    nroaulas=''
    cantpisos=''
    fechaIngreso=''
    fechaAct=''
    usuario=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_recintos_all(self, usrdep):        
        s = "Select IdLocReci, Reci, NomDep as Departamento, NomProv as Provincia, NombreMunicipio as Municipio," + \
            " NombreRecinto, NombreTipoLocLoc as Tipo_Circun, DEP, PROV, SEC," + \
            " CASE WHEN estado = 1 THEN 'Habilitado'" + \
            " WHEN estado = 2 THEN 'Rehabilitado'" + \
            " WHEN estado = 3 THEN 'Bloqueado'" + \
            " WHEN estado = 6 THEN 'Saturado'" + \
            " ELSE 'oother'  END as Estado" + \
            " from [GeografiaElectoral_app].[dbo].[GeoRecintos_Nacional]"
        if usrdep != 0 :
            s = s + " where DEP = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by Dep, Prov, Sec"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_recinto_idreci(self, idreci, idlocreci):
        s = "select a.IdLocReci, a.Reci, g.CircunDist, b.DepLoc, c.NomDep, b.ProvLoc, " + \
            "d.NomProv, b.SecLoc, e.NomSec, a.NomReci, a.ZonaReci, a.MaxMesasReci, " + \
            "a.Direccion, a.latitud, a.longitud, a.estado, a.tipoRecinto, " + \
            "a.codRue, a.codRueEdif, a.depend, a.nroAulas, a.cantPisos, a.fechaIngreso, a.fechaAct, a.usuario " + \
            "from [GeografiaElectoral_app].[dbo].[RECI] a " + \
            "inner join [GeografiaElectoral_app].[dbo].[LOC] b on a.IdLocReci=b.IdLoc " + \
            "inner join [GeografiaElectoral_app].[dbo].[DEP] c on b.DepLoc=c.Dep " + \
            "inner join [GeografiaElectoral_app].[dbo].[PROV] d on b.ProvLoc=d.Prov and b.DepLoc=d.DepProv " + \
            "inner join [GeografiaElectoral_app].[dbo].[SEC] e on b.SecLoc=e.Sec and b.DepLoc=e.DepSec and b.ProvLoc=e.ProvSec " + \
            "inner join [GeografiaElectoral_app].[dbo].[ZONA] f on a.IdLocReci=f.IdLocZona and a.ZonaReci=f.Zona " + \
            "inner join [GeografiaElectoral_app].[dbo].[DIST] g on f.IdLocZona=g.IdLocDist and f.DistZona=g.Dist " + \
            "where a.IdLocReci = %d and a.Reci = %d"
        mod_recinto = idlocreci, idreci
        self.cur.execute(s, mod_recinto)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
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
            self.nroaulas = row[20]
            self.cantpisos = row[21]
            self.fechaIngreso = row[22]
            self.fechaAct = row[23]
            self.usuario = row[24]
            return True


    def add_recinto(self, idlocreci, reci, nomreci, zonareci, \
                    maxmesasreci, direccion, latitud, longitud, \
                    estado, tiporecinto, codrue, \
                    codrueedif, depend, nroaulas, \
                    cantpisos, fechaIngreso, fechaAct, usuario):

        new_recinto = idlocreci, reci, nomreci, '', '', zonareci, \
            maxmesasreci, direccion, latitud, longitud, \
            estado, tiporecinto, codrue, codrueedif, \
            depend, nroaulas, cantpisos, fechaIngreso, fechaAct, usuario

        s = "insert into [GeografiaElectoral_app].[dbo].[RECI] (IdLocReci, Reci, NomReci, SupReci, ApoyoReci, " + \
            " ZonaReci, MaxMesasReci, Direccion, latitud, " + \
            " longitud, estado, tipoRecinto, codRue, codRueEdif, " + \
            " depend, nroAulas, cantPisos, fechaIngreso, fechaAct, usuario) VALUES " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_recinto)
            self.cx.commit()
            print("recinto adicionado...") 
        except:
            print("Error - actualización de recinto...")


    def upd_recinto(self, idlocreci, reci, nomreci, zonareci, \
                    maxmesasreci, direccion, latitud, longitud, \
                    estado, tiporecinto, codrue, \
                    codrueedif, depend, nroaulas, \
                    cantpisos, fechaIngreso, fechaAct, usuario):

        recinto = idlocreci, nomreci, zonareci, \
            maxmesasreci, direccion, latitud, longitud, \
            estado, tiporecinto, codrue, codrueedif, \
            depend, nroaulas, cantpisos, fechaIngreso, fechaAct, usuario, reci

        s = "update GeografiaElectoral_app.dbo.reci" + \
            " set IdLocReci= %s, NomReci= %s, ZonaReci= %s, MaxMesasReci= %s, Direccion= %s, latitud= %d, " + \
            " longitud= %s, estado= %s, tipoRecinto= %s, codRue= %s, codRueEdif= %s, " + \
            " depend= %d, nroAulas= %s, cantPisos= %s, fechaIngreso= %s, fechaAct= %s, usuario= %s " + \
            " where Reci = %s"
        try:
            self.cur.execute(s, recinto)
            self.cx.commit()
            print('Recinto actualizado')
        except Exception as e:
            print("Error - actualización de Recinto...")


    def get_next_reci(self):
        self.cur.execute("select max(reci) + 1 from GeografiaElectoral_app.dbo.reci")
        row = self.cur.fetchone()
        return row[0]
# Operaciones asientos

class Exterior:
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


    def get_exterior_all(self, usrdep):        
        s = "select IdLoc, NomPais, NomDep, NomProv, NomSec, NomLoc, Estado" + \
	    " from [bdge].[dbo].[GeoAsientos_Exterior_all]"
        if usrdep != 0 :
            s = s + " where DEP = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by IdPais, Dep, Prov, Sec, IdLoc"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_exterior_idloc(self, idloc):
        s = "select a.IdLoc, a.DepLoc, a.ProvLoc, a.SecLoc, a.NomLoc," + \
            " a.PoblacionLoc, a.PoblacionElecLoc, Convert(CHAR(10),a.FechaCensoLoc,23), a.TipoLocLoc, a.fechaBaseLegLoc," + \
            " a.MarcaLoc, a.latitud, a.longitud, a.estado, a.circunConsulado," + \
            " b.NomDep as _departamento, c.NomProv as _provincia, d.NomSec as _municipio, e.descripcion as TipoCircunscripcion," + \
            " a.etapa, a.doc_idA, a.obsUbicacion, a.doc_idRN, a.obs, a.fechaIngreso, a.fechaAct, a.usuario," + \
            " g.ruta as rutaA, h.ruta as rutaRN, b.IdPais, a.doc_idAF, i.ruta as rutaAF" + \
            " from [GeografiaElectoral_app].[dbo].[LOC] a" + \
            " left join [GeografiaElectoral_app].[dbo].[DEP] b on a.DepLoc= b.Dep" + \
            " left join [GeografiaElectoral_app].[dbo].[PROV] c on a.DepLoc= c.DepProv and a.ProvLoc= c.Prov" + \
            " left join [GeografiaElectoral_app].[dbo].[SEC] d on a.DepLoc= d.DepSec and a.ProvLoc= d.ProvSec and a.SecLoc= d.Sec" + \
            " left join [GeografiaElectoral_app].[dbo].[clasif] e on a.TipoLocLoc = e.idClasif" + \
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
        return row

    def add_exterior(self, idloc, deploc, provloc, \
                    secloc, nomloc, poblacionloc, \
                    poblacionelecloc, fechacensoloc, tipolocloc, \
                    latitud, longitud, \
                    estado, circunconsulado, etapa, obsUbicacion, \
                    obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal, docActF):

        new_asiento = idloc, deploc, provloc, secloc, 0, \
            0, nomloc, poblacionloc, poblacionelecloc, fechacensoloc, \
            tipolocloc, '2007-01-01', '', 1, '', \
            '', 0, 0, 0, 0, \
            0, latitud, longitud, estado, circunconsulado, etapa, obsUbicacion, \
            obs, fechaIngreso, fechaAct, usuario, docAct, docRspNal, docActF, 0

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
            print("Error - Creacion de asiento...")

    def get_paises_all(self, usrdep):        
            s = "select IdPais, NomPais from [GeografiaElectoral_app].[dbo].[PAIS]"
            if usrdep != 0 :
                s = s + " where IdPais = %d order by IdPais"
                self.cur.execute(s, usrdep)
            else:
                s = s + " where IdPais != 32 order by IdPais"
                self.cur.execute(s)

            rows = self.cur.fetchall()
            print(rows)
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_departamentos_all(self, usrdep):        
            s = "select Dep, NomDep, IdPais from [GeografiaElectoral_app].[dbo].[DEP]"
            if usrdep != 0 :
                s = s + " where Dep = %d order by Dep"
                self.cur.execute(s, usrdep)
            else:
                s = s + " order by Dep"
                self.cur.execute(s)

            rows = self.cur.fetchall()
            print(rows)
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_provincias_all(self, usrdep):        
        s = "select DepProv, Prov, NomProv from [GeografiaElectoral_app].[dbo].[PROV]"
        if usrdep != 0 :
            s = s + " where DepProv = %d order by DepProv"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DepProv"
            print(s)
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_municipios_all(self, usrdep):        
        s = "select DepSec, ProvSec, Sec, NomSec from [GeografiaElectoral_app].[dbo].[SEC]"
        if usrdep != 0 :
            s = s + " where DepSec = %d order by DepSec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DepSec"
            print(s)
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

        

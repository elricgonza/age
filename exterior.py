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
        s = "select IdLoc, NomPais, NomDep, NomProv, NomSec, NomLoc, " + \
            "CASE WHEN estado = 101 THEN 'Habilitado TSE' " + \
                    "WHEN estado = 102 THEN 'Rehabilitado TSE' " + \
                    "WHEN estado = 103 THEN 'Suspendido TSE' " + \
                    "WHEN estado = 104 THEN 'Suprimido TSE' " + \
            "ELSE 'oother'  END as Estado" + \
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

        

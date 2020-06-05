# Operaciones resumen mundo datos

import dbg

c = dbg.cdbg()

class Paisgral:
    Pais = ''
    NomPais = ''
    NomDep = ''
    NomProv = ''
    NomSec = ''

    def get_paisgeneral(self):
        s = "select idPais as Pais, NomPais as NPais, NomDep as Departamento, NomProv as Provincia, "  + \
	    "NomSec as Seccion " + \
	    " from GeoAsientos_exterior order by idPais"
        c.sql(s)
        rows = c.cur.fetchall()
        if c.cur.rowcount == 0:
            return False
        else:
            return rows

# Operaciones asientos

class Reportes:
    idloc = 0
    deploc = 0
    provloc = 0
    secloc = 0
    nomloc = ""

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


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




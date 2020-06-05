# Operaciones usuarios

import dbg

c = dbg.cdbg()

class Pais:
    IdPais = 0
    Pais = ''
    NomPais = ''
    Nacionalidad = ''
    Estado = 0
    CodigoInternacional = ''
    CodigoInternacionalISO3166 = 0

    def get_paises(self):
        s = "select * from PAIS order by IdPais"
        c.sql(s)
        rows = c.cur.fetchall()
        if c.cur.rowcount == 0:
            return False
        else:
            return rows
        '''
        if  rows == None:
            return False
        else:
            return rows
        '''
    
    def add_pais(self, IdPais, Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166):
        new_pais = IdPais, Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166
        s = "insert into PAIS (IdPais, Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166) values " + \
            " (%s,%s, %s, %s, %s, %s, %s) "
        c.sql2(s, new_pais)
        c.cnx.commit()
        #c.cnx.close()
        print("PAIS adicionado...")

    def get_pais_id(self, IdPais):
        s = "select * from PAIS where IdPais = %d"
        c.sql2(s, IdPais)
        row = c.cur.fetchone()
        if  row == None:
            return False
        else:
            self.Pais = row[1]
            self.NomPais = row[2]
            self.Nacionalidad = row[3]
            self.Estado = row[4]
            self.CodigoInternacional = row[5]
            self.CodigoInternacionalISO3166 = row[6]
            return True

    def upd_pais(self, IdPais, Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166):
        upd_pais = (Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166, IdPais)
        s = "update PAIS " + \
            " set Pais= %s, NomPais= %s, Nacionalidad= %s, Estado= %s, CodigoInternacional= %s,  CodigoInternacionalISO3166= %d " + \
            " where IdPais = %d"
        try:
            c.sql2(s, upd_pais)
            c.cnx.commit()
            print('Pais.. Actualizado')
        except:
            print("Error --UPD-- Pais...")
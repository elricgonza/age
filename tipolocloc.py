# Operaciones provincias

import dbg

c = dbg.cdbg()

class Tipocircunscripcion:
    Tipolocloc = 0
    NombreTipoLocLoc = ''

    def get_tipocircunscripcion(self):
        s = "select * from clTipoLocLoc order by Tipolocloc"
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
    
    def add_circunscripcion(self, DepCircun, Circun, NomCircun, TipoCircun):
        new_circunscripcion = DepCircun, Circun, NomCircun, TipoCircun
        s = "insert into Circun (DepCircun, Circun, NomCircun, TipoCircun) values " + \
            " (%s,%s, %s, %s) "
        c.sql2(s, new_circunscripcion)
        c.cnx.commit()
        #c.cnx.close()
        print("CIRCUN adicionado...")
    
    
    def get_provincia_id(self, DepProv, Prov):
        s = "select * from PROV where DepProv = %d and Prov = %s"
        c.sql2(s,(DepProv,Prov))
        row = c.cur.fetchone()
        if  row == None:
            return False
        else:
            self.NomProv = row[2]
            self.codprov = row[3]
            return True

    def upd_provincia(self, DepProv, Prov, NomProv, codprov):
        upd_departamento = (NomProv, codprov, DepProv, Prov)
        s = "update PROV " + \
            " set NomProv= %s, codprov= %s " + \
            " where DepProv = %d and Prov = %d"
        try:
            c.sql2(s, upd_departamento)
            c.cnx.commit()
            print('Provincia actualizada...')
        except:
            print("Error --UPD-- departamento...")

    def del_provincia(self, id1,id2):
        s = "delete from PROV where DepProv = %d and Prov = %d"
        try:
            c.sql2(s, (id1,id2))
            c.cnx.commit()
            print('Provincia eliminado')
        except:
             print("Error --DEL-- Provincia...")
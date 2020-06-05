# Operaciones provincias

import dbg

c = dbg.cdbg()

class Provincia:
    DepProv = 0
    Prov = 0
    NomProv = ''
    codprov = 0

    def get_provincias(self):
        s = "select * from PROV order by DepProv"
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
    
    def add_provincia(self, DepProv, Prov, NomProv, codprov):
        new_provincia = DepProv, Prov, NomProv, codprov
        s = "insert into PROV (DepProv, Prov, NomProv, codprov) values " + \
            " (%s,%s, %s, %s) "
        c.sql2(s, new_provincia)
        c.cnx.commit()
        #c.cnx.close()
        print("Provincia adicionado...")
    
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
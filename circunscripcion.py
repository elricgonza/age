# Operaciones provincias

import dbg

c = dbg.cdbg()

class Circunscripcion:
    DepCircun = 0
    Circun = 0
    NomCircun = ''
    TipoCircun = 0

    def get_circunscripcion(self):
        s = "select * from Circun order by DepCircun,Circun"
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
    

    def get_circunscripcion_id(self, DepCircun, Circun):
        s = "select * from Circun where DepCircun = %d and Circun = %s"
        c.sql2(s,(DepCircun, Circun))
        row = c.cur.fetchone()
        if  row == None:
            return False
        else:
            self.NomCircun = row[2]
            self.TipoCircun = row[3]
            return True

    def upd_circunscripcion(self, DepCircun, Circun, NomCircun, TipoCircun):
        upd_circun = (NomCircun, TipoCircun, DepCircun, Circun)
        s = "update Circun " + \
            " set NomCircun= %s, TipoCircun= %s " + \
            " where DepCircun = %d and Circun = %d"
        try:
            c.sql2(s, upd_circun)
            c.cnx.commit()
            print('Circunscripcion actualizada...')
        except:
            print("Error --UPD-- departamento...")

    def del_circunscripcion(self, id1,id2):
        s = "delete from Circun where DepCircun = %d and Circun = %d"
        try:
            c.sql2(s, (id1,id2))
            c.cnx.commit()
            print('Circunscripcion eliminada')
        except:
             print("Error --DEL-- Provincia...")
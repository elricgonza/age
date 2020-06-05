# Operaciones SECCIONES

import dbg

c = dbg.cdbg()

class Seccion:
    DepSec = 0
    ProvSec = 0
    Sec = 0
    NumConceSec = 0
    NomSec = ''
    CircunSec = 0
    CodProv = 0
    CodSecc = 0

    def get_seccion(self):
        s = "select * from SEC order by DepSec, ProvSec, Sec"
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
    
    def add_seccion(self, DepSec, ProvSec, Sec, NumConceSec, NomSec, CircunSec, CodProv, CodSecc):
        new_seccion = DepSec, ProvSec, Sec, NumConceSec, NomSec, CircunSec, CodProv, CodSecc
        s = "insert into SEC (DepSec, ProvSec, Sec, NumConceSec, NomSec, CircunSec, CodProv, CodSecc) values " + \
            " (%s,%s, %s, %s,%s,%s, %s, %s) "
        c.sql2(s, new_seccion)
        c.cnx.commit()
        #c.cnx.close()
        print("SECCION adicionado...")
    
    def get_seccion_id(self, DepSec, ProvSec, Sec):
        s = "select * from SEC where DepSec = %d and ProvSec = %d and Sec = %s"
        c.sql2(s,(DepSec, ProvSec, Sec))
        row = c.cur.fetchone()
        if  row == None:
            return False
        else:
            self.NumConceSec = row[3]
            self.NomSec = row[4]
            self.CircunSec = row[5]
            self.CodProv = row[6]
            self.CodSecc = row[7]
            return True

    def upd_seccion(self, DepSec, ProvSec, Sec, NumConceSec, NomSec, CircunSec, CodProv, CodSecc):
        upd_seccion = (NumConceSec,NomSec,CircunSec,CodProv,CodSecc, DepSec, ProvSec, Sec)
        s = "update SEC " + \
            " set NumConceSec= %s, NomSec= %s, CircunSec= %s, CodProv= %s, CodSecc= %s " + \
            " where DepSec = %d and ProvSec = %d and Sec = %d"
        try:
            c.sql2(s, upd_seccion)
            c.cnx.commit()
            print('Seccion actualizada...')
        except:
            print("Error --UPD-- SECCION...")


    def del_seccion(self, id1,id2,id3):
        s = "delete from SEC where DepSec = %d and ProvSec = %d and Sec = %d"
        try:
            c.sql2(s, (id1,id2,id3))
            c.cnx.commit()
            print('SECCION eliminado')
        except:
             print("Error --DEL-- seccion...")

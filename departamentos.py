# Operaciones usuarios

import dbg

c = dbg.cdbg()

class Departamentos:
    Dep = 0
    NomDep = ''
    Diputados = 0
    DiputadosUninominales = 0
    IdPais = 0

    def get_departamentos(self):
        s = "select * from DEP order by Dep"
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
    def get_departamentos_bol(self):
        s = "select * from DEP where Dep <='9' order by Dep"
        c.sql(s)
        rows = c.cur.fetchall()
        if c.cur.rowcount == 0:
            return False
        else:
            return rows
    
    def add_departamento(self, Dep, NomDep, Diputados, DiputadosUninominales, IdPais):
        new_departamento = Dep, NomDep, Diputados, DiputadosUninominales, IdPais
        s = "insert into DEP (Dep, NomDep, Diputados, DiputadosUninominales, IdPais) values " + \
            " (%s,%s, %s, %s, %s) "
        c.sql2(s, new_departamento)
        c.cnx.commit()
        #c.cnx.close()
        print("DEPARTAMENTO adicionado...")
    
    def get_departamento_id(self, Dep):
        s = "select * from DEP where Dep = %d"
        c.sql2(s, Dep)
        row = c.cur.fetchone()
        if  row == None:
            return False
        else:
            self.NomDep = row[1]
            self.Diputados = row[2]
            self.DiputadosUninominales = row[3]
            self.IdPais = row[4]
            return True

    def upd_departamento(self, Dep, NomDep, Diputados, DiputadosUninominales, IdPais):
        upd_departamento = (NomDep, Diputados, DiputadosUninominales, IdPais, Dep)
        s = "update DEP " + \
            " set NomDep= %s, Diputados= %s, DiputadosUninominales= %s,  IdPais= %d " + \
            " where Dep = %d"
        try:
            c.sql2(s, upd_departamento)
            c.cnx.commit()
            print('Departamento actualizado')
        except:
            print("Error --UPD-- departamento...")


    def del_departamento(self, id):
        s = "delete from DEP where Dep = %d"
        try:
            c.sql2(s, id)
            c.cnx.commit()
            print('Departamento eliminado')
        except:
             print("Error --DEL-- departamento...")

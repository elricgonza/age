#Operaciones Documentos

class Documentos:
    doc_id=0
    id=0
    doc=0
    dep=0
    cite=''
    ruta=''
    fechadoc=''
    obs=''
    fecharegistro=''
    usuario=''
    fechaingreso=''
    fa=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_documentos_all(self, usrdep):                        
        s = "select id, tipoDoc, nomDep, cite, ruta, fechaAct, usuario, fechaIngreso from [bdge].[dbo].[docDepartamento]"             
        if usrdep != 0 :
            s = s + " where Dep = %d order by nomDep, fechaIngreso desc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by nomDep, fechaIngreso desc"            
            print(s)
            self.cur.execute(s) 

        rows = self.cur.fetchall()
                
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def add_documento(self, doc, dep, cite, ruta, fechadoc, obs, fecharegistro, usuario, fechaingreso):
        new_documento = doc, dep, cite, ruta, fechadoc, obs, fecharegistro, usuario, fechaingreso
        s = "insert into doc (tipoDoc, dep, cite, ruta, fechaDoc, obs, FechaAct, usuario, fechaIngreso) values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_documento)
        self.cx.commit()
        print("adicionado...")


    def upd_documento(self, id, doc, dep, cite, ruta, fechadoc, obs, usuario, fa):        
        upd_documento = (doc, dep, cite, ruta, fechadoc, obs, usuario, fa, id)        
        #s = "update doc set tipoDoc = %s, dep = %s, cite = %s, fechaDoc = %s, obs = %s, usuario = %s, fechaIngreso = %s where id = %d"
        s = "update doc " + \
            " set tipoDoc = %d, dep = %d, cite = %s, ruta = %s, fechaDoc = %s, obs = %s, usuario = %s, fechaIngreso = %s" + \
            " where id = %d"
        try:
            self.cur.execute(s, upd_documento)
            self.cx.commit()
            print('Documento actualizado')
        except:
            print("Error --UPD-- Documento...")

    def get_documento_id(self, id):
        s = "select * from doc where id = %d"
        self.cur.execute(s, id)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.tipoDoc = row[1]
            self.dep = row[2]
            self.cite = row[3]
            self.ruta = row[4]
            self.fechaDoc = row[5]
            self.obs = row[6]
            self.fechaAct = row[7]
            self.usuario = row[8]
            self.fechaIngreso = row[9]            
            return True

    def get_documentos(self):
        s = "select id, tipoDoc, nomDep, cite, ruta, fechaDoc, fechaIngreso from [bdge].[dbo].[docDepartamento]"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def del_documento(self, id):
        s = "delete from doc where id = %d"
        try:
            self.cur.execute(s, id)
            self.cx.commit()
            print('Documento eliminado')
        except:
             print("Error --DEL-- documento...")

    def get_next_iddoc(self):
        self.cur.execute("select max(id) + 1 from doc")
        row = self.cur.fetchone()
        return row[0]

    def tipo_doc(self, tipo):
        s = "select tipoDoc from tipoDocumento where id = %s"
        self.cur.execute(s, tipo)
        row = self.cur.fetchone()
        return row[0]
#Operaciones Documentos

class Documentos_pdf:
    doc_id=0
    id=0    

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_documentopdf_id(self, id):
        s = "select ruta from doc where id = %d"
        self.cur.execute(s, id)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.ruta = row[0]                    
            return True

    def get_documentospdf(self):
        s = "select id, tipoDoc, nomDep, cite, ruta, fechaDoc from [bdge].[dbo].[docDepartamento]"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def upd_documentopdf_id(self, id, ruta):        
        upd_documentopdf = (ruta, id)
        s = "update doc " + \
            " set ruta= %s where id = %d"
        try:
            self.cur.execute(s, upd_documentopdf)
            self.cx.commit()
            print('Documentopdf actualizado')
            return True
        except:
            print("Error --UPD-- Documentopdf...")
            return False

    def get_documentospdf_all(self, usrdep):                        
        s = "select id, tipoDoc, nomDep, cite, ruta, fechaDoc from [bdge].[dbo].[docDepartamento]"             
        if usrdep != 0 :
            s = s + " where Dep = %d order by fechaDoc, tipoDoc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by fechaDoc, tipoDoc"            
            print(s)
            self.cur.execute(s) 

        rows = self.cur.fetchall()
                
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

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
    codigo=0
    usuario=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_documentos_all(self, usrdep):                        
        s = "select id, tipoDoc, nomDep, cite, ruta, fechaAct, usuario, fechaIngreso, asignado from [bdge].[dbo].[docDepartamento]"             
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
        new_documento = doc, dep, cite, ruta, fechadoc, obs.strip(), fecharegistro, usuario, fechaingreso
        s = "insert into doc (tipoDoc, dep, cite, ruta, fechaDoc, obs, FechaAct, usuario, fechaIngreso) values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s) "
        try:
            self.cur.execute(s, new_documento)
            self.cx.commit()
            print("adicionado...") 
        except:
            print("Error - No se Pudo Adicionar...")


    def upd_documento(self, id, doc, dep, cite, ruta, fechadoc, obs, usuario, fa):        
        upd_documento = (doc, dep, cite, ruta, fechadoc, obs.strip(), usuario, fa, id)        
        #s = "update doc set tipoDoc = %s, dep = %s, cite = %s, fechaDoc = %s, obs = %s, usuario = %s, fechaIngreso = %s where id = %d"
        s = "update doc " + \
            " set tipoDoc = %d, dep = %d, cite = %s, ruta = %s, fechaDoc = %s, obs = %s, usuario = %s, fechaAct = %s" + \
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

    def get_next_id_doc(self):
        self.cur.execute("select ident_current('doc')+1 as IdActual")
        row = self.cur.fetchone()
        return row[0]

    def tipo_doc(self, tipo):
        s = "select tipoDoc from tipoDocumento where id = %s"
        self.cur.execute(s, tipo)
        row = self.cur.fetchone()
        return row[0]

    def get_tipo_documentos_pdfA(self, usrdep):
        s = "select id, nomDep, convert(varchar, fechaDoc, 103) as fechaDoc, cite, dep, ruta from [bdge].[dbo].[docDepartamento]"             
        if usrdep != 0:
            s = s + " where dep = %d  order by fechaAct desc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by fechaAct desc"
            self.cur.execute(s) 
        rows = self.cur.fetchall()
        return rows

    def get_tipo_documentos_pdfRN(self, usrdep):
        s = "select id, nomDep, convert(varchar, fechaDoc, 103) as fechaDoc, cite, dep, ruta from [bdge].[dbo].[docDepartamento]"             
        s = s + " where dep = 0 order by fechaAct desc"
        self.cur.execute(s) 
        rows = self.cur.fetchall()
        return rows

    def get_tipo_documentos_pdfRNExt(self, usrdep):
        s = "select id, nomDep, convert(varchar, fechaDoc, 103) as fechaDoc, cite, dep, ruta from [bdge].[dbo].[docDepartamento]"             
        s = s + " where dep = 0 order by fechaAct desc"
        self.cur.execute(s) 
        rows = self.cur.fetchall()
        return rows
    
    def diff_old_new_doc(self, row_to_upd):
        '''
        Verif. si existe dif. en registro editado
        '''
        a = self.get_documento_id(row_to_upd[0])  #19 -> idloc

        vdif = False

        if self.tipoDoc != int(row_to_upd[1]):
            print('tipoDoc dif')
            vdif = True
        if self.dep != int(row_to_upd[2]):
            print('dep dif')
            vdif = True
        if self.cite != row_to_upd[3]:
            print('cite dif')
            vdif = True
        if (self.fechaDoc == None and row_to_upd[4] != None):
            print('fechaDoc - null')
            vdif = True
        if (self.obs.strip() != row_to_upd[5].strip()):
            print('obs dif')
            vdif = True
        if (self.usuario != row_to_upd[6]):
            print('usuario dif')
            vdif = True

        return vdif

    def upd_doc(self, idA, idRN, idAct, idRspNal, docActF):
        '''
        Actualiza campo -asignado- para prever eliminación
        '''
        upd_doc2 = (idAct, idRspNal, docActF)
        s2 = "select * from GeografiaElectoral_app.dbo.loc where doc_idA = %d or doc_idRN = %d or doc_idAF = %d"
        self.cur.execute(s2, upd_doc2)
        row = self.cur.fetchone()

        if row == None:
            upd_doc1 = (idAct, idRspNal, docActF) 
            s1 = "update doc " + \
                 " set asignado = 0 where id = %d or id= %d or id= %d"
            self.cur.execute(s1, upd_doc1)
            self.cx.commit()

        upd_doc = (idA, idRN, docActF) 
        s = "update doc " + \
            " set asignado = 1 where id = %d or id= %d or id= %d"
        try:
            self.cur.execute(s, upd_doc)
            self.cx.commit()
            print('Documento actualizado')
        except:
            print("Error --UPD-- Documento...")

    def upd_doc_r(self, idA, idAct, docActF):
        upd_doc2 = (idAct, docActF)
        s2 = "select * from GeografiaElectoral_app.dbo.reci where doc_idA = %d or doc_idAF = %d"
        self.cur.execute(s2, upd_doc2)
        row = self.cur.fetchone()

        if row == None:
            upd_doc1 = (idAct, docActF) 
            s1 = "update doc " + \
                 " set asignado = 0 where id = %d or id= %d"
            self.cur.execute(s1, upd_doc1)
            self.cx.commit()

        upd_doc = (idA, docActF) 
        s = "update doc " + \
            " set asignado = 1 where id = %d or id= %d"
        try:
            self.cur.execute(s, upd_doc)
            self.cx.commit()
            print('Documento actualizado')
        except:
            print("Error --UPD-- Documento...")

    def get_cite(self, cite):
        s = "select * from bdge.dbo.doc where cite = %d"
        self.cur.execute(s, cite)
        row = self.cur.fetchone()
        if  row == None:
            return True
        else:
            return False

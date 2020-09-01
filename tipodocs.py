#Operaciones Tipo Documentos

class Tipodocs:    
    id=0
    usrdep=0
    tipodoc=0
    decripcion=''
    codigo=0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_tipodocumentos(self, usrdep):
        if usrdep != 0:
            codigo = 1
        else:
            codigo = 0

        s = "select id, tipoDoc from tipoDocumento"             
        if codigo != 0:
            s = s + " where codigo = %d or codigo = 2 order by id"
            self.cur.execute(s, codigo)
        else:
            s = s + " order by id"            
            self.cur.execute(s) 
        rows = self.cur.fetchall()
                
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_tipodocumentos_all(self):
        s = "select id, tipoDoc from tipoDocumento"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
    
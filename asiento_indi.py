#Operaciones indicadores

class AsientoIndicador:
    indi_id=0
    categoria=""

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()
 
    def get_indiCombo1_id(self, id):
        s = "select * from cate where id = %d"
        self.cur.execute(s, id)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.categoria = row[1]
        return True

    def get_indiCombo1_all(self, usrdep):                        
        s = "select id, categoria from cate" 
        self.cur.execute(s) 
        rows = self.cur.fetchall()
                
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
 
    def get_indiCombo2_id(self, id):
        s1 = "select * from subcate where id = %d"
        self.cur.execute(s1, id)
        row2 = self.cur.fetchone()
        if  row2 == None:
            return False
        else:
            self.categoria = row2[1]
        return True

    def get_indiCombo2_all(self, usrdep):  # TODO:adicionar captura de identificador de primer combo                      
        s1 = "select id, subCategoria from subcate where cate_id = 1"             
        self.cur.execute(s1) 
        rows2 = self.cur.fetchall()
                
        if self.cur.rowcount == 0:
            return False
        else:
            return rows2

    
    
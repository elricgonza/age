# Operaciones - img - para asiento/recinto u otros

class Img:
    id = 0
    img = ''
    de = ''

    _nro_rows = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_imgs(self, de):
        s = "select * from img where de = %s"
        try:
            self.cur.execute(s, de)
            rows = self.cur.fetchall()
            if  rows == None:
                return False
            else:
                self._nro_rows = self.cur.rowcount
                return rows
        except Exception as e:
            print ('Error en método  -get_imgs- ')
            print (e)

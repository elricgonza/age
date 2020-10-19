# Operaciones - i - para asiento/recinto u otros

class Indcate:
    id = 0
    categoria = ''
    usuario = ''

    _nro_rows = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_cate(self, de):
        s = "select id, categoria from cate where usuario = %s"
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

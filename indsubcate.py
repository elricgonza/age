# Operaciones - indice  subcategorias - para asiento/recinto u otros

class Indsubcate:
    id = 0
    subcategoria = ''
    cate_id = 0

    _nro_rows = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()
    
    # OBTIENE  subcategorias POR cat_id
    def get_subcate(self, de):
        s = "select id, subcategoria, cate_id from subcate where cate_id = %d"
        try:
            self.cur.execute(s, de)
            rows = self.cur.fetchall()
            if  rows == None:
                return False
            else:
                self._nro_rows = self.cur.rowcount
                return rows
        except Exception as e:
            print ('Error en método  -get_subcat x cate_id- ')
            print (e)

    # OBTIENE TODAS las subcategorias
    def get_subcate_all(self, de):
        s = "select id, subcategoria, cate_id from subcate where usuario = %d"
        try:
            self.cur.execute(s, de)
            rows = self.cur.fetchall()
            if  rows == None:
                return False
            else:
                self._nro_rows = self.cur.rowcount
                return rows
        except Exception as e:
            print ('Error en método  -get_subcat-all ')
            print (e)

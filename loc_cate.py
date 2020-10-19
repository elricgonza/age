# Operaciones - categoria y subcategoria - asiento (loc)
#import dbg

class LocCate:
    loc_id = 0
    cate_id = 0
    subcate_id = 0
    obs = ''
    fechaAct = ''
    usuario = ''
    fechaIngreso = ''

    _nro_rows = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def add_loc_img(self, idLoc, imgId, ruta, fechaAct,  usuario):
        new_row =  idLoc, imgId, ruta, fechaAct,  usuario
        s = "insert into loc_img (idLoc, imgId, ruta, fechaAct,  usuario) values " + \
            " (%s, %s, %s, %s, %s) "
        try:
            self.cur.execute(s, new_row)
            self.cx.commit()
            print("adicionado en loc_img ...")

        except Exception as e:
            print ('Error adición en -loc_img-')
            print (e)


    def get_loc_cates(self, idLoc):
        s = "select * from loc_cate where loc_id = %d order by obs"
        try:
            self.cur.execute(s, idLoc)
            rows = self.cur.fetchall()
            self._nro_rows = self.cur.rowcount  # 0 not found
            return rows

        except Exception as e:
            print ('Error en método  -get_loc_imgs- ')
            print (e)

    def add_loc_cate(self, loc_id, cate_id, subcate_id, obs, fechaAct, usuario, fechaIngreso):
        new_locCate = loc_id, cate_id, subcate_id, obs, fechaAct, usuario, fechaIngreso
        s = "insert into loc_cate (loc_id, cate_id, subcate_id, obs, fechaAct, usuario, fechaIngreso) values " + \
            " (%s,%s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_locCate)
        self.cx.commit()
       
    # borra registros en base al 'loc_id'
    def del_loc_cate(self, id):
        s = "delete from loc_cate where loc_id = %d"
        try:
            self.cur.execute(s, id)
            self.cx.commit()
        except:
            print ('Error --del--  loc_cate')
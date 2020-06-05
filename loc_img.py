# Operaciones - imágenes - asiento (loc)

class LocImg:
    idLoc = 0
    imgId = 0
    ruta = ''
    fechaAct = ''
    usuario = ''

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


    def get_loc_imgs(self, idLoc):
        s = "select * from loc_img where idLoc = %d order by imgId"
        try:
            self.cur.execute(s, idLoc)
            rows = self.cur.fetchall()
            self._nro_rows = self.cur.rowcount  # 0 not found
            return rows

        except Exception as e:
            print ('Error en método  -get_loc_imgs- ')
            print (e)


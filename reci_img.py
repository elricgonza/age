# Operaciones - imágenes - recinto (reci)

class ReciImg:
    idLoc = 0
    imgId = 0
    reci = 0
    ruta = ''
    fechaAct = ''
    usuario = ''

    _nro_rows = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def add_reci_img(self, idLoc, imgId, reci, ruta, fechaAct,  usuario):
        self.del_reci_img(idLoc, imgId, reci)
        new_row =  idLoc, imgId, reci, ruta, fechaAct,  usuario
        s = "insert into [bdge].[dbo].[reci_img] (idLoc, imgId, reci, ruta, fechaAct,  usuario) values " + \
            " (%s, %s, %s, %s, %s, %s) "
        try:
            self.cur.execute(s, new_row)
            self.cx.commit()
            print("adicionado en reci_img ...")

        except Exception as e:
            print ('Error adición en -reci_img-')
            print (e)


    def exist_img_reci(self, idLoc, imgId, reci):
        s = "select * from reci_img where idLoc= %d and imgId= %d and reci= %d"
        parm = idLoc, imgId, reci
        try:
            self.cur.execute(s, parm)
            if not self.cur.fetchall():
                return False
            else:
                return True

        except Exception as e:
            print('Error en exist_img_reci...')
            print(e)


    def del_reci_img(self, idLoc, imgId, reci):
        if self.exist_img_reci(idLoc, imgId, reci):
            s = "delete from reci_img where idLoc= %d and imgId= %d and reci= %d"
            parm = idLoc, imgId, reci
            try:
                self.cur.execute(s, parm)

            except Exception as e:
                print('Error en del_reci_img...')
                print(e)


    def get_reci_imgs(self, idLoc):
        s = "select * from reci_img where idLoc = %d order by imgId"
        try:
            self.cur.execute(s, idLoc)
            rows = self.cur.fetchall()
            self._nro_rows = self.cur.rowcount  # 0 not found
            return rows

        except Exception as e:
            print ('Error en método  -get_reci_imgs- ')
            print (e)


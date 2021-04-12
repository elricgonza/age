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


    def exist_img(self, idLoc, imgId):
        s = "select * from loc_img where idLoc= %d and imgId= %d"
        parm = idLoc, imgId
        try:
            self.cur.execute(s, parm)
            if not self.cur.fetchall():
                return False
            else:
                return True

        except Exception as e:
            print('Error en exist_img...')
            print(e)


    def del_loc_img(self, idLoc, imgId):
        if self.exist_img(idLoc, imgId):
            s = "delete from loc_img where idloc= %d and imgId= %d"
            parm = idLoc, imgId
            try:
                self.cur.execute(s, parm)

            except Exception as e:
                print('Error en del_loc_img...')
                print(e)


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


    def get_name_file_img(self, idLoc, imgId):
        ''' get name file incluído el path '''

        s = "select ruta from loc_img where idLoc = %d and imgId = %d "
        parm = idLoc, imgId
        try:
            self.cur.execute(s, parm)
            rows = self.cur.fetchall()
            if rows: # encontrado
                self._nro_rows = self.cur.rowcount
                return rows[0][0]   # de tupla 1er elem.
            else:
                self._nro_rows = 0
                return ''

        except Exception as e:
            print ('Error en método  -get_name_file_img- ')
            print (e)

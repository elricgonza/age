# Operaciones - img - para asiento/recinto u otros

class ClasifGet:
    idClasif = 0
    descripcion = ''
    clasifGrupoId = ''


    _nro_rows = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_descripcion(self, clasifGrupoId):
        s = "select * from GeografiaElectoral_app.dbo.clasif where clasifGrupoId =%s"
        try:
            self.cur.execute(s, clasifGrupoId)
            rows = self.cur.fetchall()
            if  rows == None:
                return False
            else:
                self._nro_rows = self.cur.rowcount
                return rows
        except Exception as e:
            print ('Error en método  -get_descripcion- ')
            print (e)

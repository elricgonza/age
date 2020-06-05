# Operaciones asientos

class LatLong:
    dep= 0
    departamento= ''
    prov= 0
    provincia= ''
    sec= 0
    municipio= ''
    nrocircun= 0
    circunscripcion= ''


    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_geo(self, lat, long):
        s = "select * from f_get_geo(%s, %s)"
        coord = lat, long
        self.cur.execute(s, coord)
        row = self.cur.fetchone()
        if row == None:
            return False
        else:
            self.dep = row[0]
            self.departamento = row[1]
            self.prov = row[2]
            self.provincia = row[3]
            self.sec = row[4]
            self.municipio = row[5]
            self.nrocircun = row[6]
            self.circunscripcion = row[7]
            return True

# sql - espacial -

class LatLong:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_geo(self, lat, long):
        s = "select * from f_get_geo(%s, %s)"
        coord = lat, long
        try:
            self.cur.execute(s, coord)
            row = self.cur.fetchone()
            if row:
                self.dep = row[0]
                self.departamento = row[1]
                self.prov = row[2]
                self.provincia = row[3]
                self.sec = row[4]
                self.municipio = row[5]
                self.nrocircun = row[6]
                self.circunscripcion = row[7]
                self.cod_dist = row[8]
                self.distrito = row[9]
                self.cod_zona = row[10]
                self.zona = row[11]
            return row
        except Exception as e:
            print(e)
            print('Error - get_geo: ')

# sql - espacial

class LatLongGS:

    def __init__(self, cx):
        self.cx2 = cx
        self.cur2 = cx.cursor()


    def get_dist_zona(self, lat, long):
        s = "select * from f_get_dist_zona(%s, %s)"
        coord = lat, long
        try:
            self.cur2.execute(s, coord)
            row = self.cur2.fetchone()
            if row:
                self.cod_dist = row[0]
                self.distrito = row[1]
                self.cod_zona = row[2]
                self.zona = row[3]
            return row
        except Exception as e:
            print('=========================================')
            print(e)
            print("Error - get_dist_zona...")

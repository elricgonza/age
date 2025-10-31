# Operaciones Circun

class Circun:
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_circun(self, dep):
        ''' Obtiene circunscripcionesi por dep, nal = 0 '''

        s = '''
        SELECT idCircun, nomCircun
        FROM [GeografiaElectoral_app].[dbo].[Circun]
        '''
        if dep != 0:
            s += " WHERE depCircun = %s "

        s += " ORDER BY idCircun "

        try:
            self.cur.execute(s, dep)
            rows = self.cur.fetchall()
            return rows
        except Exception as e:
            print("Error fetching circun data:", e)
            return []

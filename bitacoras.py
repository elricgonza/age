# Operaciones usuarios

class Bitacora:
    TipoTrn = ''
    Tabla = ''
    PK = ''
    Campo = ''
    ValorOriginal = ''
    ValorNuevo = ''
    FechaTrn = ''
    Usuario = ''
    AppName = ''
    HostName = ''
    Client_IP = ''




    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()
    
    def get_bitacora_all(self, usrdep):
            s = "SELECT TipoTrn, Tabla, PK, Campo, ValorOriginal, ValorNuevo, FechaTrn, Usuario, AppName, HostName, Client_IP " + \
                " FROM [bdge].[dbo].[logTransacciones] order by FechaTrn desc"
            self.cur.execute(s)
            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_pais_idbitacora(self, PK):
        s = "select TipoTrn, Tabla, PK, Campo, ValorOriginal, ValorNuevo, FechaTrn, Usuario, AppName, HostName, Client_IP " + \
            " FROM [bdge].[dbo].[logTransacciones] where PK = %d order by FechaTrn desc "
        self.cur.execute(s, PK)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.TipoTrn = row[0]
            self.Tabla = row[1]
            self.PK = row[2]
            self.Campo = row[3]
            self.ValorOriginal = row[4]
            self.ValorNuevo = row[5]
            self.FechaTrn = row[6]
            self.Usuario = row[7]
            self.AppName = row[8]
            self.HostName = row[9]
            self.Client_IP = row[10]
            
            
            return True
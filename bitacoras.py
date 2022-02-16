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
    
    def get_bitacora_all(self, inicio, final, usuario): 
        if inicio == "00-00-0000" and final == "00-00-0000":
            if usuario == 0:
                return False
            else:
                lista = usuario
                s = "select t.TipoTrn, t.Tabla, t.PK, t.Campo, t.ValorOriginal, t.ValorNuevo, t.FechaTrn, t.Usuario, t.AppName, t.HostName," + \
                    " t.Client_IP from bdge.dbo.logTransacciones t" + \
                    " left join bdge.dbo.usuarios u on t.Usuario=u.usuario" + \
                    " where u.id = %d order by t.FechaTrn desc"
        else:
            if usuario == 0:
                lista = inicio, final
                s = "select t.TipoTrn, t.Tabla, t.PK, t.Campo, t.ValorOriginal, t.ValorNuevo, t.FechaTrn, t.Usuario, t.AppName, t.HostName," + \
                    " t.Client_IP from bdge.dbo.logTransacciones t" + \
                    " left join bdge.dbo.usuarios u on t.Usuario=u.usuario" + \
                    " where Convert(char(10), t.FechaTrn,23) between %d and %d order by t.FechaTrn desc"
            else:
                lista = inicio, final, usuario
                s = "select t.TipoTrn, t.Tabla, t.PK, t.Campo, t.ValorOriginal, t.ValorNuevo, t.FechaTrn, t.Usuario, t.AppName, t.HostName," + \
                    " t.Client_IP from bdge.dbo.logTransacciones t" + \
                    " left join bdge.dbo.usuarios u on t.Usuario=u.usuario" + \
                    " where Convert(char(10), t.FechaTrn,23) between %d and %d and u.id = %d order by t.FechaTrn desc"

        self.cur.execute(s, lista)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_bitacora_1000(self, usrdep):        
        s = "select top 1000 t.TipoTrn, t.Tabla, t.PK, t.Campo, t.ValorOriginal, t.ValorNuevo, t.FechaTrn, t.Usuario, t.AppName, t.HostName," + \
            " t.Client_IP from bdge.dbo.logTransacciones t" + \
            " left join bdge.dbo.usuarios u on t.Usuario=u.usuario"
        if usrdep != 0 :
            s = s + " where u.dep = %d order by t.FechaTrn desc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by t.FechaTrn desc"
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

    def get_departamentos(self):
        s = "select Dep, nomDep from [GeografiaElectoral_app].[dbo].[DEP] where Dep<=9 order by Dep"
        self.cur.execute(s) 
        rows = self.cur.fetchall()
                
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_usuarios(self):
        s = "select id, usuario from [bdge].[dbo].[usuarios] order by id"
        self.cur.execute(s) 
        rows = self.cur.fetchall()
                
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

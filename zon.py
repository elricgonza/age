# Operaciones Zonas/Recintos

class Zon:
    idloczona = 0
    zona = 0
    nomzona = ''
    distzona = 0
    fechaingreso = ''
    fechaact = ''
    usuario = ''

    _nomloc = ''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_zon_allOLD(self, usrdep):        
        s = "select distinct l.IdLoc, l.NomLoc, z.NomZona, d.Dist, d.NomDist, d.CircunDist, z.Zona from [GeografiaElectoral_app].[dbo].[RECI] r" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on r.IdLocReci=l.IdLoc" + \
            " left join [GeografiaElectoral_app].[dbo].[ZONA] z on r.IdLocReci= z.IdLocZona and r.ZonaReci = z.Zona" + \
            " left join [GeografiaElectoral_app].[dbo].[DIST] d on r.IdLocReci= d.IdLocDist and z.DistZona = d.Dist"
        if usrdep != 0 :
            s = s + " where r.estado in (1, 2, 3, 6, 79, 80, 81, 84) and l.DepLoc = %d order by l.IdLoc, l.NomLoc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where r.estado in (1, 2, 3, 6, 79, 80, 81, 84) order by l.IdLoc, l.NomLoc"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_zon_all(self, usrdep):        
        ''' Obtiene todas las zonas asociadas a un asiento '''

        s = "select l.IdLoc, l.NomLoc, z.NomZona, d.Dist, d.NomDist, d.CircunDist, z.Zona " + \
            " from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on z.Idloczona = l.IdLoc" + \
            " left join [GeografiaElectoral_app].[dbo].[DIST] d on d.IdLocDist = z.IdLocZona and d.Dist = z.distZona "
        if usrdep != 0 :
            s = s + " where isnull(l.IdLoc,0) <> 0 and l.DepLoc = %d order by l.IdLoc, l.NomLoc"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where isnull(l.IdLoc,0) <> 0 order by l.IdLoc, l.NomLoc"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        return rows


    def get_zon_idloc(self, idloczona, idzon):
        ''' suprimirrr  '''
        up_zonadist = idloczona, idzon
        s = "select distinct l.IdLoc, l.NomLoc, z.Zona, z.NomZona, z.DistZona, z.fechaIngreso, z.fechaAct, z.usuario, d.CircunDist" + \
            " from [GeografiaElectoral_app].[dbo].[RECI] r" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on r.IdLocReci=l.IdLoc" + \
            " left join [GeografiaElectoral_app].[dbo].[ZONA] z on r.IdLocReci= z.IdLocZona and r.ZonaReci = z.Zona" + \
            " left join [GeografiaElectoral_app].[dbo].[DIST] d on r.IdLocReci= d.IdLocDist and z.DistZona = d.Dist" + \
            " where z.IdLocZona= %d and z.Zona= %d"
        self.cur.execute(s, up_zonadist)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.nomloc = row[1]
            self.idzon = row[2]
            self.nomzona = row[3]
            self.distzona = row[4]
            self.fechaIngreso = row[5]
            self.fechaAct = row[6]
            self.usuario = row[7]
            self.circundist = row[8]
            return True


    def get_zona(self, idloc, zona):
        ''' obtiene zona '''
        t = idloc, zona
        s = "select  z.*, l.nomloc " + \
            " from [GeografiaElectoral_app].[dbo].[ZONA] z " + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on z.Idloczona = l.IdLoc " + \
            " left join [GeografiaElectoral_app].[dbo].[DIST] d on d.IdLocDist = z.IdLocZona and d.Dist = z.distZona " + \
            " where z.IdLocZona = %d and z.Zona = %d"
        self.cur.execute(s, t)
        row = self.cur.fetchone()
        if row:
            self.idloczona = row[0]
            self.zona = row[1]
            self.nomzona = row[2]
            self.distzona = row[3]
            self.fechaingreso = row[4]
            self.fechaact = row[5]
            self.usuario = row[6]
            self._nomloc = row[7]
        return row


    def get_next_zon(self, idloc):
        s = "select isnull(max(zona), 0)+1 from GeografiaElectoral_app.dbo.zona where IdLocZona = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]
    

    def add_zon(self, idloczona, zona, nomzona, distzona, fecharegistro, usuario, fechaingreso):
        new_zona = idloczona, zona, nomzona.upper(), distzona, fecharegistro, usuario, fechaingreso
        s = "insert into GeografiaElectoral_app.dbo.zona (IdLocZona, Zona, NomZona, DistZona, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_zona)
        self.cx.commit()
        print("adicionado...")


    def upd_zon(self, idloczona, zona, nomzona, distzona, fechaact, usuario):      
        t = nomzona.upper(), distzona, fechaact, usuario, idloczona, zona   
        s = "update GeografiaElectoral_app.dbo.zona " + \
            " set NomZona = %s, DistZona = %s, fechaAct = %s, usuario = %s" + \
            " where IdLocZona = %d and Zona = %d"
        try:
            self.cur.execute(s, t)
            self.cx.commit()
            print('Zona actualizada')
        except Exception as e:
            print("Error --UPD-- Zona...")
            print(e)


    def get_circundist(self, idloc, idzon):        
        s = "select CircunDist, NombreRecinto from [bdge].[dbo].[GeoRecintos_all] where idEstado in (1, 2, 3, 6, 79, 80, 81, 84) and IdLoc = %d" + \
            " and Zona = %d order by Dist"
        consulta = idloc, idzon
        self.cur.execute(s, consulta)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows


    def get_next_zona(self, idloc):
        s = "select isnull(max(zona), 0)+1 from GeografiaElectoral_app.dbo.zona where IdLocZona = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]


    def nomzona_existe(self, idloc, nomzona):
        ''' Valida q no se duplique nomZona en asiento  '''

        s = "select NomZona from [GeografiaElectoral_app].[dbo].[ZONA]" + \
            "where IdLocZona= %d and nomzona= %s "
        t = idloc, nomzona
        self.cur.execute(s, t)
        row = self.cur.fetchall()
        return row


    def add_zona(self, idloczona, zona, nomzona, distzona, fechaingreso, fechaact, usuario):
        new_zona = idloczona, zona, nomzona, distzona, fechaingreso, fechaact, usuario
        s = "insert into GeografiaElectoral_app.dbo.zona (IdLocZona, Zona, NomZona, DistZona, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_zona)
        self.cx.commit()
        print("adicionado...")


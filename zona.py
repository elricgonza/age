# Operaciones Zonas/Recintos

class Zona:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_zon_all(self, usrdep):
        ''' Obtiene todas las zonas asociadas a un asiento '''

        s = "select l.IdLoc, l.NomLoc, z.NomZona, d.Dist, d.NomDist, z.zonaGeo, z.Zona " + \
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
            self.zonageo = row[7]
            self._nomloc = row[8]
        return row


    def get_zonas_idloc(self, idloc):
        ''' Retorna zonas en idLoc '''

        s = "select l.IdLoc, z.Zona, z.NomZona, d.dist, d.NomDist, l.nomloc" + \
            " from [GeografiaElectoral_app].[dbo].[ZONA] z" + \
            " inner join [GeografiaElectoral_app].[dbo].[DIST] d on z.DistZona=d.Dist and z.IdLocZona=d.IdLocDist" + \
            " inner join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=z.IdLocZona and l.IdLoc=d.IdLocDist "
        s = s + " where l.Idloc = %d order by z.NomZona"

        try:
            self.cur.execute(s, idloc)
        except Exception as e:
            print(e)

        rows = self.cur.fetchall()
        return rows


    def get_next_zon(self, idloc):
        s = "select isnull(max(zona), 0)+1 from GeografiaElectoral_app.dbo.zona where IdLocZona = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]


    def add_zon(self, idloczona, zona, nomzona, distzona, fechaingreso, fechaAct, usuario, zonageo):
        new_zona = idloczona, zona, nomzona.strip(), distzona, fechaingreso, fechaact, usuario.strip(), zonageo
        s = "insert into GeografiaElectoral_app.dbo.zona (IdLocZona, Zona, NomZona, DistZona, fechaIngreso, fechaAct, usuario, zonageo)" + \
            " values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s) "
        try:
            self.cur.execute(s, new_zona)
            self.cx.commit()
            print("adicionado...")
        except Exception as e:
            print("Error --ADD ZONA--")
            print(e)


    def upd_zon(self, idloczona, zona, nomzona, distzona, fechaact, usuario, zonageo):
        t = nomzona.strip(), distzona, fechaact, usuario.strip(), zonageo, idloczona, zona
        s = "update GeografiaElectoral_app.dbo.zona " + \
            " set NomZona = %s, DistZona = %s, fechaAct = %s, usuario = %s, zonageo = %s " + \
            " where IdLocZona = %d and Zona = %d"
        try:
            self.cur.execute(s, t)
            self.cx.commit()
            print('Zona actualizada...')
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


    def nomzona_existe_edit(self, idloc, zona, nomzona):
        ''' Valida q no se duplique nomZona en asiento por EDIT  '''

        s = "select NomZona from [GeografiaElectoral_app].[dbo].[ZONA]" + \
            "where IdLocZona= %d and nomzona= %s and zona <> %d"
        t = idloc, nomzona, zona
        try:
            self.cur.execute(s, t)
            row = self.cur.fetchall()
            return row
        except Exception as e:
            print('Error valid nomzona_existe edit')
            print(e)


    def add_zona(self, idloczona, zona, nomzona, distzona, fechaingreso, fechaact, usuario, zonaGeo):
        new_zona = idloczona, zona, nomzona.strip(), distzona, fechaingreso, fechaact, usuario.strip(), zonaGeo
        s = "insert into GeografiaElectoral_app.dbo.zona (IdLocZona, Zona, NomZona, DistZona, fechaIngreso, fechaAct, usuario, zonaGeo)" + \
            " values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_zona)
            self.cx.commit()
            print("zona add ok...")
        except Exception as e:
            print("Error zona add")
            print(e)


    def elimina_zona(self, idloc, zona):
        ''' Elimina zona '''
        s = f"delete from GeografiaElectoral_app.dbo.zona where idLocZona= {idloc} and zona= {zona}"
        try:
            self.cur.execute(s)
            self.cx.commit()
        except Exception as e:
            print("Error eliminación zona")
            print(e)

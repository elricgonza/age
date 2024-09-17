# Operaciones Zonas / Distritos / Recintos

class Distritos:
    idlocreci=0
    reci=0
    nomreci=''
    idloc=0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_dist_enable(self, usrdep): 
        ''' Obtiene distritos de recintos habilitados sg ESTADO en reci '''

        s = "select distinct d.IdLocDist, l.NomLoc, d.Dist, d.CircunDist, d.NomDist from [GeografiaElectoral_app].[dbo].[RECI] r" + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on r.IdLocReci=l.IdLoc" + \
            " left join [GeografiaElectoral_app].[dbo].[ZONA] z on r.IdLocReci= z.IdLocZona and r.ZonaReci = z.Zona" + \
            " left join [GeografiaElectoral_app].[dbo].[DIST] d on r.IdLocReci= d.IdLocDist and z.DistZona = d.Dist"
        if usrdep != 0 :
            s = s + " where r.estado in (1, 2, 3, 6, 79, 80, 81, 84) and l.DepLoc = %d order by d.IdLocDist, d.Dist"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where r.estado in (1, 2, 3, 6, 79, 80, 81, 84) order by d.IdLocDist, d.Dist"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        return rows


    def get_dist_all(self, usrdep): 
        ''' Obtiene todos los distritos en la bd habilitados/inhabilitados '''

        s = "select d.IdLocDist, l.NomLoc, d.Dist, d.CircunDist, d.NomDist " + \
            " from [GeografiaElectoral_app].[dbo].[DIST] d " + \
            " left join [GeografiaElectoral_app].[dbo].[LOC] l on d.IdLocDist=l.IdLoc " 
        if usrdep != 0 :
            s = s + " where  l.DepLoc = %d order by d.IdLocDist, d.Dist"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by d.IdLocDist, d.Dist"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        return rows


    def get_next_dist(self, idloc):
        s = "select isnull(max(dist), 0)+1 from GeografiaElectoral_app.dbo.dist where IdLocDist = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        return row[0]


    def add_dist(self, idlocdist, dist, circundist, nomdist, fecharegistro, usuario, fechaingreso):
        new_dist = idlocdist, dist, circundist, nomdist.upper(), fecharegistro, usuario, fechaingreso
        s = "insert into GeografiaElectoral_app.dbo.dist (IdLocDist, Dist, CircunDist, NomDist, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s) "
        try:
            self.cur.execute(s, new_dist)
            self.cx.commit()
            print("dist add ok")
        except Exception as e:
            print('Error --ADD-- Distrito')
            print(e)
    

    def upd_zona(self, idloczona, idzona, nomzona, fa, usuario):        
        upd_zona = (idloczona, nomzona, fa, usuario, idzona)   
        s = "update GeografiaElectoral_app.dbo.zona " + \
            " set IdLocZona = %d, NomZona = %s, fechaAct = %s, usuario = %s" + \
            " where Zona = %d"
        try:
            self.cur.execute(s, upd_zona)
            self.cx.commit()
            print('Zona actualizada')
        except:
            print("Error --UPD-- Zona...")


    def upd_dist(self, idlocdist, iddist, circundist, nomdist, fa, usuario):        
        upd_dist = circundist, nomdist.upper(), fa, usuario, idlocdist, iddist 
        s = "update GeografiaElectoral_app.dbo.dist set CircunDist = %s, NomDist = %s, fechaAct = %s, usuario = %s" + \
            " where IdLocDist = %d and Dist = %d"
        try:
            self.cur.execute(s, upd_dist)
            self.cx.commit()
            print('Distrito actualizado')
        except Exception as e:
            print("Error --UPD-- Distrito...")
            print(e)


    def get_zonadist_idloc(self, idloc, iddist):
        up_zonadist = idloc, iddist
        s = "select l.IdLoc, l.NomLoc, d.Dist, d.CircunDist, d.NomDist, d.fechaIngreso, d.fechaAct, d.usuario " + \
            "from [GeografiaElectoral_app].[dbo].[DIST] d " + \
            "inner join [GeografiaElectoral_app].[dbo].[LOC] l on l.IdLoc=d.IdLocDist " + \
            "where d.IdLocDist= %d and d.Dist= %d"
        self.cur.execute(s, up_zonadist)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.nomloc = row[1]
            self.dist = row[2]
            self.circundist = row[3]
            self.nomdist = row[4]
            self.fechaingreso = row[5]
            self.fechaact = row[6]
            self.usuario = row[7]
            return True


    def asientoz(self, azona):
        s = "select IdLoc, NomLoc from [GeografiaElectoral_app].[dbo].[LOC]" + \
            "where IdLoc= %d"
        self.cur.execute(s, azona)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idloc = row[0]
            self.nomloc = row[1]
            return True


    def get_nomdist(self, idloc, nomdist):
        con = idloc, nomdist
        s = "select NomDist from [GeografiaElectoral_app].[dbo].[DIST]" + \
            "where IdLocDist= %d and Dist= %d"
        self.cur.execute(s, con)
        row = self.cur.fetchone()
        return row[0]


    def get_ultimodist(self, nomdist, idloc):
        con1 = nomdist, idloc
        s = "select max(dist) from GeografiaElectoral_app.dbo.dist where Dist = %d and IdLocDist = %d"
        self.cur.execute(s, con1)
        row = self.cur.fetchone()
        return row[0]


    def nomdist_existe(self, idloc, nomdist):
        ''' Valida q no se duplique nomDist en asiento  '''

        s = "select NomDist from [GeografiaElectoral_app].[dbo].[DIST]" + \
            "where IdLocDist= %d and nomDist= %s "
        t = idloc, nomdist
        try:
            self.cur.execute(s, t)
            row = self.cur.fetchall()
            return row
        except Exception as e:
            print("Error valid nomdist_existe")
            print(e)


    def nomdist_existe_edit(self, idloc, dist, nomdist):
        ''' Valida q no se duplique nomDist en asiento y que no sea el editado  '''

        s = "select NomDist from [GeografiaElectoral_app].[dbo].[DIST]" + \
            "where IdLocDist= %d and nomDist= %s  and dist <> %d "
        t = idloc, nomdist, dist
        try:
            self.cur.execute(s, t)
            row = self.cur.fetchall()
            return row
        except Exception as e:
            print("Error valid nomdist_existe")
            print(e)


    def get_dists_en_idloc(self, idloc):        
        s = "select IdLocDist, Dist, CircunDist, NomDist from [GeografiaElectoral_app].[dbo].[DIST] where IdLocDist = %d order by Dist"
        self.cur.execute(s, idloc)
        rows = self.cur.fetchall()
        return rows


    def elimina_dist(self, idloc, dist):
        ''' Elimina distrito '''
        s = f"delete from GeografiaElectoral_app.dbo.dist where idLocDist= {idloc} and dist= {dist}"
        try:
            self.cur.execute(s)
            self.cx.commit()
        except Exception as e:
            print("Error eliminación dist")
            print(e)


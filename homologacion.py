# Operaciones asientos

class Homologacion:
    idlocreci=0
    reci=0
    nomreci=''
    estado=0
    fechaAct=''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_homologacion_all(self, usrdep, inicio, final):
        if inicio == "00-00-0000" and final == "00-00-0000":
            return False
        else:           
            s = "Select id, idLoc, reci, nomDep as Departamento, nomLoc, nomReci," + \
                " idloc2, reci2, nomReci2" + \
                " from [bdge].[dbo].[hom]"
            if usrdep != 0 :
                lista = usrdep, inicio, final
                s = s + " where dep = %d and Convert(CHAR(10),fechaAct,23) between %d and %d order by prov, sec"
                self.cur.execute(s, lista)
            else:
                lista = inicio, final
                s = s + " where Convert(CHAR(10),fechaAct,23) between %d and %d order by Dep, Prov, Sec"
                self.cur.execute(s, lista)

            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_homojurisd_all(self, usrdep, inicio, final):
        if inicio == "00-00-0000" and final == "00-00-0000":
            return False
        else:           
            s = "Select id, idLoc, reci, nomDep as Departamento, nomLoc, nomReci," + \
                " idloc2, reci2, nomReci2" + \
                " from [bdge].[dbo].[actJurisd]"
            if usrdep != 0 :
                lista = usrdep, inicio, final
                s = s + " where dep = %d and idLoc <> idloc2 and origen = 'R' and Convert(CHAR(10),fechaAct,23) between %d and %d order by prov, sec"
                self.cur.execute(s, lista)
            else:
                lista = inicio, final
                s = s + " where idLoc <> idloc2 and origen = 'R' and Convert(CHAR(10),fechaAct,23) between %d and %d order by Dep, Prov, Sec"
                self.cur.execute(s, lista)

            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_homologacion_idhom(self, idhom):
        s = "Select dep, prov, sec, idLoc, dist, zona, reci, nomDep, nomProv, nomSec, nomLoc, nomDist, nomZona, nomReci," + \
            " direccion, circun, idTipoCircun, tipoCircun, idTipoRecinto, tipoRecinto, latitud, longitud, doc, doc1, idLoc2," + \
            " reci2, nomDep2, nomProv2, nomSec2, nomLoc2, nomDist2, nomZona2, nomReci2, direccion2, circun2, tipoCircun2," + \
            " tipoRecinto2, latitud2, longitud2, id" + \
            " from [bdge].[dbo].[hom]" + \
            " where id = %d"    
        self.cur.execute(s, idhom)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dep = row[0]
            self.prov = row[1]
            self.sec = row[2]
            self.idloc = row[3]
            self.dist = row[4]
            self.zona = row[5]
            self.reci = row[6]
            self.departamento = row[7]
            self.provincia = row[8]
            self.municipio = row[9]
            self.asiento = row[10]
            self.nomdist = row[11]
            self.nomzona = row[12]
            self.recinto = row[13]
            self.direccion = row[14]
            self.circun = row[15]
            self.idtipocircun = row[16]
            self.tipocircun = row[17]
            self.idtiporecinto = row[18]
            self.tiporecinto = row[19]
            self.latitud = row[20]
            self.longitud = row[21]
            self.doc = row[22]
            self.doc1 = row[23]
            self.idloc2 = row[24]
            self.reci2 = row[25]
            self.departamento2 = row[26]
            self.provincia2 = row[27]
            self.municipio2 = row[28]
            self.asiento2 = row[29]
            self.nomdist2 = row[30]
            self.nomzona2 = row[31]
            self.recinto2 = row[32]
            self.direccion2 = row[33]
            self.circun2 = row[34]
            self.tipocircun2 = row[35]
            self.tiporecinto2 = row[36]
            self.latitud2 = row[37]
            self.longitud2 = row[38]
            self.idhom = row[39]
            return True

    def get_homojurisd_idhom(self, idhom):
        s = "Select dep, prov, sec, idLoc, dist, zona, reci, nomDep, nomProv, nomSec, nomLoc, nomDist, nomZona, nomReci," + \
            " direccion, circun, idTipoCircun, tipoCircun, idTipoRecinto, tipoRecinto, latitud, longitud, doc, doc1, idLoc2," + \
            " reci2, nomDep2, nomProv2, nomSec2, nomLoc2, nomDist2, nomZona2, nomReci2, direccion2, circun2, tipoCircun2," + \
            " tipoRecinto2, latitud2, longitud2, id" + \
            " from [bdge].[dbo].[actJurisd]" + \
            " where id = %d"    
        self.cur.execute(s, idhom)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.dep = row[0]
            self.prov = row[1]
            self.sec = row[2]
            self.idloc = row[3]
            self.dist = row[4]
            self.zona = row[5]
            self.reci = row[6]
            self.departamento = row[7]
            self.provincia = row[8]
            self.municipio = row[9]
            self.asiento = row[10]
            self.nomdist = row[11]
            self.nomzona = row[12]
            self.recinto = row[13]
            self.direccion = row[14]
            self.circun = row[15]
            self.idtipocircun = row[16]
            self.tipocircun = row[17]
            self.idtiporecinto = row[18]
            self.tiporecinto = row[19]
            self.latitud = row[20]
            self.longitud = row[21]
            self.doc = row[22]
            self.doc1 = row[23]
            self.idloc2 = row[24]
            self.reci2 = row[25]
            self.departamento2 = row[26]
            self.provincia2 = row[27]
            self.municipio2 = row[28]
            self.asiento2 = row[29]
            self.nomdist2 = row[30]
            self.nomzona2 = row[31]
            self.recinto2 = row[32]
            self.direccion2 = row[33]
            self.circun2 = row[34]
            self.tipocircun2 = row[35]
            self.tiporecinto2 = row[36]
            self.latitud2 = row[37]
            self.longitud2 = row[38]
            self.idhom = row[39]
            return True

    def get_hom_all(self, idhom):
        s = "select h.id, h.idLoc, h.reci, h.nomDep, h.nomLoc, h.nomReci, h.latitud, h.longitud, h.idLoc2, h.reci2, h.nomDep2, h.nomLoc2, h.nomReci2," + \
            " h.latitud2, h.longitud2" + \
            " from [bdge].[dbo].[hom] h inner join [GeografiaElectoral_app].[dbo].[RECI] r on h.idLoc=r.IdLocReci and (h.reci=r.Reci or h.reci2=r.Reci)" + \
            " where h.id = %d"
        self.cur.execute(s, idhom)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
    
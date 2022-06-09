# Operaciones asientos

class Reportes:
    idloc = 0
    deploc = 0
    provloc = 0
    secloc = 0
    nomloc = ""

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_rep_asientos_all(self, usrdep):        
        s = "select IdLoc, DEP, NomDep as Departamento, PROV, NomProv as Provincia, SEC, NombreMunicipio as Municipio," + \
            " AsientoElectoral as Asiento, tipoCircunscripcion, estado, etapa, urbanorural, PoblacionElectoral, PoblacionCensal" + \
            " from [bdge].[dbo].[GeoAsientos_Nacional_all]"
        if usrdep != 0 :
            s = s + " where DEP = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DEP, PROV, SEC"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_rep_recintos_all(self, usrdep):        
        s = "Select IdLocReci, Reci, DEP, NomDep as Departamento, PROV, NomProv as Provincia, SEC, NombreMunicipio as Municipio," + \
            " NombreRecinto, NomDist, NomZona, CircunDist, TipoCircunscripcion, Estado, MaxMesasReci, ambientesDisp, Direccion," + \
            " latitud, longitud" + \
            " from [bdge].[dbo].[GeoRecintos_all]"
        if usrdep != 0 :
            s = s + " where DEP = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by Dep, Prov, Sec"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_rep_homologacion_all(self, usrdep):           
        s = "Select idLoc, reci, nomDep as Departamento, nomLoc, nomReci," + \
            " idloc2, reci2, nomReci2" + \
            " from [bdge].[dbo].[hom]"
        if usrdep != 0 :
            s = s + " where dep = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by Dep, Prov, Sec"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_rep_homojurisd_all(self, usrdep):           
        s = "Select idLoc, reci, nomDep as Departamento, nomLoc, nomReci," + \
            " idloc2, reci2, nomReci2" + \
            " from [bdge].[dbo].[actJurisd]"
        if usrdep != 0 :
            s = s + " where dep = %d and idLoc <> idloc2 and origen = 'R' order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " where idLoc <> idloc2 and origen = 'R' order by Dep, Prov, Sec"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_rep_jurisdiccion_all(self, usrdep):           
        s = "Select idLoc, reci, nomDep as Departamento, nomProv, nomSec, nomLoc, nomReci," + \
            " idloc2, reci2, nomDep2, nomProv2, nomSec2, nomReci2, fechaAct, usuario, origen" + \
            " from [bdge].[dbo].[actJurisd]"
        if usrdep != 0 :
            s = s + " where dep = %d order by prov, sec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by Dep, Prov, Sec"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_rep_logtransaccion_all(self, usrdep):              
        s = "select top(3000) GeografiaElectoral_app.dbo.DEP.Dep, GeografiaElectoral_app.dbo.DEP.NomDep as Departamento," + \
            " GeografiaElectoral_app.dbo.SEC.Sec, GeografiaElectoral_app.dbo.SEC.NomSec as Municipio," + \
            " case when bdge.dbo.logTransacciones.TipoTrn='U' then 'Update'" + \
                " when bdge.dbo.logTransacciones.TipoTrn='I' then 'Insert'" + \
                " when bdge.dbo.logTransacciones.TipoTrn='D' then 'Delete'" + \
                " else bdge.dbo.logTransacciones.TipoTrn end as Accion, bdge.dbo.logTransacciones.Tabla," + \
                " substring(bdge.dbo.logTransacciones.PK,PATINDEX('%=%',bdge.dbo.logTransacciones.PK)+1,PATINDEX('%>%',bdge.dbo.logTransacciones.PK)-PATINDEX('%=%',bdge.dbo.logTransacciones.PK)-1) as idLoc," + \
                " GeografiaElectoral_app.dbo.LOC.NomLoc as Asiento, bdge.dbo.logTransacciones.Campo, bdge.dbo.logTransacciones.ValorOriginal, bdge.dbo.logTransacciones.ValorNuevo," + \
                " Convert(CHAR(10),bdge.dbo.logTransacciones.FechaTrn,23) as Fecha, bdge.dbo.logTransacciones.Usuario" + \
            " from GeografiaElectoral_app.dbo.DEP" + \
            " LEFT JOIN GeografiaElectoral_app.dbo.PROV ON GeografiaElectoral_app.dbo.DEP.Dep = GeografiaElectoral_app.dbo.PROV.DepProv" + \
            " LEFT JOIN GeografiaElectoral_app.dbo.SEC ON GeografiaElectoral_app.dbo.DEP.Dep = GeografiaElectoral_app.dbo.SEC.DepSec AND" + \
            " GeografiaElectoral_app.dbo.PROV.Prov = GeografiaElectoral_app.dbo.SEC.ProvSec" + \
            " LEFT JOIN GeografiaElectoral_app.dbo.LOC ON GeografiaElectoral_app.dbo.DEP.Dep = GeografiaElectoral_app.dbo.LOC.DepLoc AND" + \
            " GeografiaElectoral_app.dbo.SEC.Sec = GeografiaElectoral_app.dbo.LOC.SecLoc AND GeografiaElectoral_app.dbo.PROV.Prov = GeografiaElectoral_app.dbo.LOC.ProvLoc" + \
            " LEFT JOIN bdge.dbo.logTransacciones ON substring(bdge.dbo.logTransacciones.PK,PATINDEX('%=%',bdge.dbo.logTransacciones.PK)+1,PATINDEX('%>%',bdge.dbo.logTransacciones.PK)-PATINDEX('%=%',bdge.dbo.logTransacciones.PK)-1)=GeografiaElectoral_app.dbo.LOC.idLoc"
        if usrdep != 0 :
            #s = s + " where GeografiaElectoral_app.dbo.DEP.Dep = %d order by GeografiaElectoral_app.dbo.PROV.prov, GeografiaElectoral_app.dbo.SEC.sec"
            s = s + " where GeografiaElectoral_app.dbo.DEP.Dep = %d order by bdge.dbo.logTransacciones.FechaTrn desc"
            self.cur.execute(s, usrdep)
        else:
            #s = s + " order by GeografiaElectoral_app.dbo.DEP.Dep, GeografiaElectoral_app.dbo.PROV.Prov, GeografiaElectoral_app.dbo.SEC.Sec"
            s = s + " order by bdge.dbo.logTransacciones.FechaTrn desc"
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
    
    def get_paises_all(self, usrdep):
            s = "select IdPais, NomPais from [GeografiaElectoral_app].[dbo].[PAIS]"
            if usrdep != 0 :
                s = s + " where IdPais = %d order by IdPais"
                self.cur.execute(s, usrdep)
            else:
                s = s + " where IdPais != 32 order by IdPais"
                self.cur.execute(s)

            rows = self.cur.fetchall()
            print(rows)
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_departamentos_all(self, usrdep):
            s = "select Dep, NomDep, IdPais from [GeografiaElectoral_app].[dbo].[DEP]"
            if usrdep != 0 :
                s = s + " where Dep = %d order by Dep"
                self.cur.execute(s, usrdep)
            else:
                s = s + " order by Dep"
                self.cur.execute(s)

            rows = self.cur.fetchall()
            print(rows)
            if self.cur.rowcount == 0:
                return False
            else:
                return rows


    def get_provincias_all(self, usrdep):
        s = "select DepProv, Prov, NomProv from [GeografiaElectoral_app].[dbo].[PROV]"
        if usrdep != 0 :
            s = s + " where DepProv = %d order by DepProv"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DepProv"
            print(s)
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_municipios_all(self, usrdep):
        s = "select DepSec, ProvSec, Sec, NomSec from [GeografiaElectoral_app].[dbo].[SEC]"
        if usrdep != 0 :
            s = s + " where DepSec = %d order by DepSec"
            self.cur.execute(s, usrdep)
        else:
            s = s + " order by DepSec"
            print(s)
            self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_rep_ext_asie_all(self):        
        s = "select IdLoc, NomPais, Dep, NomDep, Prov, NomProv, Sec, NomSec, NomLoc, estado, pobElec" + \
        " from [bdge].[dbo].[GeoAsientos_Exterior_all]" + \
        " order by IdPais, Dep, Prov, Sec, IdLoc"
        self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_rep_ext_reci_all(self):        
        s = "select NomPais, Dep, NomDep, Prov, NomProv, Sec, NomSec, IdLoc, NomLoc, Reci, NombreRecinto, estado, pobElec" + \
        " from [bdge].[dbo].[GeoRecintos_Exterior_all]" + \
        " order by IdPais, Dep, Prov, Sec, IdLoc, Reci"
        self.cur.execute(s)

        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows
class Gerencial:
    ''' Reportes de asientos/recintos (tablas) actualizados '''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_deptos_all(self):
        s = "select Dep, NomDep from GeografiaElectoral_app.dbo.DEP where Dep>0 and Dep<10"
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

    def id_usuario(self, user):
        s = "select usuario from [bdge].[dbo].[usuarios] where id = %d order by id"
        self.cur.execute(s, user)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.usuario = row[0]
            return True

    def get_gerencial_asi(self, inicio, final, dpto, usuario, accion):
        if inicio != "00-00-0000" and final != "00-00-0000":
            if dpto != 0:
                if usuario != 0: 
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Registrados'''
                            lista = usuario, dpto, inicio, final                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA) and usr = %s and Dep = %s " + \
                                "and Convert(char(10), fechaAct,23) between %d and %d"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            lista = usuario, dpto, inicio, final
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) and b.usr = %s and b.Dep = %s " + \
                                "and Convert(char(10), b.fechaAct,23) between %d and %d order by a.Dep, a.Prov, a.Sec"

                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            print(rows)
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''   
                            lista = usuario, dpto, inicio, final                         
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) and a.usr = %s and a.Dep = %s " + \
                                "and Convert(char(10), a.fechaAct,23) between %d and %d order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False
                else:
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Registrados'''
                            lista = dpto, inicio, final                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA) and Dep = %s and Convert(char(10), fechaAct,23) between %d and %d"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            lista = dpto, inicio, final                            
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) and b.Dep = %s " + \
                                "and Convert(char(10), b.fechaAct,23) between %d and %d order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''
                            lista = dpto, inicio, final                            
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) and a.Dep = %s " + \
                                "and Convert(char(10), a.fechaAct,23) between %d and %d " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False
            else:
                if usuario != 0: 
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Registrados'''
                            lista = usuario, inicio, final                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA) and usr = %s and Convert(char(10), fechaAct,23) between %d and %d"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            lista = usuario, inicio, final
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) and b.usr = %s " + \
                                "and Convert(char(10), b.fechaAct,23) between %d and %d order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''   
                            lista = usuario, inicio, final                         
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) and a.usr = %s " + \
                                "and Convert(char(10), a.fechaAct,23) between %d and %d " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False
                else:
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Registrados'''
                            lista = inicio, final                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA) and Convert(char(10), fechaAct,23) between %d and %d"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            lista = inicio, final
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) and Convert(char(10), b.fechaAct,23) between %d and %d " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''
                            lista = inicio, final                            
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) and Convert(char(10), fechaAct,23) between %d and %d " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False
        else:
            if dpto != 0:
                if usuario != 0: 
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Registrados'''
                            lista = usuario, dpto                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA) and usr = %s and Dep = %s"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            lista = usuario, dpto                            
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) and b.usr = %s and b.Dep = %s " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''   
                            lista = usuario, dpto                         
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) and a.usr = %s and a.Dep = %s " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False
                else:
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Registrados'''
                            lista = dpto                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA) and Dep = %s"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            lista = dpto
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) and b.Dep = %s " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''
                            lista = dpto                            
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) and a.Dep = %s " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False
            else:
                if usuario != 0: 
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Registrados'''
                            lista = usuario                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA) and usr = %s"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            lista = usuario                            
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) and b.usr = %s " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''   
                            lista = usuario                         
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) and a.usr = %s" + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s, lista)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False
                else:
                    if accion != 0:
                        if accion == '1':
                            '''Asientos Nuevos'''                            
                            s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, " + \
                                "PoblacionCensal, latitud, longitud, idEstado, Estado, idUrbanoRural, descUrbanoRural, fechaAct, usr, IdLoc, etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes " + \
                                "where IdLoc not in (select IdLoc from bdge.dbo.GeoAsientos_ReportesA)"
                            self.cur.execute(s)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows

                        if accion == '2':
                            '''Asientos Modificados'''
                            s = "delete from bdge.dbo.asi_mod"
                            try:
                                self.cur.execute(s)
                                self.cx.commit()
                            except:
                                 print("Error eliminación datos")

                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, " + \
                                "a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, a.PoblacionElectoral, a.PoblacionCensal, " + \
                                "a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.etapa, " + \
                                "b.Dep as DepN, b.Prov as ProvN, b.Sec as SecN, b.NomDep as NomDepN, b.NomProv as NomProvN, b.NombreMunicipio as NombreMunicipioN, " + \
                                "b.AsientoElectoral as AsientoElectoralN, b.TipoLocLoc as TipoLocLocN, b.TipoCircunscripcion as TipoCircunscripcionN, " + \
                                "b.PoblacionElectoral as PoblacionElectoralN, b.PoblacionCensal as PoblacionCensalN, b.latitud as latitudN, b.longitud as longitudN, " + \
                                "b.idEstado as idEstadoN, b.estado as estadoN, b.idUrbanoRural as idUrbanoRuralN, b.descUrbanoRural as descUrbanoRuralN, b.etapa as etapaN, a.IdLoc " + \
                                "from bdge.dbo.GeoAsientos_ReportesA a, bdge.dbo.GeoAsientos_Reportes b " + \
                                "where a.IdLoc = b.IdLoc " + \
                                "and (a.Dep <> b.Dep or a.NomDep <> b.NomDep " + \
                                "or a.Prov <> b.Prov or a.NomProv <> b.NomProv " + \
                                "or a.Sec <> b.Sec or a.NombreMunicipio <> b.NombreMunicipio " + \
                                "or a.TipoLocLoc <> b.TipoLocLoc or a.TipoCircunscripcion <> b.TipoCircunscripcion " + \
                                "or a.latitud <> b.latitud or a.longitud <> b.longitud " + \
                                "or a.idEstado <> b.idEstado or a.AsientoElectoral <> b.AsientoElectoral " + \
                                "or a.idUrbanoRural <> b.idUrbanoRural or a.PoblacionElectoral <> b.PoblacionElectoral " + \
                                "or a.PoblacionCensal <> b.PoblacionCensal or a.fechaAct <> b.fechaAct " + \
                                "or a.usr <> b.usr or a.idEtapa <> b.idEtapa " + \
                                "or a.doc_idA <> b.doc_idA or a.doc_idRN <> b.doc_idRN or a.doc_idAF <> b.doc_idAF " + \
                                "or a.doc_idAT <> b.doc_idAT or a.doc_idRNT <> b.doc_idRNT) " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                for asiento in rows:
                                    asi = asiento[0], asiento[1], asiento[2], asiento[3], asiento[4], asiento[5], asiento[6], asiento[7], asiento[8], \
                                          asiento[9], asiento[10], asiento[11], asiento[12], asiento[13], asiento[14], asiento[15], asiento[16], \
                                          asiento[17], asiento[18], asiento[19], asiento[20], asiento[21], asiento[22], asiento[23], asiento[24], \
                                          asiento[25], asiento[26], asiento[27], asiento[28], asiento[29], asiento[30], asiento[31], asiento[32], \
                                          asiento[33], asiento[34], asiento[35], asiento[36]
                                    s = "insert into bdge.dbo.asi_mod (Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                        "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                        "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                        "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                        "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                        "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                        "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc) VALUES " + \
                                        "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " + \
                                        "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                                    self.cur.execute(s, asi)
                                    self.cx.commit()

                                s = "select Dep, Prov, Sec, NomDep, NomProv, NombreMunicipio, " + \
                                    "AsientoElectoral, TipoLocLoc, TipoCircunscripcion, PoblacionElectoral, PoblacionCensal, " + \
                                    "latitud, longitud, idEstado, estado, idUrbanoRural, descUrbanoRural, Etapa, " + \
                                    "DepN, ProvN, SecN, NomDepN, NomProvN, NombreMunicipioN, " + \
                                    "AsientoElectoralN, TipoLocLocN, TipoCircunscripcionN, " + \
                                    "PoblacionElectoralN, PoblacionCensalN, latitudN, longitudN, " + \
                                    "idEstadoN, estadoN, idUrbanoRuralN, descUrbanoRuralN, EtapaN, IdLoc " + \
                                    "from bdge.dbo.asi_mod"
                                self.cur.execute(s)
                                rows = self.cur.fetchall()
                                if self.cur.rowcount == 0:
                                    return False
                                else:
                                    return rows

                        if accion == '3':
                            '''Asientos Suprimidos'''                            
                            s = "select a.Dep, a.Prov, a.Sec, a.NomDep, a.NomProv, a.NombreMunicipio, a.AsientoElectoral, a.TipoLocLoc, a.TipoCircunscripcion, " + \
                                "a.PoblacionElectoral, a.PoblacionCensal, a.latitud, a.longitud, a.idEstado, a.estado, a.idUrbanoRural, a.descUrbanoRural, a.IdLoc, a.etapa " + \
                                "from bdge.dbo.GeoAsientos_Reportes a, bdge.dbo.GeoAsientos_ReportesA b " + \
                                "where a.IdLoc = b.IdLoc and (a.idEstado <> b.idEstado and a.idEstado in(18, 19, 77, 78)) " + \
                                "order by a.Dep, a.Prov, a.Sec"
                            self.cur.execute(s)
                            rows = self.cur.fetchall()
                            if self.cur.rowcount == 0:
                                return False
                            else:
                                return rows
                    else:
                        return False


    def get_gerencial_reci(self, inicio, final, dpto, usuario, accion):
        v_fecha = True if (inicio != "00-00-0000" and final != "00-00-0000")  else False
        v_dpto = True if dpto != 0 else False
        v_usuario = True if usuario != 0 else False

        # nuevos - accion = 1
        s = "select d.Dep, p.Prov, s.Sec, d.NomDep, p.NomProv, s.NomSec as NombreMunicipio, a.ambientesDisp, l.IdLoc, l.NomLoc as AsientoElectoral, " + \
            "a.Reci, a.NomReci, di.CircunDist, " + \
            "CASE " + \
            "WHEN d.dep = 1 THEN 67 " + \
            "WHEN d.dep = 2 AND di.CircunDist = 1 THEN 68 " + \
            "WHEN d.dep = 2 AND l.tipolocloc in (67,69) AND (di.CircunDist between 6 and 19) THEN 67 " + \
            "WHEN d.dep = 3 AND di.CircunDist = 2 THEN 68 " + \
            "WHEN d.dep = 3 AND l.tipolocloc in (67,69) AND (di.CircunDist between 20 and 28) THEN 67 " + \
            "WHEN d.dep = 4 AND di.CircunDist = 3 THEN 68 " + \
            "WHEN d.dep = 4 AND l.tipolocloc in (67,69) AND (di.CircunDist between 29 and 32) THEN 67 " + \
            "WHEN d.dep = 5 THEN 67 " + \
            "WHEN d.dep = 6 AND di.CircunDist = 4 THEN 68 " + \
            "WHEN d.dep = 6 AND l.tipolocloc in (67,69) AND (di.CircunDist between 40 and 43) THEN 67 " + \
            "WHEN d.dep = 7 AND di.CircunDist = 5 THEN 68 " + \
            "WHEN d.dep = 7 AND l.tipolocloc in (67,69) AND (di.CircunDist between 44 and 57) THEN 67 " + \
            "WHEN d.dep = 8 AND di.CircunDist = 6 THEN 68 " + \
            "WHEN d.dep = 8 AND l.tipolocloc in (67,69) AND (di.CircunDist between 58 and 61) THEN 67 " + \
            "WHEN d.dep = 9 AND di.CircunDist = 7 THEN 68 " + \
            "WHEN d.dep = 9 AND l.tipolocloc in (67,69) AND (di.CircunDist between 62 and 63) THEN 67 " + \
            "ELSE l.tipolocloc END AS TipoLocLoc, " + \
            "CASE " + \
            "WHEN d.dep = 1 THEN 'Uninominal' " + \
            "WHEN d.dep = 2 AND di.CircunDist = 1 THEN 'Especial' " + \
            "WHEN d.dep = 2 AND l.tipolocloc in (67,69) AND (di.CircunDist between 6 and 19) THEN 'Uninominal' " + \
            "WHEN d.dep = 3 AND di.CircunDist = 2 THEN 'Especial' " + \
            "WHEN d.dep = 3 AND l.tipolocloc in (67,69) AND (di.CircunDist between 20 and 28) THEN 'Uninominal' " + \
            "WHEN d.dep = 4 AND di.CircunDist = 3 THEN 'Especial' " + \
            "WHEN d.dep = 4 AND l.tipolocloc in (67,69) AND (di.CircunDist between 29 and 32) THEN 'Uninominal' " + \
            "WHEN d.dep = 5 THEN 'Uninominal' " + \
            "WHEN d.dep = 6 AND di.CircunDist = 4 THEN 'Especial' " + \
            "WHEN d.dep = 6 AND l.tipolocloc in (67,69) AND (di.CircunDist between 40 and 43) THEN 'Uninominal' " + \
            "WHEN d.dep = 7 AND di.CircunDist = 5 THEN 'Especial' " + \
            "WHEN d.dep = 7 AND l.tipolocloc in (67,69) AND (di.CircunDist between 44 and 57) THEN 'Uninominal' " + \
            "WHEN d.dep = 8 AND di.CircunDist = 6 THEN 'Especial' " + \
            "WHEN d.dep = 8 AND l.tipolocloc in (67,69) AND (di.CircunDist between 58 and 61) THEN 'Uninominal' " + \
            "WHEN d.dep = 9 AND di.CircunDist = 7 THEN 'Especial' " + \
            "WHEN d.dep = 9 AND l.tipolocloc in (67,69) AND (di.CircunDist between 62 and 63) THEN 'Uninominal' " + \
            "END AS TipoCircunscripcion, " + \
            "di.Dist, di.NomDist, z.Zona, z.NomZona, " + \
            "a.MaxMesasReci, a.Direccion, a.latitud, a.longitud, es.idClasif as idEstado, es.descripcion as estado, tr.idClasif as idTipoRecinto, " + \
            "tr.descripcion as TipoRecinto, ur.idClasif as idUrbanoRural, ur.descripcion as descUrbanoRural, et.descripcion as Etapa " + \
            "FROM GeografiaElectoral_app.dbo.RECI a " + \
            "LEFT OUTER JOIN GeografiaElectoral_appA.dbo.RECI b ON b.IdLocReci = a.IdLocReci and b.Reci = a.Reci " + \
            "INNER JOIN GeografiaElectoral_app.dbo.LOC l ON a.IdLocReci = l.IdLoc " + \
            "INNER JOIN GeografiaElectoral_app.dbo.DEP d ON l.DepLoc = d.Dep " + \
            "INNER JOIN GeografiaElectoral_app.dbo.PROV p ON l.ProvLoc = p.Prov AND d.Dep = p.DepProv " + \
            "INNER JOIN GeografiaElectoral_app.dbo.SEC s ON l.SecLoc = s.Sec AND d.Dep = s.DepSec AND p.Prov = s.ProvSec " + \
            "INNER JOIN GeografiaElectoral_app.dbo.ZONA z ON a.ZonaReci=z.Zona AND l.IdLoc = z.IdLocZona " + \
            "INNER JOIN GeografiaElectoral_app.dbo.DIST di ON z.DistZona=di.Dist AND l.IdLoc=di.IdLocDist " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS es ON a.estado = es.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS tr ON a.tipoRecinto = tr.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS ur ON l.urbanoRural = ur.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS et ON a.etapa = et.idClasif " + \
            "WHERE b.IdLocReci is NULL"


        # modificados - accion = 2
        s2 = "select d.Dep, p.Prov, s.Sec, d.NomDep, p.NomProv, s.NomSec as NombreMunicipio, a.ambientesDisp, l.IdLoc, l.NomLoc as AsientoElectoral, " + \
            "a.Reci, a.NomReci, di.CircunDist, " + \
            "CASE " + \
            "WHEN d.dep = 1 THEN 67 " + \
            "WHEN d.dep = 2 AND di.CircunDist = 1 THEN 68 " + \
            "WHEN d.dep = 2 AND l.tipolocloc in (67,69) AND (di.CircunDist between 6 and 19) THEN 67 " + \
            "WHEN d.dep = 3 AND di.CircunDist = 2 THEN 68 " + \
            "WHEN d.dep = 3 AND l.tipolocloc in (67,69) AND (di.CircunDist between 20 and 28) THEN 67 " + \
            "WHEN d.dep = 4 AND di.CircunDist = 3 THEN 68 " + \
            "WHEN d.dep = 4 AND l.tipolocloc in (67,69) AND (di.CircunDist between 29 and 32) THEN 67 " + \
            "WHEN d.dep = 5 THEN 67 " + \
            "WHEN d.dep = 6 AND di.CircunDist = 4 THEN 68 " + \
            "WHEN d.dep = 6 AND l.tipolocloc in (67,69) AND (di.CircunDist between 40 and 43) THEN 67 " + \
            "WHEN d.dep = 7 AND di.CircunDist = 5 THEN 68 " + \
            "WHEN d.dep = 7 AND l.tipolocloc in (67,69) AND (di.CircunDist between 44 and 57) THEN 67 " + \
            "WHEN d.dep = 8 AND di.CircunDist = 6 THEN 68 " + \
            "WHEN d.dep = 8 AND l.tipolocloc in (67,69) AND (di.CircunDist between 58 and 61) THEN 67 " + \
            "WHEN d.dep = 9 AND di.CircunDist = 7 THEN 68 " + \
            "WHEN d.dep = 9 AND l.tipolocloc in (67,69) AND (di.CircunDist between 62 and 63) THEN 67 " + \
            "ELSE l.tipolocloc END AS TipoLocLoc, " + \
            "CASE " + \
            "WHEN d.dep = 1 THEN 'Uninominal' " + \
            "WHEN d.dep = 2 AND di.CircunDist = 1 THEN 'Especial' " + \
            "WHEN d.dep = 2 AND l.tipolocloc in (67,69) AND (di.CircunDist between 6 and 19) THEN 'Uninominal' " + \
            "WHEN d.dep = 3 AND di.CircunDist = 2 THEN 'Especial' " + \
            "WHEN d.dep = 3 AND l.tipolocloc in (67,69) AND (di.CircunDist between 20 and 28) THEN 'Uninominal' " + \
            "WHEN d.dep = 4 AND di.CircunDist = 3 THEN 'Especial' " + \
            "WHEN d.dep = 4 AND l.tipolocloc in (67,69) AND (di.CircunDist between 29 and 32) THEN 'Uninominal' " + \
            "WHEN d.dep = 5 THEN 'Uninominal' " + \
            "WHEN d.dep = 6 AND di.CircunDist = 4 THEN 'Especial' " + \
            "WHEN d.dep = 6 AND l.tipolocloc in (67,69) AND (di.CircunDist between 40 and 43) THEN 'Uninominal' " + \
            "WHEN d.dep = 7 AND di.CircunDist = 5 THEN 'Especial' " + \
            "WHEN d.dep = 7 AND l.tipolocloc in (67,69) AND (di.CircunDist between 44 and 57) THEN 'Uninominal' " + \
            "WHEN d.dep = 8 AND di.CircunDist = 6 THEN 'Especial' " + \
            "WHEN d.dep = 8 AND l.tipolocloc in (67,69) AND (di.CircunDist between 58 and 61) THEN 'Uninominal' " + \
            "WHEN d.dep = 9 AND di.CircunDist = 7 THEN 'Especial' " + \
            "WHEN d.dep = 9 AND l.tipolocloc in (67,69) AND (di.CircunDist between 62 and 63) THEN 'Uninominal' " + \
            "END AS TipoCircunscripcion, " + \
            "di.Dist, di.NomDist, z.Zona, z.NomZona, " + \
            "a.MaxMesasReci, a.Direccion, a.latitud, a.longitud, es.idClasif as idEstado, es.descripcion as estado, tr.idClasif as idTipoRecinto, " + \
            "tr.descripcion as TipoRecinto, ur.idClasif as idUrbanoRural, ur.descripcion as descUrbanoRural, et.descripcion AS Etapa, " + \
            "dd.Dep as DepN, pp.Prov as ProvN, ss.Sec as SecN, dd.NomDep as NomdepN, pp.NomProv as NomProvN, " + \
            "ss.NomSec as NombreMunicipioN, b.ambientesDisp as ambientesDispN, ll.IdLoc as IdLocN, " + \
            "ll.NomLoc as AsientoElectoralN, b.Reci as ReciN, b.NomReci as NomReciN, dii.CircunDist as CircunDistN, "+ \
            "CASE " + \
            "WHEN dd.dep = 1 THEN 67 " + \
            "WHEN dd.dep = 2 AND dii.CircunDist = 1 THEN 68 " + \
            "WHEN dd.dep = 2 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 6 and 19) THEN 67 " + \
            "WHEN dd.dep = 3 AND dii.CircunDist = 2 THEN 68 " + \
            "WHEN dd.dep = 3 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 20 and 28) THEN 67 " + \
            "WHEN dd.dep = 4 AND dii.CircunDist = 3 THEN 68 " + \
            "WHEN dd.dep = 4 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 29 and 32) THEN 67 " + \
            "WHEN dd.dep = 5 THEN 67 " + \
            "WHEN dd.dep = 6 AND dii.CircunDist = 4 THEN 68 " + \
            "WHEN dd.dep = 6 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 40 and 43) THEN 67 " + \
            "WHEN dd.dep = 7 AND dii.CircunDist = 5 THEN 68 " + \
            "WHEN dd.dep = 7 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 44 and 57) THEN 67 " + \
            "WHEN dd.dep = 8 AND dii.CircunDist = 6 THEN 68 " + \
            "WHEN dd.dep = 8 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 58 and 61) THEN 67 " + \
            "WHEN dd.dep = 9 AND dii.CircunDist = 7 THEN 68 " + \
            "WHEN dd.dep = 9 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 62 and 63) THEN 67 " + \
            "ELSE ll.tipolocloc END AS TipoLocLocN, " + \
            "CASE " + \
            "WHEN dd.dep = 1 THEN 'Uninominal' " + \
            "WHEN dd.dep = 2 AND dii.CircunDist = 1 THEN 'Especial' " + \
            "WHEN dd.dep = 2 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 6 and 19) THEN 'Uninominal' " + \
            "WHEN dd.dep = 3 AND dii.CircunDist = 2 THEN 'Especial' " + \
            "WHEN dd.dep = 3 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 20 and 28) THEN 'Uninominal' " + \
            "WHEN dd.dep = 4 AND dii.CircunDist = 3 THEN 'Especial' " + \
            "WHEN dd.dep = 4 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 29 and 32) THEN 'Uninominal' " + \
            "WHEN dd.dep = 5 THEN 'Uninominal' " + \
            "WHEN dd.dep = 6 AND dii.CircunDist = 4 THEN 'Especial' " + \
            "WHEN dd.dep = 6 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 40 and 43) THEN 'Uninominal' " + \
            "WHEN dd.dep = 7 AND dii.CircunDist = 5 THEN 'Especial' " + \
            "WHEN dd.dep = 7 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 44 and 57) THEN 'Uninominal' " + \
            "WHEN dd.dep = 8 AND dii.CircunDist = 6 THEN 'Especial' " + \
            "WHEN dd.dep = 8 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 58 and 61) THEN 'Uninominal' " + \
            "WHEN dd.dep = 9 AND dii.CircunDist = 7 THEN 'Especial' " + \
            "WHEN dd.dep = 9 AND ll.tipolocloc in (67,69) AND (dii.CircunDist between 62 and 63) THEN 'Uninominal' " + \
            "END AS TipoCircunscripcionN, " + \
            "dii.Dist as DistN, dii.NomDist as NomDistN, zz.Zona as ZonaN, zz.NomZona as NomZonaN, b.MaxMesasReci as MaxMesasReciN, " + \
            "b.Direccion as DireccionN, b.latitud as latitudN, b.longitud as longitudN, ess.idClasif as idEstadoN, ess.descripcion as estadoN, " + \
            "trr.idClasif as idTipoRecintoN, trr.descripcion as TipoRecintoN, urr.idClasif as idUrbanoRuralN, urr.descripcion as descUrbanoRuralN, ett.descripcion AS EtapaN " + \
            "from GeografiaElectoral_app.dbo.RECI a " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.RECI b ON a.IdLocReci = b.IdLocReci and a.Reci = b.Reci " + \
            "INNER JOIN GeografiaElectoral_app.dbo.LOC l ON a.IdLocReci = l.IdLoc " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.LOC ll ON b.IdLocReci = ll.IdLoc " + \
            "INNER JOIN GeografiaElectoral_app.dbo.DEP d ON l.DepLoc = d.Dep " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.DEP dd ON ll.DepLoc = dd.Dep " + \
            "INNER JOIN GeografiaElectoral_app.dbo.PROV p ON l.ProvLoc = p.Prov AND d.Dep = p.DepProv " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.PROV pp ON ll.ProvLoc = pp.Prov AND dd.Dep = pp.DepProv " + \
            "INNER JOIN GeografiaElectoral_app.dbo.SEC s ON l.SecLoc = s.Sec AND d.Dep = s.DepSec AND p.Prov = s.ProvSec " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.SEC ss ON ll.SecLoc = ss.Sec AND dd.Dep = ss.DepSec AND pp.Prov = ss.ProvSec " + \
            "INNER JOIN GeografiaElectoral_app.dbo.ZONA z ON a.IdLocReci = z.IdLocZona AND a.IdLocReci = l.IdLoc AND a.ZonaReci = z.Zona " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.ZONA zz ON b.IdLocReci = zz.IdLocZona AND b.IdLocReci = ll.IdLoc AND b.ZonaReci = zz.Zona " + \
            "INNER JOIN GeografiaElectoral_app.dbo.DIST di ON a.IdLocReci = di.IdLocDist AND a.IdLocReci = l.IdLoc AND z.DistZona = di.Dist " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.DIST dii ON b.IdLocReci = dii.IdLocDist AND b.IdLocReci = ll.IdLoc AND zz.DistZona = dii.Dist " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS tc ON l.TipoLocLoc = tc.idClasif " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.clasif AS tcc ON ll.TipoLocLoc = tcc.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS es ON a.estado = es.idClasif " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.clasif AS ess ON b.estado = ess.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS tr ON a.tipoRecinto = tr.idClasif " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.clasif AS trr ON b.tipoRecinto = trr.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS ur ON l.urbanoRural = ur.idClasif " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.clasif AS urr ON ll.urbanoRural = urr.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS et ON a.etapa = et.idClasif " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.clasif AS ett ON b.etapa = ett.idClasif " + \
            "WHERE (a.NomReci <> b.NomReci or a.estado <> b.estado or a.tipoRecinto <> b.tipoRecinto or a.depend <> b.depend or " + \
            "a.etapa <> b.etapa or a.latitud <> b.latitud or a.longitud <> b.longitud or a.Direccion <> b.Direccion " + \
            "or a.ZonaReci <> b.ZonaReci or a.codRue <> b.codRue or a.codRueEdif <> b.codRueEdif or a.cantPisos <> b.cantPisos " + \
            "or a.fechaAct <> b.fechaAct or a.usuario <> b.usuario or a.doc_idA <> b.doc_idA or a.doc_idAF <> b.doc_idAF " + \
            "or a.nacionId <> b.nacionId or a.ambientesDisp <> b.ambientesDisp or a.doc_idT <> b.doc_idT or a.MaxMesasReci <> b.MaxMesasReci) "


        # suprimidos - accion = 3
        s3 = "select d.Dep, p.Prov, s.Sec, d.NomDep, p.NomProv, s.NomSec as NombreMunicipio, a.ambientesDisp, l.IdLoc, l.NomLoc as AsientoElectoral, " + \
            "a.Reci, a.NomReci, di.CircunDist, " + \
            "CASE " + \
            "WHEN d.dep = 1 THEN 67 " + \
            "WHEN d.dep = 2 AND di.CircunDist = 1 THEN 68 " + \
            "WHEN d.dep = 2 AND l.tipolocloc in (67,69) AND (di.CircunDist between 6 and 19) THEN 67 " + \
            "WHEN d.dep = 3 AND di.CircunDist = 2 THEN 68 " + \
            "WHEN d.dep = 3 AND l.tipolocloc in (67,69) AND (di.CircunDist between 20 and 28) THEN 67 " + \
            "WHEN d.dep = 4 AND di.CircunDist = 3 THEN 68 " + \
            "WHEN d.dep = 4 AND l.tipolocloc in (67,69) AND (di.CircunDist between 29 and 32) THEN 67 " + \
            "WHEN d.dep = 5 THEN 67 " + \
            "WHEN d.dep = 6 AND di.CircunDist = 4 THEN 68 " + \
            "WHEN d.dep = 6 AND l.tipolocloc in (67,69) AND (di.CircunDist between 40 and 43) THEN 67 " + \
            "WHEN d.dep = 7 AND di.CircunDist = 5 THEN 68 " + \
            "WHEN d.dep = 7 AND l.tipolocloc in (67,69) AND (di.CircunDist between 44 and 57) THEN 67 " + \
            "WHEN d.dep = 8 AND di.CircunDist = 6 THEN 68 " + \
            "WHEN d.dep = 8 AND l.tipolocloc in (67,69) AND (di.CircunDist between 58 and 61) THEN 67 " + \
            "WHEN d.dep = 9 AND di.CircunDist = 7 THEN 68 " + \
            "WHEN d.dep = 9 AND l.tipolocloc in (67,69) AND (di.CircunDist between 62 and 63) THEN 67 " + \
            "ELSE l.tipolocloc END AS TipoLocLoc, " + \
            "CASE " + \
            "WHEN d.dep = 1 THEN 'Uninominal' " + \
            "WHEN d.dep = 2 AND di.CircunDist = 1 THEN 'Especial' " + \
            "WHEN d.dep = 2 AND l.tipolocloc in (67,69) AND (di.CircunDist between 6 and 19) THEN 'Uninominal' " + \
            "WHEN d.dep = 3 AND di.CircunDist = 2 THEN 'Especial' " + \
            "WHEN d.dep = 3 AND l.tipolocloc in (67,69) AND (di.CircunDist between 20 and 28) THEN 'Uninominal' " + \
            "WHEN d.dep = 4 AND di.CircunDist = 3 THEN 'Especial' " + \
            "WHEN d.dep = 4 AND l.tipolocloc in (67,69) AND (di.CircunDist between 29 and 32) THEN 'Uninominal' " + \
            "WHEN d.dep = 5 THEN 'Uninominal' " + \
            "WHEN d.dep = 6 AND di.CircunDist = 4 THEN 'Especial' " + \
            "WHEN d.dep = 6 AND l.tipolocloc in (67,69) AND (di.CircunDist between 40 and 43) THEN 'Uninominal' " + \
            "WHEN d.dep = 7 AND di.CircunDist = 5 THEN 'Especial' " + \
            "WHEN d.dep = 7 AND l.tipolocloc in (67,69) AND (di.CircunDist between 44 and 57) THEN 'Uninominal' " + \
            "WHEN d.dep = 8 AND di.CircunDist = 6 THEN 'Especial' " + \
            "WHEN d.dep = 8 AND l.tipolocloc in (67,69) AND (di.CircunDist between 58 and 61) THEN 'Uninominal' " + \
            "WHEN d.dep = 9 AND di.CircunDist = 7 THEN 'Especial' " + \
            "WHEN d.dep = 9 AND l.tipolocloc in (67,69) AND (di.CircunDist between 62 and 63) THEN 'Uninominal' " + \
            "END AS TipoCircunscripcion, " + \
            "di.Dist, di.NomDist, z.Zona, z.NomZona, " + \
            "a.MaxMesasReci, a.Direccion, a.latitud, a.longitud, es.idClasif as idEstado, es.descripcion as estado, tr.idClasif as idTipoRecinto, " + \
            "tr.descripcion as TipoRecinto, ur.idClasif as idUrbanoRural, ur.descripcion as descUrbanoRural, et.descripcion AS Etapa " + \
            "from GeografiaElectoral_app.dbo.RECI a " + \
            "INNER JOIN GeografiaElectoral_appA.dbo.RECI b ON a.IdLocReci = b.IdLocReci and a.Reci = b.Reci " + \
            "INNER JOIN GeografiaElectoral_app.dbo.LOC l ON a.IdLocReci = l.IdLoc " + \
            "INNER JOIN GeografiaElectoral_app.dbo.DEP d ON l.DepLoc = d.Dep " + \
            "INNER JOIN GeografiaElectoral_app.dbo.PROV p ON l.ProvLoc = p.Prov AND d.Dep = p.DepProv " + \
            "INNER JOIN GeografiaElectoral_app.dbo.SEC s ON l.SecLoc = s.Sec AND d.Dep = s.DepSec AND p.Prov = s.ProvSec " + \
            "INNER JOIN GeografiaElectoral_app.dbo.ZONA z ON a.IdLocReci = z.IdLocZona and z.Zona = a.ZonaReci " + \
            "INNER JOIN GeografiaElectoral_app.dbo.DIST di ON z.IdLocZona = di.IdLocDist and z.DistZona = di.Dist " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS es ON a.estado = es.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS tr ON a.tipoRecinto = tr.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS ur ON l.urbanoRural = ur.idClasif " + \
            "INNER JOIN GeografiaElectoral_app.dbo.clasif AS et ON a.etapa = et.idClasif " + \
            "WHERE (a.estado <> b.estado and a.estado in(4, 5, 82, 83))"

        ''' posibles opciones seleccionadas - total 8
            NO considera la variable -accion- que debe estar seleccionada para cualquier consulta
            0 0 0
            0 0 1
            0 1 0
            0 1 1
            1 0 0
            1 0 1
            1 1 0
            1 1 1
        '''
        t = ()  # parámetros query

        # 0 0 0
        if not v_fecha and not v_dpto and not v_usuario:
            if accion == '1':
                pass
            elif accion == '2':
                s = s2
            elif accion == '3':
                s = s3
            else:
                pass

        # 0 0 1
        if not v_fecha and not v_dpto and v_usuario:
            t = usuario
            cond =  " and a.usuario = %s"
            if accion == '1':
                s += cond
            elif accion == '2':
                s = s2 + cond
            elif accion == '3':
                s = s3 + cond
            else:
                pass

        # 0 1 0
        if not v_fecha and v_dpto and not v_usuario:
            t = dpto
            cond = " and d.dep = %s"
            if accion == '1':
                s += cond
            elif accion == '2':
                s = s2 + cond
            elif accion == '3':
                s = s3 + cond
            else:
                pass

        # 0 1 1
        if not v_fecha and v_dpto and v_usuario:
            t = dpto, usuario
            cond = " and d.dep = %s and a.usuario = %s"
            if accion == '1':
                s += cond
            elif accion == '2':
                s = s2 + cond
            elif accion == '3':
                s = s3 + cond
            else:
                pass

        # 1 0 0
        if v_fecha and not v_dpto and not v_usuario:
            t = inicio, final
            cond = " and Convert(char(10), a.fechaAct,23) between %d and %d"
            if accion == '1':
                s += cond
            elif accion == '2':
                s = s2 + cond
            elif accion == '3':
                s = s3 + cond
            else:
                pass

        # 1 0 1
        if v_fecha and not v_dpto and v_usuario:
            t = inicio, final, usuario
            cond = " and Convert(char(10), a.fechaAct,23) between %d and %d and a.usuario = %s"
            if accion == '1':
                s += cond
            elif accion == '2':
                s = s2 + cond
            elif accion == '3':
                s = s3 + cond
            else:
                pass

        # 1 1 0
        if v_fecha and v_dpto and not v_usuario:
            t = inicio, final, dpto
            cond = " and Convert(char(10), a.fechaAct,23) between %d and %d and d.dep = %s"
            if accion == '1':
                s += cond
            elif accion == '2':
                s = s2 + cond
            elif accion == '3':
                s = s3 + cond
            else:
                pass

        # 1 1 1
        if v_fecha and v_dpto and v_usuario:
            t = inicio, final, dpto, usuario
            cond = " and Convert(char(10), a.fechaAct,23) between %d and %d and d.dep = %s and a.usuario = %s"
            if accion == '1':
                s += cond
            elif accion == '2':
                s = s2 + cond
            elif accion == '3':
                s = s3 + cond
            else:
                pass

        self.cur.execute(s, t)
        rows = self.cur.fetchall()
        return rows

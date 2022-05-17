# Operaciones asientos

class LatLong:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_geos(self, lat, long):
        s = "select ST_SetSRID(ST_MakePoint(%s, %s), 4326) as geom from auxiliar where idloc=108"
        coord = long, lat
        self.cur.execute(s, coord)
        row = self.cur.fetchone()
        if row == None:
            return False
        else:
            self.geom = row[0]
            return True

    def del_geo_asiento(self):
        s = "delete from asientos"
        try:
            self.cur.execute(s)
            self.cx.commit()
            print('Asientos eliminados')
        except:
             print("Error --DEL-- asiento...")


    def del_geo_recinto(self):
        s = "delete from recintos"
        try:
            self.cur.execute(s)
            self.cx.commit()
            print('Recintos eliminados')
        except:
             print("Error --DEL-- recinto...")


    def add_geo_asiento(self, cod_dep, cod_prov, cod_mun, departamento, provincia, municipio, idloc, asiento, \
                    	doc_act, fecha_doc_act, pob_electoral, pob_censal, tipo_circunscripcion, etapa, estado, \
                    	latitud, longitud, obs, geom, fechaIngreso, fechaAct, usuario, situacion):
        new_asiento = cod_dep, cod_prov, cod_mun, departamento, provincia, municipio, idloc, asiento, \
                      doc_act, fecha_doc_act, pob_electoral, pob_censal, tipo_circunscripcion, etapa, estado, \
                      latitud, longitud, obs, geom, fechaIngreso, fechaAct, usuario, '', situacion
        
        s = "insert into asientos(cod_dep, cod_prov, cod_mun, " + \
            "departamento, provincia, municipio, idloc, asiento, doc_act, fecha_doc_act, " + \
            "pob_electoral, pob_censal, tipo_circun, etapa, estado, latitud, longitud, " + \
            "obs, geom, fecha_ingreso, fecha_act, usuario, gdb_geomattr_data, situacion) VALUES " + \
            "(%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_asiento)
            self.cx.commit()
            print("Asiento adicionado...") 
        except:
            print("Error - actualización de asiento...")


    def add_geo_recinto(self, id, cod_dep, cod_prov, cod_mun, departamento, provincia, municipio, idloc, asiento, reci, recinto, \
                    	doc_act, fecha_doc_act, cod_dist, distrito, cod_zona, zona, direccion, circun, tipo_circunscripcion, \
                    	tipo_recinto, etapa, estado, latitud, longitud, geom, fechaIngreso, fechaAct, usuario, situacion):
        new_recinto = id, cod_dep, cod_prov, cod_mun, departamento, provincia, municipio, idloc, asiento, reci, recinto, \
                      doc_act, fecha_doc_act, cod_dist, distrito, cod_zona, zona, direccion, circun, tipo_circunscripcion, \
                      tipo_recinto, etapa, estado, latitud, longitud, '', geom, fechaIngreso, fechaAct, usuario, '', situacion
       
        s = "insert into recintos(id, cod_dep, cod_prov, cod_mun, departamento, provincia, municipio, " + \
            "idloc, asiento, reci, recinto, doc_act, fecha_doc_act, cod_dist, distrito, cod_zona, zona, direccion, " + \
            "circun, tipo_circun, tipo_recinto, etapa, estado, latitud, longitud, obs, geom, fecha_ingreso, " + \
            "fecha_act, usuario, gdb_geomattr_data, situacion) VALUES " + \
            "(%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        try:
            self.cur.execute(s, new_recinto)
            self.cx.commit()
            print("Recinto adicionado...") 
        except:
            print("Error - actualización de recinto...")
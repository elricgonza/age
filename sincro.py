# Operaciones sincro-nización

class LatLong:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_geos(self, lat, long):
        ''' Crea objeto geométrico '''
        s = "select f_crea_geom(%s, %s) as geom"
        coord = long, lat
        try:
            self.cur.execute(s, coord)
        except Exception as e:
            print(e)
            print('Error conversión --f_crea_geom--')

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


    def add_geo_asiento(self, *new):
        s = '''
            insert into asientos(cod_dep, cod_prov, cod_mun,
            departamento, provincia, municipio, idloc, asiento, doc_act, fecha_doc_act,
            pob_electoral, pob_censal, tipo_circun, etapa, estado, latitud, longitud,
            obs, geom, fecha_ingreso, fecha_act, usuario, gdb_geomattr_data, situacion) VALUES
            (%s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s)
        '''
        try:
            self.cur.execute(s, new)
            self.cx.commit()
        except Exception as e:
            print(e)
            print("Error - actualización de asiento...")


    def add_geo_recinto(self, *new):
        s = """
            insert into recintos(id, cod_dep, cod_prov, cod_mun, departamento, provincia, municipio,
            idloc, asiento, reci, recinto, doc_act, fecha_doc_act, cod_dist,
            distrito, cod_zona, zona, direccion, circun, tipo_circun, tipo_recinto,
            etapa, estado, latitud, longitud, obs, geom, fecha_ingreso,
            fecha_act, usuario, gdb_geomattr_data, situacion) VALUES
            (%s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s,
             %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s)
        """
        try:
            self.cur.execute(s, new)
            self.cx.commit()
        except Exception as e:
            print(e)

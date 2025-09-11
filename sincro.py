# Operaciones sincro-nización

from dataclasses import dataclass
from typing import Optional
from datetime import datetime


class LatLong:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_geos(self, lat, long):
        ''' Crea objeto geométrico '''
        s = "select f_crea_geom(%s, %s) as geom"
        coord = long, lat
        #print('pppp------------------------')
        #print(coord)
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
        except:
            print("Error - actualización de asiento...")


    def add_geo_recintoK(self, id, cod_dep, cod_prov, cod_mun, departamento, provincia, municipio, idloc, asiento, reci, recinto, \
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
        except Exception as e:
            print(e)
            print("Error - actualización de recinto...")


    def add_geo_recinto(self, r):
        s = """
            insert into recintos(id, cod_dep, cod_prov, cod_mun, departamento,
            provincia, municipio, idloc, asiento, reci,
            recinto, doc_act, fecha_doc_act, cod_dist, distrito,
            cod_zona, zona, direccion, circun, tipo_circun,
            tipo_recinto, etapa, estado, latitud, longitud,
            obs, geom, fecha_ingreso, fecha_act, usuario,
            gdb_geomattr_data, situacion) VALUES  
            (?, ?, ?, ?, ?,  ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?,
            ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?,  ?, ?, ?, ?, ?,  ?, ?)"
        """
        s = """
            insert into recintos(id, cod_dep, cod_prov, cod_mun, departamento,
            provincia, municipio, idloc, asiento, reci,
            recinto, doc_act, fecha_doc_act, cod_dist, distrito,
            cod_zona, zona, direccion, circun, tipo_circun,
            tipo_recinto, etapa, estado, latitud, longitud,
            obs, geom, fecha_ingreso, fecha_act, usuario,
            gdb_geomattr_data, situacion) VALUES  
            (%s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s,  %s, %s)"
        """
        s = "insert into asientos(cod_dep, cod_prov, cod_mun, " + \
            "departamento, provincia, municipio, idloc, asiento, doc_act, fecha_doc_act, " + \
            "pob_electoral, pob_censal, tipo_circun, etapa, estado, latitud, longitud, " + \
            "obs, geom, fecha_ingreso, fecha_act, usuario, gdb_geomattr_data, situacion) VALUES " + \
            "(?, ?, ?, ?, ?,  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"

        params = (r.id, r.cod_dep, r.cod_prov, r.cod_mun, r.departamento, \
                 r.provincia, r.municipio, r.idloc, r.asiento, r.reci, \
                 r.recinto, r.doc_act, r.fecha_doc_act, r.cod_dist, r.distrito,\
                 r.cod_zona, r.zona, r.direccion, r.circun, r.tipo_circun, \
                 r.tipo_recinto, r.etapa, r.estado, r.latitud, r.longitud, \
                 r.obs, r.geom, r.fecha_ingreso, r.fecha_act, r.usuario, \
                 r.gdb_geomattr_data, r.situacion)

        try:
            self.cur.execute(s, params)
            self.cx.commit() 
        except Exception as e:
            print(e)
            print("Error - actualización de recinto...")

@dataclass
class RecintoGeo:
    id: int
    cod_dep: int
    cod_prov: int
    cod_mun: int
    departamento: str
    provincia: str
    municipio: str
    idloc: int
    asiento: str
    reci: int
    recinto: str
    doc_act: str
    fecha_doc_act: datetime #= datetime(0,0,0, 0,0,0)
    cod_dist: int
    distrito: str
    cod_zona: int
    zona: str
    direccion: str
    circun: int
    tipo_circun: str
    tipo_recinto: str
    etapa: str
    estado: str
    latitud: float
    longitud: float
    obs: Optional[str] # = ''
    geom: bytes #bytearray #bytes
    fecha_ingreso: datetime #= datetime.now()
    fecha_act: datetime #= datetime.now()
    usuario: str
    gdb_geomattr_data: bytes
    situacion: str


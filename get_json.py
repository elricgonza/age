''' get's for visor '''

import json

class GetJson:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()


    def get_dep(self, dep):
        s = f'select departamento, st_asgeojson(geom) from departamento where cod_dep= {dep}'
        self.cur.execute(s)
        row = self.cur.fetchone()

        geo_json = {
            "type": "Feature",
            "name": row[0],
            "properties": {},
            "geometry": json.loads(row[1])
        }
        return geo_json


    def get_prov(self, dep):
        s = ''' 
        SELECT jsonb_build_object(
            'crs',      '{ type: name, properties: { name: urn:ogc:def:crs:OGC:1.3:CRS84 } }',
            'name',     'trian',
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        FROM (
          SELECT jsonb_build_object(
            'type',       'Feature',
            'dep',        cod_dep,  
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT cod_dep::varchar(255) || '-' || cod_prov::varchar(255) as cod, 
            provincia, cod_dep, geom FROM provincias
            '''
        
        if (dep == '0'):
            sss = s + ' ) inputs) features;'
        else:
            ss = f'WHERE cod_dep= {dep} '
            sss = s + ss + ' ) inputs) features;'

        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json


    def get_mun(self, dep):
        s = ''' 
        SELECT jsonb_build_object(
            'crs',      '{ type: name, properties: { name: urn:ogc:def:crs:OGC:1.3:CRS84 } }',
            'name',     'trian',
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        FROM (
          SELECT jsonb_build_object(
            'type',       'Feature',
            'dep',        cod_dep,  
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT cod_dep::varchar(255) || '-' || cod_prov::varchar(255) || '-' || cod_mun::varchar(255) as cod, 
            municipio, cod_dep, geom FROM municipios
            '''
        
        if (dep == '0'):
            sss = s + ' ) inputs) features;'
        else:
            ss = f'WHERE cod_dep= {dep} '
            sss = s + ss + ' ) inputs) features;'

        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json


    def get_cir(self, dep):
        # get circunscripciones
        s = ''' 
        SELECT jsonb_build_object(
            'crs',      '{ type: name, properties: { name: urn:ogc:def:crs:OGC:1.3:CRS84 } }',
            'name',     'trian',
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        FROM (
          SELECT jsonb_build_object(
            'type',       'Feature',
            'dep',     cod_dep,  
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT circun, cod_dep, geom FROM circun
            '''

        if (dep == '0'):
            sss = s + ' ) inputs) features;'
        else:
            ss = f'WHERE cod_dep= {dep} '
            sss = s + ss + ' ) inputs) features;'

        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json


    def get_reci(self, dep):
        s = '''
        SELECT jsonb_build_object(
            'crs',      '{ type: name, properties: { name: urn:ogc:def:crs:OGC:1.3:CRS84 } }',
            'name',     'trian',
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        FROM (
          SELECT jsonb_build_object(
            'type',       'Feature',
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT recinto,  
                idloc::varchar(255) || '-' || reci::varchar(255) as idlocreci,
                departamento || '-' || provincia || '-' || municipio as dpm,
                cod_dep::varchar(255) || '-' || cod_prov::varchar(255) || '-' || cod_mun::varchar(255) as cod,
                tipo_circun || ' - ' || circun::varchar(255) as circun,
                zona, direccion, geom 
                FROM recintos
        '''
        
        if (dep == '0'):
            sss = s + ' ) inputs) features;'
        else:
            ss = f'WHERE cod_dep= {dep} '
            sss = s + ss + ' ) inputs) features;'

        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json


    def get_reci_mts(self, plat, plong, pmts):
        s = '''
        SELECT jsonb_build_object(
            'crs',      '{ type: name, properties: { name: urn:ogc:def:crs:OGC:1.3:CRS84 } }',
            'name',     'trian',
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        FROM (
          SELECT jsonb_build_object(
            'type',       'Feature',
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT recinto,  
                dist, geom
        '''
        ss = f'FROM f_get_points_mts_reci({plat}, {plong}, {pmts}) '
        
        sss = s + ss +  ' ) inputs) features;'

        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json


    def get_asi(self, dep):
        s = '''
        SELECT jsonb_build_object(
            'crs',      '{ type: name, properties: { name: urn:ogc:def:crs:OGC:1.3:CRS84 } }',
            'name',     'trian',
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        FROM (
          SELECT jsonb_build_object(
            'type',       'Feature',
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT asiento,  
                idloc::varchar(255) as idloc,
                departamento || '-' || provincia || '-' || municipio as dpm,
                cod_dep::varchar(255) || '-' || cod_prov::varchar(255) || '-' || cod_mun::varchar(255) as cod,
                tipo_circun,
                pob_electoral, pob_censal, geom 
                FROM asientos
        '''
        
        if (dep == '0'):
            sss = s + ' ) inputs) features;'
        else:
            ss = f'WHERE cod_dep= {dep} '
            sss = s + ss + ' ) inputs) features;'

        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json


    def get_loc(self, dep):
        s = '''
        SELECT jsonb_build_object(
            'crs',      '{ type: name, properties: { name: urn:ogc:def:crs:OGC:1.3:CRS84 } }',
            'name',     'trian',
            'type',     'FeatureCollection',
            'features', jsonb_agg(features.feature)
        )
        FROM (
          SELECT jsonb_build_object(
            'type',       'Feature',
            'id',         id,
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT id, nom_localidad, geom FROM g_localidad
                '''
        
        if (dep == '0'):
            print('dep IGUAL A  0')
            sss = s + ' ) inputs) features;'
        else:
            print('dep DIFERENTE a 0')
            ss = f'WHERE ut_sup_id= {dep} '
            sss = s + ss + ' ) inputs) features;'
        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json

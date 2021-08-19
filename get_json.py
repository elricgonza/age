import json
# get for visor

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
            'id',         id,
            'dep',        cod_dep,  
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT id, provincia, cod_dep from FROM provincias
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
            'id',         id,
            'dep',        cod_dep,  
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT id, municipio, cod_dep, geom FROM municipios
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


    def get_circun(self, dep):
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
            'dep',     cod_dep,  
            'geometry',   ST_AsGeoJSON(geom)::jsonb,
            'properties', to_jsonb(inputs) - 'id' - 'geom'
          ) AS feature
          FROM (SELECT id, nom_circunscripcion, ut_sup_id, geom FROM ge_circun
            '''
        
        if (dep == '0'):
            sss = s + ' ) inputs) features;'
        else:
            ss = f'WHERE ut_sup_id= {dep} '
            sss = s + ss + ' ) inputs) features;'

        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json


    def get_nal(self):
        '''
        s = 'select row_to_json(fc) ' + \
                'from (select 'FeatureCollection' as Type, array_to_json(array_agg(f)) as features ' + \
                'from (select 'Feature' as Type, ' + \
                '   ST_AsGeoJSON(lg.geom)::json as geometry, ' + \
                '   ( ' + \
                '   select row_to_json(t) ' + \
                '   from (select id, nom_ut_sup, geom) t ' + \
                '   ) ' + \
                '   as properties ' + \
                '   from g_ut_sup as lg ) as f ) as fc'


        s = "select row_to_json(fc) " + \
                "from (select 'FeatureCollection' as Type, array_to_json(array_agg(f)) as features " + \
                "from (select 'Feature' as Type, " + \
                "   ST_AsGeoJSON(lg.geom)::json as geometry, " + \
                "   ( " + \
                "   select row_to_json(t) " + \
                "   from (select id, nom_ut_sup, geom) t " + \
                "   ) " + \
                "   as properties " + \
                "   from g_ut_sup as lg ) as f ) as fc"
        '''

        s = '''
        select row_to_json(fc)   
                from (select 'FeatureCollection' as Type, array_to_json(array_agg(f)) as features   
                from (select 'Feature' as Type,   
                   ST_AsGeoJSON(lg.geom)::json as geometry,   
                   (   
                   select row_to_json(t)   
                   from (select id, nom_ut_sup, geom) t   
                   )   
                   as properties   
                   from g_ut_sup as lg ) as f ) as fc
        '''

        s = '''
        select row_to_json(fc)   
                from (select 'FeatureCollection' as Type, array_to_json(array_agg(f)) as features   
                from (select 'Feature' as Type,   
                   ST_AsGeoJSON(lg.geom)::json as geometry,   
                   (   
                   select row_to_json(t)   
                   from (select id, nom_ut_sup, geom) t   
                   )   
                   as properties   
                   from g_ut_sup as lg where id=6 ) as f ) as fc
        '''

        s = '''
        SELECT row_to_json(fc)
 FROM ( SELECT 'FeatureCollection' As type, array_to_json(array_agg(f)) As features
 FROM (SELECT 'Feature' As type
    , ST_AsGeoJSON(lg.geom)::json As geometry
    , row_to_json((id, nom_ut_sup)) As properties
   FROM g_ut_sup As lg   ) As f )  As fc;
        '''

        s = '''
SELECT jsonb_build_object(
    'type',     'FeatureCollection',
    'features', jsonb_agg(feature)
)
FROM (
  SELECT jsonb_build_object(
    'type',       'Feature',
    'id',         id,
    'geometry',   ST_AsGeoJSON(geom)::jsonb,
    'properties', to_jsonb(row) - 'id' - 'geom'
  ) AS feature
  FROM (SELECT * FROM g_ut_sup) row) features;
        '''

 #16:40
        s = '''
SELECT jsonb_build_object(
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
  FROM (SELECT id, geom FROM g_ut_sup) inputs) features;
        '''
        
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
  FROM (SELECT id, nombre, geom FROM trian) inputs) features;
        '''
        #R
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
  FROM (SELECT id, nom_ut_sup, geom FROM g_ut_sup
    WHERE trim(nom_ut_sup) = 'Tarija' or trim(nom_ut_sup)='Pando' )
   inputs) features;
        '''

        self.cur.execute(s)

        geo_json = self.cur.fetchone()
        # delete - 1er, penùltimo y último  caracter para visor leaflet
        #geo_json = geo_json[1:-2]
        geo_json = geo_json[0]
        return geo_json


    def get_reci_nal(self):
        #R
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
          FROM (SELECT id, nom_asiento, geom FROM ge_asiento)
           inputs) features;
                '''
            #WHERE trim(nom_ut_sup) = 'Tarija' or trim(nom_ut_sup)='Pando' )

        self.cur.execute(s)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json

    def get_loc(self, dep):
        #R
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
        #WHERE trim(nom_ut_sup) = 'Tarija' or trim(nom_ut_sup)='Pando' )
        print('----------------------------')
        #print(sss)
        print('----------------------------')
        self.cur.execute(sss)

        geo_json = self.cur.fetchone()
        geo_json = geo_json[0]
        return geo_json

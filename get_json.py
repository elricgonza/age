import json
# get for visor

class GetJson:
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_dep(self, dep):
        print('---------------------------get_json')
        print(dep)
        print('---------------------------')
        s = f'select nom_ut_sup, st_asgeojson(geom) from g_ut_sup where id= {dep}'
        #s = "select nom_ut_sup, st_asgeojson(geom) from g_ut_sup where id= %d"
        print(s)
        self.cur.execute(s)
        
        row = self.cur.fetchone()

        geo_json = {
            "type": "Feature",
            "name": row[0],
            "properties": {},
            "geometry": json.loads(row[1])
        }

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

        self.cur.execute(s)

        geo_json = self.cur.fetchone()
        return geo_json


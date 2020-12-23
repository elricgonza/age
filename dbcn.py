''' Conexiones a db's: MsSQL Server y Postgres '''

import pymssql as mss

import sys
import psycopg2 as pg
import psycopg2.extensions
import psycopg2.extras

def get_db_ms():
    #pms = ("192.168.110.1","appgeoh","1234qweAS","bdge")
    pms = ("10.100.107.31","appgeoh","1234qweAS","bdge")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql ok -bdge-")
        return cx
    except:
        print("Error en conexión... -bdge-")


def get_db_pg():
    #ppg = {'host': '192.168.46.216',  \
    ppg = {'host': '192.168.80.220',  \
        'user': 'appgeo', \
        'password': 'appgeo', \
        'port': '5432', \
        'dbname': 'geodb'}
    try:
        cx = pg.connect(**ppg)
        #cx.set_isolation_level(0)  # Avoid transactions, autocommit
        #self.cur = cx.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print("cnx postgres ok -geodb-")
        return cx
    except pg.DatabaseError as e:
        print("Error en conexión... Postgres -geodb-")
        print(e)
        sys.exit()

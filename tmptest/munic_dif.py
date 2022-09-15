# -*- coding: utf-8 -*-

''' Migra a MsSQL Server 2008 '''

import pymssql as mss

import sys
import psycopg2 as pg
import psycopg2.extensions
import psycopg2.extras
import datetime

def get_db_ms():
    #pms = ("localhost","sa","123qweAS","GeografiaElectoral_app")
    pms = ("10.100.15.54","appgeo","1234qweAS","GeografiaElectoral_app")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql ok -app-")
        return cx
    except:
        print("Error en conexión... -app-")


def get_db_pg():
    ppg = {'host': '10.100.15.54',  \
        'user': 'appgeo', \
        'password': 'appgeo', \
        'port': '5432', \
        'dbname': 'bdgeo'}
    try:
        cx = pg.connect(**ppg)
        #cx.set_isolation_level(0)  # Avoid transactions, autocommit
        #self.cur = cx.cursor(cursor_factory=psycopg2.extras.DictCursor)
        print("cnx postgres ok -geodb-")
        return cx
    except pg.DatabaseError as e:
        print("Error en conexión... Postgres -bdgeo-")
        print(e)
        sys.exit()


def get_db_08():
    pms = ("10.100.15.54","appgeo","1234qweAS","GeografiaElectoral_app")
    #pms = ("10.100.15.54","appgeo","1234qweAS","bdge")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql-mig ok ")
        return cx
    except:
        print("Error en conexión... -GeografiaElectoral_mig-")


def migra():
    global cxms
    global cx08
    cxms = get_db_ms()
    cxpg = get_db_pg()

    curms = cxms.cursor()
    curpg = cxpg.cursor()


    # loc
    s = 'delete from municipios_sql'
    curpg.execute(s)
    cxpg.commit()

    s = 'select depsec, provsec, sec, nomsec from sec where depsec <= 9'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    x = datetime.datetime.now()
    print('---MUNIC - Fecha y Hora inicio: = %s' %x)
    for row in rows:
        s = """
        insert into municipios_sql(depsec, provsec, sec, nomsec)
            values (%s, %s, %s, %s)
        """
        curpg.execute(s, (
            row[0], row[1], row[2], row[3]
            ))
        n+= 1

        #if (n % 1000 == 0):
        #    print(n)

    print(n)
    cxpg.commit()

    x = datetime.datetime.now()
    print('---Fecha y Hora End: = %s' %x)

if __name__ == '__main__':
    migra()

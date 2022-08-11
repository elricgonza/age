''' Migra a MsSQL Server 2008 '''

import pymssql as mss

import sys
import psycopg2 as pg
import psycopg2.extensions
import psycopg2.extras

def get_db_ms():
    pms = ("localhost","sa","123qweAS","GeografiaElectoral_app")
    #pms = ("10.100.15.54","appgeo","1234qweAS","bdge")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql ok -bdge-")
        return cx
    except:
        print("Error en conexión... -bdge-")


def get_db_08():
    pms = ("localhost","sa","123qweAS","GeografiaElectoral08")
    #pms = ("10.100.15.54","appgeo","1234qweAS","bdge")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql-08 ok ")
        return cx
    except:
        print("Error en conexión... -GeografiaElectoral08-")


def migra():
    global cxms
    global cx08
    cxms = get_db_ms()
    #cx08 = get_db_08()

    curms = cxms.cursor()
    #cur08 = cx08.cursor()

    ''' 
    s = 'delete from dep'
    cur08.execute(s)
    cur08.commit()
    '''

    s = 'select * from dep'
    curms.execute(s)
    rows = curms.fetchall()
    for row in rows:
        print(row)



if __name__ == '__main__':
    migra()

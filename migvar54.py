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
    #pms = ("10.100.15.54","appgeo","1234qweAS","GeografiaElectoral_app")
    #pms = ("10.100.15.53","sa","123qweAS","GeografiaElectoral_app")
    pms = ("10.100.15.54","sa","123qweAS","work")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql ok -app-")
        return cx
    except:
        print("Error en conexión... -app-")


def get_db_08():
    pms = ("10.100.107.31","sa","Ugle2018two","work")
    #pms = ("10.100.107.31","appgeoh","1234qweAS","GeografiaElectoral_mig")
    #pms = ("10.100.15.54","appgeo","1234qweAS","bdge")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql-mig ok ")
        return cx
    except:
        print("Error en conexión... -GeografiaElectoral_mig-")


def migra_lpcasi():
    global cxms
    global cx08
    cxms = get_db_ms()
    cx08 = get_db_08()

    curms = cxms.cursor()
    cur08 = cx08.cursor()

 
    # LPCASI
    x = datetime.datetime.now()
    print('---LPCASI - Fecha y Hora inicio: = %s' %x)

    s = 'delete from lpcasi'
    curms.execute(s)
    cxms.commit()

    s = 'select * from lpcasi'
    cur08.execute(s)
    rows = cur08.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into lpcasi (mobs, dep, departamento, prov, provincia, 
                    sec, municipio, idloc, asiento, tipocircun, 
                    lat, long, lat2, long2, accion, 
                    obs, daprox, obs1, rev2)
                values (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s)
        """
        curms.execute(s, (
            row[0], row[1], row[2], row[3], row[4], 
            row[5], row[6], row[7], row[8], row[9], 
            row[10], row[11], row[12], row[13], row[14], 
            row[15], row[16], row[17], row[18]))
        n+= 1
        if n % 50 == 0:
            print(n)
    cxms.commit()

    x = datetime.datetime.now()
    print(n)
    print('---END LPCASI Fecha y Hora End: = %s' %x)
 

def migra_lpcreci():
    global cxms
    global cx08
    cxms = get_db_ms()
    cx08 = get_db_08()

    curms = cxms.cursor()
    cur08 = cx08.cursor()

 
    # LPCRECI
    x = datetime.datetime.now()
    print('---LPCRECI - Fecha y Hora inicio: = %s' %x)

    s = 'delete from lpcreci'
    curms.execute(s)
    cxms.commit()

    s = 'select * from lpcreci'
    cur08.execute(s)
    rows = cur08.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into lpcreci (mobs, dep, departamento, prov, provincia, 
                    sec, municipio, idloc, asiento, reci, 
                    recinto, lat, long, lat2, long2, 
                    accion, obs, [obs tse], rev2)
                values (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s)
        """
        curms.execute(s, (
            row[0], row[1], row[2], row[3], row[4], 
            row[5], row[6], row[7], row[8], row[9], 
            row[10], row[11], row[12], row[13], row[14], 
            row[15], row[16], row[17], row[18]))
        n+= 1
        if n % 50 == 0:
            print(n)
    cxms.commit()

    x = datetime.datetime.now()
    print(n)
    print('---END LPCRECI Fecha y Hora End: = %s' %x)


def migra_agisreci():
    global cxms
    global cx08
    cxms = get_db_ms()
    cx08 = get_db_08()

    curms = cxms.cursor()
    cur08 = cx08.cursor()

 
    # AGISRECI
    x = datetime.datetime.now()
    print('---AGISRECI - Fecha y Hora inicio: = %s' %x)

    s = 'delete from agisreci'
    curms.execute(s)
    cxms.commit()

    s = 'select * from agisreci'
    cur08.execute(s)
    rows = cur08.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into agisreci ([OBJECTID *], Nro, dep, NomDep, prov, 
                    NomProv, sec, NombreMuni, idloc, asientoEle, 
                    reci, NombreReci, Dist, NomDist, Zona, 
                    NomZona, MaxMesasRe, Direccion, CircunDist, NombreTipo, 
                    latitud, longitud, idTipoReci, idEstado, Documentos,
                    Observacio, Accion, Control, Aprobacion, RecAprob, 
                    [SHAPE *], created_user, created_date, last_edited_user, last_edited_date,
                    idUrbanoRural)
                values (%s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s,
                    %s)
        """
        curms.execute(s, (
            row[0], row[1], row[2], row[3], row[4], 
            row[5], row[6], row[7], row[8], row[9], 
            row[10], row[11], row[12], row[13], row[14], 
            row[15], row[16], row[17], row[18], row[19],
            row[20], row[21], row[22], row[23], row[24],
            row[25], row[26], row[27], row[28], row[29],
            row[30], row[31], row[32], row[33], row[34],
            row[35]))
        n+= 1
        if n % 100 == 0:
            print(n)
    cxms.commit()

    x = datetime.datetime.now()
    print(n)
    print('---END AGISRECI Fecha y Hora End: = %s' %x)


if __name__ == '__main__':
    migra_lpcasi()
    #migra_lpcreci()
    #migra_agisreci()

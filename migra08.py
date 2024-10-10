# -*- coding: utf-8 -*-

''' Migra a MsSQL Server 2008 
    Previo check inexistencia de triggers  - test 
    no migradas: Circun, clasifGrupo y PAIS
    tested 10 oct/2024
'''

import pymssql as mss

import sys
import psycopg2 as pg
import psycopg2.extensions
import psycopg2.extras
import datetime

def get_db_ms():
    #pms = ("localhost","sa","123qweAS","GeografiaElectoral_app")
    #pms = ("10.100.15.54","appgeo","1234qweAS","GeografiaElectoral_app")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql ok -app-")
        return cx
    except:
        print("Error en conexión... -app-")


def get_db_08():
    pms = ("10.100.107.31","appgeoh","1234qweAS","GeografiaElectoral_mig")
    #pms = ("10.100.15.54","appgeo","1234qweAS","bdge")
    try:
        cx = mss.connect(*pms)
        print("cnx mssql-mig ok ")
        return cx
    except:
        print("Error en conexión... -GeografiaElectoral_mig-")


def migresto():
    # clasif
    x = datetime.datetime.now()
    print('---CLASIF - Fecha y Hora inicio: = %s' %x)
    
    s = 'delete from clasif'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.clasif'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into clasif (idClasif, descripcion, clasifGrupoId, clasifSubGrupo)
                values (%s, %s, %s, %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3] )) 
        n+= 1
        if n % 50 == 0:
            print(n)
    cx08.commit()

    x = datetime.datetime.now()
    print(n)
    print('---END CLASIF Fecha y Hora End: = %s' %x)

    # check si necesario
    '''
    # clasifGrupo
    x = datetime.datetime.now()
    print('---clasifGrupo - Fecha y Hora inicio: = %s' %x)
    
    s = 'delete from clasifGrupo'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.clasifGrupo'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into clasifGrupo (idClasifGrupo, descripcion)
                values (%s, %s)
        """
        cur08.execute(s, (
            row[0], row[1] )) 
        n += 1
        if n % 50 == 0:
            print(n)
    cx08.commit()

    x = datetime.datetime.now()
    print(n)
    print('---END clasifGrupo Fecha y Hora End: = %s' %x)
    '''
 
    # dep
    x = datetime.datetime.now()
    print('---DEP - Fecha y Hora inicio: = %s' %x)

    s = 'delete from dep'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.dep'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into dep (Dep, NomDep, Diputados, DiputadosUninominales, idPais,
                fechaIngreso, fechaAct, usuario, descNivelId)
                values (%s, %s, %s, %s, %s,
                %s, %s, %s, %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3], row[4], 
            row[5], row[6], row[7], row[8] ))
        n+= 1
        if n % 50 == 0:
            print(n)
    cx08.commit()
    x = datetime.datetime.now()
    print('---END DEP - Fecha y Hora End: = %s' %x)


    # prov
    x = datetime.datetime.now()
    print('---PROV - Fecha y Hora inicio: = %s' %x)

    s = 'delete from prov'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.prov'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into prov (DepProv, Prov, NomProv, codprov, 
                fechaIngreso, fechaAct, usuario, descNivelId)
                values (%s, %s, %s, %s, 
                %s, %s, %s, %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3], 
            row[4], row[5], row[6], row[7] ))
        n+= 1
        if n % 50 == 0:
            print(n)
    cx08.commit()
    x = datetime.datetime.now()
    print(n)
    print('---END PROV - Fecha y Hora End: = %s' %x)


    # sec
    x = datetime.datetime.now()
    print('---SEC - Fecha y Hora inicio: = %s' %x)

    s = 'delete from sec'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.sec'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into sec (DepSec, ProvSec, Sec, NumConceSec,  NomSec, 
                CircunSec, CodProv, CodSecc,  
                fechaIngreso, fechaAct, usuario, descNivelId)
                values (%s, %s, %s, %s, %s,
                %s, %s, %s,
                %s, %s, %s, %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3], row[4],
            row[5], row[6], row[7], 
            row[8], row[9], row[10], row[11] ))
        n+= 1
        if n % 100 == 0:
            print(n)
    cx08.commit()
    x = datetime.datetime.now()
    print(n)
    print('---END SEC - Fecha y Hora End: = %s' %x)

    
def migdist():
    # dist
    x = datetime.datetime.now()
    print('---DIST - Fecha y Hora inicio: = %s' %x)

    s = 'delete from dist'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.dist'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into dist (IdLocDist, Dist, CircunDist, NomDist, 
                fechaIngreso, fechaAct, usuario)
                values (%s, %s, %s, %s,
                %s, %s, %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3], 
            row[4], row[5], row[6]))
        n+= 1
        if n % 1000 == 0:
            print(n)
    cx08.commit()
    x = datetime.datetime.now()
    print(n)
    print('---END DIST - Fecha y Hora End: = %s' %x)


def migzona():
    # zona
    x = datetime.datetime.now()
    print('---ZONA - Fecha y Hora inicio: = %s' %x)

    s = 'delete from zona'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.zona'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    for row in rows:
        s = """
            insert into zona (IdLocZona, Zona, NomZona, DistZona, 
                fechaIngreso, fechaAct, usuario)
                values (%s, %s, %s, %s,
                %s, %s, %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3], 
            row[4], row[5], row[6]))
        n+= 1
        if n % 1000 == 0:
            print(n)
    cx08.commit()
    x = datetime.datetime.now()
    print(n)
    print('---END ZONA - Fecha y Hora End: = %s' %x)


def migreci():
    # reci
    s = 'delete from reci'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.reci'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    x = datetime.datetime.now()
    print('---RECI - Fecha y Hora inicio: = %s' %x)
    for row in rows:
        s = """
        insert into reci (IdLocReci, Reci, NomReci, SupReci, ApoyoReci,
            ZonaReci, MaxMesasReci, Direccion, Direccionrecinto, latitud,
            longitud, estado, tipoRecinto, codRue, codRueEdif,
            depend, cantPisos, fechaIngreso, fechaAct, usuario,
            etapa, doc_idA, doc_idAF, nacionId, ambientesDisp,
            doc_idT)
            values (%s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3], row[4], 
            row[5], row[6], row[7], row[8], row[9], 
            row[10], row[11], row[12], row[13], row[14], 
            row[15], row[16], row[17], row[18], row[19], 
            row[20], row[21], row[22], row[23], row[24], 
            row[25]))
        n+= 1
        if (n % 1000 == 0):
            print(n)

    print(n)
    cx08.commit()

    x = datetime.datetime.now()
    print('---END RECI - Fecha y Hora End: = %s' %x)

    
def migloc():
    # loc
    print('---migra LOC---')
    s = 'delete from loc'
    cur08.execute(s)
    cx08.commit()

    s = 'select * from geografiaElectoral_app.dbo.loc'
    curms.execute(s)
    rows = curms.fetchall()

    n = 0
    x = datetime.datetime.now()
    print('---LOC - Fecha y Hora inicio: = %s' %x)
    for row in rows:
        s = """
        insert into loc (IdLoc, DepLoc, ProvLoc, SecLoc, Loc,
            IdCanLoc, NomLoc, PoblacionLoc, PoblacionElecLoc, FechaCensoLoc, 
            TipoLocLoc, fechaBaseLegLoc, CodBaseLegLoc, MarcaLoc, EsCabeceraCanLoc,
            EsCabeceraSecLoc, CodProv, CodSecc, TipoCircun, Circun,
            EstadoMapa, latitud, longitud, estado, circunConsulado,
            etapa, obsUbicacion, obs, fechaIngreso, fechaAct,
            usuario, doc_idA, doc_idRN, doc_idAF, urbanoRural,
            doc_idAT, doc_idRNT)
            values (%s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s,
                %s, %s)
        """
        cur08.execute(s, (
            row[0], row[1], row[2], row[3], row[4], 
            row[5], row[6], row[7], row[8], row[9], 
            row[10], row[11], row[12], row[13], row[14], 
            row[15], row[16], row[17], row[18], row[19], 
            row[20], row[21], row[22], row[23], row[24], 
            row[25], row[26], row[27], row[28], row[29], 
            row[30], row[31], row[32], row[33], row[34], 
            row[35], row[36]))
        n += 1
        if (n % 1000 == 0):
            print(n)

    print(n)
    cx08.commit()

    x = datetime.datetime.now()
    print('---END LOC - Fecha y Hora End: = %s' %x)

if __name__ == '__main__':
    global cxms
    global cx08
    cxms = get_db_ms()
    cx08 = get_db_08()

    curms = cxms.cursor()
    cur08 = cx08.cursor()

    migresto()
    migloc()
    migreci()
    migdist()
    migzona()

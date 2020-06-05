# Operaciones historicoDEP en bbdd -> bdge

import db

c = db.cdb()

class Historicolocloc2:
    id = 0
    fecha = ''
    usSesion = ''
    dirIp = ''
    accion = ''

    anteidloc = 0
    antedeploc = 0
    anteprovloc = 0
    antesecloc = 0
    antenomloc = ""
    antepoblacionloc = 0
    antepoblacionelecloc = 0
    antefechacensoloc = ''
    antetipolocloc = ''
    antefechabaselegloc = ''
    antemarcaloc = ''    
    antelatitud = 0
    antelongitud = 0
    anteestado = 0
    antecircunconsulado = ''

    actuidloc = 0
    actudeploc = 0
    actuprovloc = 0
    actusecloc = 0
    actunomloc = ""
    actupoblacionloc = 0
    actupoblacionelecloc = 0
    actufechacensoloc = ''
    actutipolocloc = ''
    actufechabaselegloc = ''
    actumarcaloc = ''
    actulatitud = 0
    actulongitud = 0
    actuestado = 0
    actucircunconsulado = ''

    anteetapa = 0
    antedocAct = ''
    antefechaDocAct = ''
    anteobsUbicacion = ''
    antedocRspNal = ''
    antefechaRspNal = ''
    anteobs = ''
    antefechaIngreso = ''
    antefechaAct = ''

    actuetapa = 0
    actudocAct = ''
    actufechaDocAct = ''
    actuobsUbicacion = ''
    actudocRspNal = ''
    actufechaRspNal = ''
    actuobs = ''
    actufechaIngreso = ''
    actufechaAct = ''
        
    camposModificados = ''

    def add_historicolocloc2(self, usSesion,dirIp,accion, anteidloc, antedeploc, anteprovloc, \
                    antesecloc, antenomloc, antepoblacionloc, \
                    antepoblacionelecloc, antefechacensoloc, antetipolocloc, \
                    antemarcaloc, antelatitud, antelongitud, \
                    anteestado, antecircunconsulado, \

                    actuidloc, actudeploc, actuprovloc, \
                    actusecloc, actunomloc, actupoblacionloc, \
                    actupoblacionelecloc, actufechacensoloc, actutipolocloc, \
                    actumarcaloc, actulatitud, actulongitud, \
                    actuestado, actucircunconsulado, \
                    
                    anteetapa, antedocAct, antefechaDocAct, \
                    anteobsUbicacion, antedocRspNal, antefechaRspNal, \
                    anteobs, antefechaIngreso, antefechaAct, \

                    actuetapa, actudocAct, actufechaDocAct, \
                    actuobsUbicacion, actudocRspNal, actufechaRspNal, \
                    actuobs, actufechaIngreso, actufechaAct, \

                    camposModificados):

        new_historico = usSesion,dirIp,accion, anteidloc, antedeploc, anteprovloc, antesecloc, 0, \
            0, antenomloc, antepoblacionloc, antepoblacionelecloc, antefechacensoloc, \
            antetipolocloc, '2007-01-01', '', antemarcaloc, '', \
            '', 0, 0, 0, 0, \
            0, antelatitud, antelongitud, anteestado, antecircunconsulado, \
            actuidloc, actudeploc, actuprovloc, actusecloc, 0, \
            0, actunomloc, actupoblacionloc, actupoblacionelecloc, actufechacensoloc, \
            actutipolocloc, '2007-01-01', '', actumarcaloc, '', \
            '', 0, 0, 0, 0, \
            0, actulatitud, actulongitud, actuestado, actucircunconsulado, \
            anteetapa, antedocAct, antefechaDocAct, \
            anteobsUbicacion, antedocRspNal, antefechaRspNal, \
            anteobs, antefechaIngreso, antefechaAct, \
            actuetapa, actudocAct, actufechaDocAct, \
            actuobsUbicacion, actudocRspNal, actufechaRspNal, \
            actuobs, actufechaIngreso, actufechaAct, \
            camposModificados

        s = "insert into historicoLOCLOC2 (fecha,usSesion,dirIp,accion, anteidloc, antedeploc, anteprovloc, antesecloc, anteloc, " + \
            " anteidcanloc, antenomloc, antepoblacionloc, antepoblacionelecloc, antefechacensoloc, " + \
            " antetipolocloc, antefechabaselegloc, antecodbaselegloc, antemarcaloc, anteescabeceracanloc, " + \
            " anteescabecerasecloc, antecodprov, antecodsecc, antetipocircun, antecircun, " + \
            " anteestadomapa, antelatitud, antelongitud, anteestado, antecircunconsulado, " + \
            " actuidloc, actudeploc, actuprovloc, actusecloc, actuloc, " + \
            " actuidcanloc, actunomloc, actupoblacionloc, actupoblacionelecloc, actufechacensoloc, " + \
            " actutipolocloc, actufechabaselegloc, actucodbaselegloc, actumarcaloc, actuescabeceracanloc, " + \
            " actuescabecerasecloc, actucodprov, actucodsecc, actutipocircun, actucircun, " + \
            " actuestadomapa, actulatitud, actulongitud, actuestado, actucircunconsulado, " + \
            " anteetapa, antedocAct, antefechaDocAct, anteobsUbicacion, antedocRspNal, antefechaRspNal,anteobs, antefechaIngreso, antefechaAct, " + \
            " actuetapa, actudocAct, actufechaDocAct, actuobsUbicacion, actudocRspNal, actufechaRspNal,actuobs, actufechaIngreso, actufechaAct, " + \
            " camposModificados) VALUES " + \
            " (GETDATE(),%s, %s, %s,  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,  %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s,%s, %s) "
        try:
            c.sql2(s, new_historico)
            c.cnx.commit()
            print(" historicoLOC-LOC2 adicionado...")
        except:
            print("Error - actualización de historicoLOC-LOC2...")










    




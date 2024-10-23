# Importa datos Excel -> Tabla

import openpyxl
from flask import Flask, flash
import datetime as dt

class Importa:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def importa_dist(self, excel_file, table_name, dep, usr):
        # 1ro elimina dist de departamento
        del_query = f'''
            DELETE FROM [GeografiaElectoral_app].[dbo].[{table_name}] WHERE IdLocDist
            IN (SELECT IdLoc from [GeografiaElectoral_app].[dbo].[LOC] 
                WHERE DepLoc = {dep})
        '''
        self.cur.execute(del_query)

        # importa
        n = 0
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active     #Seleccionar la hoja activa
        fecha = dt.datetime.now()

        for row in sheet.iter_rows(min_row=2, values_only=True): # 2 para omitir el encabezado
            insert_query = f'insert into  [GeografiaElectoral_app].[dbo].[{table_name}] (IdLocDist, Dist, CircunDist, NomDist, fechaIngreso, fechaAct, usuario) ' \
                    ' values (%s, %s, %s, %s, %s, %s, %s) '

            t = row[0], row[1], row[2], row[3], fecha, fecha, usr  # Cambia según el número de columnas 
            try:
                self.cur.execute(insert_query, t)
                n += 1
            except Exception as e:
                flash(e, 'alert-info')
                return False

        # Confirmar cambios y cerrar la conexión
        self.cx.commit()
        self.cur.close()
        msg = f'Proceso concluído, registros importados: {n}'
        flash(msg, 'alert-success')

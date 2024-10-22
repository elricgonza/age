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

        print('-------------------------')
        print(del_query)
        print('-------------excel_file')
        print(excel_file)

        '''
        try:
            self.cur.execute(del_query)
            #self.cx.commit()
            #self.cx.close()
            flash('del-query ok')
        except Exception as e:
            print(e)
            flash('Error al importar a DIST del-reinicio', 'alert-warning')
        '''

        # importa
        n = 0
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active     #Seleccionar la hoja activa
        fecha = dt.datetime.now()

        for row in sheet.iter_rows(min_row=2, values_only=True): # 2 para omitir el encabezado
            insert_query = f'''
                INSERT INTO [GeografiaElectoral_app].[dbo].[{table_name}] (IdLocDist, Dist, CircunDist, NomDist, fechaIngreso, fechaAct, usuario)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            #test
            insert_query = f'''
                INSERT INTO [GeografiaElectoral_app].[dbo].[{table_name}] (IdLocDist, Dist, CircunDist, NomDist, fechaIngreso, fechaAct, usuario)
                VALUES ({row[0]}, {row[1]}, {row[2]}, '{row[3]}', '{fecha}', '{fecha}', '{usr}')
            '''
            print('=========================')
            print(insert_query)
            values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # Cambia según el número de columnas --ok
            #values = tuple(row)
            print('/////')
            print(values)
            #try:
            #self.cur.execute(insert_query, values)
            self.cur.execute(insert_query)
            #except Exception as e:
            #    print('Error - Importa Dist')
            #    print(e)
            n += 1


        self.cx.commit()
        self.cur.close()

        flash('okkk', 'alert-success')
        # Confirmar cambios y cerrar la conexión
        '''
        try:
            self.cx.commit()
            self.cur.close()
            self.cx.close()
            msg = f'Proceso concluído, registros importados: {n}'
            flash(msg, 'alert-success')
            return True
        except Exception as e:
            print('Error - Importa Dist, commit')
            print(e)
            flash('Error al importar a DIST', 'alert-warning')
            return False
        '''

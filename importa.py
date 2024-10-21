# Importa datos Excel -> Tablas

import openpyxl
from flask import Flask, flash

class Importa:

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def importa_dist(self, excel_file, table_name, dep):
        # 1ro elimina dist de departamento
        del_query = '''
            DELETE FROM {table_name} WHERE IdLocDist
            IN (SELECT IdLoc from [GeografiaElectoral_app].[dbo].[LOC] 
                WHERE DepLoc = {dep})
        '''
        try:
            self.cur.execute(del_query)
            self.cx.commit()
            self.cx.close()
        except Exception as e:
            print(e)
            flash('Error al importar a DIST reinicio', 'alert-warning')

        # importa
        n = 0
        workbook = openpyxl.load_workbook(excel_file)
        sheet = workbook.active     #Seleccionar la hoja activa

        for row in sheet.iter.rows(min_row=2, values_only=True): # 2 para omitir el encabezado
            insert_query = f'''
                INSERT INTO {table_name} (IdLocDist, Dist, CircunDist, NomDist, fechaIngreso, fechaAct, usuario)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            '''
            #values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])  # Cambia según el número de columnas --ok
            values = tuple(row)
            try:
                self.cur.execute(insert_query, values)
            except Exception as e:
                print('Error - Importa Dist')
                print(e)
            n += 1

        # Confirmar cambios y cerrar la conexión
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

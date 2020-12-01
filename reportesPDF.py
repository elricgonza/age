# Reportes asientos
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.platypus import Table,TableStyle,Frame,Paragraph,Spacer
from reportlab.lib.units import cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
class ReportesPDF:
    
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def reporte_consulta(self, usrdep, dpto, prov, muni, cir1, cir2, cir3, estado, inicio, final): 
            nombreArchivo = "reporte.pdf"
            tituloDocumento = "Reportes OEP"
            titulo = "Reporte General de Asientos"
            subTitulo = "OEP"
            lineTexto = []
            flow_obj=[]
    
            pdf = SimpleDocTemplate(
                nombreArchivo,
                pagesize=letter
            )       
            s = "select IdLoc, NomDep as Departamento, NomProv as Provincia, NombreMunicipio as Municipio, "  + \
                "AsientoElectoral as Asiento, NombreTipoLocLoc as Tipo_Circun," + \
                "CASE WHEN estado = 1 THEN 'Habilitado TED' " + \
                    "WHEN estado = 2 THEN 'Rehabilitado TED' " + \
                    "WHEN estado = 3 THEN 'Suspendido TED' " + \
                    "WHEN estado = 4 THEN 'Suprimido TED' " + \
                    "WHEN estado = 101 THEN 'Habilitado TSE' " + \
                    "WHEN estado = 102 THEN 'Rehabilitado TSE' " + \
                    "WHEN estado = 103 THEN 'Suspendido TSE' " + \
                    "WHEN estado = 104 THEN 'Suprimido TSE' " + \
                "ELSE 'oother'  END as Estado" + \
                    " from [bdge].[dbo].[GeoAsientos_Nacional_all]"
            if dpto != "":
                if prov != "":
                    if muni != "":
                        if cir1 == '1' and cir2 == '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 == '1' and cir2 == '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir2
                                    self.cur.execute(s, consulta)
                        if cir1 == '1' and cir2 != '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 == '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 == '1' and cir2 != '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir1
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 == '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir2
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 != '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d and (TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 != '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, muni, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and Sec = %d" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, muni
                                    self.cur.execute(s, consulta)
                    else:
                        if cir1 == '1' and cir2 == '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 == '1' and cir2 == '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir2
                                    self.cur.execute(s, consulta)
                        if cir1 == '1' and cir2 != '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, cir1, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 == '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir2, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, cir2, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir2, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, cir2, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 == '1' and cir2 != '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir1, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, cir1
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 == '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir2, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, cir2, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir2, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, cir2
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 != '2' and cir3 == '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir3, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, cir3, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, cir3, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d and (TipoLocLoc = %d)" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov, cir3
                                    self.cur.execute(s, consulta)
                        if cir1 != '1' and cir2 != '2' and cir3 != '3':
                            if estado != "":
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d" + \
                                            " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, estado, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d" + \
                                            " and estado = %d order by PROV, SEC"
                                    consulta = dpto, prov, estado
                                    self.cur.execute(s, consulta)
                            else:
                                if inicio != "" and final != "":
                                    s = s + " where Dep = %d and Prov = %d" + \
                                            " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                    consulta = dpto, prov, inicio, final
                                    self.cur.execute(s, consulta)
                                else:
                                    s = s + " where Dep = %d and Prov = %d" + \
                                            " order by PROV, SEC"
                                    consulta = dpto, prov
                                    self.cur.execute(s, consulta)
                else:
                    if cir1 == '1' and cir2 == '2' and cir3 == '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, cir2, cir3, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, cir1, cir2, cir3, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, cir2, cir3, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " order by PROV, SEC"
                                consulta = dpto, cir1, cir2, cir3
                                self.cur.execute(s, consulta)
                    if cir1 == '1' and cir2 == '2' and cir3 != '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, cir2, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, cir1, cir2, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, cir2, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " order by PROV, SEC"
                                consulta = dpto, cir1, cir2
                                self.cur.execute(s, consulta)
                    if cir1 == '1' and cir2 != '2' and cir3 == '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, cir3, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, cir1, cir3, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, cir3, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " order by PROV, SEC"
                                consulta = dpto, cir1, cir3
                                self.cur.execute(s, consulta)
                    if cir1 != '1' and cir2 == '2' and cir3 == '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir2, cir3, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, cir2, cir3, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir2, cir3, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                        " order by PROV, SEC"
                                consulta = dpto, cir2, cir3
                                self.cur.execute(s, consulta)
                    if cir1 == '1' and cir2 != '2' and cir3 != '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, cir1, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir1, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " order by PROV, SEC"
                                consulta = dpto, cir1
                                self.cur.execute(s, consulta)
                    if cir1 != '1' and cir2 == '2' and cir3 != '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir2, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, cir2, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir2, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " order by PROV, SEC"
                                consulta = dpto, cir2
                                self.cur.execute(s, consulta)
                    if cir1 != '1' and cir2 != '2' and cir3 == '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir3, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, cir3, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, cir3, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d and (TipoLocLoc = %d)" + \
                                        " order by PROV, SEC"
                                consulta = dpto, cir3
                                self.cur.execute(s, consulta)
                    if cir1 != '1' and cir2 != '2' and cir3 != '3':
                        if estado != "":
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d" + \
                                        " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, estado, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d" + \
                                        " and estado = %d order by PROV, SEC"
                                consulta = dpto, estado
                                self.cur.execute(s, consulta)
                        else:
                            if inicio != "" and final != "":
                                s = s + " where Dep = %d" + \
                                        " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                                consulta = dpto, inicio, final
                                self.cur.execute(s, consulta)
                            else:
                                s = s + " where Dep = %d" + \
                                        " order by PROV, SEC"
                                consulta = dpto
                                self.cur.execute(s, consulta)
            else:
                if cir1 == '1' and cir2 == '2' and cir3 == '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, cir2, cir3, estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d order by PROV, SEC"
                            consulta = cir1, cir2, cir3, estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, cir2, cir3, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " order by PROV, SEC"
                            consulta = cir1, cir2, cir3
                            self.cur.execute(s, consulta)
                if cir1 == '1' and cir2 == '2' and cir3 != '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, cir2, estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d order by PROV, SEC"
                            consulta = cir1, cir2, estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, cir2, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " order by PROV, SEC"
                            consulta = cir1, cir2
                            self.cur.execute(s, consulta)
                if cir1 == '1' and cir2 != '2' and cir3 == '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, cir3, estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d order by PROV, SEC"
                            consulta = cir1, cir3, estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, cir3, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " order by PROV, SEC"
                            consulta = cir1, cir3
                            self.cur.execute(s, consulta)
                if cir1 != '1' and cir2 == '2' and cir3 == '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir2, cir3, estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and estado = %d order by PROV, SEC"
                            consulta = cir2, cir3, estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir2, cir3, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d or TipoLocLoc = %d)" + \
                                    " order by PROV, SEC"
                            consulta = cir2, cir3
                            self.cur.execute(s, consulta)
                if cir1 == '1' and cir2 != '2' and cir3 != '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and estado = %d order by PROV, SEC"
                            consulta = cir1, estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir1, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " order by PROV, SEC"
                            consulta = cir1
                            self.cur.execute(s, consulta)
                if cir1 != '1' and cir2 == '2' and cir3 != '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir2, estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and estado = %d order by PROV, SEC"
                            consulta = cir2, estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir2, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " order by PROV, SEC"
                            consulta = cir2
                            self.cur.execute(s, consulta)
                if cir1 != '1' and cir2 != '2' and cir3 == '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir3, estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and estado = %d order by PROV, SEC"
                            consulta = cir3, estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = cir3, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where (TipoLocLoc = %d)" + \
                                    " order by PROV, SEC"
                            consulta = cir3
                            self.cur.execute(s, consulta)
                if cir1 != '1' and cir2 != '2' and cir3 != '3':
                    if estado != "":
                        if inicio != "" and final != "":
                            s = s + " where estado = %d and Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = estado, inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " where estado = %d order by PROV, SEC"
                            consulta = estado
                            self.cur.execute(s, consulta)
                    else:
                        if inicio != "" and final != "":
                            s = s + " where Convert(CHAR(10),fechaIngreso,23) between %d and %d order by PROV, SEC"
                            consulta = inicio, final
                            self.cur.execute(s, consulta)
                        else:
                            s = s + " order by PROV, SEC"
                            self.cur.execute(s)

            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                pdf = canvas.Canvas(nombreArchivo)
                pdf.setTitle(tituloDocumento)
                data_row = rows
                count=len(data_row)
                print(count)
                if count > 55:
                    num=int(count/45)
                else:
                    num=int(60/45)
                a=int(count/num)
                count_new=[0]
                x=0
                while(x+a<count):
                    x=x+a
                    count_new.append(x)
                #frame1=Frame(10,40,360,280,showBoundary=1)
                #styles=getSampleStyleSheet()
                #text=""" This is the database report for pagination <b></b>,<br></br>"""
                #t1=Paragraph(text,style=styles["Normal"])
                #flow_obj.append(t1)
                #flow_obj.append(Spacer(6,6))
                #text=""" data generated at: """ + str(datetime.datetime.now())
                #t2=Paragraph(text,style=styles["Normal"])
                #flow_obj.append(t2)
                #frame1.addFromList(flow_obj, pdf)
                #pdf.showPage()
                pdfmetrics.registerFont(
                    TTFont('abc', 'static/fonts/SakBunderan.ttf')
                )
                """pdf.setFont('abc', 16)
                pdf.drawCentredString(300, 770, titulo)
                pdf.showPage()"""
                #looping for pagination
                for j in range(len(count_new)):
                    frame=Frame(20,30,550,780,showBoundary=1)
                    pdf.setFont('abc', 12)
                    pdf.drawString(200, 790, "Reporte General de Asientos")
                    pdf.drawString(40, 770, "Fecha del Reporte.: "+ str(datetime.datetime.now()))           
                    flow_obj.append(Spacer(0,30))
                    data1=[["IdLoc","Departamento","Provincia", "Municipio", "Asiento", "Tipo_Circun", "Estado"]]
                    if(j==len(count_new)-1):
                        for row in data_row[count_new[j]:]:
                            data1.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                        table=Table(data1,colWidths=[30,60,60,120,120,60,60],rowHeights=[15 for i in range(len(data1))]) 
                        ts=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                       ("BACKGROUND",(0,0),(-1,0),colors.yellow),
                                       ("BACKGROUND",(0,1),(-1,-1),colors.ghostwhite),
                                       ("SIZE",(0,0),(-1,-1),6,colors.yellow),
                                       ("ALIGN",(0,0),(-1,-1),"LEFT")])
                        table.setStyle(ts)
                        flow_obj.append(Spacer(8,8))
                        flow_obj.append(table)
                        frame.addFromList(flow_obj, pdf)
                        pdf.showPage()    
                    else:       
                        for row in data_row[count_new[j]:count_new[j+1]]:                            
                         data1.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                        table=Table(data1,colWidths=[30,60,60,120,120,60,60],rowHeights=[15 for i in range(len(data1))]) 
                        ts=TableStyle([("GRID",(0,0),(-1,-1),1,colors.black),
                                       ("BACKGROUND",(0,0),(-1,0),colors.yellow),
                                       ("BACKGROUND",(0,1),(-1,-1),colors.ghostwhite),
                                       ("SIZE",(0,0),(-1,-1),6,colors.yellow),
                                       ("ALIGN",(0,0),(-1,-1),"LEFT")])
                        table.setStyle(ts)
                        flow_obj.append(Spacer(8,8))
                        flow_obj.append(table)
                        
                        frame.addFromList(flow_obj, pdf)
                        pdf.showPage()
                pdf.save()
                return rows

            #https://github.com/youtubetotaltechnology/source/blob/master/reportlab_tutorial_57.py
            #https://decodigo.com/python-crear-pdf-reportlab
            #https://medium.com/@saijalshakya/generating-pdf-with-reportlab-in-django-ee0235c2f133
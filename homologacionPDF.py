# Reportes asientos
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter,landscape, A4
from reportlab.platypus import TableStyle
from reportlab.lib import colors
from reportlab.platypus import Table,TableStyle,Frame,Paragraph,Spacer
from reportlab.lib.units import cm, mm, inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.colors import black, purple, white
import datetime
from arrow import utcnow, get
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
class HomologacionPDF:
    
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def reporte_consulta_h(self, usrdep, inicio, final): 
            nombreArchivo = "reporteh.pdf"
            tituloDocumento = "Reportes OEP"
            titulo = "Reporte General de Homologaciones"
            subTitulo = "OEP"
            lineTexto = []
            flow_obj=[]
    
            pdf = SimpleDocTemplate(
                nombreArchivo,
                pagesize=A4
            )       
            s = "select idLoc, reci, nomDep, nomLoc, nomReci, latitud, longitud, idLoc2, reci2, nomDep2, nomLoc2, nomReci2, latitud2, longitud2" + \
                " from [bdge].[dbo].[hom]"
            if usrdep != 0:
                consulta = usrdep, inicio, final
                s = s + " where dep = %d and Convert(CHAR(10),fechaAct,23) between %d and %d order by id"
                self.cur.execute(s, consulta)
            else:
                consulta = inicio, final
                s = s + " where Convert(CHAR(10),fechaAct,23) between %d and %d order by id"
                self.cur.execute(s, consulta)

            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                pdf = canvas.Canvas(nombreArchivo, pagesize=landscape(A4))
                pdf.setTitle(tituloDocumento)
                data_row = rows
                count=len(data_row)
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

                pdfmetrics.registerFont(
                    TTFont('abc', 'static/fonts/SakBunderan.ttf')
                )
                for j in range(len(count_new)):
                    frame=Frame(30,30,800,550,showBoundary=1)
                    pdf.setFont('abc', 12)
                    pdf.drawString(330, 550, "Reporte General de Homologaciones")
                    fecha = utcnow().to("local").format("dddd, DD - MMMM - YYYY", locale="es")
                    fechaReporte = fecha.replace("-", "de")
                    pdf.drawString(35, 565, "Fecha del Reporte.: "+ fechaReporte)           
                    flow_obj.append(Spacer(0,30))
                    data1=[["IdLoc","Reci","Departamento", "Asiento", "Recinto", "Latitud", "Longitud", "IdLoc2","Reci2","Departamento2", "Asiento2", "Recinto2", "Latitud2", "Longitud2"]]
                    if(j==len(count_new)-1):
                        for row in data_row[count_new[j]:]:
                            data1.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]])
                        table=Table(data1,colWidths=[30,30,50,100,100,40,40,30,30,50,100,100,40,40],rowHeights=[15 for i in range(len(data1))]) 
                        ts=TableStyle([
                                ("BACKGROUND", (0, 0),(-1, 0), purple),
                                ("SIZE",(0,0),(-1,-1),6,colors.purple),
                                ("ALIGN", (0, 0),(0, -1), "LEFT"),
                                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), # Texto centrado y alineado a la izquierda
                                ("INNERGRID", (0, 0), (-1, -1), 0.50, black), # Lineas internas
                                ("BOX", (0, 0), (-1, -1), 0.25, black), # Linea (Marco) externa
                                ])
                        table.setStyle(ts)
                        flow_obj.append(Spacer(8,8))
                        flow_obj.append(table)
                        frame.addFromList(flow_obj, pdf)
                        pdf.showPage()    
                    else:       
                        for row in data_row[count_new[j]:count_new[j+1]]:                            
                         data1.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]])
                        table=Table(data1,colWidths=[30,30,50,100,100,40,40,30,30,50,100,100,40,40],rowHeights=[15 for i in range(len(data1))]) 
                        ts=TableStyle([
                                ("BACKGROUND", (0, 0),(-1, 0), purple),
                                ("SIZE",(0,0),(-1,-1),6,colors.purple),
                                ("ALIGN", (0, 0),(0, -1), "LEFT"),
                                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), # Texto centrado y alineado a la izquierda
                                ("INNERGRID", (0, 0), (-1, -1), 0.50, black), # Lineas internas
                                ("BOX", (0, 0), (-1, -1), 0.25, black), # Linea (Marco) externa
                                ])
                        table.setStyle(ts)
                        flow_obj.append(Spacer(8,8))
                        flow_obj.append(table)
                        frame.addFromList(flow_obj, pdf)
                        pdf.showPage()
                pdf.save()
                return rows
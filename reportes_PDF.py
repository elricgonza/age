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
class Reportes_PDF:
    
    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def reporte_consulta(self, usrdep): 
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
            if usrdep != 0 :
                print(usrdep)
                s = s + " where DEP = %d order by PROV, SEC"
                print(s)
                self.cur.execute(s, usrdep)
            else:
                s = s + " order by DEP, PROV, SEC"
                print(s)
                self.cur.execute(s)

            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                pdf = canvas.Canvas(nombreArchivo)
                pdf.setTitle(tituloDocumento)

                data_row = rows
                count=len(data_row)
                num=int(count/45)
                a=int(count/num)
                count_new=[0]
                x=0
                while(x+a<count):
                    x=x+a
                    count_new.append(x)
                #frame1=Frame(10,40,360,280,showBoundary=1)
                #styles=getSampleStyleSheet()
                #text="""
                #This is the database report for pagination <b></b>,<br></br>"""
                #t1=Paragraph(text,style=styles["Normal"])
                #flow_obj.append(t1)
                #flow_obj.append(Spacer(6,6))
                #text="""
                #data generated at: """ + str(datetime.datetime.now())
                #t2=Paragraph(text,style=styles["Normal"])
                #flow_obj.append(t2)
                #frame1.addFromList(flow_obj, pdf)
                #pdf.showPage()
                pdfmetrics.registerFont(
                    TTFont('abc', 'static/fonts/SakBunderan.ttf')
                )
                pdf.setFont('abc', 16)
                pdf.drawCentredString(300, 770, titulo)
                pdf.showPage()
                #looping for pagination
                for j in range(len(count_new)):
                    frame=Frame(10,40,560,780,showBoundary=1)
                    data1=[["IdLoc","Departamento","Provincia", "Municipio", "Asiento", "Tipo_Circun", "Estado"]]
                    if(j==len(count_new)-1):
                        for row in data_row[count_new[j]:]:
                            data1.append([row[0],row[1],row[2],row[3],row[4],row[5],row[6]])
                        table=Table(data1,colWidths=[30,50,50,120,120,40,50],rowHeights=[15 for i in range(len(data1))]) 
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
                        table=Table(data1,colWidths=[30,50,50,120,120,40,50],rowHeights=[15 for i in range(len(data1))]) 
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
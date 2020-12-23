# Operaciones usuarios

class Pais:
    IdPais = 0
    Pais = ''
    NomPais = ''
    Nacionalidad = ''
    Estado = 0
    CodigoInternacional = ''
    CodigoInternacionalISO3166 = 0
    fechaIngreso = ''
    fechaAct = ''
    usuario = ''

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_paises_all(self, usrdep):
            s = "select IdPais, Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166, fechaIngreso, fechaAct, usuario " + \
                " from [GeografiaElectoral_app].[dbo].[PAIS] order by Pais"
            self.cur.execute(s)
            rows = self.cur.fetchall()
            if self.cur.rowcount == 0:
                return False
            else:
                return rows

    def get_pais_idpais(self, idpais):
        s = "select IdPais, Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166, fechaIngreso, fechaAct, usuario" + \
            " from [GeografiaElectoral_app].[dbo].[PAIS] where IdPais = %d"
        self.cur.execute(s, idpais)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.idpais = row[0]
            self.pais = row[1]
            self.nompais = row[2]
            self.nacionalidad = row[3]
            self.estado = row[4]
            self.codigointer = row[5]
            self.codigointerISO = row[6]
            self.fechaingreso = row[7]
            self.fechaactual = row[8]
            self.usuario = row[9]
            return True

    def add_pais(self, idpais, pais, nompais, nal, estado, codinter, codinteriso3166, fecharegistro, fechaactual, usuario):
        new_pais = idpais, pais, nompais, nal, estado, codinter, codinteriso3166, fecharegistro, fechaactual, usuario
        s = "insert into GeografiaElectoral_app.dbo.pais (IdPais, Pais, NomPais, Nacionalidad, Estado, CodigoInternacional, CodigoInternacionalISO3166, fechaIngreso, fechaAct, usuario) values " + \
            " (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        self.cur.execute(s, new_pais)
        self.cx.commit()
        print("adicionado...")

    def upd_pais(self, idpais, pais, nompais, nal, estado, codinter, codinteriso3166, fecharegistro, fechaactual, usuario):
        new_pais = pais, nompais, nal, estado, codinter, codinteriso3166, fechaactual, usuario, idpais
        s = "update [GeografiaElectoral_app].[dbo].[PAIS]" + \
            " set Pais= %s, NomPais= %s, Nacionalidad= %s, Estado= %s, CodigoInternacional= %s, " + \
            " CodigoInternacionalISO3166= %s, fechaAct= %s, usuario= %s " + \
            " where [GeografiaElectoral_app].[dbo].[PAIS].IdPais = %d"
        try:
            self.cur.execute(s, new_pais)
            self.cx.commit()
            print('Pais actualizado')
        except Exception as e:
            print("Error - actualización de Pais")
            print(e)

    def get_next_idpais(self):
        self.cur.execute("select max(IdPais) + 1 from GeografiaElectoral_app.dbo.pais")
        row = self.cur.fetchone()
        return row[0]

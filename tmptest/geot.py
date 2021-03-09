import geo
import dbcn

cxms = dbcn.get_db_ms()
cxpg = dbcn.get_db_pg()

g = geo.LatLong(cxpg)

lat = -15.2673 #-16.5001
long = -69.0427 # -68.2147

if g.get_geo(lat, long):
    print(g.departamento.strip() + ' - ' + g.provincia + ' - ' + g.municipio)
else:
    print("not foundd...")

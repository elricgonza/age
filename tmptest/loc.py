import sys

sys.path.insert(0, '/var/www/flasks/age/')

import recintos as reci
import dbcn

cxms = dbcn.get_db_ms()
cxpg = dbcn.get_db_pg()

r = reci.Recintos(cxms);
row = r.get_recinto_idreci(205,729)
print(row)

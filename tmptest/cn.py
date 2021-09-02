import sys

sys.path.insert(0, '/var/www/flasks/age_vstwo/')

import dbcn

cxms = dbcn.get_db_ms()
#cxpg = dbcn.get_db_pg()

if cxms:
    print(cxms)
else:
    print('errrrrr')

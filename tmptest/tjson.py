import sys

sys.path.insert(0, '/var/www/flasks/age/')

import get_json
import dbcn

cxms = dbcn.get_db_ms()
cxpg = dbcn.get_db_pg()

j = get_json.GetJson(cxpg);

r = j.get_reci_mts(-16.5282, -68.1691, 650)
print(r)


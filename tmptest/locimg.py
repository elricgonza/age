import sys

sys.path.insert(0, '/var/www/flasks/age/')

import loc_img
import dbcn

cxms = dbcn.get_db_ms()
cxpg = dbcn.get_db_pg()

li = loc_img.LocImg(cxms);

if (li.get_name_file_img(97, 9)):
    print('verd')
    print(li.get_name_file_img(97, 9))
    print(li._nro_rows)
else:
    print('fals')
    print(li.get_name_file_img(97, 9))
    print(li._nro_rows)


print('----2da v--------')

if (li.get_name_file_img(97, 2)):
    print('verd')
    print(li.get_name_file_img(97, 2))
    print(li._nro_rows)
else:
    print('fals')
    print(li.get_name_file_img(97, 2))
    print(li._nro_rows)


import loc_img
import dbcn

cxms = dbcn.get_db_ms()
cxpg = dbcn.get_db_pg()

li = loc_img.LocImg(cxms)

print (li.del_loc_img(1114, 3))

# Operaciones - categoria y subcategoria - asiento (loc)
#import dbg
from flask import Flask, render_template, request, redirect, url_for, session, jsonify, flash
class LocCate:
    loc_id = 0
    cate_id = 0
    subcate_id = 0
    obs = ''
    fechaAct = ''
    usuario = ''
    fechaIngreso = ''

    _nro_rows = 0

    def __init__(self, cx):
        self.cx = cx
        self.cur = cx.cursor()

    def get_loc_cates(self, idLoc):
        s = "select lc.loc_id, c.idClasifGrupo, c.descripcion as categoria, sc.idClasif, sc.descripcion as subcategoria, lc.obs," + \
            " lc.fechaAct, lc.usuario, lc.fechaIngreso, lc.id" + \
            " from loc_cate lc" + \
            " inner join GeografiaElectoral_app.dbo.clasifGrupo c on lc.cate_id=c.idClasifGrupo" + \
            " inner join GeografiaElectoral_app.dbo.clasif sc on lc.subcate_id=sc.idClasif" + \
            " where lc.loc_id=%d order by lc.id"
        try:
            self.cur.execute(s, idLoc)
            rows = self.cur.fetchall()
            self._nro_rows = self.cur.rowcount  # 0 not found
            return rows

        except Exception as e:
            print ('Error en método  -get_loc_imgs- ')
            print (e)

    def get_categorias_all(self):
        s = "select * from [GeografiaElectoral_app].[dbo].[clasifGrupo] where idClasifGrupo in (10, 11, 12, 13)"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_subcategorias_all(self, cate_id):
        s = "select idClasif, descripcion as subcategoria, clasifGrupoId from [GeografiaElectoral_app].[dbo].[clasif] where clasifGrupoId = %d"
        self.cur.execute(s, cate_id)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_subcategorias_all1(self):
        s = "select idClasif, descripcion as subcategoria, clasifGrupoId from [GeografiaElectoral_app].[dbo].[clasif]"
        self.cur.execute(s)
        rows = self.cur.fetchall()
        if self.cur.rowcount == 0:
            return False
        else:
            return rows

    def get_loc_cates_id(self, idloc, sec):
        s = "select id from loc_cate where loc_id = %d and id = %d"
        ids = idloc, sec
        self.cur.execute(s, ids)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.sec = row[0]            
            return True

    def get_loc_cates_idloc(self, idloc):
        s = "select cate_id, subcate_id, obs, usuario from loc_cate where loc_id = %d"
        self.cur.execute(s, idloc)
        row = self.cur.fetchone()
        if  row == None:
            return False
        else:
            self.cate_id = row[0]
            self.subcate_id = row[1]
            self.obs = row[2]
            self.usuario = row[3]
            return True

    def add_loc_cate(self, loc_id, cate_id, subcate_id, obs, fechaAct, usuario, fechaIngreso, nextid):
        new_locCate = loc_id, cate_id, subcate_id, obs, fechaAct, usuario, fechaIngreso, nextid
        s = "insert into loc_cate (loc_id, cate_id, subcate_id, obs, fechaAct, usuario, fechaIngreso, id) values" + \
            " (%s, %s, %s, %s, %s, %s, %s, %s) "
        try:
            self.cur.execute(s, new_locCate)
            self.cx.commit()
            flash("Se ha insertado el Registro", 'alert-success')
        except:
            flash("Error al insertar Registro", 'alert-warning')            

    def upd_loc_cate(self, indicador):
        if self.diff_old_new_indi(indicador):
            s = "update loc_cate set cate_id = %d, subcate_id = %d, obs = %s, fechaAct = %s, usuario = %s" + \
            " where loc_id = %d and id = %d"
            try:
                self.cur.execute(s, indicador)
                self.cx.commit()
                flash("Se ha Modificado el Registro", 'alert-success')
            except Exception as e:
                flash("Error al modificar Registro", 'alert-warning')


    def diff_old_new_indi(self, row_to_upd):
        indi = self.get_loc_cates_idloc(row_to_upd[5])  #5 -> idloc

        vdif = False

        if self.cate_id != int(row_to_upd[0]):
            print('cate_id dif')
            print(self.cate_id)
            print(row_to_upd[0])
            vdif = True
        if self.subcate_id != int(row_to_upd[1]):
            print('subcate_id dif')
            vdif = True
        if self.obs != row_to_upd[2]:
            print('obs dif')
            print(self.obs)
            print(row_to_upd[2])
            vdif = True
        if (self.usuario != row_to_upd[4]):
            print('usuario dif')
            vdif = True

        return vdif


    # borra registros en base al 'loc_id'
    def del_loc_cate(self, loc_id, sec):
        s = "delete from loc_cate where loc_id = %d and id = %d"
        del_locCate = loc_id, sec
        try:
            self.cur.execute(s, del_locCate)
            self.cx.commit()
            flash("Se ha Eliminado el Registro", 'alert-success')
        except:
            flash("Error al eliminar Registro", 'alert-warning')    

    def get_next_idloccate(self, idloc):
        self.cur.execute("select max(id) + 1 from bdge.dbo.loc_cate where loc_id = %s", idloc)
        row = self.cur.fetchone()
        if row == (None,):
           return 1
        else:
           return row[0]

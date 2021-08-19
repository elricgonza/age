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

    def upd_loc_cate(self, loc_id, cate_id, subcate_id, obs, fechaAct, usuario, sec):        
        upd_locCate = (cate_id, subcate_id, obs, fechaAct, usuario, loc_id, sec)        
        s = "update loc_cate set cate_id = %d, subcate_id = %d, obs = %s, fechaAct = %s, usuario = %s" + \
            " where loc_id = %d and id = %d"
        try:
            self.cur.execute(s, upd_locCate)
            self.cx.commit()
            flash("Se ha Modificado el Registro", 'alert-success')
        except:
            flash("Error al modificar Registro", 'alert-warning')
       
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

from model.actividad_clave import actividad_clave
from .sqlserver import SQLServerController

class actividad_claveController():
    def __init__(self):
        self.sqlserver = SQLServerController()

    def createActividadClave(self, nombre, descripcion, fecha_fin, id_evaluacion, id_objetivo, id_usuario, id_plan, id_accion):
        sql = '''SELECT MAX(ID_ACTIVIDAD)+1 FROM ACTIVIDAD_CLAVE'''
        id_actividad = self.sqlserver.selectn(sql)[0][0]
        if id_actividad is None:
            id_actividad = 1

        Actividad_clave = actividad_clave(id_actividad = id_actividad, nombre = nombre, descripcion = descripcion, fecha_fin = fecha_fin, id_evaluacion = id_evaluacion, id_objetivo = id_objetivo, id_usuario = id_usuario, id_plan =id_plan, id_accion = id_accion)
        sql = '''INSERT INTO ACTIVIDAD_CLAVE (ID_ACTIVIDAD, nombre, descripcion, fecha_fin, id_evaluacion, id_objetivo, id_usuario, id_plan, id_accion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        val = (Actividad_clave.id_actividad, Actividad_clave.nombre, Actividad_clave.descripcion, Actividad_clave.fecha_fin, Actividad_clave.id_evaluacion, Actividad_clave.id_objetivo, Actividad_clave.id_usuario, Actividad_clave.id_plan, Actividad_clave.id_accion)
        print(val)
        self.sqlserver.insert(sql, val)


    def updateActividadClave(self, id_actividad, nombre, descripcion, fecha_fin, id_evaluacion, id_objetivo, id_usuario, id_plan, id_accion):
        sql = '''UPDATE ACTIVIDAD_CLAVE
                SET NOMBRE = ?, DESCRIPCION = ?, FECHA_FIN = ?, ID_EVALUACION = ?, ID_OBJETIVO = ?, ID_USUARIO = ?, ID_PLAN = ?, ID_ACCION = ?
                WHERE ID_ACTIVIDAD = ?'''
        val = ( nombre, descripcion, fecha_fin, id_evaluacion, id_objetivo, id_usuario, id_plan, id_accion, id_actividad)
        self.sqlserver.insert(sql, val)

    def getActividadClaveObjetivo(self, id_objetivo):
        sql = '''SELECT ID_actividad, NOMBRE FROM actividad_clave
                WHERE ID_objetivo = ?'''
        val = (id_objetivo)
        return self.sqlserver.select(sql, val)

    def getActividadClave(self, id_actividad):
        sql = '''SELECT DESCRIPCION 
                FROM ACTIVIDAD_CLAVE
                WHERE ID_ACTIVIDAD = ?'''
        val = (id_actividad)
        return self.sqlserver.select(sql, val)

    def getLastActividadClave(self):
        sql = "SELECT * FROM OBJETIVO WHERE ID_OBJETIVO = (SELECT MAX(ID_OBJETIVO)+ FROM OBJETIVO)"

        return self.sqlserver.selectn(sql)

    def deleteActividadClave(self, id_objetivo):
        sql = '''DELETE FROM OBJETIVO
                WHERE ID_OBJETIVO = ?'''
        val = (id_objetivo)
        self.sqlserver.insert(sql, val)
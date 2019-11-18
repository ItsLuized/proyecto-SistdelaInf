from model.objetivo import Objetivo
from .sqlserver import SQLServerController

class objetivoController():
    def __init__(self):
        self.sqlserver = SQLServerController()

    def createObjetivo(self, nombre, completud_por, id_imperativo):
        sql = '''SELECT MAX(ID_OBJETIVO)+1 FROM OBJETIVO'''
        id_objetivo = self.sqlserver.selectn(sql)[0][0]
        if id_objetivo is None:
            id_objetivo = 1

        objetivo = Objetivo(id_objetivo = id_objetivo, nombre = nombre, completud_por = completud_por, id_imperativo = id_imperativo)
        sql = '''INSERT INTO OBJETIVO (ID_OBJETIVO, NOMBRE, COMPLETUD_POR, ID_IMPERATIVO)
                VALUES (?, ?, ?, ?)'''
        val = (objetivo.id_objetivo, objetivo.nombre, objetivo.completud_por, objetivo.id_imperativo)
        print(val)
        self.sqlserver.insert(sql, val)


    def updateObjetivo(self, nombre, completud_por, id_objetivo):
        sql = '''UPDATE OBJETIVO
                SET NOMBRE = ?, COMPLETUD_POR = ?
                WHERE ID_OBJETIVO = ?'''
        val = (nombre, completud_por, id_objetivo)
        self.sqlserver.insert(sql, val)

    def getObjetivosImperativo(self, id_imperativo):
        sql = '''SELECT ID_OBJETIVO, NOMBRE FROM OBJETIVO
                WHERE ID_IMPERATIVO = ?'''
        val = (id_imperativo)
        return self.sqlserver.select(sql, val)

    def getObjetivo(self, id_objetivo):
        sql = '''SELECT NOMBRE, COMPLETUD_POR 
                FROM OBJETIVO
                WHERE ID_OBJETIVO = ?'''
        val = (id_objetivo)
        return self.sqlserver.select(sql, val)

    def getLastObjetivo(self):
        sql = "SELECT * FROM OBJETIVO WHERE ID_OBJETIVO = (SELECT MAX(ID_OBJETIVO)+ FROM OBJETIVO)"

        return self.sqlserver.selectn(sql)

    def deleteObjetivo(self, id_objetivo):
        sql = '''DELETE FROM OBJETIVO
                WHERE ID_OBJETIVO = ?'''
        val = (id_objetivo)
        self.sqlserver.insert(sql, val)
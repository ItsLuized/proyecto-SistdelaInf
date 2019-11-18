from model.objetivo import objetivo
from .sqlserver import SQLServerController

class imperativoController():
    def __init__(self):
        self.sqlserver = SQLServerController()

    def CreateObjetivo(self, nombre, completud_por, id_imperativo):
        sql = '''SELECT MAX(ID_OBJETIVO)+1 FROM IMPERATIVO'''
        id_objetivo = self.sqlserver.selectn(sql)
        if id_objetivo is None:
            id_objetivo = 1

        Objetivo = objetivo(id_objetivo, nombre, completud_por, id_imperativo)
        sql = '''INSERT INTO OBJETIVO (ID_OBJETIVO, NOMBRE, COMPLETUD_POR, ID_IMPERATIVO)
                VALUES (?, ?, ?, ?)'''
        val = (Objetivo.id_objetivo, Objetivo.nombre, Objetivo.completud_por, Objetivo.id_imperativo)
        print(val)
        self.sqlserver.insert(sql, val)

    def updateObjetivo(self, nombre, completud_por, id_objetivo):
        sql = '''UPDATE OBJETIVO
                SET NOMBRE = ?, COMPLETUD_POR = ?
                WHERE ID_OBJETIVO = ?'''
        val = (nombre, completud_por, id_objetivo)
        self.sqlserver.insert(sql, val)

    def getObjetivos(self):
        sql = '''SELECT ID_OBJETIVO, NOMBRE FROM OBJETIVO'''
        return self.sqlserver.selectn(sql)

    def getObjetivo(self, id_objetivo):
        sql = '''SELECT NOMBRE, COMPLETUD_POR 
                FROM OBJETIVO
                WHERE ID_OBJETIVO = ?'''
        val = (id_objetivo)
        return self.sqlserver.select(sql, val)

    def deleteObjetivo(self, id_objetivo):
        sql = '''DELETE FROM OBJETIVO
                WHERE ID_OBJETIVO = ?'''
        val = (id_objetivo)
        self.sqlserver.insert(sql, val)
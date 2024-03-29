from model.imperativo import Imperativo
from .sqlserver import SQLServerController

class imperativoController():
    def __init__(self):
        self.sqlserver = SQLServerController()

    def CreateImperativo(self,nombre, fecha_inicio, fecha_fin, id_usuario):
        sql = '''SELECT MAX(ID_IMPERATIVO)+1 FROM IMPERATIVO'''
        id_imperativo = self.sqlserver.selectn(sql)[0][0]
        if id_imperativo is None:
            id_imperativo = 1

        imperativo = Imperativo(id_imperativo, nombre, fecha_inicio, fecha_fin, id_usuario)
        sql = '''INSERT INTO IMPERATIVO (ID_IMPERATIVO, NOMBRE, FECHA_INICIO, FECHA_FIN, ID_USUARIO)
                VALUES (?, ?, ?, ?, ?)'''
        val = (imperativo.id_imperativo, imperativo.nombre, imperativo.fecha_inicio, imperativo.fecha_fin, imperativo.id_usuario)
        print(val)
        self.sqlserver.insert(sql, val)

    def updateImperativo(self, id_imperativo, nombre, fecha_inicio, fecha_fin, id_usuario):
        sql = '''UPDATE IMPERATIVO
                SET NOMBRE = ?, FECHA_INICIO = ?, FECHA_FIN = ?, ID_USUARIO = ?
                WHERE ID_IMPERATIVO = ?'''
        val = (nombre, fecha_inicio, fecha_fin, id_usuario, id_imperativo)
        self.sqlserver.insert(sql, val)

    def getImperativos(self):
        sql = '''SELECT ID_IMPERATIVO, I.NOMBRE, U.NOMBRE
                FROM IMPERATIVO I
                INNER JOIN USUARIO U
                ON U.ID_USUARIO = I.ID_USUARIO'''
        return self.sqlserver.selectn(sql)

    def getImperativo(self, id_imperativo):
        sql = '''SELECT ID_IMPERATIVO, NOMBRE, FECHA_INICIO, FECHA_FIN, ID_USUARIO
                FROM IMPERATIVO
                WHERE ID_IMPERATIVO = ?'''
        val = (id_imperativo)
        return self.sqlserver.select(sql, val)

    def deleteImperativo(self, id_imperativo):
        sql = '''DELETE FROM IMPERATIVO
                WHERE ID_IMPERATIVO = ?'''
        val = (id_imperativo)
        self.sqlserver.insert(sql, val)

    def getLastImperativo(self):
        sql = "SELECT * FROM IMPERATIVO WHERE ID_IMPERATIVO = (SELECT MAX(id_imperatibo)+1 FROM imperativo)"

        return self.sqlserver.selectn(sql)
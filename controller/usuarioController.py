from model.usuario import Usuario
from .sqlserver import SQLServerController

class usuarioController():
    def __init__(self):
        self.sqlserver = SQLServerController()


    def createUser(self, nombre, email, contraseña, id_cargo):
        sql = 'SELECT MAX(id_usuario)+1 FROM usuario'
        id_usuario = self.sqlserver.selectn(sql)[0][0]
        if id_usuario is None:
            id_usuario = 1
        usuario = Usuario(id_usuario = id_usuario, nombre = nombre, email = email, contraseña = contraseña, id_cargo = id_cargo)
        sql = '''INSERT INTO usuario (ID_USUARIO, NOMBRE, CORREO, CONTRASENA, ID_CARGO)
                VALUES (?, ?, ?, ?, ?);'''
        val = (usuario.id_usuario, usuario.nombre, usuario.email, usuario.contraseña, usuario.id_cargo)
        print (val)
        self.sqlserver.insert(sql, val)

    def updateUser(self, nombre,  email, contraseña, id_cargo, id_usuario):

        sql = '''UPDATE usuario
                SET nombre = ?, correo = ?, contrasena = ?, id_cargo = ?
                WHERE ID_USUARIO = ?'''
        val = (nombre, email, contraseña, id_cargo, id_usuario)
        self.sqlserver.insert(sql, val)

    def deleteUser(self, id_usuario):
        sql = '''DELETE FROM USUARIO
                WHERE ID_USUARIO = ?'''
        val = (id_usuario)
        self.sqlserver.insert(sql, val)

    def getUsers(self):
        sql = '''SELECT ID_USUARIO, NOMBRE, CORREO, CONTRASENA, CARGO 
        FROM USUARIO U
        INNER JOIN CARGO C
        ON C.ID_CARGO = U.ID_CARGO'''

        return self.sqlserver.selectn(sql)

    def getNombreUser(self, correo):
        sql = '''SELECT NOMBRE FROM USUARIO WHERE CORREO LIKE ?'''
        val = (correo)
        return self.sqlserver.select(sql, val)[0][0]

    def get_user(self):
        sql = "SELECT * FROM usuario WHERE ID_USUARIO = (SELECT MAX(id_usuario)+1 FROM usuario)"
        return self.sqlserver.selectn(sql)

    def getUser(self, id_usuario):
        sql = '''SELECT * FROM USUARIO WHERE ID_USUARIO = ?'''
        val = (id_usuario)
        return self.sqlserver.select(sql, val)
    
    def getUserNameCargo(self, nombre, cargo):
        sql = '''SELECT ID_USUARIO, NOMBRE, CORREO, CONTRASENA, CARGO
                FROM USUARIO U
                INNER JOIN CARGO C
                ON C.ID_CARGO = U.ID_CARGO
                WHERE NOMBRE LIKE ? AND CARGO LIKE ?'''
        val = (nombre, cargo)
        return self.sqlserver.select(sql,val)

    def getPassword(self, email):
        sql = "SELECT CONTRASENA FROM USUARIO WHERE CORREO LIKE ?"
        val = (email) 
        return self.sqlserver.select(sql,val)

    def getCargo(self, email):
        sql = '''SELECT CARGO FROM USUARIO U
                INNER JOIN CARGO C
                ON C.ID_CARGO = U.ID_CARGO
                WHERE CORREO LIKE ?'''
        val = (email)
        return self.sqlserver.select(sql, val)[0][0]

    def emailExists(self, email):
        sql = 'SELECT CORREO FROM USUARIO WHERE CORREO LIKE ?'
        val = (email)        
        exists = self.sqlserver.select(sql, val)
        print(exists)
        if exists:
            return True
        else:
            return False
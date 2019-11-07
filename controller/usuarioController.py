from model.usuario import Usuario
from .sqlserver import SQLServerController

# USUARIO
class usuarioController():
    def __init__(self):
        self.sqlserver = SQLServerController()


    def createUser(self, nombre, email, contraseña, id_cargo, estado):
        sql = 'SELECT MAX(id_usuario)+1 FROM usuario'
        id_usuario = self.sqlserver.selectn(sql)[0][0]
        if id_usuario is None:
            id_usuario = 1
        usuario = Usuario(id_usuario = id_usuario, nombre = nombre, email = email, contraseña = contraseña, id_cargo = id_cargo, estado = estado)
        sql = '''INSERT INTO usuario (ID_USUARIO, NOMBRE, CORREO, CONTRASENA, ID_CARGO, ESTADO)
                VALUES (?, ?, ?, ?, ?, ?);'''
        val = (usuario.id_usuario, usuario.nombre, usuario.email, usuario.contraseña, usuario.id_cargo, usuario.estado)
        print (val)
        self.sqlserver.insert(sql, val)

    def updateUser(self, oldNombre, nombre, oldEmail, email, contraseña, id_cargo, estado):
        sql = 'SELECT id_usuario FROM usuario WHERE (nombre LIKE ? AND correo LIKE ?);'
        val = (oldNombre, oldEmail)
        id_usuario = self.sqlserver.select(sql, val)

        sql = '''UPDATE usuario
                SET nombre = ?, correo = ?, contrasena = ?, id_cargo = ?, estado = ?'''
        val = (nombre, correo, contraseña, id_cargo, estado)

        

    def getUser(self):
        sql = "SELECT * FROM usuario WHERE ID_USUARIO = (SELECT MAX(id_usuario)+1 FROM usuario)"
        return self.sqlserver.selectn(sql)

    def getPassword(self, email):
        sql = "SELECT CONTRASENA FROM USUARIO WHERE CORREO LIKE ?"
        val = (email) 
        return self.sqlserver.select(sql,val)[0][0]

    def emailExists(self, email):
        sql = 'SELECT CORREO FROM USUARIO WHERE CORREO LIKE ?'
        val = (email)
        
        exists = self.sqlserver.select(sql, val)
        if exists:
            return True
        else:
            return False
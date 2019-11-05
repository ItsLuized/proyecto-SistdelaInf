from model.usuario import Usuario
from .sqlserver import SQLServerController

# USUARIO
class usuarioController():
    def __init__(self):
        self.sqlserver = SQLServerController()


    def createUser(self, nombre, email, contraseña, id_cargo, estado):
        id_usuario = 'SELECT MAX(id_usuario) FROM usuario'
        usuario = Usuario(id_usuario = id_usuario, nombre = nombre, email = email, contraseña = contraseña, id_cargo = id_cargo, estado = estado)
        sql = '''INSERT INTO usuario (id_usuario, nombre, email, contraseña, id_cargo, estado)
                VALUES (%s, %s, %s, %s, %s, %s)'''
        values = (usuario.id_usuario, usuario.nombre, usuario.email, usuario.contraseña, usuario.id_cargo, usuario.estado)

        self.sqlserver.insert(sql, values)
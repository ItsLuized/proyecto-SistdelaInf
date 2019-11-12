from flask import Flask, render_template, flash, url_for, request, redirect
from controller.usuarioController import usuarioController

app = Flask(__name__)


@app.route('/')
def loginPage():
    return render_template('login.html')


@app.route('/register')
def registerPage():
    return render_template('crear-usuario.html')


@app.route('/login',  methods=['POST'])
def login():
    if request.method == 'POST':
        if request.form['correo'] == 'admin@correo.com' and request.form['contrasena'] == 'admin':
            return redirect('/home')
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html', nombre='Nombre Ejemplo')
    # Cambiar la igualdad de nombre por alguna consulta de SQL que retorne el nombre de la persona

@app.route('/enconstruccion')
def construccion():
    return render_template('construccion.html')

@app.route('/planestrategico')
def planEstrategico():
    return render_template('plan-estrategico.html')

@app.route('/crearusuario')
def pagCrearUsuario():
    return render_template('crear-usuario.html')

@app.route('/actividadescargos')
def actividadesCargos():
    return render_template('actividades-cargos.html')

@app.route('/actividadesclaves')
def actividadesClave():
    return render_template('actividades-clave.html')

@app.route('/administrarusuarios')
def administrarUsuario():
    return render_template('administrar-usuario.html', nombre = 'Nombre Ejemplo')

@app.route('/help')
def ayuda():
    return render_template('ayuda.html')

@app.route('/cargos')
def cargos():
    return render_template('cargos.html')

@app.route('/configuration')
def configuracion():
    return render_template('configuracion.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/notificacion')
def notificaciones():
    return render_template('notificaciones.html')

@app.route('/objetivos')
def objetivos():
    return render_template('objetivos.html')

@app.route('/perfil')
def perfil():
    return render_template('perfil.html', nombre = 'Camilo Vega') #Cambiar parametro nombre y mandar los demás parametros

@app.route('/planoperativo')
def planOperativo():
    return render_template('plan-operativo.html')

@app.route('/masactividadesclave')
def verMasActividadesClave():
    return render_template('ver-mas-actividades-clave.html')

@app.route('/masimperativos')
def verMasImperativos():
    return render_template('ver-mas-imperativos.html')

@app.route('/masobjetivos')
def verMasObjetivos():
    return render_template('ver-mas-objetivos.html')


# Back-end

# USUARIO
@app.route('/usuario/create', methods=['POST'])
def crearUsuario():
    print(request.json)
    nombre = request.json['nombre']
    email = request.json['email']
    contraseña = request.json['contrasena']
    id_cargo = request.json['id_cargo']
    estado = request.json['estado']
    if nombre == "" or email == "" or contraseña == "" or id_cargo == None:
        return  404 # CORREGIR ESTO, PUES DA ERROR AL NO RETORNAR ALGO

    a = usuarioController()
    a.createUser(nombre, email, contraseña, id_cargo, estado)
    return str(a.getUser())


# @app.route('/usuario/update', methods = ['POST'])
# def updateUsuario():
#    if request.method == 'POST':


if __name__ == "__main__":
    app.run(debug=True)

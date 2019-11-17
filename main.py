from flask import Flask, render_template, flash, url_for, request, redirect, jsonify, abort
from controller.usuarioController import usuarioController

app = Flask(__name__)

global nombre
nombre = ''
global cargo
cargo = ''
global loggedIn
loggedIn = False

@app.route('/')
def loginPage():
    global loggedIn
    loggedIn = False
    global nombre
    nombre = ''
    global cargo
    cargo = ''
    return render_template('login.html')


@app.route('/register')
def registerPage():
    global loggedIn
    if loggedIn == True:
        return render_template('crear-usuario.html')
    else:
        return redirect('/')


@app.route('/login',  methods=['POST'])
def login():
    if request.method == 'POST':
        correo = request.form['correo']
        a = usuarioController()
        if a.emailExists(correo) == True:
            password = a.getPassword(correo)[0][0]
            print(password)
            if request.form['contrasena'] == password:
                global nombre 
                nombre = a.getNombreUser(correo)
                global cargo
                cargo = a.getCargo(correo)
                global loggedIn
                loggedIn = True
                return redirect('/home')
            else:
                return redirect('/')
        else:
            return redirect('/')
    return render_template('login.html')


@app.route('/home')
def home():
    global loggedIn
    if loggedIn == True:
        global nombre
        return render_template('home.html', nombre = nombre)
    else:
        return redirect('/')

@app.route('/enconstruccion')
def construccion():
    global loggedIn
    if loggedIn == True:
        return render_template('construccion.html')
    else:
        return redirect('/')


@app.route('/planestrategico')
def planEstrategico():
    global loggedIn
    if loggedIn == True:
        return render_template('plan-estrategico.html')
    else:
        return redirect('/')

@app.route('/crearusuario', methods=['GET', 'POST'])
def pagCrearUsuario():
    global loggedIn
    if loggedIn == True:
        if request.method == 'GET':
            return render_template('crear-usuario.html')
        else: 
            return redirect('/menu')
    else:
        return redirect('/')
    

@app.route('/actividadescargos')
def actividadesCargos():
    global loggedIn
    if loggedIn == True:
        return render_template('actividades-cargos.html')
    else:
        return redirect('/')

@app.route('/actividadesclaves')
def actividadesClave():
    global loggedIn
    if loggedIn == True:
        return render_template('actividades-clave.html')
    else:
        return redirect('/')

@app.route('/administrarusuarios')
def administrarUsuario():
    global loggedIn
    if loggedIn == True:
        global cargo
        if cargo == 'ADMINISTRADOR':
            a = usuarioController()
            data = a.getUsers()
            columnas = ["id","nombre","email","password", "cargo"]
            result = []

            for d in data:
                result.append(dict(zip(columnas,d)))
            print(result)
            return render_template('administrar-usuario.html', data = result)
        else: return redirect('/menu')
    else:
        return redirect('/')
    

@app.route('/help')
def ayuda():
    global loggedIn
    if loggedIn == True:
        return render_template('ayuda.html')
    else:
        return redirect('/')

@app.route('/cargos')
def cargos():
    global loggedIn
    if loggedIn == True:
        return render_template('cargos.html')
    else:
        return redirect('/')

@app.route('/configuration')
def configuracion():
    global loggedIn
    if loggedIn == True:
        return render_template('configuracion.html')
    else:
        return redirect('/')

@app.route('/menu')
def menu():
    global loggedIn
    if loggedIn == True:
        return render_template('menu.html')
    else:
        return redirect('/')

@app.route('/notificacion')
def notificaciones():
    global loggedIn
    if loggedIn == True:
        return render_template('notificaciones.html')
    else:
        return redirect('/')

@app.route('/objetivos')
def objetivos():
    global loggedIn
    if loggedIn == True:
        return render_template('objetivos.html')
    else:
        return redirect('/')

@app.route('/perfil')
def perfil():
    global nombre
    global cargo
    global loggedIn
    if loggedIn == True:
        a = usuarioController()
        data = a.getUserNameCargo(nombre, cargo)
        columnas = ["id","nombre","email","password", "cargo"]
        result = []

        for d in data:
            result.append(dict(zip(columnas,d)))
        print(result)
        return render_template('perfil.html', data = result) #Cambiar parametro nombre y mandar los demás parametros
    else:
        return redirect('/')

@app.route('/planoperativo')
def planOperativo():
    global loggedIn
    if loggedIn == True:
        return render_template('plan-operativo.html')
    else:
        return redirect('/')

@app.route('/masactividadesclave')
def verMasActividadesClave():
    global loggedIn
    if loggedIn == True:
        return render_template('ver-mas-actividades-clave.html')
    else:
        return redirect('/')

@app.route('/masimperativos')
def verMasImperativos():
    global loggedIn
    if loggedIn == True:
        return render_template('ver-mas-imperativos.html')
    else:
        return redirect('/')

@app.route('/masobjetivos')
def verMasObjetivos():
    global loggedIn
    if loggedIn == True:
        return render_template('ver-mas-objetivos.html')
    else:
        return redirect('/')


# Back-end

# USUARIO
@app.route('/usuario/create', methods=['POST'])
def crearUsuario():
    global loggedIn
    if loggedIn == True:
        print(request.json)
        nombre = request.json['nombre']
        email = request.json['email']
        contraseña = request.json['contrasena']
        id_cargo = request.json['id_cargo']
        estado = request.json['estado']
        if nombre == "" or email == "" or contraseña == "" or id_cargo == None:
            return 400 # CORREGIR ESTO, PUES DA ERROR AL NO RETORNAR ALGO

        a = usuarioController()
        a.createUser(nombre, email, contraseña, id_cargo, estado)
        return str(a.get_user())


@app.route('/usuario/<id_usuario>', methods = ['GET', 'POST'])
def updateUsuario(id_usuario):
    global loggedIn
    if loggedIn == True:

        if request.method == 'POST':
            print(request.json)
            print(request.is_json)
            nombre = request.form['nombre']
            email = request.form['email']
            contrasena = request.form['password']
            id_cargo = request.form['id_cargo']
            estado = request.form['estado']
            if nombre == "" or email == "" or contrasena == "" or id_cargo == "" or estado == "":
                return 400

            a = usuarioController()
            a.updateUser(nombre, email, contrasena, id_cargo, estado, id_usuario)
            return redirect('/administrarusuarios')

        ## GET Method    
        else:
            a = usuarioController()
            usuario = a.getUser(id_usuario)
            columnas = ["id","nombre","email","password", "estado", "cargo"]
            result = []

            for d in usuario:
                result.append(dict(zip(columnas,d)))
            print(result)
            return render_template('editar-usuario.html', data = result) 
    else:
        return redirect('/')

@app.route('/usuario/update', methods=['POST'])
def updateUser(self):
    global loggedIn
    if loggedIn == True:
        print(request.json)
        print(request.is_json)
        id_usuario = request.json['id_usuario']
        nombre = request.json['nombre']
        email = request.json['correo']
        contrasena = request.json['contrasena']
        id_cargo = request.json['id_cargo']
        estado = request.json['estado']
        if nombre == "" or email == "" or contrasena == "":
            return 400

        a = usuarioController()
        a.updateUser(nombre, email, contrasena, id_cargo, estado, id_usuario)
        return str(a.getUser(id_usuario))
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, flash, url_for, request, redirect, jsonify, abort
from controller.usuarioController import usuarioController
from controller.imperativoController import imperativoController
from controller.objetivoController import objetivoController
from controller.actividad_claveController import actividad_claveController

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
        return render_template('home.html', nombre=nombre)
    else:
        return redirect('/')


@app.route('/enconstruccion')
def construccion():
    global loggedIn
    if loggedIn == True:
        return render_template('construccion.html')
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


@app.route('/<id_imperativo>/<id_objetivo>/actividadesclaves')
def actividadesClave(id_imperativo, id_objetivo):
    global loggedIn
    if loggedIn == True:
        ac = actividad_claveController()
        data = ac.getActividadClaveObjetivo(id_objetivo)
        columnas = ["id", "nombre"]
        result = []

        for d in data:
            result.append(dict(zip(columnas, d)))
        return render_template('actividades-clave.html', data=result)
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
            columnas = ["id", "nombre", "email", "password", "cargo"]
            result = []

            for d in data:
                result.append(dict(zip(columnas, d)))
            print(result)
            return render_template('administrar-usuario.html', data=result)
        else:
            return redirect('/menu')
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

# ------------------------- OBJETIVOS -------------------------#
@app.route('/<id_imperativo>/objetivos')
def objetivos(id_imperativo):
    global loggedIn
    if loggedIn == True:
        o = objetivoController()
        data = o.getObjetivosImperativo(id_imperativo)
        columnas = ["id", "nombre"]
        result = []

        for d in data:
            result.append(dict(zip(columnas, d)))
        print(result)
        return render_template('objetivos.html', data=result, id_imperativo = id_imperativo)
    else:
        return redirect('/')

@app.route('/<id_imperativo>/objetivo')
def agregarObjetivo(id_imperativo):
    global loggedIn
    if loggedIn == True:
        return render_template('crear-objetivo.html', id_imperativo=id_imperativo)
    else:
        return redirect('/')

@app.route('/api/<int:id_imperativo>/objetivo', methods = ['GET', 'POST'])
def createObjetivo(id_imperativo):
    global loggedIn
    if loggedIn == True:
        if request.method == 'POST':
            o = objetivoController()    
            print(request.json)
            nombre = request.json["nombre"]
            completud_por = request.json["completud_por"]
            print("nombre : {0}, completud_por: {1}", (nombre, completud_por))
            o.createObjetivo(nombre, completud_por, id_imperativo)
            return redirect('/{}/objetivos'.format(id_imperativo))
        else:
            return redirect('/{}/objetivos'.format(id_imperativo))
    else:
        return redirect('/')


@app.route('/masobjetivos')
def verMasObjetivos():
    global loggedIn
    if loggedIn == True:
        return render_template('ver-mas-objetivos.html')
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
        columnas = ["id", "nombre", "email", "password", "cargo"]
        result = []

        for d in data:
            result.append(dict(zip(columnas, d)))
        print(result)
        return render_template('perfil.html', data=result)
    else:
        return redirect('/')

# ----------------------------- Imperativos -----------------------------#
@app.route('/planestrategico')
def planEstrategico():
    global loggedIn
    if loggedIn == True:
        i = imperativoController()
        data = i.getImperativos()
        columnas = ["id", "nombre_imperativo", "lider"]
        result = []

        for d in data:
            result.append(dict(zip(columnas, d)))
        return render_template('plan-estrategico.html', data=result)
    else:
        return redirect('/')


@app.route('/imperativo', methods=['GET', 'POST'])
def agregarImperativo():
    global loggedIn
    if loggedIn == True:
        if request.method == 'GET':
            a = usuarioController()
            data = a.getUsers()
            columnas = ["id", "nombre", "correo", "contrasena", "cargo"]
            result = []

            for d in data:
                result.append(dict(zip(columnas, d)))
            return render_template('crear-imperativo.html', data=result)
        else:
            return redirect('/planestrategico')
    else:
        return redirect('/')


@app.route('/api/imperativo', methods=['POST'])
def Imperativo():
    global loggedIn
    if loggedIn == True:

        # POST Method
        if request.method == 'POST':
            print(request.json)
            i = imperativoController()
            nombre = request.json["nombre"]
            fecha_inicio = request.json["fecha_inicio"]
            fecha_fin = request.json["fecha_fin"]
            id_usuario = request.json["id_usuario"]
            if nombre == '' or fecha_inicio == '' or fecha_fin == '' or id_usuario == '':
                return jsonify(codigo=400)

            i.CreateImperativo(nombre, fecha_inicio, fecha_fin, id_usuario)
            return str(i.getLastImperativo())
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


@app.route('/masimperativos/<int:id_imperativo>', methods=['GET', 'PUT'])
def verMasImperativos(id_imperativo):
    global loggedIn
    if loggedIn == True:
        if request.method == 'GET':
            i = imperativoController()
            u = usuarioController()
            data = i.getImperativo(id_imperativo)
            columnas = ["id_imperativo", "nombre", "fecha_inicio", "fecha_fin", "id_usuario"]
            result = []

            names = u.getUsers()
            column =["id", "nombre", "correo", "contrasena", "cargo"]
            nombres = []

            for d in data:
                result.append(dict(zip(columnas, d)))

            for name in names:
                nombres.append(dict(zip(column, name)))
            return render_template('ver-mas-imperativos.html', data=result, nombres=nombres)
        else:
            i = imperativoController()
            print(request.json)
            nombre = request.json['nombre']
            id_usuario = request.json['id_usuario']
            fecha_inicio = request.json['fecha_inicio']
            fecha_fin = request.json['fecha_fin']

            i.updateImperativo(id_imperativo, nombre, fecha_inicio, fecha_fin, id_usuario)
            
    else:
        return redirect('/')




# Back-end

#----------------------------- USUARIO -----------------------------#
@app.route('/usuario/create', methods=['POST'])
def crearUsuario():
    global loggedIn
    if loggedIn == True:
        print(request.json)
        nombre = request.json['nombre']
        email = request.json['email']
        contraseña = request.json['contrasena']
        id_cargo = request.json['id_cargo']
        if nombre == "" or email == "" or contraseña == "" or id_cargo == None:
            return 400  # CORREGIR ESTO, PUES DA ERROR AL NO RETORNAR ALGO

        a = usuarioController()
        a.createUser(nombre, email, contraseña, id_cargo)
        return str(a.get_user())


@app.route('/usuario/<id_usuario>', methods=['GET', 'POST', 'DELETE'])
def updateUsuario(id_usuario):
    global loggedIn
    global cargo
    if loggedIn == True:
        if cargo == 'ADMINISTRADOR':
            # POST Method
            if request.method == 'POST':
                nombre = request.form['nombre']
                email = request.form['email']
                contrasena = request.form['password']
                id_cargo = request.form['id_cargo']
                if nombre == "" or email == "" or contrasena == "" or id_cargo == "":
                    return 400

                a = usuarioController()
                a.updateUser(nombre, email, contrasena, id_cargo, id_usuario)
                return redirect('/administrarusuarios')

            # GET Method
            elif request.method == 'GET':
                a = usuarioController()
                usuario = a.getUser(id_usuario)
                columnas = ["id", "nombre", "email", "password", "cargo"]
                result = []

                for d in usuario:
                    result.append(dict(zip(columnas, d)))
                print(result)
                return render_template('editar-usuario.html', data=result)
            else:
                redirect('/menu')
    else:
        return redirect('/')


@app.route('/usuario/delete/<id_usuario>')
def deleteUsuario(id_usuario):
    global loggedIn
    if loggedIn == True:
        global cargo
        if cargo == 'ADMINISTRADOR':
            a = usuarioController()
            a.deleteUser(id_usuario)
            return redirect('/administrarusuarios')
        else:
            return redirect('/menu')
    else:
        return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)

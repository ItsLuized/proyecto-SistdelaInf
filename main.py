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
        if request.form['email'] == 'admin@correo.com' and request.form['contraseña'] == 'admin':
            return redirect('/home')
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html', nombre='Inicio')
    # Cambiar la igualdad de nombre por alguna consulta de SQL que retorne el nombre de la persona


@app.route('/planestrategico')
def planEstrategico():
    return render_template('plan-estrategico.html')


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
    print (nombre)
    a = usuarioController()
    a.createUser(nombre, email, contraseña, id_cargo, estado)
    return str(a.getUser())

    
# @app.route('/usuario/update', methods = ['POST'])
# def updateUsuario():
#    if request.method == 'POST':


if __name__ == "__main__":
    app.run(debug=True)

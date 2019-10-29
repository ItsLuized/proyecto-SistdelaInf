from flask import Flask, render_template, flash, url_for, request, redirect

app = Flask(__name__)

@app.route('/')
def loginPage():
    return render_template('login.html')
    
@app.route('/login',  methods = ['POST'])
def login():
    if request.method == 'POST':
        if request.form['email'] == 'admin@correo.com' and request.form['contraseña'] == 'admin':
            return redirect('/home')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html', nombre = 'Nombre') 
    #Cambiar la igualdad de nombre por alguna consulta de SQL que retorne el nombre de la persona

@app.route('/planestrategico')
def planEstrategico():
    return render_template('plan-estrategico.html')

if __name__ == "__main__":
    app.run(debug=True)
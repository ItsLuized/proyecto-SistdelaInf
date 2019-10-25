from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('prueba1.html')
    
@app.route('/login',  methods = ['POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['email'] != 'admin@correo.com' or request.form['contraseña'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return "<h1> Lo lograste prro :V</h1>"
    return render_template('prueba1.html', error=error)
    
if __name__ == "__main__":
    app.run(debug=True)
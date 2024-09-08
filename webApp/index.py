# llama el framework flask desde el paquete flask
from flask import Flask, render_template, request, redirect, url_for
import db

# encapsula  flask en una variable
app=Flask(__name__)

# se define la ruta, la cual inicia por /
@app.route('/')
# y luego con una funcion se le da valor
def home():
    # aqui retorna lo que uno le diga (en este caso un texto simple)
    #> return 'Home Page'
    return render_template('home.html')

@app.route('/actividades')
def actividades():
    cuentos=db.lectura_data()
    return render_template('actividades.html',cuentos=cuentos)

@app.route('/phishh')
def phishh():
    return render_template('phishh.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')

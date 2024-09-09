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

@app.route('/operaciones')                                          # las rutas inician con /
def operaciones():                                                  # se define la funcion
    cuentos=db.consulta()                                           # aqui se especifica la funcion a ejecutar dentro de esa ruta
    return render_template('op/operaciones.html',cuentos=cuentos)   # aqui en el render template se especifica la ruta

@app.route('/insertar')
def insertar():
    return render_template('op/insertar.html')

@app.route('/actualizar')
def actualizar():
    return render_template('op/actualizar.html')

@app.route('/borrar')
def borrar():
    return render_template('op/borrar.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')

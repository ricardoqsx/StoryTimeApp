# llama el framework flask desde el paquete flask
from flask import Flask, render_template, request, redirect, url_for
from config import config

# encapsula  flask en una variable
app=Flask(__name__)

# se define la ruta, la cual inicia por /
@app.route('/')
# y luego con una funcion se le da valor
def home():
    # aqui retorna lo que uno le diga (en este caso un texto simple)
    #> return 'Home Page'
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/phishh')
def phishh():
    return render_template('phishh.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')

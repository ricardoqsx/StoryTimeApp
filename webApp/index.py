# llama el framework flask desde el paquete flask
from flask import Flask, render_template, request, redirect, url_for
import db # <- en db.py esta toda la logica de operaciones relacionadas a la base de datos

# encapsula  flask en una variable
app=Flask(__name__)


# se define la ruta, la cual inicia por /
@app.route('/')
# y luego con una funcion se le da valor
def home():
    # aqui retorna lo que uno le diga (puede ser un texto simple o una pagina web)
    #> return 'Home Page'
    return render_template('home.html')

@app.route('/operaciones')                                          # las rutas inician con /
def operaciones():                                                  # se define la funcion
    cuentos=db.consulta()                                           # aqui se especifica la funcion a ejecutar dentro de esa ruta, por defecto no esta definido pero todas las funciones tienen un metodo GET
    return render_template('op/operaciones.html',cuentos=cuentos)   # aqui en el render template se especifica la ruta, adicionalmente se especifica la variable donde esta encapsulada la consulta a la BD

@app.route('/insertar', methods=['GET', 'POST'])                    # en este caso se especifican los 2 metodos ya que segun el caso (la logica) seran usados
def insertar():
    if request.method == 'POST':                                    # en un if se declara que si la http request es POST
        # Validar entradas
        titulo = request.form.get('titulo')                         # toma todos los valores listados a continuacion a partir del formulario de insertar.html y los guarda en una variable c/u
        categoria = request.form.get('categoria')
        descripcion = request.form.get('descripcion')
        db.insertar(titulo, categoria, descripcion)                 # aqui toma los valores y ejecuta la funcion insertar para guardar los valores en la BD
        return redirect(url_for('insertar'))                        # y finalmente retorna la URL declarada en la funcion insertar, como luego de ejecutar el if el metodo sera GET, devuelve insertar.html
    # Renderizar el formulario de inserción                         # adicionalmente, esto funciona como endpoint y por ende como una API la cual recoge los datos y los trabaja en el backend
    return render_template('op/insertar.html')

@app.route('/actualizar', methods=['GET', 'POST'])
def actualizar():
    return render_template('op/actualizar.html',cuentos=cuentos)

@app.route('/borrar', methods=['GET', 'POST'])
def borrar():
    if request.method == 'POST':
        # Obtén los IDs de los cuentos seleccionados
        cuentos_ids = request.form.getlist('cuentos_ids')
        
        # Llama a la función para eliminar cuentos
        db.borrar(cuentos_ids)
        
        # Redirecciona a la misma página después de la eliminación
        return redirect(url_for('borrar'))
    
    # Si el método es GET, simplemente obtén y muestra los cuentos
    cuentos=db.consulta()
    return render_template('op/borrar.html',cuentos=cuentos)

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

#@app.route('/actualizar', methods=['GET', 'POST'])
#def actualizar():
    # cambiare el enfoque:
    # creare un menu desplegable a partir del cual muestre todos los titulos
    # y en el formulario que envie, precargue una celda, para que el usuario 
    # actualice la fila
#    if request.method == 'POST':
        # Obtener los IDs seleccionados
#        selected_ids = request.form.getlist('cuentos_ids')

        # Preparar listas para los datos a actualizar
#        titles = []
#        categories = []
#        descriptions = []

        # Recolectar datos para los IDs seleccionados
#        for cuento_id in selected_ids:
#            title = request.form.getlist('titulo')
#            category = request.form.getlist('categoria')
#            description = request.form.getlist('descripcion')
#            db.actualizar(selected_ids, titles, categories, descriptions)
#            return redirect(url_for('actualizar'))  # Redirigir después de actualizar
#    cuentos=db.consulta()
#    return render_template('op/actualizar.html',cuentos=cuentos)

    # el problema estoy casi seguro que tiene que ver con que no se esta iterando sobre
    # los valores que trae el formulario, o no se estan guardando correctamente, 
    # lo que lleva a que siempre se este actualizando el valor de la primera columna
    # efectivo, realice una prueba en la primera columna y se actualizo

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')

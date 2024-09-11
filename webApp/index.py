# llama el framework flask desde el paquete flask
from flask import Flask, flash, render_template, request, redirect, url_for
import db
import secrets
# encapsula  flask en una variable
app=Flask(__name__)

secret_key = secrets.token_hex(16)

app.secret_key = secret_key

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

@app.route('/insertar', methods=['GET', 'POST'])
def insertar():
    if request.method == 'POST':
        # Validar entradas
        titulo = request.form.get('titulo', '').strip()
        categoria = request.form.get('categoria', '').strip()
        descripcion = request.form.get('descripcion', '').strip()

        if not titulo or not categoria or not descripcion:
            flash('Todos los campos son obligatorios', 'error')
            return redirect(url_for('insertar'))
        
        # Intentar insertar en la base de datos
        try:
            db.insertar(titulo, categoria, descripcion)
            flash('Datos insertados con éxito', 'success')
        except Exception as e:
            flash(f'Error al insertar datos: {str(e)}', 'error')

        return redirect(url_for('insertar'))

    # Renderizar el formulario de inserción
    return render_template('op/insertar.html')

@app.route('/actualizar')
def actualizar():
    return render_template('op/actualizar.html')

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

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')

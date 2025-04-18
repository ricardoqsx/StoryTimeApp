# app/db.py
import mariadb

# datos de conexion a la base de datos
conexion = mariadb.connect(
    host="pydb",
    user="pyuser",
    password="pypass",
    database="storytime"
)
# se crea el cursor para hacer consultas a la bd
cursor = conexion.cursor()

# Crean las 2 tablas principales para la base de datos, 
# una de usuario y otra para los cuentos

def crear_bd():
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS cuentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL,
            categoria VARCHAR(100) NOT NULL,
            descripcion VARCHAR(100) NOT NULL)"""
    )
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS usuarios (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            user VARCHAR(25) NOT NULL,
            password VARCHAR(100) NOT NULL,
            full_name VARCHAR(50) NOT NULL)"""
    )
    cursor.execute("SELECT COUNT(*) FROM cuentos")
    # este if basicamente verifica si la tabla no esta vacia, si lo esta entonces inserta los valores
    if cursor.fetchone()[0] == 0:
        # valores de prueba para la base de datos
        cursor.execute(
            """INSERT INTO cuentos (titulo, categoria, descripcion) VALUES
            ('Administración de Bases de Datos con MariaDB', 'Bases de Datos', 'Guía sobre bases de datos MariaDB.'),
            ('Guía de Iniciación a Kubernetes', 'Orquestación de Contenedores', 'Tutorial sobre Kubernetes.'),
            ('Creación de Aplicaciones Web con Flask', 'Desarrollo Web', 'Desarrolla aplicaciones web usando Flask.'),
            ('Gestión de Proyectos con Git', 'Control de Versiones', 'Uso de Git para proyectos.'),
            ('Desarrollo de Aplicaciones con Flutter', 'Desarrollo Móvil', 'Crea apps móviles con Flutter y Dart.'),
            ('Administración de Redes con WireGuard', 'Redes', 'Configura conexiones VPN seguras con WireGuard.'),
            ('Despliegue de Aplicaciones con Docker', 'Contenedores', 'Despliega aplicaciones con Docker.'),
            ('Análisis de Datos con Python', 'Análisis de Datos', 'Usa Python para analizar grandes volúmenes de datos.')"""
                )
    # Confirmar los cambios realizados
    conexion.commit()
    print("Datos insertados correctamente.")
    

# Función para leer los datos de la tabla 'cuentos'
def consulta():
    cursor.execute("SELECT * FROM cuentos")
    cuentos = cursor.fetchall()  # Recupera todos los resultados
    return cuentos  # Devuelve los resultados

def insertar(titulo, categoria, descripcion):
    query = "INSERT INTO cuentos (titulo, categoria, descripcion) VALUES (%s, %s, %s)"
    cursor.execute(query, (titulo, categoria, descripcion))
    conexion.commit()

def actualizar(ids_seleccionados, titulos, categorias, descripciones):
    query = """
    UPDATE cuentos
    SET 
        titulo = %s,
        categoria = %s,
        descripcion = %s
    WHERE id = %s;
    """
    # Acceder al valor correspondiente en cada lista
    cursor.execute(query, (titulos, categorias, descripciones, ids_seleccionados))
    conexion.commit()     

def borrar(cuentos_ids):
    # Eliminar los cuentos seleccionados
    for cuento_id in cuentos_ids:
        cursor.execute("DELETE FROM cuentos WHERE id = %s", (cuento_id,))    
    conexion.commit()

def get_id(cuento_id):
    cursor.execute("select titulo from cuentos where id = %s",(cuento_id))
    cursor.commit()

# Ejecutar las consultas
crear_bd()
consulta()

# Cerrar la conexión con la base de datos

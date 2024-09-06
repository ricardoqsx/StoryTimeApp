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
queries=conexion.cursor()

# Crean las 2 tablas principales para la base de datos, 
# una de usuario y otra para los cuentos

def crear_bd():
    queries.execute(
        """CREATE TABLE IF NOT EXISTS cuentos (
            id INT AUTO_INCREMENT PRIMARY KEY,
            titulo VARCHAR(100) NOT NULL,
            categoria VARCHAR(100) NOT NULL,
            archivo LONGBLOB NOT NULL)"""
    )
    queries.execute(
        """CREATE TABLE IF NOT EXISTS usuarios (
            user_id INT AUTO_INCREMENT PRIMARY KEY,
            user VARCHAR(25) NOT NULL,
            password VARCHAR(100) NOT NULL,
            full_name VARCHAR(50) NOT NULL)"""
    )

def lectura_data():
    queries.execute(
        "select * from cuentos"
    )

# ejecutando el query
# comentado temporalmente -> crear_bd()

# cierra la conexion con la base de datos
conexion.close()


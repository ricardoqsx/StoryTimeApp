# app/db.py

import mariadb

# datos de conexion a la base de datos
conexion = mariadb.connect(
    host="pydb",
    user="pyuser",
    password="pypass",
    database="b4ck3nd"
)

# se crea el cursor para hacer consultas a la bd
cursor = conexion.cursor()
queries=conexion.cursor()

# Crear tabla si no existe
queries.execute(
    """CREATE TABLE IF NOT EXISTS personas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        edad INT NOT NULL)"""
)

# cierra la conexion con la base de datos
conexion.close()
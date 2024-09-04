# app/db.py

import mysql.connector

conexion = mysql.connector.connect(
    host="pydb",
    user="pyuser",
    password="pypass",
    database="b4ck3nd"
)

cursor = conexion.cursor()


# Crear tabla si no existe
def crear_tabla():
    query = """
    CREATE TABLE IF NOT EXISTS personas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        edad INT NOT NULL
    )
    """
    cursor.execute(query)
    conexion.commit()
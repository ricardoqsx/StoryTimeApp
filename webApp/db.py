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
    cursor.execute(
        """INSERT INTO cuentos (titulo, categoria, descripcion) VALUES
        ('Introducción a Docker', 'Contenedores', 'Conceptos básicos sobre Docker y el uso de contenedores.'),
        ('Administración de Bases de Datos con MariaDB', 'Bases de Datos', 'Guía sobre administración de bases de datos MariaDB.'),
        ('Curso de Virtualización con VMware', 'Virtualización', 'Domina VMware para la virtualización de servidores y entornos.'),
        ('Fundamentos de Redes en Linux', 'Redes', 'Conceptos básicos de redes y su configuración en Linux.'),
        ('Guía de Iniciación a Kubernetes', 'Orquestación de Contenedores', 'Tutorial para principiantes sobre Kubernetes.'),
        ('Seguridad en Servidores Web', 'Seguridad', 'Prácticas esenciales para asegurar servidores web contra amenazas.'),
        ('Creación de Aplicaciones Web con Flask', 'Desarrollo Web', 'Desarrolla aplicaciones web usando Flask, un microframework.'),
        ('Implementación de Apache Guacamole', 'Acceso Remoto', 'Guía para implementar Apache Guacamole en contenedores Docker.'),
        ('Optimización de Sistemas Operativos', 'Sistemas Operativos', 'Técnicas para optimizar sistemas operativos Linux y Windows.'),
        ('Gestión de Proyectos con Git y GitHub', 'Control de Versiones', 'Uso de Git y GitHub para la gestión de proyectos.'),
        ('Desarrollo de Aplicaciones Móviles con Flutter', 'Desarrollo Móvil', 'Crea apps móviles multiplataforma con Flutter y Dart.'),
        ('Administración de Redes con WireGuard', 'Redes', 'Configura y administra conexiones VPN seguras con WireGuard.'),
        ('Certificación en Nagios', 'Monitorización', 'Información clave para la certificación en Nagios.'),
        ('Despliegue de Aplicaciones con Docker Compose', 'Contenedores', 'Despliega aplicaciones multicontenedor con Docker Compose.'),
        ('Análisis de Datos con Python', 'Análisis de Datos', 'Usa Python para analizar grandes volúmenes de datos.')"""
            )
    # Confirmar los cambios realizados
    conexion.commit()
    print("Datos insertados correctamente.")
    

# Función para leer los datos de la tabla 'cuentos'
def lectura_data():
    cursor.execute("SELECT * FROM cuentos")
    cuentos = cursor.fetchall()  # Recupera todos los resultados
    return cuentos  # Devuelve los resultados
    
    #for cuento in cursor.fetchall():
    #    print(cuento)

# Ejecutar las consultas
crear_bd()
lectura_data()

# Cerrar la conexión con la base de datos

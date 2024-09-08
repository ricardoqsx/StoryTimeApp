# Proyecto Final StoryTime

Describiendo la logica de la aplicacion storytime (nombre provisional)

## Objetivos:
* La aplicacion basicamente mostraria cuentos con base cientifica
* las historias/cuentos deben ser para niños
* deben ser historias muy ricas culturalmente hablando. (eso luego se inventa con chatGPT)


===============================
===============================

## Tecnologias a utilizar:

### por el lado del frontend

	- Flutter
	- Dart
	- HTML5
	- CSS3
	- SQLite
	- BootStrap

### del lado del Backend

	- MariaDB
	- Docker
	- Python
	- Flask
	- Linux

===============================
===============================

El app constaria de 2 partes

1- Una aplicacion web para administradores/moderadores de la plataforma con la cual puedan hacer CRUD:
	- Create: (crear nuevos cuentos) 
	- Read: (leer el contenido de la base de datos)
	- Update: (Actualizar cuentos que por ejemplo, tengan fallos)
	- Delete: borrar cuentos que el administrador decida.

===============================

Se me ocurre esta app tenga un login (usuario y contraseña de la base de datos)
y que al entrar tenga 3 botones de diferentes colores uno al lado del otro a centrados, y abajo los cuentos que estan en la base de datos
para que entonces, si el moderador/administrador decide crear, modificar o borrar un cuento, toque el respectivo boton
todo esto aplicable a los cuentos que se muestren en la aplicacion, y asi estos tendrian acceso a hacer modificaciones en el mismo.

Esta aplicacion web seria realizada con Flask para la interface web, HTML y CSS para la maquetacion y la conexion con la base de datos se haria mediante python

===============================

la base de datos: contaria con los siguientes campos (tentativo?)
	- id: numerico
	- titulo: cadena larga
	- categoria: cadena
	- archivo: (formato html, el webView recibiria el archivo y lo
	  interpretaria)
tiene que tener 2 usuarios (por ahora), 
	- un admin con todos los permisos
	- usuario sin privilegios (el que leeria de manera remota el 
	  contenido y haria el get)
Se deben almacenar los cuentos alojados en una base de datos remota, para esto se podria utilizar la siguiente metodologia:
	- crear un API con python (alojado en un servidor Linux, Debian 12 Bookworm) que reciba las peticiones y entregue los cuentos
    - SQLite funcionaria como base de datos local para almacenar los cuentos y servirlos a la aplicacion.
Todo esto estaria empaquetado en 2 contenedores de Docker (uno para el WebApp, otro para la base de datos), los cuales (previamente Docker instalado y funcionando) logre aislar el backend y permita mantener una consistencia en las dependencias del backend

===============================
===============================

2- La aplicacion en si, descargable desde el Google Play, 

El app contaria con varias pantallas:

	1. el inicio: donde podria mostrar un preview para que cuando el usuario al seleccionar, pueda leer el cuento completo
	2. el cuento en si, el cual este formateado con HTML (para facilidad, usar una webView), la lectura puede ser con 
	   desplazamiento vertical o con botones de avanzar (tratandolo como una especie de libro)
	   (opcional creo que debe tener un boton donde si el niño se cansa de leer, pueda dejar una especie de "marcador" para continuar luego)
	3. pantallas de settings donde se cambien cosas como el tipo de 
	   letra, tamaño, modo claro/oscuro, lenguaje del app (usando un traductor puede ser?)
	4. una pantalla de creditos, about/acerca de

si todo esto se logra, estamos en el exito!!!
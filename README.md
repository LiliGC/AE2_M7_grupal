<h2 align="center">Trabajo Grupal</h2>
<h1 align="center">Aprendizaje Esperado 2 - Módulo 7</h1>
<h3 align="center">Grupo 1</h3>

Se cambió la base de datos a Mysql en settings.
Creamos el modelo de formulario de contacto, pide el nombre, correo electronico, tipo de mensaje (felicitaciones,
consultas, sugerencias, reclamos) y el mensaje. Estos mensajes pueden ser revisados por el administrador en el admin.
También está la posibilidad de que el usuario registrado que envió el mensaje pueda ver los que ha enviado y editarlos.
Aplicamos una actualización en los templates.

Instrucciones instalación:

- Clonar el repositorio
- Crear el entorno virtual
- Instalar el archivo de requirements.txt
- Hacer las migraciones, makemigrations y luego migrate.
- Crear el superusuario o proceder a cargar el archivo de datos que usamos el que nombramos data.json mediante:
```python manage.py loaddata data.json```
- Aplicar el comando `migrate`.
- Y por ultimo correr el servidor con python manage.py runserver.

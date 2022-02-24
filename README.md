# Despliegue de Flask - Python Intensivo
Aplicación sencilla hecha en Flask y Gunicorn para desplegar en Heroku. Parte del curso Python Intensivo.

* Crear una cuenta de Heroku
* Descargar e instalar Heroku CLI, Git y algún editor IDE (como Visual Studio Code).
* En la consola de comandos (CMD, Bash, etc), apuntando a tu carpeta de proyecto:
  >heroku login
* Abrirá el navegador y debes iniciar sesión
* En Heroku Dashboard crea un nuevo proyecto y sigue los pasos en pantalla.
* En la consola de comandos `reemplazando nombre-de-tu-app` por nombre de proyecto que usaste en heroku
  >heroku git:remote -a nombre-de-tu-app
  * `Esto vinculará tu proyecto con el gestor de versiones online de heroku.`
* Para desplegar
  >git push heroku master
  * `Esto 'empujará' tus cambios hacia el repositorio online de heroku y hará público tu proyecto.`
* Aún falta encender tu servidor. Ejecuta en la línea de comandos:
  >heroku ps:scale web=1
  * `Esto hace 'escalar' tu proyecto encendiendo los servidores y apuntando al servicio creado por gunicorn (ver Procfile)`
* Posterior a esto:
    1. Heroku leerá el runtime.txt para instalar los requisitos del servidor. En este caso `instalará python`.
    2. Heroku leerá el Procfile para ejecutar el servicio. En este caso `para el servicio web ejecutará el servicio wsgi y apuntando a main.py`.
    3. Heroku leerá requirements.txt para instalar las librerías de python. En este caso `flask y gunicorn`.
    4. Gunicorn `iniciará el proceso de main.py`.
    5. El proceso Main `iniciará Flask` y cualquier otra librería de python.
    6. Flask es el servidor y `comenzará correr las funciones y rutas especificadas` cuando reciba una petición GET o POST (protocolo HTTP) a través de un navegador, aplicativo web o Postman.
    7. La aplicación es accesible después del GIT PUSH hecho anteriormente y enlace debe tener una forma 
        >https://nombre-de-tu-app.herokuapp.com/service
## "Quiero cambiar el código"
Si ya se pudo desplegar y todo va bien, puedes modificar el código en tu editor, y al terminar ejecuta en tu línea de comandos:
>git add .
>git commit -m "Alguna descripción de lo que acabas de modificar"
>git push heroku main

Esto añadirá los cambios a una estapa stage donde Git entiende que estas list@ con tus cambios recientes, hará un `commit` o punto de control con tu descripción al cual puedes regresar si dañas algo, y finnalmente, hará `push` para subir tus cambios al repositorio de Heroku. En pocos minutos deberías ser capaz de ver tus cambios en la web.
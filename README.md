# Entrega_Final

Pasos Tener instalado

django 5.0.3 python 3.11 vsc 1.87.0 Comentario: Se ha creado el archivo mediante django, con startproyect, pararse en la carpeta correspondiente con el cd EntregaTP3 y luego con colocar la App a través de python manage.py startapp Se ha tomato un template de start bootstrap. Para los templates, se a usado el padre para crear herencia para las otras plantillas. Arrastrar la carpeta al vsc y comenzamos:

python manage.py makemigrations para poder crear las tablas de las class en la db Luego se hace el python manage.py migrate Instalar un visor de sqlite Viewer ir a la terminal y correr el python manage.py runserver para ver el server ctrl+C para cerrar el server Las clases son

-class Armaduras nombre_armadura tipo_armadura lv_armadura

-class Personajes nombre raza averno

-class Build nombre tipo_daño Total_daño

-class Pets nombre raza nivel

Los URLS son

path("crear_build/", crear_build, name="Build"), path("crear_armaduras/", crear_armaduras,name="Armaduras" ), path("crear_personaje/", crear_personaje, name="Personaje"), path("buscar_personaje/", buscar_personaje,), path("", inicio, name="Home"),

inicio= http://127.0.0.1:8000/AppTP3/ crear PERSONAJE= http://127.0.0.1:8000/AppTP3/crear_personaje/ Crear BUILD = http://127.0.0.1:8000/AppTP3/crear_build/ Crear ARMADURAS= http://127.0.0.1:8000/AppTP3/crear_armaduras/ Buscar PERSONAJE= http://127.0.0.1:8000/AppTP3/buscar_personaje/ Ver resultados= http://127.0.0.1:8000/AppTP3/buscar_personaje/

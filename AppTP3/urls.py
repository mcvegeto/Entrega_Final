from django.urls import path
from AppTP3.views import *

urlpatterns = [

    path("crear_build/", crear_build, name="Build"),
    path("ver_build/", ver_build, name= "ver_build"),
    path("actualizar_build/<build>", actualizar_build, name= "actualizar_build"),
    path("borrar_build/<build>", borrar_build, name= "borrar_build"),

    path("crear_armaduras/", crear_armaduras,name="Armaduras" ),
    path("ver_armaduras/", ver_armaduras, name= "ver_armaduras"),
    path("actualizar_armaduras/<armaduras>", actualizar_armaduras, name= "actualizar_armaduras"),
    path("borrar_armaduras/<armaduras>", borrar_armaduras, name= "borrar_armaduras"),

    path("crear_personaje/", crear_personaje, name="Personaje"),
    path("ver_personaje/", ver_personaje, name= "ver_personaje"),
    path("buscar_personaje/", buscar_personaje, name="Buscar"),
    path("borrar_personaje/<personaje>", borrar_personaje, name= "borrar_personaje"),
    path("actualizar_personaje/<personaje>", actualizar_personaje, name= "actualizar_personaje"),

    path("crear_pet/", crear_pet, name="Pet"),
    path("ver_pet/", ver_pet, name= "ver_pet"),
    path("actualizar_pet/<pet>", actualizar_pet, name= "actualizar_pet"),
    path("borrar_pet/<pet>", borrar_pet, name= "borrar_pet"),

    path("", inicio, name="Home"),
]
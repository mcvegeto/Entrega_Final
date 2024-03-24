from django.shortcuts import render
from django.http import HttpResponse
from AppTP3.models import Build, Personajes, Armaduras, Pet
from AppTP3.forms  import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.



# CRUD INICIO.

def inicio (request):
    return render(request, "inicio.html", {"mensaje": "Bienvenido a la Pagina de Diablo 4"})




# CRUD ARMADURAS.

def crear_armaduras(request):
    if request.method == "POST": #CUANDO APRIETO EL BOTON ENVIAR 
        build_nuevo = Armaduras(nombre_armadura = request.POST["nombre_armadura"],tipo_armadura=request.POST ["tipo_armadura"],lv_armadura=request.POST ["lv_armadura"] )
        build_nuevo.save()
        return render(request,  "inicio.html")
    return render(request, "armaduras/crear_armaduras.html")


@login_required
def ver_armaduras(request):

    todas_armaduras =Armaduras.objects.all()

    return render(request, "armaduras/ver_armaduras.html", {"total":todas_armaduras})


@login_required
def actualizar_armaduras (request, armaduras):

    armadura_elegido = Armaduras.objects.get(id=armaduras)

    if request.method == "POST":

        formulario = ArmadurasFormulario(request.POST)

        if formulario.is_valid():
            
            info_dic = formulario.cleaned_data
            
            armadura_elegido.nombre_armadura = info_dic["nombre_armadura"]
            armadura_elegido.tipo_armadura = info_dic["tipo_armadura"]
            armadura_elegido.lv_armadura = info_dic["lv_armadura"]

            armadura_elegido.save()


            return render(request,  "inicio.html")
    else:

        formulario = ArmadurasFormulario(initial={"nombre_armadura": armadura_elegido.nombre_armadura, "tipo_armadura": armadura_elegido.tipo_armadura, "lv_armadura": armadura_elegido.lv_armadura})

    return render(request, "armaduras/actualizar_armaduras.html", {"formu":formulario})

@login_required
def borrar_armaduras(request, armaduras):

    armadura_elegido = Armaduras.objects.get(id=armaduras)

    armadura_elegido.delete()

    return render(request, "inicio.html")




# CRUD PERSONAJE.

def crear_personaje(request):

    if request.method == "POST": #CUANDO APRIETO EL BOTON ENVIAR 
        
        build_nuevo = Personajes(nombre = request.POST["nombre"],raza=request.POST ["raza"],averno=request.POST ["averno"] )
        build_nuevo.save()
        return render(request,  "inicio.html")
    return render(request, "personaje/crear_personaje.html")

@login_required
def ver_personaje(request):

    todas_personaje =Personajes.objects.all()

    return render(request, "personaje/ver_personaje.html", {"total":todas_personaje})

@login_required
def actualizar_personaje (request, personaje):

    personaje_elegido = Personajes.objects.get(id=personaje)

    if request.method == "POST":

        formulario = PersonajeFormulario(request.POST)

        if formulario.is_valid():
            
            info_dic = formulario.cleaned_data
            
            personaje_elegido.nombre = info_dic["nombre"]
            personaje_elegido.raza = info_dic["raza"]
            personaje_elegido.averno = info_dic["averno"]

            personaje_elegido.save()


            return render(request,  "inicio.html")
    else:

        formulario = PersonajeFormulario(initial={"nombre": personaje_elegido.nombre, "raza": personaje_elegido.raza, "averno": personaje_elegido.averno})

    return render(request, "personaje/actualizar_personaje.html", {"formu":formulario})

@login_required
def borrar_personaje(request, personaje):

    personaje_elegido = Personajes.objects.get(id=personaje)

    personaje_elegido.delete()

    return render(request, "inicio.html")

    

def buscar_personaje (request):

    if request.GET:

        nombre = request.GET["nombre"]
        personaje = Personajes.objects.filter(nombre__icontains=nombre)

        mensaje = f"Resultado sobre el personaje {nombre} :"
    
        return render(request, "personaje/resultado_personaje.html", {"mensaje":mensaje, "resultados":personaje})
    
    return render(request, "personaje/resultado_personaje.html")      


# CRUD BUILD.

def crear_build(request):

    if request.method == "POST": #CUANDO APRIETO EL BOTON ENVIAR 
        
        build_nuevo = Build(nombre = request.POST["nombre"],tipo_daño=request.POST ["tipo_daño"],Total_daño=request.POST ["Total_daño"]  )
        build_nuevo.save()
        return render(request,  "inicio.html")
    return render(request,  "builds/crear_build.html")

@login_required
def ver_build(request):

    todas_build =Build.objects.all()

    return render(request, "builds/ver_build.html", {"total":todas_build})


@login_required
def actualizar_build (request, build):

    build_elegido = Build.objects.get(id=build)

    if request.method == "POST":

        formulario = BuidsFormulario(request.POST)

        if formulario.is_valid():
            
            info_dic = formulario.cleaned_data
            
            build_elegido.nombre = info_dic["nombre"]
            build_elegido.tipo_daño = info_dic["tipo_daño"]
            build_elegido.Total_daño = info_dic["Total_daño"]

            build_elegido.save()


            return render(request,  "inicio.html")
    else:

        formulario = BuidsFormulario(initial={"nombre": build_elegido.nombre, "tipo_daño": build_elegido.tipo_daño, "Total_daño": build_elegido.Total_daño})

    return render(request, "builds/actualizar_build.html", {"formu":formulario})

@login_required
def borrar_build(request, build):

    build_elegido = Build.objects.get(id=build)

    build_elegido.delete()

    return render(request, "inicio.html")



# CRUD PET.

def crear_pet(request):
    if request.method == "POST": #CUANDO APRIETO EL BOTON ENVIAR 
        pet_nuevo = Pet(nombre = request.POST["nombre"],raza=request.POST ["raza"],nivel=request.POST ["nivel"] )
        pet_nuevo.save()
        return render(request,  "inicio.html")
    return render(request, "pets/crear_pet.html")


@login_required
def ver_pet(request):

    todas_pet =Pet.objects.all()

    return render(request, "pets/ver_pet.html", {"total":todas_pet})


@login_required
def actualizar_pet (request, pet):

    pet_elegido = Pet.objects.get(id=pet)

    if request.method == "POST":

        formulario = PetFormulario(request.POST)

        if formulario.is_valid():
            
            info_dic = formulario.cleaned_data
            
            pet_elegido.nombre = info_dic["nombre"]
            pet_elegido.raza = info_dic["raza"]
            pet_elegido.nivel = info_dic["nivel"]

            pet_elegido.save()


            return render(request,  "inicio.html")
    else:

        formulario = PetFormulario(initial={"nombre": pet_elegido.nombre, "raza": pet_elegido.raza, "nivel": pet_elegido.nivel})

    return render(request, "pets/actualizar_pet.html", {"formu":formulario})

@login_required
def borrar_pet(request, pet):

    pet_elegido = Pet.objects.get(id=pet)

    pet_elegido.delete()

    return render(request, "inicio.html")




#Iniciar Sesion

def iniciar_sesion(request):

        if request.method == "POST":

            formulario = AuthenticationForm(request, data = request.POST)

            if formulario.is_valid():
            
                info_dic = formulario.cleaned_data
            
                usuario = authenticate(username = info_dic["username"], password = info_dic["password"])

                if usuario is not None:

                    login(request, usuario)


                    return render(request,  "inicio.html", {"mensaje" : f"Bienvenido {usuario}"})
            else:

                return render(request, "inicio.html", {"mensaje" : "ERROR EN LOS DATOS IINGRESADOS"})

        else:
            
            formulario = AuthenticationForm()

        return render(request, "registro/inicio_sesion.html", {"formu":formulario})


#Registrarse

def registrarse(request):
    
    if request.method == "POST":

        formulario = UserCreationForm(request.POST)

        if formulario.is_valid():

             formulario.save()
              
             return render (request, "inicio.html", {"mensaje" : "El usuario ha sido Creado con Exito."})
    else:

        formulario = UserCreationForm()

    return render(request, "registro/registro.html" , {"formu": formulario})


#cerrar sesion

def cerrar_sesion(request):

    logout(request)

    return render(request, "inicio.html", {"mensaje" : "El usuario ha cerrado la sesion con Exito."})
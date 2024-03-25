from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class ArmadurasFormulario(forms.Form):

    nombre_armadura = forms.CharField(max_length=30)
    tipo_armadura = forms.CharField(max_length=30)
    lv_armadura = forms.IntegerField()


class BuidsFormulario(forms.Form):

    nombre = forms.CharField(max_length = 60)
    tipo_daño = forms.CharField(max_length = 60)
    Total_daño = forms.IntegerField()


class PersonajeFormulario(forms.Form):

    nombre = forms.CharField(max_length = 60)
    raza = forms.CharField(max_length = 60)
    averno = forms.IntegerField()


class PetFormulario(forms.Form):

    nombre = forms.CharField(max_length = 60)
    raza = forms.CharField(max_length = 60)
    nivel = forms.IntegerField()


class RegistroUsuario(UserCreationForm):

    class Meta:

        model = User
        fields = ["username", "last_name", "first_name", "email", "password1", "password2"]


class EditarUsuario(UserChangeForm):

    password = None

    class Meta:

        model = User
        fields = ["last_name", "first_name", "email"]



class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()
    
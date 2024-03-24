from django import forms

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
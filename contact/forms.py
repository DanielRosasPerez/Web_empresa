# CREAMOS UN FORMULARIO:

from django import forms

class ContactForm(forms.Form):

     # Cuando usamos "required=True" hacemos estos campos obligatorios.
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={"class":"form-control", "placeholder":"Juan Pérez"}
    ), min_length=10, max_length=100)
    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
        attrs={"class":"form-control", "placeholder":"usuario@gmail.com"}
    ), min_length=10, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={"class":"form-control", "rows":5, "placeholder":"Escribe tu mensaje..."}
    ), min_length=30, max_length=1000) # Al igualar el parámetro "widget" a "forms.Textarea", creamos una caja de texto grande que nos servirá para insertar contenido.
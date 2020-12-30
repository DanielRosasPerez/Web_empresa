from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name="contact"), # Cuando en las URLs principales (aquellas que se encuentran en urls.py del proyecto), declaremos directamente en path a cada aplicación (por ejemplo; "contact/"), debemos dejar el path propio de la aplicación vacío ('').
]
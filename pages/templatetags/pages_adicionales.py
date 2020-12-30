# Debemos registrar a "templatetags" dentro de la libreria de "templates":

from django import template
from pages.models import Page

register = template.Library() # Aquí se lleva a cabo el registro del tag simple en la librería de templates.
@register.simple_tag # De esta manera, transformamos una función "normal" en un tag simple y lo registramos en la librería de templates.

def get_page_list(): # Creamos un nuevo template en donde hacer uso de este script:
    pages = Page.objects.all()
    return pages
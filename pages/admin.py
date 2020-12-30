from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ("title", "order") # De esta manera, en el panel de administrador se nos mostrará primero la columna "title" y después "order", ambos, con sus respectivos alias (Título y Orden).
 
admin.site.register(Page, PageAdmin)
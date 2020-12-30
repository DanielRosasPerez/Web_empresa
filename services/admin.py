from django.contrib import admin

from .models import Service # Importamos el modelo "Service" del directorio "models.py", el cual se encuentra
# en el mismo nivel de carpetas que este archivo "admin.py", por esa razón ocupamos el "." despues de "from".

class ServiceAdmin(admin.ModelAdmin): # Con la finalidad de mostrar los campos ocultos como sólo lectura.
    readonly_fields = ("created", "updated")

# Register your models here.

# admin.site.register(model, admin_class)
admin.site.register(Service, ServiceAdmin) # Hemos registrado nuestro modelo.
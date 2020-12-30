from django.contrib import admin
from .models import Link

# Register your models here.

class LinkAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated") # Hacemos visibles los campos "created" y "updated" en modo solo lectura.

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name="Personal").exists(): # Comprobamos si el usuario pertenece al grupo "Personal".
            return ("created", "updated", "key", "name")
        else:
            return ("created", "updated")

admin.site.register(Link, LinkAdmin)

from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Título")
    #content = models.TextField(verbose_name="Contenido")
    content = RichTextField(verbose_name="Contenido") # De esta manera, dentro del panel de administrador en el apartado de "Contenido", nos aparecerá un editor robusto para edir el contenido.
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:

        verbose_name = "Página"
        verbose_name_plural = "Páginas"
        ordering = ["order", "title"] # De esta manera, le decimos django que ordene los datos comenzando por "order" y despues por "title".

    def __str__(self):
        return self.title
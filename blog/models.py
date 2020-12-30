from django.db import models

# Create your models here. (EN REALIDAD, ESTO SERÍA EL EQUIVALENTE A TABLAS).

# Primer Modelo:
class Category(models.Model):

    name = models.CharField(max_length=100, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:

        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ["-created"] # Se ordena las instancias de las recientemente creadas a las más viejas.

    def __str__(self):
        return self.name

# Segundo Modelo:
from django.utils.timezone import now # Se importa la zona horario del lugar en donde se esta desarrollando el proyecto.
from django.contrib.auth.models import User # Importamos el modelo "User", el cual contiene a los usuarios registrados en nuestro panel de administrador.

class Post(models.Model):
    
    title = models.CharField(max_length=200, verbose_name="Título")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(verbose_name="Fecha de Publicación", default=now)
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True) # De esta manera el campo "image" se vuelve opcional. Es decir, podemos no subir una imagen.
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE) # Como parámetros pasamos los usuarios registrados, el verbose_name y "on_delete". Lo que hará valor "models.CASCADE" asignado al parámetro "on_delete", será eliminar en cascada todas las entradas relacionadas con este "autor". Esto mismo se aprecia en SQL. Otro valor posible para este parámetro es "models.PROTECT", el cual evita que se elimine esta entrada para evitar dejar vacios en nuestras tablas relacionadas con este autor. Sin embargo, de incluir imágenes, debemos (mandatoriamente), de hacer "null=True" y "blank=True" para poder permitir que el campo "image" quede vacío en la base de datos.
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts") # De esta forma relacionamos este modelo con el modelo "Category". La realzación es Muchos a Muchos dado que se van a seleccionar varias categorías para una sola entrada.
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:

        verbose_name = "Entrada" # Alias de la columna en donde se mostrarán las intancias creadas a partir de esta clase.
        verbose_name_plural = "Entradas" # Alias que se le dará a la clase o modelo. El cual aparece del aparece del lado izquierdo, debajo del nombre de la aplicación.
        ordering = ["-created"] # Ordena del más recientemente creado al más viejo.

    def __str__(self):
        return self.title # Nos devuelve como nombre el valor asignado al campo "title" de la instancia creada.
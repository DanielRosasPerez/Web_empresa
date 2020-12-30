from django.db import models

# Create your models here.
class Service(models.Model): # La clase Project esta heredando de la clase Model.

    # NOTA: CADA QUE AGREGUEMOS CAMPOS NUEVOS A NUESTRO MODELO, DEBEMOS CREAR LA MIGRACIÓN Y MIGRARLA A LA 
    # APLICACIÓN. Es decir:
    # 1. Creamos el/los campo(os) deseado(s) dentro de esta clase o modelo.
    # 2. Creamos la migración: python manage.py makemigrations <nombre_de_la_app>.
    # 3. Migramos (vaya la redundacia), la migración creada a la aplicación: python manage.py migrate <nombre_de_la_app>.

    Title = models.CharField(max_length=200, verbose_name="Título")
    
    Subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    
    Content = models.TextField(verbose_name="Contenido")
    
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    # upload_projects = "<carpeta_de_almacenamiento>", nos sirve para decirle al archivo imagen en donde debe
    # guardarse una vez alguien suba una imagen.
    
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación") # Se añadirá la hora y el día automáticamente cuando un objeto
    # de esta clase se genere.
    
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización") # Se añadirá la fecha y hora automáticamente cuando
    # cualquier objeto creado a partir de esta instancia se modifique.

    class Meta():

        verbose_name= "Lista Servicios" # Asignamos un alias a la columna que mostrará las instancias creadas
        # a partir del modelo "Service".

        verbose_name_plural="Servicios" # Asignamos un alias al "modelo".

        ordering=["-created"] # Las instancias creadas/modificadas a partir de este "modelo", se ordenarán 
        # considerando la fecha y hora de creación de la más actual a la más vieja. (Sin importar si la fecha de
        # modificaciones en caso de que se modifiquen. Es decir, si la más vieja se modifico, no por ello aparecerá
        # primero).

    def __str__(self):
        return self.Title # Nos muestra el nombre de la instacia.
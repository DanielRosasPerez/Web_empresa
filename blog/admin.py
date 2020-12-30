from django.contrib import admin
from .models import Category, Post

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    
    #list_display = ("title", "author", "published", "categories") # Para mostrar el nombre de una columna con una relación de "ManyToMany" (por ejemplo; "categories"), es necesario crear nuestros propios campos, de lo contario, no será posible mostrar esta columna.
    list_display = ("title", "author", "published", "post_categories") # De esta manera, podremos mostrar la columna "categories". Es importante crear un método con el mismo nombre (como se aprecia abajo con el método "post_categories"), para poder realizar la maniobra y mostrar esta columna.

    ordering = ("author", "published") # En caso de declarar solamente un elemento, debemos dejar una coma, es decir: ("author",). De otra forma, nos saldrá error.
    
    #search_fields = ("author__username", "categories__name") # De esta manera, estamos buscando en el campo "autor" (el cual de manera interna en la BD esta declarado como "username"); esta referencia se realiza con "__". Lo mismo ocurre con "categories". Fórmula: <nombre_dado_al_campo>__<nombre_por_default_dentro_de_la_BD>
    search_fields = ("title", "content") # De esta manera, generamos un widget de busqueda basado en el campo "title" y el campo "content". Es decir, al ingresar la palabra a encontrar dentro widget de busqueda generado, este buscará en el "Título" y en el "Contenido".
    
    date_hierarchy = "published" # De esta manera jerarquizamos los datos dentro del modelo "Post" basandos en el campo "published". Funcionaría como una especie de filtro, dejando solo aquella información que se encuentre dentro de un mes específico, una año, etc.
    
    list_filter = ("author__username", "categories__name") # A este parámetro podemos pasarle campos para que los filtre. Normalmente, estos campos para filtrar son relaciones, dado que suelen ser los que se van repitiendo. No tiene sentido añadir un filtro por título dado que solo se mostrarán post que tengan exactamente el mismo título.

    def post_categories(self, obj): # Creamos un método para poder mostrar la columna ManyToMany "categories".
        # "obj" representa a cada instancia dentro de la columna "categories". Por lo tanto, iremos iterando sobre estas.
        return ", ".join([row.name for row in obj.categories.all().order_by("name")]) # Es decir, estamos iterando sobre cada fila de la tabla (o modelo) "Post" y estamos extrayendo exclusivamente el valor correspondiente a la columna "categories" por cada fila. Posteriormente, dado que cada valor dentro de "categories" tiene una relación "ManyToMany", lo usamos para acceder al parámetro "name" de cada instacia creada a partir del modelo "Category".

    post_categories.short_description = "Categorías" # Estamos sobreescribiendo el atributo "short_description" (este atributo lo contiene cualquier método creado dentro de cada modelo), para poder mostrar un alias como nombre de la columna "categories".


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)

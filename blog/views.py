from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.

def blog(request):
    posts = Post.objects.all() # Nos devuelve todas las instancias generadas usando el modelo "Post".
    return render(request, "blog/blog.html", {"posts":posts})

def category(request, category_id):
    """
    Forma rudimentaria de filtrar contenido:
    #category = Category.objects.get(id=category_id) # "Model.objects.get(id=...)" nos permite recuperar las filas del modelo (o tabla), filtrando (para nuestro caso), por el "id" o "PRIMARY KEY" en el caso de SQL.
    
    category = get_object_or_404(Category, id=category_id) # En caso de no encontrar la página solicitada, nos aparecerá el error 404 (NOT FOUND), lo cual esta pensado para el usuario final.
    posts = Post.objects.filter(categories=category) # Filtramos las instancias creadas apartir del modelo Post, por categorias.
    
    return render(request, "blog/category.html", {"category":category, "posts":posts})
    """

    category = get_object_or_404(Category,id=category_id)
    return render(request, "blog/category.html", {"category":category})
    
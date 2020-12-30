from .models import Link

def diccionario_contexto(request): # Creamos esta función para extender las funcionalidades del diccionario de contexto.
    ctx = {} # ctx stands for contexto. Creamos el diccionario de contexto vacío.
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url # Hemos generado un diccionario con las redes sociales para cada key. Es decir, {"LINK_FACEBOOK": "www.facebook.com", ...}
    return ctx

# Al agregar el este script directamente a settings.py (más específicamente a "context_processors"), 
# podremos acceder desde cualquier template de cualquier aplicación a este diccionario.
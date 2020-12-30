from django.shortcuts import render
from .models import Service

# Create your views here.

def services(request):
    services = Service.objects.all() # Nos devuelve todos las instancias creadas a partir del modelo "Service".
    return render(request, "services/services.html", {"services": services})
    # {'services':services} es un diccionario de contexto.

    # Al solicitar acceder a la vista "services", (vaya la redudancia), solicitaremos accesar a 
    # "services/services.html" para después cargar el diccionario de contexto, el cual nos devolverá
    # una lista con los distintas instancias creadas a partir del modelo "Service". Finalmente
    # loopearemos sobre está. Este loop se aprecia en "services.html".
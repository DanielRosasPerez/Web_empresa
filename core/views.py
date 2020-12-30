from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, template_name="core/inicio.html")

def about(request):
    return render(request, template_name="core/about.html")

def store(request):
    #return HttpResponse("<h1>Bienvenidos</h1>")
    return render(request, template_name="core/store.html")
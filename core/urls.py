from django.urls import path
from . import views # from "el mismo directorio" import "views".

urlpatterns = [
    # Paths de la aplicación core:
    path('', views.home, name="home"),
    path("about/", views.about, name="about"), # De esta manera, en lugar de mostrar "core/about.html",
    # se mostrará "about/". Es decir path("<alias>", views.<función>, name="<nombre_de_la_función>")
    path("store/", views.store, name="store"),
]

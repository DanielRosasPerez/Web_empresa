from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    contact_form = ContactForm() # Estoy creando una instancia directamente desde la clase "ContactForm".

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid(): # Comprobamos si todos los campos obligatorios de nuestro formulario han sido llenados.
            name = request.POST.get("name", '') # Recuperamos los elementos del campo "name" (cuyo alias o verbose_name es Nombre). Por default se agrega una segunda opción (''), en caso de que no haya contenido en este campo.
            email = request.POST.get("email", '')
            content = request.POST.get("content", '')

            # Una vez hemos obtenido el valor de cada campo, enviamos el correo de confirmación y redireccionamos:
            email = EmailMessage(
                subject="La Caffettiera: Nuevo mensaje de contacto",
                body="De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                from_email="no-contestar@inbox.mailtrap.io",
                to=["daniel020197s@gmail.com", "papilor117DR@hotmal.com"],
                reply_to=[email], # Mandamos el correo a donde va a responder la persona que nos ha mandado el formulario.
                )
            try:
                email.send() # Al llamar a esta función mandaremos el email.
                return redirect(reverse("contact")+"?ok") # De esta manera, redireccionamos y nos llevará a la dirección (url), especificada en views (name="contact") y concatenara la cadena "?ok".
            except:
                # En caso de que algo salga mal, mostraremos el siguiente template:
                return redirect(reverse("contact")+"?fail")
            
    return render(request, "contact/contact.html", {"form":contact_form})
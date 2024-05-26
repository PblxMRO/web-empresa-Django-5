from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.
def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(data= request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Ceffettierra: Nuevo mensaje de contacto",
                "De {} <{}>\n\n{}".format(name, email, content),
                "juan.pablo.mro@gmail.com",
                ["juan.pablo.mro@gmail.com"],
                reply_to=[email]
            )
        try:
            email.send()
            return redirect(reverse('contact')+"?ok")
        except:
             #No se pudo enviar el mensaje, redireccionamos a Fail
             return redirect(reverse('contact')+"?fail")
    return render(request, "contact/contact.html", {'form': contact_form})
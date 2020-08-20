from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Banner, Images


def home(request):

    if request.method == "POST":
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contacto nuevo',
            ('\nNombre: ' + name + "\nEmail: " + email + "\nMensaje: " + message),
            settings.EMAIL_HOST_USER,
            ['arqauster@gmail.com'],
            fail_silently=False
        )
        return HttpResponseRedirect(reverse("home-home"))

    context = {
        "background": Banner.objects.all(),
        "images": Images.objects.all(),
    }

    return render(request, "home/home.html", context)
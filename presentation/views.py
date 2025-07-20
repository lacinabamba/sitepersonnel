from django.http import BadHeaderError
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
import ssl
import certifi
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())


def accueil(request):
    return render(request, 'presentation/accueil.html')

def about(request):
    return render(request, 'presentation/about.html')

def skills(request):
    return render(request, 'presentation/skills.html')

def projects(request):
    return render(request, 'presentation/projects.html')

def contact(request):
    context = {}
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"Nouveau message de {name}"
        full_message = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['lacina4698@gmail.com'])
            context["message_sent"] = True
        except BadHeaderError:
            context["error"] = True
        except Exception:
            context["error"] = True

    return render(request, 'presentation/contact.html', context)
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
    message_sent = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        subject = f"Nouveau message de {name}"
        full_message = f"Nom: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
        ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())
        send_mail(subject, full_message, settings.EMAIL_HOST_USER, ['lacina4698@gmail.com'])
        message_sent = True

    return render(request, 'presentation/contact.html', {'message_sent': message_sent})

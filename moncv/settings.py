"""
Django settings for moncv project.
"""

import os
from pathlib import Path
import ssl
import certifi
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Forcer la vérification SSL avec certifi (utile pour certaines plateformes)
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# =========================================================
# 🔐 SECURITY SETTINGS
# =========================================================
# BASE_DIR reste inchangé
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY depuis .env
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'change-me-in-env')

# DEBUG depuis .env
DEBUG = os.getenv('DEBUG', 'False') == 'True'

# ALLOWED_HOSTS
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '').split(',')

# =========================================================
# 📦 APPLICATIONS
# =========================================================
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'presentation',  # Ton app perso
]

# =========================================================
# 🌐 MIDDLEWARE
# =========================================================
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'moncv.urls'

# =========================================================
# 📂 TEMPLATES
# =========================================================
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'moncv.wsgi.application'

# =========================================================
# 🗄️ DATABASE
# =========================================================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# =========================================================
# 🔐 PASSWORD VALIDATION
# =========================================================
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# =========================================================
# 🌍 INTERNATIONALIZATION
# =========================================================
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Abidjan'
USE_I18N = True
USE_TZ = True

# =========================================================
# 📦 STATIC & MEDIA FILES
# =========================================================
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'presentation', 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Pour collectstatic

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# =========================================================
# 📧 EMAIL SETTINGS (Gmail SMTP)
# =========================================================
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', 'lacina4698@gmail.com')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', 'qprv inkr lgki oagt')

# =========================================================
# ✅ AUTRES CONFIG
# =========================================================
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEBUG=False

ALLOWED_HOSTS = ['.onrender.com', '127.0.0.1', 'localhost']

#.env
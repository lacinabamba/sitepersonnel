from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('presentation.urls')),  # Redirige vers l'app "presentation"
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),  # Mapear a la vista de inicio de sesión
    path('register/', views.register),  # Mapear a la vista de registro
    path('profile/', views.profile),  # Mapear a la vista de perfil
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),  
    path('register/', views.register),
    path('profile/', views.profile),  
    path('api/', include('module.urls'))
]

from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('module.urls')),
    path('user/', include('user.urls')),
    path('comments/', include('comments.urls')),
    path('exam/',include('exam.urls')),
    path('cource/',include('cource.urls')),
]

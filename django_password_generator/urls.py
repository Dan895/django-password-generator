"""
URL configuration for django_password_generator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from generator import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('about', views.about, name='about'),
    # la ruta inicial la declaran un par de '' vacios: esto muestra un 'Page not found'
    # esto es equivalente a '/' (el directorio raiz)
    path('', views.home, name='home'),
    # esta es la forma simple de llamarlo
    # path('password', views.password)
    
    # si queremos que el nombre de la pagina
    # sea uno y no importando como se llame en 
    # home.html usamos la propiedad 'name' y en 
    # home.html usamos la sintaxis especial
    # que proporciona django (ver home.html):
    path('generate-password', views.password, name='password')
]

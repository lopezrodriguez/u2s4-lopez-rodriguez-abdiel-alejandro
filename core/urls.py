from django.urls import path
# views: el archivo que acabás de escribir, en la misma carpeta
from . import views 

urlpatterns = [
    # '': todo lo que llegue a la raíz del sitio se delega a core/urls.py
    path('', views.inicio, name='inicio'), 

    path('servicios/', views.servicios, name='servicios'),
] 

from django.urls import path
from . import views

urlpatterns = [
    path('mensajes/', views.mensajes_lista, name='mensajes_lista'),
    path('crear/', views.crear_mensaje, name='crear_mensaje'),
]

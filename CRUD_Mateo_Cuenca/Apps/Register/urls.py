from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('buscarDoc/', views.buscarDoc),
    path('buscarDoc/formularioSuscriptor/', views.formularioSuscriptor),
    path('buscarDoc/formularioSuscriptor/registrarSuscriptor/',views.registrarSuscriptor),
    path('buscarDoc/formmodificarSuscriptor/', views.formmodificarSuscriptor),
    path('buscarDoc/confirmaModificacion/formmodificarSuscriptor/', views.formmodificarSuscriptor),
    path('buscarDoc/formmodificarSuscriptor/ModificarSuscriptor/', views.modificarSuscriptor),
    path('buscarDoc/confirmaModificacion/formmodificarSuscriptor/ModificarSuscriptor/', views.modificarSuscriptor),
    path('buscarDoc/confirmaModificacion/', views.confirmaModificacion),


]
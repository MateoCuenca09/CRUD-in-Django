from ast import If
from asyncio.windows_events import NULL
from email import message
from inspect import _void
from pickle import TRUE
from telnetlib import ENCRYPT
from tkinter import messagebox
from urllib import request
from django.forms import PasswordInput
from django.shortcuts import redirect, render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.hashers import make_password

from .models import Suscripcion, Suscriptor

from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView



# Create your views here.

def home(request):
    Listasuscripcion = Suscripcion.objects.all()
    Listasuscriptor = Suscriptor.objects.all()
    return render (request, "GestionSuscripciones.html", {"suscripcion": Listasuscripcion, "suscriptor": Listasuscriptor})


def buscarDoc(request):
     tipodocumento = request.POST['tipoDocumento']
     numDocumento = request.POST['numDocumento']
     if Suscriptor.objects.filter(NumeroDocumento=numDocumento,TipoDocumento=tipodocumento):
        suscriptor = Suscriptor.objects.get(NumeroDocumento=numDocumento,TipoDocumento=tipodocumento)
        suscripcion = Suscripcion.objects.get(IdSuscriptor = suscriptor.IdSuscriptor)
        if suscripcion.FechaFin == None:
          messages.info(request,"Usted tiene ya tiene una suscripcion vigente!")
          return redirect ('/')

        else:
          return render(request,"ConsultaAlta.html", {"suscriptor":suscriptor})           

     else:
        return render(request, "DarDeAlta.html", {"numDocumento": numDocumento,"tipoDocumento": tipodocumento})


def registrarSuscriptor(request):
    if request.method == 'POST':
     tipodocumento = request.POST['tipoDocumento']
     numDocumento = request.POST['numDocumento']
     nombre = request.POST['txtNombre']
     apellido = request.POST['txtApellido']
     direccion = request.POST['txtDireccion']
     email = request.POST['email']
     telefono = request.POST['numTelefono']
     nombreUsuario = request.POST['txtNombreUsuario']
     password = request.POST['password']
     encryptpas = make_password(password)
     if Suscriptor.objects.filter(NumeroDocumento=numDocumento,TipoDocumento=tipodocumento):
      message.info(request,"Error al registrar, ya se encuentra registrado!")
      return redirect('/')
     else:
      suscriptor = Suscriptor.objects.create(
       TipoDocumento = tipodocumento,
        NumeroDocumento = numDocumento, 
        Nombre = nombre,
        Apellido = apellido, 
        Direccion = direccion,
        Email = email,
        Telefono = telefono,
        NombreUsuario = nombreUsuario,
        Password = encryptpas
        )    
     suscriptcion = Suscripcion.objects.create(
      IdSuscriptor = suscriptor,
      FechaAlta = datetime.now(),
      )  
     messages.info(request,"Suscriptor Registrado con exito")
     return render(request,"RegistroSucces.html",{"nombreUsuario":nombreUsuario,"password":password})



def formularioSuscriptor(request):
    tipodocumento = request.POST['tipoDocumento']
    numDocumento = request.POST['numDocumento']     
    return render(request, "RegistrarSuscriptor.html", {"numDocumento": numDocumento,"tipoDocumento": tipodocumento})

def formmodificarSuscriptor(request):
  if 'modificar' in request.POST:
    tipoDocumento = request.POST['tipoDocumento']
    numDocumento = request.POST['numDocumento']
    return render(request,"ModificarSuscriptor.html",{"numDocumento": numDocumento,"tipoDocumento": tipoDocumento})
  elif 'registrar_suscripcion' in request.POST:
    tipoDocumento = request.POST['tipoDocumento']
    numDocumento = request.POST['numDocumento']
    suscriptor = Suscriptor.objects.get(NumeroDocumento=numDocumento,TipoDocumento=tipoDocumento)

    suscripcion = Suscripcion.objects.get(IdSuscriptor = suscriptor.IdSuscriptor)
    if suscripcion.FechaFin == None:
       messages.info(request,"Usted tiene ya tiene una suscripcion vigente!")
       return redirect ('/')

    else:
      suscripcion.FechaAlta = datetime.now()
      suscripcion.FechaFin = None
      suscripcion.MotivoFin = None
      suscripcion.save()
      messages.info(request,"Suscripcion Registrada con exito!")
      return redirect('/')
    
def modificarSuscriptor(request):
     tipodocumento = request.POST['tipoDocumento']
     numDocumento = request.POST['numDocumento']
     nombre = request.POST['txtNombre']
     apellido = request.POST['txtApellido']
     direccion = request.POST['txtDireccion']
     email = request.POST['email']
     telefono = request.POST['numTelefono']
     nombreUsuario = request.POST['txtNombreUsuario']
     password = request.POST['password']
     encryptpas = make_password(password)
     suscriptor = Suscriptor.objects.get(NumeroDocumento=numDocumento,TipoDocumento=tipodocumento)
     suscriptor.Nombre = nombre
     suscriptor.Apellido = apellido
     suscriptor.Direccion = direccion
     suscriptor.Email = email
     suscriptor.Telefono = telefono
     suscriptor.NombreUsuario = nombreUsuario
     suscriptor.Password = encryptpas
     suscriptor.save()
     messages.info(request,"Se han modificado los datos con EXITO")
     return redirect('/')


def confirmaModificacion(request):
  tipodocumento = request.POST['tipoDocumento']
  numDocumento = request.POST['numDocumento']  
  suscriptor = Suscriptor.objects.get(NumeroDocumento=numDocumento,TipoDocumento=tipodocumento)
  return render(request, "NuevaSuscripcion.html", {"suscriptor":suscriptor})

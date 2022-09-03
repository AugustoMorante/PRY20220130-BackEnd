from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):
    usuarios = Usuario.objects.all()
    return render(request, "gestionUsuarios.html", {"usuarios": usuarios})

def registrarUsuario(request):
    usuario_codigo = request.POST['numUsuario_Codigo']
    usuario_correo = request.POST['txtUsuario_Correo']
    usuario_contrasena = request.POST['txtUsuario_Contrasena']
    usuario_rol = request.POST['txtUsuario_Rol']

    usuario = Usuario.objects.create(
        Usuario_Codigo = usuario_codigo, Usuario_Correo = usuario_correo, Usuario_Contrasena = usuario_contrasena, Usuario_Rol = usuario_rol)
    return redirect('/')

def edicionUsuario(request, usuario_codigo):
    usuario = Usuario.objects.get(Usuario_Codigo = usuario_codigo)
    return render(request, "edicionUsuario.html", {"usuario": usuario})

def editarUsuario(request):
    usuario_codigo = request.POST['numUsuario_Codigo']
    usuario_correo = request.POST['txtUsuario_Correo']
    usuario_contrasena = request.POST['txtUsuario_Contrasena']
    usuario_rol = request.POST['txtUsuario_Rol']

    usuario = Usuario.objects.get(Usuario_Codigo = usuario_codigo)
    usuario.Usuario_Correo = usuario_correo
    usuario.Usuario_Contrasena = usuario_contrasena
    usuario.Usuario_Rol = usuario_rol
    usuario.save()

    return redirect('/')

def eliminarUsuario(request, usuario_codigo):
    usuario = Usuario.objects.get(Usuario_Codigo =  usuario_codigo)
    usuario.delete()
    return redirect('/')
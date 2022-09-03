from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarUsuario/', views.registrarUsuario),
    path('edicionUsuario/<usuario_codigo>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('eliminarUsuario/<usuario_codigo>', views.eliminarUsuario)
]
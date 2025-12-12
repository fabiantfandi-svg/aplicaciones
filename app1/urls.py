from django.urls import path
from .views import UsuarioLeerCrear, UsuarioEditarEliminar, mostrar_usuarios

urlpatterns = [
    path('usuario/', UsuarioLeerCrear.as_view(), name='usu'),
    path('usuarios/<int:pk>', UsuarioEditarEliminar.as_view(), name='usu-detail'),
    path('mostrar/', mostrar_usuarios, name='mostrar_usuarios'),
]

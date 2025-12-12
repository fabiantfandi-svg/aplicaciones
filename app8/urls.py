from django.urls import path
from .views import BibliotecaLeerCrear,BibliotecaEditarEliminar, biblioteca_template

urlpatterns = [
    path('biblioteca/',BibliotecaLeerCrear.as_view(),name='bibl'),
    path('bibliotecas/<int:pk>',BibliotecaEditarEliminar.as_view(),name='bibl-detail'),
    path('mostrar/', biblioteca_template, name='app8_mostrar'),
]
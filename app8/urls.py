from django.urls import path
from .views import BibliotecaLeerCrear,BibliotecaEditarEliminar

urlpatterns = [
    path('biblioteca/',BibliotecaLeerCrear.as_view(),name='bibl'),
    path('bibliotecas/<int:pk>',BibliotecaEditarEliminar.as_view(),name='bibl-detail')
]
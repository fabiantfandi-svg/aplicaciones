from django.urls import path
from .views import ArticuloLeerCrear,ArticuloEditarEliminar,articulo_template

urlpatterns = [
    path('articulo/',ArticuloLeerCrear.as_view(),name='arti'),
    path('articulos/<int:pk>',ArticuloEditarEliminar.as_view(),name='arti-detail'),
    path('mostrar/', articulo_template, name='app3_mostrar'),
]
from django.urls import path
from .views import ArticuloLeerCrear,ArticuloEditarEliminar

urlpatterns = [
    path('articulo/',ArticuloLeerCrear.as_view(),name='arti'),
    path('articulos/<int:pk>',ArticuloEditarEliminar.as_view(),name='arti-detail')
]
from django.urls import path
from .views import ArticuloEtiquetaLeerCrear,ArticuloEtiquetaEditarEliminar, articulo_etiqueta_template

urlpatterns = [
    path('artieti/',ArticuloEtiquetaLeerCrear.as_view(),name='areq'),
    path('artisetis/<int:pk>',ArticuloEtiquetaEditarEliminar.as_view(),name='areq-detail'),
    path('mostrar/', articulo_etiqueta_template, name='app9_mostrar'),
]
from django.urls import path
from .views import EtiquetaLeerCrear,EtiquetaEditarEliminar, etiqueta_template

urlpatterns = [
    path('etiqueta/',EtiquetaLeerCrear.as_view(),name='etiq'),
    path('etiquetas/<int:pk>',EtiquetaEditarEliminar.as_view(),name='etiq-detail'),
    path('mostrar/', etiqueta_template, name='app9_mostrar'),
]
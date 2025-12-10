from django.urls import path
from .views import EtiquetaLeerCrear,EtiquetaEditarEliminar

urlpatterns = [
    path('etiqueta/',EtiquetaLeerCrear.as_view(),name='etiq'),
    path('etiquetas/<int:pk>',EtiquetaEditarEliminar.as_view(),name='etiq-detail')
]
from django.urls import path
from .views import ArticuloEtiquetaLeerCrear,ArticuloEtiquetaEditarEliminar

urlpatterns = [
    path('artieti/',ArticuloEtiquetaLeerCrear.as_view(),name='areq'),
    path('artisetis/<int:pk>',ArticuloEtiquetaEditarEliminar.as_view(),name='areq-detail')
]
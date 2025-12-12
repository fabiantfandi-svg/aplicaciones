from django.urls import path
from .views import CategoriaLeerCrear,CategoriaEditarEliminar, mostrar_categorias

urlpatterns = [
    path('categoria/',CategoriaLeerCrear.as_view(),name='cate'),
    path('categorias/<int:pk>',CategoriaEditarEliminar.as_view(),name='cate-detail'),
    path('mostrar/', mostrar_categorias, name='mostrar_categorias'),
]


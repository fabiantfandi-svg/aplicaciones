from django.urls import path
from .views import CategoriaLeerCrear,CategoriaEditarEliminar

urlpatterns = [
    path('categoria/',CategoriaLeerCrear.as_view(),name='cate'),
    path('categorias/<int:pk>',CategoriaEditarEliminar.as_view(),name='cate-detail')
]
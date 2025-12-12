from django.urls import path
from .views import FavoritoLeerCrear,FavoritoEditarEliminar, favorito_template

urlpatterns = [
    path('favorito/',FavoritoLeerCrear.as_view(),name='favo'),
    path('favoritos/<int:pk>',FavoritoEditarEliminar.as_view(),name='favo-detail'),
    path('mostrar/', favorito_template, name='app7_mostrar'),
]
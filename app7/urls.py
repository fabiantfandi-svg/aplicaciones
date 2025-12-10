from django.urls import path
from .views import FavoritoLeerCrear,FavoritoEditarEliminar

urlpatterns = [
    path('favorito/',FavoritoLeerCrear.as_view(),name='favo'),
    path('favoritos/<int:pk>',FavoritoEditarEliminar.as_view(),name='favo-detail')
]
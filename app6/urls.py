from django.urls import path
from .views import ComentarioLeerCrear,ComentarioEditarEliminar

urlpatterns = [
    path('comentario/',ComentarioLeerCrear.as_view(),name='come'),
    path('comentarios/<int:pk>',ComentarioEditarEliminar.as_view(),name='come-detail')
]
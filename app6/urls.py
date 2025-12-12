from django.urls import path
from .views import ComentarioLeerCrear,ComentarioEditarEliminar, comentario_template

urlpatterns = [
    path('comentario/',ComentarioLeerCrear.as_view(),name='come'),
    path('comentarios/<int:pk>',ComentarioEditarEliminar.as_view(),name='come-detail'),
    path('mostrar/', comentario_template, name='app6_mostrar'),
]
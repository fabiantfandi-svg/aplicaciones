from django.urls import path
from .views import RevisionLeerCrear,RevisionEditarEliminar, revision_template

urlpatterns = [
    path('revision/',RevisionLeerCrear.as_view(),name='revis'),
    path('revisiones/<int:pk>',RevisionEditarEliminar.as_view(),name='revis-detail'),
    path('mostrar/', revision_template, name='app5_mostrar'),
]
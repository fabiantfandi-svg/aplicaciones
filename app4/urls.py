from django.urls import path
from .views import RevisorLeerCrear,RevisorEditarEliminar,revisor_template

urlpatterns = [
    path('revisor/',RevisorLeerCrear.as_view(),name='revi'),
    path('revisores/<int:pk>',RevisorEditarEliminar.as_view(),name='revi-detail'),
    path('mostrar/', revisor_template, name='app4_mostrar'),
]
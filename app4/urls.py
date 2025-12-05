from django.urls import path
from .views import RevisorLeerCrear,RevisorEditarEliminar

urlpatterns = [
    path('revisor/',RevisorLeerCrear.as_view(),name='revi'),
    path('revisores/<int:pk>',RevisorEditarEliminar.as_view(),name='revi-detail')
]
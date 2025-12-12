from django.shortcuts import render
from .models import Revisor
from .serializers import RevisorSerializers
from rest_framework import generics

class RevisorLeerCrear(generics.ListCreateAPIView):
    queryset = Revisor.objects.all()
    serializer_class = RevisorSerializers

class RevisorEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Revisor.objects.all()
    serializer_class = RevisorSerializers
def revisor_template(request):
    revisores = Revisor.objects.all()
    return render(request, "app4/mostrar.html", {"revisores": revisores})

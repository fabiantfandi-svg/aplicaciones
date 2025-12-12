from django.shortcuts import render
from .models import Etiqueta
from .serializers import EtiquetaSerializers
from rest_framework import generics

class EtiquetaLeerCrear(generics.ListCreateAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializers

class EtiquetaEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etiqueta.objects.all()
    serializer_class = EtiquetaSerializers
def etiqueta_template(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, "app9/mostrar.html", {"etiquetas": etiquetas})

from django.shortcuts import render
from .models import ArticuloEtiqueta
from .serializers import ArticuloEtiquetaSerializers
from rest_framework import generics

class ArticuloEtiquetaLeerCrear(generics.ListCreateAPIView):
    queryset = ArticuloEtiqueta.objects.all()
    serializer_class = ArticuloEtiquetaSerializers

class ArticuloEtiquetaEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticuloEtiqueta.objects.all()
    serializer_class = ArticuloEtiquetaSerializers
def articulo_etiqueta_template(request):
    artieti = ArticuloEtiqueta.objects.all()
    return render(request, "app10/mostrar.html", {"artieti": artieti})

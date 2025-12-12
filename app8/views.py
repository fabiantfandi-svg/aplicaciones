from django.shortcuts import render
from .models import Biblioteca
from .serializers import BibliotecaSerializers
from rest_framework import generics

class BibliotecaLeerCrear(generics.ListCreateAPIView):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializers

class BibliotecaEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Biblioteca.objects.all()
    serializer_class = BibliotecaSerializers
def biblioteca_template(request):
    biblioteca = Biblioteca.objects.all()
    return render(request, "app8/mostrar.html", {"biblioteca": biblioteca})

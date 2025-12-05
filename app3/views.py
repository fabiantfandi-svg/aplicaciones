from django.shortcuts import render
from .models import Articulo
from .serializers import ArticuloSerializers
from rest_framework import generics

class ArticuloLeerCrear(generics.ListCreateAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializers

class ArticuloEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializers
from django.shortcuts import render
from .models import Categoria
from .serializers import CategoriaSerializers
from rest_framework import generics

class CategoriaLeerCrear(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers

class CategoriaEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializers
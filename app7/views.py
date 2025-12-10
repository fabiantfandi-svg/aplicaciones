from django.shortcuts import render
from .models import Favorito
from .serializers import FavoritoSerializers
from rest_framework import generics

class FavoritoLeerCrear(generics.ListCreateAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializers

class FavoritoEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializers

from django.shortcuts import render
from .models import Usuario
from .serializers import UsuarioSerializers
from rest_framework import generics

class UsuarioLeerCrear(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers
class UsuarioEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializers

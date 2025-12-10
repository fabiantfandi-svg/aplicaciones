from django.shortcuts import render
from .models import Comentario
from .serializers import ComentarioSerializers
from rest_framework import generics

class ComentarioLeerCrear(generics.ListCreateAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializers

class ComentarioEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializers

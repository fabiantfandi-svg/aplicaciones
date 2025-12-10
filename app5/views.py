from django.shortcuts import render
from .models import Revision
from .serializers import RevisionSerializers
from rest_framework import generics

class RevisionLeerCrear(generics.ListCreateAPIView):
    queryset = Revision.objects.all()
    serializer_class = RevisionSerializers

class RevisionEditarEliminar(generics.RetrieveUpdateDestroyAPIView):
    queryset = Revision.objects.all()
    serializer_class = RevisionSerializers

from rest_framework import serializers
from .models import Revision

class RevisionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Revision
        fields = ['id_revision','articulo','revisor','fecha_asignacion','fecha_completa','comentarios','calificacion','recomendacion']
from rest_framework import serializers
from .models import Revisor

class RevisorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Revisor
        fields = ['id_revisor','usuario','area_expertise','max_articulos','disponible','fecha_registro']
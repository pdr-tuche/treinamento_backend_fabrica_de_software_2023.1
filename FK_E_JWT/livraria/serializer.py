from rest_framework import serializers
from .models import Livraria
class LivrariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livraria
        fields= '__all__'
from rest_framework import serializers
from .models import Pote

class PoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pote
        fields = '__all__'
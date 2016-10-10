from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from home.models import Historico_irrigacao





class HistoricoCreateSerializer(ModelSerializer):
    class Meta:
        model = Historico_irrigacao
        fields = [
            'pote',
            'hora_do_acionamento',
            'umidade_inicio',
        ]



class HistoricoDetailSerializer(ModelSerializer):
    class Meta:
        model = Historico_irrigacao
        fields = [
            'pote',
            'hora_do_acionamento',
            'umidade_inicio',
        ]
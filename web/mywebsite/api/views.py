from django.shortcuts import render

# Create your views here.

from .serializers import HistoricoCreateSerializer, HistoricoDetailSerializer
from django.db.models import Q
from rest_framework import viewsets
from home.models import Historico_irrigacao
from rest_framework.generics import CreateAPIView, ListAPIView





# Create your views here.
class HistoricoCreateAPIView(CreateAPIView):
    queryset = Historico_irrigacao.objects.all()
    serializer_class = HistoricoCreateSerializer



class HistoricoListAPIView(ListAPIView):

    serializer_class = HistoricoDetailSerializer
    def get_queryset(self, *args, **kwargs):

        queryset_list = Historico_irrigacao.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(pote__codigo__icontains=query)|
                Q(umidade_inicio__icontains=query)
            ).distinct()
        return queryset_list






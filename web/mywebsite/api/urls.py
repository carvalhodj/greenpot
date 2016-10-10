from django.conf.urls import url
from django.contrib import admin

from .views import HistoricoCreateAPIView, HistoricoListAPIView



urlpatterns = [

    url(r'^$', HistoricoListAPIView.as_view(), name='list'),
    url(r'^create/$', HistoricoCreateAPIView.as_view(), name='create'),




]
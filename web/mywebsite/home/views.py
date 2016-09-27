from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy
from .models import Planta, Pote
from home.forms import RegistroForm, MeuForm


class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'all_plantas'

    def get_queryset(self):
        return Planta.objects.all()


class RegistrarUsuario(CreateView):
    model = User
    template_name = 'home/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home')

class DetailView(generic.DetailView):

    model = Planta
    template_name = 'home/detail.html'

class PoteCreate(CreateView):

    model = Pote
    template_name = 'home/album_form.html'
    form_class= MeuForm
    success_url = reverse_lazy('home')

  
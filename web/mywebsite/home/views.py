from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy
from .models import Planta, Pote, Usuario_Pote
from home.forms import RegistroForm, MeuForm




class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'all_plantas'

    def get_queryset(self):
        usuario = self.request.user
        teste = Usuario_Pote.objects.filter(user=usuario)
        print(teste)
        return teste


class RegistrarUsuario(CreateView):
    model = User
    template_name = 'home/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('home')

class DetailView(generic.DetailView):

    model = Planta
    template_name = 'home/detail.html'

class PoteCreate(View):

    model = Pote


    form_class= MeuForm
    template_name = 'home/album_form.html'

    def get(self, request):
        form =self.form_class(None)
        return render(request, self.template_name,{'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            pote = form.save(commit=False)

            codigo = form.cleaned_data['codigo']
            planta = form.cleaned_data['planta']
            pote.save()
            teste = Pote.objects.get(codigo=codigo)
            print(teste.pk)
            username = request.user
            print(username.pk)

            userpote = Usuario_Pote()
            userpote.user = username
            userpote.pote = teste
            userpote.save()

            return redirect('home')









        return render(request, self.template_name, {'form': form})








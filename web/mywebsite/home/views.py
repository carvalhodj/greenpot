from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy
from .models import Planta, Pote, Usuario_Pote
from home.forms import RegistroForm, MeuForm, ContactForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PoteSerializer

from .mqttClient import Teste

#from .forms import SignUpForm


class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'all_plantas'

    def get_queryset(self):
        usuario = self.request.user
        potes = Usuario_Pote.objects.filter(user=usuario)
        return potes




def contact(request):
    form = ContactForm(request.POST or None)

    context = {
        "form": form,
    }
    return render(request, "home/forms.html", context)




class DetailView(generic.DetailView):

    model = Planta
    template_name = 'home/detail.html'

class RegistrarUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = 'home/cadastro_form.html'

    #success_url = reverse_lazy('home')
    def get(self, request):
        form =self.form_class(None)
        return render(request, self.template_name,{'form':form})
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            pote = form.save(commit=False)
            pote.save()

            return redirect('login')
        return render(request, self.template_name, {'form': form})


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
            pote.save()
            x = Teste()

            teste = Pote.objects.get(codigo=codigo)
            username = request.user
            umidade = teste.planta.umidade
            x.EnviarUmidade(umidade)
            userpote = Usuario_Pote()
            userpote.user = username
            userpote.pote = teste
            userpote.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})


class PoteUpdate(UpdateView):
    model = Pote
    fields = ['codigo','planta']

class PoteDelete(DeleteView):
    model = Pote
    success_url = reverse_lazy('home')

class PoteList(APIView):

    def get(self, request):
        potes = Pote.objects.all()
        serializer = PoteSerializer(potes, many=True)
        return Response(serializer.data)

    def post(self):
        pass





from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.core.urlresolvers import reverse_lazy
from .models import Planta, Pote, Usuario_Pote, Historico_irrigacao
from home.forms import RegistroForm, MeuForm, ContactForm

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PoteSerializer
from home.controler import cadastroControler,BuscarControler,listAdapterControler

#from mqttClient import Commqtt


#commqtt = Commqtt()


cadastro = cadastroControler.CadastroControler()

buscar = BuscarControler.BuscarControler()

listadapter = listAdapterControler.ListAdapter()

class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'all_plantas'
    def get_queryset(self):
        usuario = self.request.user
        lista = listadapter.ListAdapterHome(usuario)
        return lista


def contact(request):
    form = ContactForm(request.POST or None)

    context = {"form": form,}
    return render(request, "home/forms.html", context)


def historico(request, codigo):

    post = get_object_or_404(Pote, codigo=codigo)
    historicopote = buscar.BuscarHistoricoPote(post)
    historicop = list(reversed(historicopote))
    return render(request, 'home/historico.html',{'historicopote': historicop})

def historicoapi(request, codigo):

    return render(request, 'home/historicoapi.html',{'codigo':codigo})

def PoteOn(request, codigo):

    post = get_object_or_404(Pote, codigo=codigo)
    post.estado = 1
    post.save()
    commqtt.AcionamentoPote(1)

    return redirect('home')


def PoteOff(request, codigo):
    post = get_object_or_404(Pote, codigo=codigo)
    post.estado = 0
    post.save()
    commqtt.AcionamentoPote(0)

    return redirect('home')

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
            #codigo = form.cleaned_data['codigo']
            usuario = request.user
            cadastro.CadastrarUsuarioPote(pote, usuario)
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






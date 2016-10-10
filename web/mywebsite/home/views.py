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




from .controler import CadastroControler, BuscarControler

#from .forms import SignUpForm

cadastro = CadastroControler()

buscar = BuscarControler()

class HomeView(generic.ListView):
    template_name = 'home/home.html'
    context_object_name = 'all_plantas'

    def get_queryset(self):
        usuario = self.request.user
        potes = Usuario_Pote.objects.filter(user=usuario)
        return potes

class HistoricoView(generic.DetailView):
    context_object_name = 'historico_list'
    template_name = 'home/historico.html'
    model = Pote


    def get_context_data(self,**kwargs):
        context = super(HistoricoView, self).get_context_data(**kwargs)
        context['historico']= Historico_irrigacao.objects.all()


        return context



def contact(request):
    form = ContactForm(request.POST or None)

    context = {
        "form": form,
    }
    return render(request, "home/forms.html", context)


def historico(request, codigo):
    post = get_object_or_404(Pote, codigo=codigo)
    historicopote = Historico_irrigacao.objects.filter(pote=post)
    return render(request, 'home/historico.html',{'historicopote': historicopote})



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
    # Mandar uma msg MqTT para resetar o vaso

class PoteList(APIView):

    def get(self, request):
        potes = Pote.objects.all()
        serializer = PoteSerializer(potes, many=True)
        return Response(serializer.data)

    def post(self):
        pass





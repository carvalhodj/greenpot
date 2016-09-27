from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  django import forms
from .models import Planta, Pote

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',

        ]
        labels = {
             'username': 'Nome do usuario',
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'email':'e-mail',
        }


class MeuForm(forms.ModelForm):
    # Cria Conteudo


    # Define Widgets
    codigo = forms.CharField(required=True)
    planta = forms.ModelChoiceField(queryset= Planta.objects.all().order_by('id'), widget=forms.Select)
    # Associa formulario ao modelo
    class Meta:
        model = Pote
        fields = [
            'codigo',
            'planta',

        ]
        labels = {
            'codigo': 'Codigo',
            'planta': 'Nome da planta',

        }

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from  django import forms
from .models import Planta, Pote






class ContactForm(forms.Form):
    username = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

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

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()




    def clean_username(self):
        cd = self.cleaned_data
        name = cd.get('username')
        print len(name)
        if len(name)< 3:
            raise forms.ValidationError("Porfavor nome maior")
        return name

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

    def clean_codigo(self):
        pote = self.cleaned_data
        codigo = pote.get('codigo')
        if len(codigo) != 10:
            raise forms.ValidationError("Codigo deve ter 10 digitos")
            return codigo
        try:
            pote = Pote.objects.get(codigo=codigo)
            raise forms.ValidationError("Pote existe no sistema")
            return codigo
        except Pote.DoesNotExist:
            pode = None
            return codigo


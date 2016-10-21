from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
from django.conf import settings
# Create your models here.

class Planta(models.Model):
    nome = models.CharField(max_length=250)
    planta_logo = models.CharField(max_length=1000)
    descricao_planta = models.CharField(max_length=1500)
    umidade = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return u'{0}'.format(self.nome)


class Pote(models.Model):
    def __str__(self):
        return str(self.codigo)
    codigo = models.IntegerField(primary_key=True)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    estado = models.BooleanField(default=1)
    regiao = models.CharField(max_length=10)


class Usuario_Pote(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pote = models.ForeignKey(Pote, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username +  " " + " " + str(self.pote.codigo)

class Historico_irrigacao(models.Model):
    pote = models.ForeignKey(Pote, on_delete=models.CASCADE)
    hora_do_acionamento = models.CharField(max_length=10)
    umidade_inicio = models.CharField(max_length=10)
    hora_do_desligamento = models.CharField(max_length=10)
    umidade_final = models.CharField(max_length=10)
    data = models.DateTimeField(default=date.today(), editable=False,)
    def __str__(self):
        return self.hora_do_acionamento





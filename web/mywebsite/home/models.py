from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.conf import settings
# Create your models here.

class Planta(models.Model):
    nome = models.CharField(max_length=250)

    planta_logo = models.CharField(max_length=1000)

    descricao_planta = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.nome

    def __unicode__(self):
        return u'{0}'.format(self.nome)


class Pote(models.Model):
    def __str__(self):
        return self.codigo
    codigo = models.CharField(max_length=10)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)


class Usuario_Pote(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pote = models.ForeignKey(Pote, on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username +  " " +" " + self.pote.codigo








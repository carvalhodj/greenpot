from .models import Planta, Pote, Usuario_Pote, Historico_irrigacao
from DominioDTO import AdapterHistoricoUmidadeAtual


class CadastroControler:
    def CadastrarPote(self, pote):
        pote.save()
        umidade = pote.planta.umidade
        #commqtt.EnviarUmidade(umidade)


    def CadastrarUsuarioPote(self, pote, user):
        self.CadastrarPote(pote)
        userpote = Usuario_Pote()
        userpote.user = user
        userpote.pote = pote
        userpote.save()
    def CadastrarHistoricoIrrigacao(self,pote,hora,umidade):
        historico = Historico_irrigacao()
        historico.pote = pote
        historico.hora_do_acionamento = hora
        historico.umidade_inicio = umidade
        historico.save()

class BuscarControler:
    def BuscarPoteCodigo(self,codigo):
        pote = Pote.objects.get(codigo=codigo)
        return pote
    def BuscarHistoricoPote(self, pote ):
        historicopote = Historico_irrigacao.objects.filter(pote=pote)
        return historicopote
    def BuscarPostesUsuario(self,usuario):
        potes = Usuario_Pote.objects.filter(user=usuario)
        return potes


class ListAdapter:
    def ListAdapterHome(self, usuario):
        buscar = BuscarControler()
        potes=buscar.BuscarPostesUsuario(usuario)
        lista = []
        for x in potes:
            historicopote = buscar.BuscarHistoricoPote(x.pote)
            if len(historicopote) != 0:
                ultimo = historicopote[len(historicopote) - 1]
                historicoumidadeatual = AdapterHistoricoUmidadeAtual(x, ultimo.umidade_inicio)
                lista.append(historicoumidadeatual)
            else:
                historicoumidadeatual = AdapterHistoricoUmidadeAtual(x, '')
                lista.append(historicoumidadeatual)
        return lista










































'''
usuario = self.request.user
potes = Usuario_Pote.objects.filter(user=usuario)
lista = []
for x in potes:

    historicopote = Historico_irrigacao.objects.filter(pote=x.pote)
    if len(historicopote) != 0:
        print historicopote
        ultimo = historicopote[len(historicopote) - 1]
        print ultimo
        print ultimo.umidade_inicio
        historicoumidadeatual = AdapterHistoricoUmidadeAtual(x, ultimo.umidade_inicio)
        lista.append(historicoumidadeatual)
    else:

        historicoumidadeatual = AdapterHistoricoUmidadeAtual(x, '')
        lista.append(historicoumidadeatual)

return lista
'''
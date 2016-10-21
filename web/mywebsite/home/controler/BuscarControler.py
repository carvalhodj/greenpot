from home.models import Planta, Pote, Usuario_Pote, Historico_irrigacao
from datetime import date



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

    def BuscarUltimaInsercaoHistorico(self,historico):
        ultimo = historico[len(historico) - 1]
        return ultimo

    def BuscarPotesPlantaRegiao(self, planta,regiao):
        potes = Pote.objects.filter(planta=planta,regiao=regiao)
        return potes

    def BuscarAcionamentoDia(self, pote):
        historicopote = Historico_irrigacao.objects.filter(pote=pote,data=date.today())
        acionamentos = len(historicopote)
        return acionamentos
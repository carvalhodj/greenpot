from home.models import Planta, Pote, Usuario_Pote, Historico_irrigacao
from home.dominioDTO.AdapterHistoricoUmidadeAtualDTO import AdapterHistoricoUmidadeAtual
from home.controler.BuscarControler import BuscarControler
from home.outlier.calOutilier import calcularOutilier
calcular = calcularOutilier()
class ListAdapter:
    def ListAdapterHome(self, usuario):
        buscar = BuscarControler()
        potes=buscar.BuscarPostesUsuario(usuario)
        lista = []
        for x in potes:
            historicopote = buscar.BuscarHistoricoPote(x.pote)
            if len(historicopote) != 0:
                ultimo = buscar.BuscarUltimaInsercaoHistorico(historicopote)
                if (ultimo.umidade_final == ""):
                    historicoumidadeatual = AdapterHistoricoUmidadeAtual(x, ultimo.umidade_inicio)
                else:
                    historicoumidadeatual = AdapterHistoricoUmidadeAtual(x, ultimo.umidade_final)

            else:
                historicoumidadeatual = AdapterHistoricoUmidadeAtual(x, '')
            outpote = calcular.OutilierPote(x.pote)
            historicoumidadeatual.setAlerta(outpote)

            lista.append(historicoumidadeatual)
        return lista

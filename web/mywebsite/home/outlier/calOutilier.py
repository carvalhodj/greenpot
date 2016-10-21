from home.controler.BuscarControler import BuscarControler
from home.dominioDTO. AdapterListAcionamentoPoteDTO import AdapterListAcionamentoPote

from outliers import smirnov_grubbs as grubbs


buscar = BuscarControler()

class calcularOutilier:
    def OutilierPote(self, pote):
        postespr = buscar.BuscarPotesPlantaRegiao(pote.planta,pote.regiao)
        listaobj = []
        listaac = []
        for i in postespr:
            acionamentos = buscar.BuscarAcionamentoDia(i)
            listadapter = AdapterListAcionamentoPote(i,acionamentos)
            listaobj.append(listadapter)
            listaac.append(acionamentos)

        min = grubbs.min_test_indices(listaac,alpha=0.50)
        max = grubbs.max_test_indices(listaac,alpha=0.50)

        if (len(min) == 1):
            adplistacionamento=listaobj[min[0]]
            poteoutlier = adplistacionamento.getPote()
            if poteoutlier == pote:
                return 1
        if (len(max) == 1):
            adplistacionamento=listaobj[max[0]]
            poteoutlier = adplistacionamento.getPote()
            if poteoutlier == pote:
                return 2








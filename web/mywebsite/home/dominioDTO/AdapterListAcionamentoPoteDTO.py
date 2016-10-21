class AdapterListAcionamentoPote:
    def __init__(self,pote,acionamento):
        self._pote = pote
        self._acionamento = acionamento
    def getPote(self):
        return self._pote
    def setPote(self, pote):
        self._pote = pote
    def getAcionamento(self):
        return self._acionamento
    def setAcionamento(self, acionamento):
        self._acionamento = acionamento
    def __str__(self):
        return str(self._pote.codigo) +  " " + " " + str(self._acionamento)
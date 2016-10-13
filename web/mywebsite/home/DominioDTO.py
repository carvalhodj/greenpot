class AdapterHistoricoUmidadeAtual:
    def __init__(self,pote,umidadeatual):
        self._pote = pote
        self._umidadeatual = umidadeatual
    def getPote(self):
        return self._pote
    def setPote(self, pote):
        self._pote = pote
    def getUmidadeatual(self):
        return self._umidadeatual
    def setUmidadeatual(self, umidadeatual):
        self._umidadeatual = umidadeatual



class AdapterHistoricoUmidadeAtual:
    def __init__(self,pote,umidadeatual,alerta=None):
        self._pote = pote
        self._umidadeatual = umidadeatual
        self._alerta = alerta
    def getPote(self):
        return self._pote
    def setPote(self, pote):
        self._pote = pote
    def getUmidadeatual(self):
        return self._umidadeatual
    def setUmidadeatual(self, umidadeatual):
        self._umidadeatual = umidadeatual
    def getAlerta(self):
        return self._alerta
    def setAlerta(self,alerta):
        self._alerta = alerta
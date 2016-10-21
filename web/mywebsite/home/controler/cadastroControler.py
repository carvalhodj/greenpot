from home.models import Planta, Pote, Usuario_Pote, Historico_irrigacao




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
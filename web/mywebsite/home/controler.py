from .models import Planta, Pote, Usuario_Pote

class CadastroControler:
    def CadastrarPote(self, pote):
        pote.save()

    def CadastrarUsuarioPote(self, pote, user):
        userpote = Usuario_Pote()
        userpote.user = user
        userpote.pote = pote
        userpote.save()

class BuscarControler:
    def BuscarPoteCodigo(self,codigo):
        pote = Pote.objects.get(codigo=codigo)
        return pote


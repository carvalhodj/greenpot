import paho.mqtt.client as mqtt
from .models import Pote
from .controler import BuscarControler, CadastroControler

buscar = BuscarControler()

cadastrocontroler = CadastroControler()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("greenpot/1122334490/treshold/req")
    client.subscribe("greenpot/1122334490/treshold/rec")
    client.subscribe("greenpot/1122334490/historico")


def on_message(client, userdata, msg):
#    if msg.payload[0] == "T":
#        q = (msg.payload).split('-')
#        try:
#            pote = buscar.BuscarPoteCodigo(q[1])
#            treshold = pote.planta.umidade
#            client.publish("greenpot/1122334490/treshold/rec", treshold)
#        except Pote.DoesNotExist:
#            pote = 0
#    else:
#        print msg.payload

    if (msg.topic == 'greenpot/1122334490/treshold/req'):
        q = (msg.payload).split('-')
        try:
            pote = buscar.BuscarPoteCodigo(q[1])
            treshold = pote.planta.umidade
            client.publish("greenpot/1122334490/treshold/rec", treshold)
        except Pote.DoesNotExist:
            pote = 0


    if (msg.topic == 'greenpot/1122334490/historico'):
        q = (msg.topic).split('/')

        pote = buscar.BuscarPoteCodigo(str(q[1]))

        info = (msg.payload).split('_')
        if (info[0]=="I"):
            cadastrocontroler.CadastrarHistoricoIrrigacao(pote, info[1], info[2])
            print "guardando no ba.nco.."
        if (info[0]=="F"):
            pote = buscar.BuscarPoteCodigo(q[1])
            historicopote = buscar.BuscarHistoricoPote(pote)
            ultimo=buscar.BuscarUltimaInsercaoHistorico(historicopote)
            ultimo.hora_do_desligamento = info[1]
            ultimo.umidade_final = info[2]
            ultimo.save()
            print "guardando no ba.nco.."



    print "ok"


def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

#client.publish("temp/airton", "my message")

class Commqtt:
    def EnviarUmidade(self, umidade):
        client.publish("temp/carvalhodj", umidade)
    def AcionamentoPote(self, param):
        if param == 1:
            client.publish("greenpot/1122334490/power","L")
        if param == 0:
            client.publish("greenpot/1122334490/power", "D")


client.loop_start()
'''
if (msg.topic == 'greenpot/1122334490/historico'):
    q = (msg.topic).split('/')
    print q[1]
    pote = buscar.BuscarPoteCodigo(str(q[1]))

    info = (msg.payload).split('_')
    # cadastrocontroler.CadastrarHistoricoIrrigacao(pote, info[1], info[2])
    print "guardando no banco..."

'''
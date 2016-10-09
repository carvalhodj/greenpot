import paho.mqtt.client as mqtt
from .models import Pote
from .controler import BuscarControler

buscar = BuscarControler()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("temp/greenpot")

def on_message(client, userdata, msg):
    if msg.payload[0] == "T":
        q = (msg.payload).split('-')
        try:
            pote = buscar.BuscarPoteCodigo(q[1])
            treshold = pote.planta.umidade
            client.publish("temp/greenpot", treshold)
        except Pote.DoesNotExist:
            pote = 0
    else:
        print msg.payload

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


client.loop_start()
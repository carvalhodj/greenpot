import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print("Connected with result code "+str(rc))
	client.subscribe("temp/carvalhodj")

def on_message(client, userdata, msg):
	print msg.payload

def on_publish(mosq, obj, mid):
    print("mid: " + str(mid))

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60)
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish

#client.publish("temp/airton", "my message")

class Teste:
	def EnviarUmidade(self, umidade):
		client.publish("temp/carvalhodj", umidade)


client.loop_start()
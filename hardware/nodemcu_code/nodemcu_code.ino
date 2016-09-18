#include <PubSubClient.h>
#include <ESP8266WiFi.h>

#define LED D4

const char *ssid = "ZEFINHA";
const char *password = "11240039099ZRM";
const char *mqtt_server = "52.67.167.93";

void setupWIFI();
void reconectar();
void blinkar();
void callback(char* topic, byte* payload, unsigned int length);

WiFiClient espClient;
PubSubClient client(espClient);
long unsigned lastMsg = 0;
char msg[50];
int value = 0;

void setup() {
  pinMode(LED, OUTPUT);
  Serial.begin(115200);
  setupWIFI();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  client.subscribe("temp/carvalhodj");

}

void loop(void) {
  if (!client.connected()) {
    reconectar();
  }
  client.loop();
  long unsigned now = millis();
  // Nessa função é onde a brincadeira acontece. A cada segundo ele PUBLICA aquele CONTADOR de -20 a 50 para o Broker MQTT(mosquitto.org)
  if (now - lastMsg > 1000) {
    lastMsg = now;
    value++;
    if(value >=10) value = -10;
    snprintf (msg, 75, "%ld", value);
    Serial.print("Mensagem a ser Publicada: ");
    Serial.println(msg);
    client.publish("temp/carvalhodj", msg);
    //blinkar();
  }
}

void callback(char* topic, byte* payload, unsigned int length)
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");
  for (int i = 0; i < length; i++) {
    Serial.print((char)payload[i]);
  }
  Serial.println();
  String s = String((char *) payload); // Converter o byte array para uma String
  switch ( s.toInt() ) // Converter a String para inteiro
  {
     case 1:
      digitalWrite(LED, LOW);   // Turn the LED on (Note that LOW is the voltage level
      break;
 
     case 2:
      digitalWrite(LED, HIGH);  // Turn the LED off by making the voltage HIGH
      break;

     default:
      digitalWrite(LED, HIGH);  // Turn the LED off by making the voltage HIGH
      break;
  }
}

void setupWIFI() {
  WiFi.begin(ssid, password);
  Serial.print("Conectando na rede: ");
  Serial.println(ssid);
  while (WiFi.status() != WL_CONNECTED) {
   Serial.print(".");
   delay(500);
  }
}

void reconectar() {
  while (!client.connected()) {
    Serial.println("Conectando ao Broker MQTT.");
    if (client.connect("ESP8266")) {
      Serial.println("Conectado com Sucesso ao Broker");
      client.subscribe("temp/carvalhodj");
    } else {
      Serial.print("Falha ao Conectador, rc=");
      Serial.print(client.state());
      Serial.println(" tentando se reconectar...");
      delay(3000);
    }
  }
}

void blinkar()
{
  digitalWrite(LED, LOW);
  delay(500);
  digitalWrite(LED, HIGH);
}



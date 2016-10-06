#include <EEPROM.h>
#include <PubSubClient.h>
#include <ESP8266WiFi.h>


#define POWER D4
#define PUMP D2

const char *ssid = "DEJOTA.B";
const char *password = "a1b2C#D$";
const char *mqtt_server = "test.mosquitto.org";

void setupWIFI();
void reconectar();
void callback(char* topic, byte* payload, unsigned int length);

WiFiClient espClient;
PubSubClient client(espClient);

long unsigned lastMsg = 0;
char msg[50];
int value = 0;
uint8_t treshold = 0;
int umidade = 1000;
bool ligaDesliga = false;

void setup() {
  pinMode(POWER, OUTPUT);
  pinMode(PUMP, OUTPUT);
  digitalWrite(POWER, HIGH);
  digitalWrite(PUMP, LOW);
  EEPROM.begin(4);
  Serial.begin(115200);
  setupWIFI();
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  client.subscribe("temp/carvalhodj");
}

void loop() {
  if (!client.connected()) {
    reconectar();
  }
  client.loop();
  umidade -= 50;
  //client.publish("greenpots/codes", (char *) umidade);
  if (!ligaDesliga) {
    Serial.println("Sistema desligado!");
  } 
  else {
      if (treshold == 0) {
        Serial.println("Favor setar o limiar de umidade!");
        Serial.println(EEPROM.read(0));
      }
      else if (umidade < treshold) {
        while (umidade < 1000){
          digitalWrite(PUMP, HIGH);
          umidade += 20;
          Serial.println("Irrigando...");
          Serial.println(umidade);
          delay(1000);
        }
      digitalWrite(PUMP, LOW);
      }
      else {
      Serial.println("Ainda úmido.");
      }
 }
 delay(2000);
}

void callback(char* topic, byte* payload, unsigned int length)
{ 
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.println("] ");
    switch ((char) payload[0]) {
      case 'L':
        digitalWrite(POWER, LOW);
        ligaDesliga = true;
        Serial.println("Ligado");
        break;

       case 'D':
        digitalWrite(POWER, HIGH);
        digitalWrite(PUMP, LOW);
        ligaDesliga = false;
        break;

       default:
//        if (EEPROM.read(0) > 0) {
//          treshold = EEPROM.read(0);
//          EEPROM.end();
//        }
   
        String s = ((char *) payload);
        int x = s.toInt();
        EEPROM.write(0, x);
        treshold = EEPROM.read(0);
        EEPROM.end();
        
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

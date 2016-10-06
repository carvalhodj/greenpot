#include <PubSubClient.h>
#include <ESP8266WiFi.h>

#define POWER D4
#define PUMP D2

const char *ssid = "d3jotaRedmi2Pro";
const char *password = "qwertyasd";
const char *mqtt_server = "test.mosquitto.org";

void setupWIFI();
void reconectar();
void verificarUmidade();
void callback(char* topic, byte* payload, unsigned int length);

WiFiClient espClient;
PubSubClient client(espClient);

//long unsigned lastMsg = 0;
//char msg[50];
int value = 0;
int treshold = 0;
int umidade = 1000;
bool ligaDesliga = false;

void setup() {
  /* Definindo o comportamento
   *  dos pinos de Power e da 
   *  Bomba e setando seus valores
   *  iniciais...
   */
  pinMode(POWER, OUTPUT);
  pinMode(PUMP, OUTPUT);
  digitalWrite(POWER, HIGH);
  digitalWrite(PUMP, LOW);
  Serial.begin(115200);
  /* Conectando à rede WiFi 
   *  
   */
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
  umidade -= 50; // Simulação de decrescimento de umidade
  //client.publish("greenpots/codes", (char *) umidade);
  if (!ligaDesliga) {
    Serial.println("Sistema desligado!");
  } 
  else {
//      if (treshold == 0) {
//        Serial.println("Favor setar o limiar de umidade!");
//      }
//      else if (umidade < treshold) {
//        while (umidade < 1000){
//          digitalWrite(PUMP, HIGH);
//          umidade += 20;
//          Serial.println("Irrigando...");
//          delay(1000);
//        }
//      digitalWrite(PUMP, LOW);
//      }
//      else {
//      Serial.println("Ainda úmido.");
//      }
        verificarUmidade();
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
        String s = ((char *) payload);
        treshold = s.toInt();
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

void verificarUmidade() {
  /* Função para realizar o processo de verificação do valor da umidade do solo do vaso e, se preciso,
   *  acionar a bomba para irrigar. A umidade descresce com o tempo, e após apresentar um valor menor que
   *  o limiar da respectiva planta, a bomba é acionada, sendo desativada ao atingir um nível de umidade "ideal".
   *  Caso não haja o valor do limiar, o processo não é iniciado...
   */
  if (treshold == 0) {
    Serial.println("Favor setar o limiar de umidade!");
  }
  else if (umidade < treshold) {
    while (umidade < 1000) {
      digitalWrite(PUMP, HIGH);
      umidade += 20;
      Serial.println("Irrigando...");
      delay(1000);
      }
      digitalWrite(PUMP, LOW);
  }
  else {
    Serial.println("Ainda úmido.");
  }
}


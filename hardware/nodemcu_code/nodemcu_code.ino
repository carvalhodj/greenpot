#include <PubSubClient.h>
#include <ESP8266WiFi.h>
#include <NTPClient.h>
#include <WiFiUdp.h>

#define POWER D4
#define PUMP D2

#define MQTT_KEEPALIVE 60

const char *ssid = "d3jotaRedmi2Pro";
const char *password = "qwertyasd";
const char *mqtt_server = "test.mosquitto.org";
const char *unique_code = "1122334490";
const char *topic_tresh_req = "greenpot/1122334490/treshold/req";
const char *topic_tresh_rec = "greenpot/1122334490/treshold/rec";
const char *topic_power = "greenpot/1122334490/power";
const char *topic_historico = "greenpot/1122334490/historico";

void setupWIFI();
void reconectar();
void verificarUmidade();
void requisitarNivelUmidade();
int publicarHistorico(int umidade, char momento);
void callback(char* topic, byte* payload, unsigned int length);

WiFiClient espClient;
PubSubClient client(espClient);
WiFiUDP ntpUDP;

char msg[50];
char msgHistorico[20];
char msgBuf[50];
int previousTime = 0;
int currentTime = 0;
int value = 0;
int treshold = 0;
int umidade = 1000;
bool ligaDesliga = false;

NTPClient timeClient(ntpUDP, "europe.pool.ntp.org", -10800, 60000);

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
//  client.subscribe(topic_tresh_req);
  client.subscribe(topic_tresh_rec);
  client.subscribe(topic_power);
  client.subscribe(topic_historico);
  requisitarNivelUmidade();
  timeClient.begin();
}

void loop() {
  if (!client.connected()) {
    reconectar();
  }
  client.loop();
  //Serial.println(treshold);
  umidade -= 50; // Simulação de decrescimento de umidade
  //client.publish("greenpots/codes", (char *) umidade);
  if (!ligaDesliga) {
    Serial.println("Sistema desligado!");
  } 
  else {
        verificarUmidade();
 }
 delay(2000);
}

void callback(char* topic, byte* payload, unsigned int length)
{ 
    Serial.print("Message arrived [");
    Serial.print(topic);
    Serial.println("] ");
    switch ((char) topic[20]) {
      case 't':
      {
        if(topic[31] == 'c')
        {
        String bytePayload = ((char *) payload);
        treshold = bytePayload.toInt();
        break;
        }
        else
        {
          int x = 0;
        }
      }
      case 'p':
      {
        if((char) payload[0] == 'L')
        {
          digitalWrite(POWER, LOW);
          ligaDesliga = true;
          Serial.println("Ligado");
          break;
        }
        else if ((char) payload[0] == 'D')
        {
          digitalWrite(POWER, HIGH);
          digitalWrite(PUMP, LOW);
          ligaDesliga = false;
          break;
        }
        else
        {
          ligaDesliga = ligaDesliga;
          break;
        }
      }
      default:
      {
        int x = 0;
      }
    }
//    switch ((char) payload[0]) {
//      case 'L':
//        digitalWrite(POWER, LOW);
//        ligaDesliga = true;
//        Serial.println("Ligado");
//        break;
//
//       case 'D':
//        digitalWrite(POWER, HIGH);
//        digitalWrite(PUMP, LOW);
//        ligaDesliga = false;
//        break;
//
//       default:
//        String s = ((char *) payload);
//        treshold = s.toInt();
//    }
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
//      client.subscribe(topic_tresh_req);
      client.subscribe(topic_tresh_rec);
      client.subscribe(topic_power);
      client.subscribe(topic_historico);
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
    requisitarNivelUmidade();
  }
  else if (umidade < treshold) {
    publicarHistorico(umidade, 'I');
    while (umidade < 1000) {
      digitalWrite(PUMP, HIGH);
      umidade += 20;
      Serial.println("Irrigando...");
      delay(1000);
      }
    publicarHistorico(umidade, 'F');
      digitalWrite(PUMP, LOW);
  }
  else {
    Serial.println("Ainda úmido.");
  }
}

void requisitarNivelUmidade() {
  /* Função para requsitar o nível de umidade mínimo para a
   *  sobrevivência da respectiva planta
   */
  //client.subscribe(topic_tresh_req);
  //client.subscribe(topic_tresh_rec);
  sprintf(msg, "T-%s", unique_code);
  client.publish(topic_tresh_req, msg);
}

int publicarHistorico(int umidade, char momento) {
  /* Função para publicar os dados históricos do pote
   *  
   */
   timeClient.update();
   //Serial.println(timeClient.getFormattedTime());
   timeClient.getFormattedTime().toCharArray(msgBuf, 50);
   sprintf(msgHistorico, "%c_%s_%d", momento, msgBuf, umidade);
   Serial.println(msgHistorico);
   return 0;
}


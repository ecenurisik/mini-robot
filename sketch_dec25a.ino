void setup() {
  Serial.begin(9600);  
  Serial1.begin(9600);   
  Serial.println("Başlangıç tamamlandı.");
}

void loop() {
  if (Serial1.available()) {
    String gelenVeri = Serial1.readString();
    Serial.println("Bluetooth'dan Gelen: " +gelenVeri);
}
}
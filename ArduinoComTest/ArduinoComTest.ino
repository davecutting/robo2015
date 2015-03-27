int x = 0;
int y = 0;

void setup () {
  Serial.begin(57600);
  // Serial.println('Setup Complete');
}

void loop () {
  if (Serial.available()) {
    if (Serial.find("(")) {
      x = Serial.parseInt();
      y = Serial.parseInt();
      //myTuple = Serial.read();
      //Serial.print("I recieved :  ");
      Serial.print(x);
      Serial.print(", ");
      Serial.println(y);
      //Serial.println(myTuple);
    }
  }
  
}

###Based on Arduino code ###

'''int tilt_s1 = 2;
int tilt_s2 = 3;

void setup(){
 pinMode(tilt_s1, INPUT);
 pinMode(tilt_s2, INPUT);
 Serial.begin(9600);
}

void loop(){
  int position = getTiltPosition();
  Serial.println(position);
  delay(200); //only here to slow down the serial output
}

int getTiltPosition(){
   int s1 = digitalRead(tilt_s1);
   int s2 = digitalRead(tilt_s2);
   return (s1 << 1) | s2; //bitwise math to combine the values'''


import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.IN) ###Button 1
GPIO.setup(4, GPIO.IN) ###Button 2
GPIO.setwarnings(False)##switch off other ports

while True:
    if GPIO.input(25) == 0 and GPIO.input(4) == 0:
        print ("Down")
    if GPIO.input(25) == 1 and GPIO.input(4) == 1:
        print("Up")
    if GPIO.input(25) == 1 and GPIO.input(4) == 0:
        print("Left")
    if GPIO.input(25) == 0 and GPIO.input(4) == 1:
        print("Right")      

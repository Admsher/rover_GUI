#include <Servo.h>
#include <ros.h>
#include <std_msgs/Int8.h>
#define basemotor_pwm1 6
#define basemotor_pwm2 7
#define basemotor_dir1 5
#define basemotor_dir2 4
#define spectromtor_pwm 3
#define spectromotor_dir 8

Servo myservo1;  // create servo object to control a servo
// twelve servo objects can be created on most boards
Servo myservo2;
int pos1 = 0;    // variable to store the servo position
int pos2= 0;
int velmotor=255;
int velmotor_spectro=70;
ros::NodeHandle nh;


void setup() {
  myservo1.attach(9);  // attaches the servo on pin 9 to the servo object
  myservo2.attach(10);
  pinMode(basemotor1_pwm,OUTPUT);
  pinMode(basemotor2_pwm,OUTPUT);
  pinMode(spectromotor_pwm,OUTPUT);
  pinMode(basemotor1_dir,OUTPUT);
  pinMode(basemotor2_dir,OUTPUT);
  pinMode(spectromotor_dir,OUTPUT);
  
  nh.initNode();
  nh.subscribe(sub1);
}

void callback(const std_msgs::Int8& msg) {
  int8_t value_given=msg.data;
  
      //Servo1
  
  if(value_given==1){
  for (pos1 = 0; pos1 <= 90; pos1 +=1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }}

 else if(value_given==2){
  for (pos1 = 90; pos1 >= 0; pos1 -= 1) { // goes from 180 degrees to 0 degrees
    myservo1.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }}
  
  
    //Servo2
                                              
  if(value_given==3){
  for (pos2 = 0; pos2 <= 90; pos2 +=1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo2.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }}

 else if(value_given==4){
  for (pos2 = 90; pos2 >= 0; pos2 -= 1) { // goes from 180 degrees to 0 degrees
    myservo2.write(pos);              // tell servo to go to position in variable 'pos'
    delay(15);                       // waits 15ms for the servo to reach the position
  }}
else
{
}
if (value_given==5  && velmotor==255){
velmotor=velmotor/2;
 }

else if (value_given==5 && velmotor==255/2){
velmotor = velmotor; 

}
else if (value_given==-5  && velmotor==255/2){
velmotor=velmotor*2;
 }                                                        //Change motor speed

else if(value_given==5 && velmotor==255){
velmotor = velmotor; 

}
else{
}

if(value_given==6){           
    digitalWrite(basemotor1_dir,HIGH); 
    analogWrite(basemotor1_pwm,velmotor);
  }
else if(value_given==-6){                                      //Basemotor1
    digitalWrite(basemotor1_dir,LOW); 
    analogWrite(basemotor1_pwm,velmotor);
  }  
                                                           
else if(value_given==7){
    digitalWrite(basemotor2_dir,HIGH); 
    analogWrite(basemotor2_pwm,velmotor);
  }                                                           //Basemotor2
else if(value_given== -7){
    digitalWrite(basemotor2_dir,LOW); 
    analogWrite(basemotor2_pwm,velmotor);
  }
 
else if(value_given== 8){
    digitalWrite(spectromotor_dir,HIGH); 
    analogWrite(spectromotor_pwm,velmotor_spectro);
  }                                                          //Spectromotor
 
 else if(value_given== -8){
    digitalWrite(spectromotor_dir,LOW); 
    analogWrite(spectromotor_pwm,velmotor_spectro);
  } 
  
  

}
ros::Subscriber<std_msgs::Int8> sub("ld", callback );
void loop(){
  nh.spinOnce();
  }

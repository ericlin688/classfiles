//leftmost potentiometer controls base motor
#include <Servo.h>

//declare motors
Servo base;
Servo mainarm;
Servo extender;
Servo claw;

//declare initial angles
int base_angle_act = 90;
int main_arm_act = 90;
int claw_angle_act = 45;

//Declare regular delay
int wait = 10;

void setup() {
  Serial.begin(9600);
  //turn on potentiometers
  pinMode(A0,INPUT);
  pinMode(A1,INPUT);
  pinMode(A2,INPUT);
  //attach motors
  base.attach(11);
  extender.attach(10);
  mainarm.attach(9);
  claw.attach(6);

  //Set motors to initial angles
  base.write(base_angle_act);
  mainarm.write(main_arm_act);
  claw.write(claw_angle_act);
}

void loop() {
  //Control for base motor
  int base_steer_angle = map(analogRead(A0),0,1023,0,180);
  if (base_steer_angle!=base_angle_act){
    base_angle_act = base_angle_act + abs(base_steer_angle-base_angle_act)/(base_steer_angle-base_angle_act);
    base.write(base_angle_act);
  }
  
  //Control for mainarm motor
  int main_steer_angle = map(analogRead(A1),0,1023,0,135);
  if (main_steer_angle!=main_arm_act){
    main_arm_act = main_arm_act + abs(main_steer_angle-main_arm_act)/(main_steer_angle-main_arm_act);
    mainarm.write(main_arm_act);
  }
  
  //Control for extender motor
  int extender_steer_angle = map(analogRead(A2),0,1023,0,180);
  extender.write(extender_steer_angle);

  Serial.print("base = ");
  Serial.println(base_steer_angle);
  Serial.print("mainarm = ");
  Serial.println(main_steer_angle);
  Serial.print("extender = ");
  Serial.println(extender_steer_angle);
  
  delay(wait);
}

#include <Braccio++.h>



//declarare puncte
struct point{
  float base ;
  float shoulder ;
  float elbow;
  float vwrist;
  float rwrist ;
  float gripper;
} ;

point home={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point1={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point2={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point3={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point4={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point5={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point6={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point7={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point8={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point9={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point10={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point11={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point12={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point13={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point14={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point15={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point16={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point17={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point18={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point19={90.0 ,85.0,157.5,157.5,157.5,157.5};
point point20={90.0 ,85.0,157.5,157.5,157.5,157.5};


bool start_home ;
int speed ;
//declarare functii 
double  speed_convert(int speed);
void move_home(struct point P_T_MOVE,int speed);
void move_relative(struct point P_T_MOVE,int speed);


void setup() {
   

  // put your setup code here, to run once:
  Serial.begin(9600);
  if (Braccio.begin())
  {

    Braccio.moveTo(home.gripper, home.rwrist,home.vwrist, home.elbow, home.shoulder, home.base);
    delay(500);
  }
    


}

void loop() {





  // put your main code here, to run repeatedly:
  while(point1.shoulder<120.0){
    point1.shoulder++;
    Braccio.moveTo(point1.gripper, point1.rwrist,point1.vwrist, point1.elbow, point1.shoulder, point1.base);
    delay(100);
  }
  Serial.println(point1.shoulder);
}



double  speed_convert(int speed){




}


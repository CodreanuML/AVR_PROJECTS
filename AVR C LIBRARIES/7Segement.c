/*
 * 7Segment.c
 *
 * Created: 5/20/2023 6:03:44 PM
 *  Author: mcodrea2
 */ 



#include <AvrGeneral.h>

# define F_CPU 16000000UL


/// FUNCTIONS TO SET UP THE COMMON CATODE PIN

int display_SET(int pin){
	PinMode(pin,OUT);
	return pin;
}


///FUNCTIONS USED TO TURN DISPLAY ON OFF
void display_ON(int display){
	DigitalWrite(display,LOW);
}

void display_OFF(int display){
	DigitalWrite(display,HIGH);
}

////FUNCTION TO SET UP PINS FOR EVERY SEGMENT 
int set_digit_pin(int pin){
	PinMode(pin,OUT);
	return pin;
}


/// FUNCTIONS USED TO DISPLAY A DIGIT
void clear_all(int a,int b,int c,int d,int e,int f,int g){
	DigitalWrite(a,HIGH);
	DigitalWrite(b,HIGH);
	DigitalWrite(c,HIGH);
	DigitalWrite(d,HIGH);
	DigitalWrite(e,HIGH);
	DigitalWrite(f,HIGH);
	DigitalWrite(g,HIGH);
}

void show_no(int a,int b,int c,int d,int e,int f,int g,int no){
	
	switch(no){
		case 0 : 
				DigitalWrite(a,LOW);
				DigitalWrite(b,LOW);
				DigitalWrite(c,LOW);
				DigitalWrite(d,LOW);
				DigitalWrite(e,LOW);
				DigitalWrite(f,LOW);
				DigitalWrite(g,HIGH);
				break;
		case 1 :
				DigitalWrite(a,HIGH);
				DigitalWrite(b,LOW);
				DigitalWrite(c,LOW);
				DigitalWrite(d,HIGH);
				DigitalWrite(e,HIGH);
				DigitalWrite(f,HIGH);
				DigitalWrite(g,HIGH);
				break;
		case 2 :
				DigitalWrite(a,LOW);
				DigitalWrite(b,LOW);
				DigitalWrite(c,HIGH);
				DigitalWrite(d,LOW);
				DigitalWrite(e,LOW);
				DigitalWrite(f,HIGH);
				DigitalWrite(g,LOW);
				break;
		case 3 :
				DigitalWrite(a,LOW);
				DigitalWrite(b,LOW);
				DigitalWrite(c,LOW);
				DigitalWrite(d,LOW);
				DigitalWrite(e,HIGH);
				DigitalWrite(f,HIGH);
				DigitalWrite(g,LOW);
				break;				
		case 4 :
				DigitalWrite(a,HIGH);
				DigitalWrite(b,LOW);
				DigitalWrite(c,LOW);
				DigitalWrite(d,HIGH);
				DigitalWrite(e,HIGH);
				DigitalWrite(f,LOW);
				DigitalWrite(g,LOW);
				break;						
		case 5 :
				DigitalWrite(a,LOW);
				DigitalWrite(b,HIGH);
				DigitalWrite(c,LOW);
				DigitalWrite(d,LOW);
				DigitalWrite(e,HIGH);
				DigitalWrite(f,LOW);
				DigitalWrite(g,LOW);
				break;
		case 6 :
				DigitalWrite(a,LOW);
				DigitalWrite(b,HIGH);
				DigitalWrite(c,LOW);
				DigitalWrite(d,LOW);
				DigitalWrite(e,LOW);
				DigitalWrite(f,LOW);
				DigitalWrite(g,LOW);
				break;
		case 7 :
				DigitalWrite(a,LOW);
				DigitalWrite(b,LOW);
				DigitalWrite(c,LOW);
				DigitalWrite(d,HIGH);
				DigitalWrite(e,HIGH);
				DigitalWrite(f,HIGH);
				DigitalWrite(g,HIGH);
				break;
		case 8 :
				DigitalWrite(a,LOW);
				DigitalWrite(b,LOW);
				DigitalWrite(c,LOW);
				DigitalWrite(d,LOW);
				DigitalWrite(e,LOW);
				DigitalWrite(f,LOW);
				DigitalWrite(g,LOW);
				break;
		case 9 :
				DigitalWrite(a,LOW);
				DigitalWrite(b,LOW);
				DigitalWrite(c,LOW);
				DigitalWrite(d,LOW);
				DigitalWrite(e,HIGH);
				DigitalWrite(f,LOW);
				DigitalWrite(g,LOW);
				break;
		
	}
	

}

/*
 * 7Segment.h
 *
 * Created: 5/20/2023 6:03:44 PM
 *  Author: mcodrea2
 */ 




/// THIS LIBRARY IS USED TO CONTROL A SEVEN SEGMENT DISPLAY USING AvrGeneral.h AND BUILDING A GENERAL WIRING SCHEMA 

/// EXAMPLE OF USAGE.

//int display1
//int a , int b ,int c,int d, int e, int f,int g


//display1=display_SET(7); Display catode is on pin 7

//a=set_digit_pin(0); Setting every digit on every pin a is on pin 0 , b on pin 2 , c on pin 5 ,d on pin 4 , e on pin 3 , f on pin 1 ,g on pin 6.
//b=set_digit_pin(2);
//c=set_digit_pin(5);
//d=set_digit_pin(4);
//e=set_digit_pin(3);
//f=set_digit_pin(1);
//g=set_digit_pin(6);

//display_ON(display1); Turn display ON


//show_no(a,b,c,d,e,f,g,no); SHOWING NUMBER  .









# define F_CPU 16000000UL
#ifndef SevenSegment_H_
#define SevenSegment_H_


#include <AvrGeneral.h>
/// FUNCTIONS TO SET UP THE COMMON CATODE PIN
int  display_SET(int pin);


///FUNCTIONS USED TO TURN DISPLAY ON OFF
void display_ON(int display);
void display_OFF(int display);



////FUNCTION TO SET UP PINS FOR EVERY SEGMENT 
int set_digit_pin(int pin);


/// FUNCTIONS USED TO DISPLAY A DIGIT
void clear_all(int a,int b,int c,int d,int e,int f,int g);
void show_no(int a,int b,int c,int d,int e,int f,int g,int no);




#endif /* 7Segment_H_ */

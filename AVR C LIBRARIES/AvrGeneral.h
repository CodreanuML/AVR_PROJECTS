/*
 * AvrGeneral.h
 *
 * Created: 2/2/2023 3:15:32 PM
 *  Author: MCODREA2
 */ 


#ifndef AVRGENERAL_H_
#define AVRGENERAL_H_


#define IN 0
#define OUT 1

#define LOW 0
#define HIGH 1

//Function for controlling current Status of a pin INPUT or OUT 
//PinNO  corespons with Arduino Pinout  Mode with OUT or INPUT
//PinNO values between 0-13 , Mode values 0 ,1 


void PinMode(int PinNO, int Mode ) ;
void DigitalWrite(int PinNO,int Mode);
int DigitalRead(int PinNO);


#endif /* AVRGENERAL_H_ */
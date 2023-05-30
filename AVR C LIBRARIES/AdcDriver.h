/*
 * AdcDacDriver.h
 *
 * Created: 2/2/2023 3:15:32 PM
 *  Author: MCODREA2
 */ 
# define F_CPU 16000000UL


#ifndef ADCDRIVER_H_
#define ADCDRIVER_H_



void ADC_Init();               /// function to Initialize THE ADC 


// function is used to read an analog channel using pooling method 
int ADC_Read(char channel);   /// function to read a chanel 

#endif /* ADCDRIVER_H_ */

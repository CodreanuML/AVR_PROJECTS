/*
 * CFile1.c
 *
 * Created: 2/2/2023 3:14:08 PM
 *  Author: MCODREA2
 * This library is used to control all IN OUT PINS OF AVR 
 * Check Description In Header File
 */ 
#include <avr/io.h>

/* Function Variables description
DDRx - Data Direction Register
PORTx - Pin Output Register
PINx - Pin Input Register
x could be PORT A,B,C,D 

Port Description :
Phisycal    Function    ArduinoFunction


1            PC6 -      reset
2            PD0 -      digital pin 0 Rx
3            PD1 -      digital pin 1 Tx
4            PD2 -      digital pin 2
5            PD3 -      digital pin 3 PWM
6            PD4 -      digital pin 4
7			 VCC -	    VCC
8            GND -      GND
9            PB6 -      crystal
10           PB7 -      crystal
11           PD5 -      digital pin 5 PWM
12           PD6-       digital pin 6 PWM
13           PD7-       digital pin 7
14           PB0-       digital pin 8   
15           PB1-       digital pin 9 PWM
16           PB2-       digital pin 10 PWM
17           PB3-       digital pin 11 PWM
18           PB4-       digital pin 12 
19           PB5-       digital pin 13
20           AVCC-      AVCC
21           AREF-      AREF
22           GND-       GND
23           PC0-       analog input 0  
24           PC1-       analog input 1  
25           PC2-       analog input 2  
26           PC3-       analog input 3  
27           PC4-       analog input 4  
28           PC5-       analog input 5 


*/


/* SHIFF A VALUE TO THE LEFT WITH THE SPECIFIED POSITION AND ADD 1 TO THE END */
char shift_and_add(char value, int shift_count) {
	int add_value = 1;
	for (int i = 0; i < shift_count; i++) {
		value = (value << 1) | add_value;
		add_value = add_value << 1;
	}
	return value;
}


/* V1 - PinMode - Expanded Functionality */

void PinMode(int PinNO, int Mode ){
	switch (PinNO){
		case 0 : 
			if (Mode==1){
				DDRD  =DDRD | 0b000000001 ;			
			}
			else if (Mode==0) {
				
				DDRD =DDRD & 0b111111110 ;	
			}
		
		    break ;
		
		case 1 : 
			if (Mode==1){
				DDRD  =DDRD | 0b00000010 ;
			}
			else if (Mode==0) {
				
				DDRD  =DDRD & 0b11111101 ;
			}
			
			break ;		
		case 2 :
			if (Mode==1){
				DDRD  =DDRD | 0b00000100 ;
				
			}
			else if (Mode==0) {
				
				DDRD  =DDRD & 0b11111011 ;
			}
			
			break ;
		case 3 :
			if (Mode==1){
				DDRD  =DDRD | 0b00001000 ;
			}
			else if (Mode==0) {
				
				DDRD  =DDRD & 0b11110111 ;
			}
			
			break ; 
		case 4 : 
			if (Mode==1){
				DDRD  =DDRD | 0b00010000 ;
			}
			else if (Mode==0) {
				
				DDRD  =DDRD & 0b11101111 ;
			}
			
			break ;			
		case 5 : 
			if (Mode==1){
				DDRD  =DDRD | 0b00100000 ;
			}
			else if (Mode==0) {
				
				DDRD  =DDRD & 0b11011111 ;
			}
			
			break ;
		case 6 : 
			if (Mode==1){
				DDRD  =DDRD | 0b01000000 ;
			}
			else if (Mode==0) {
				
				DDRD  =DDRD & 0b10111111 ;
			}
			
			break ;			
		case 7 : 
			if (Mode==1){
				DDRD  =DDRD | 0b10000000 ;
			}
			else if (Mode==0) {
				
				DDRD  =DDRD & 0b01111111 ;
			}
			
			break ;
		case 8 : 		
			if (Mode==1){
			DDRB  =DDRB | 0b00000001 ;
			}
			else if (Mode==0) {
			
			DDRB  =DDRB & 0b11111110 ;
			}
		
		break ;
		case 9 : 
			if (Mode==1){
				DDRB  =DDRB | 0b00000010 ;
			}
			else if (Mode==0) {
				
				DDRB  =DDRB & 0b11111101 ;
			}
			
			break ;
		case 10 : 
			if (Mode==1){
				DDRB  =DDRB | 0b00000100 ;
			}
			else if (Mode==0) {
				
				DDRB  =DDRB & 0b11111011 ;
			}
			
			break ;
		case 11 : 
			if (Mode==1){
				DDRB  =DDRB | 0b00001000 ;
			}
			else if (Mode==0){
				
				DDRB  =DDRB & 0b11110111 ;
			}
			
			break ;
		case 12 : 
			if (Mode==1){
				DDRB  =DDRB | 0b00010000 ;
			}
			else if (Mode==0) {
				
				DDRB  =DDRB & 0b11101111 ;
			}
			
			break ;
		case 13 : 
			if  (Mode==1){
				DDRB  =DDRB | 0b00100000 ;
			}
			else if (Mode==0) {
				
				DDRB  =DDRB & 0b11011111 ;
			}
			
			break ;
	}
	
	
	} ;
	
/* V2 - PinMode - Contracted Functionality */

/*void PinMode(int PinNO, int Mode ){
	char ON = 0b00000001 ;
	char OFF = 0b11111111;
	if (PinNO<=7){
		if (Mode==1){
			DDRD |=ON<<PinNO ;
		}
		else
		{
			DDRD &=shift_and_add(OFF,PinNO);
		}
	}
	else if (PinNO>7 && PinNO <=13){
		if (Mode==1){
			DDRB |=ON<<(PinNO-8) ;
		}
		else
		{
			DDRB &=shift_and_add(OFF,PinNO-8);
		}					
	}		
} */

/* V1 - DigitalWrite - Expanded Functionality */
 void DigitalWrite(int PinNO,int Mode){
	switch (PinNO){
		case 0 :
		if (Mode==1){
			PORTD  =PORTD | 0b000000001 ;
		}
		else if (Mode==0) {
			
			PORTD =PORTD & 0b111111110 ;
		}
		
		break ;
		
		case 1 :
		if (Mode==1){
			PORTD  =PORTD | 0b00000010 ;
		}
		else if (Mode==0) {
			
			PORTD  =PORTD & 0b11111101 ;
		}
		
		break ;
		case 2 :
		if (Mode==1){
			PORTD  =PORTD | 0b00000100 ;
			
		}
		else if (Mode==0) {
			
			PORTD  =PORTD & 0b11111011 ;
		}
		
		break ;
		case 3 :
		if (Mode==1){
			PORTD  =PORTD | 0b00001000 ;
		}
		else if (Mode==0) {
			
			PORTD  =PORTD & 0b11110111 ;
		}
		
		break ;
		case 4 :
		if (Mode==1){
			PORTD  =PORTD | 0b00010000 ;
		}
		else if (Mode==0) {
			
			PORTD  =PORTD & 0b11101111 ;
		}
		
		break ;
		case 5 :
		if (Mode==1){
			PORTD  =PORTD | 0b00100000 ;
		}
		else if (Mode==0) {
			
			PORTD  =PORTD & 0b11011111 ;
		}
		
		break ;
		case 6 :
		if (Mode==1){
			PORTD  =PORTD | 0b01000000 ;
		}
		else if (Mode==0) {
			
			PORTD  =PORTD & 0b10111111 ;
		}
		
		break ;
		case 7 :
		if (Mode==1){
			PORTD  =PORTD | 0b10000000 ;
		}
		else if (Mode==0) {
			
			PORTD  =PORTD & 0b01111111 ;
		}
		
		break ;
		case 8 :
		if (Mode==1){
			PORTB  =PORTB | 0b00000001 ;
		}
		else if (Mode==0) {
			
			PORTB  =PORTB & 0b11111110 ;
		}
		
		break ;
		case 9 :
		if (Mode==1){
			PORTB  =PORTB | 0b00000010 ;
		}
		else if (Mode==0) {
			
			PORTB  =PORTB & 0b11111101 ;
		}
		
		break ;
		case 10 :
		if (Mode==1){
			PORTB  =PORTB | 0b00000100 ;
		}
		else if (Mode==0) {
			
			PORTB  =PORTB & 0b11111011 ;
		}
		
		break ;
		case 11 :
		if (Mode==1){
			PORTB  =PORTB | 0b00001000 ;
		}
		else if (Mode==0){
			
			PORTB  =PORTB & 0b11110111 ;
		}
		
		break ;
		case 12 :
		if (Mode==1){
			PORTB  =PORTB | 0b00010000 ;
		}
		else if (Mode==0) {
			
			PORTB  =PORTB & 0b11101111 ;
		}
		
		break ;
		case 13 :
		if  (Mode==1){
			PORTB  =PORTB | 0b00100000 ;
		}
		else if (Mode==0) {
			
			PORTB =PORTB & 0b11011111 ;
		}
		
		break ;
	}
	
	
	
} 

/* V2 - DigitalWrite - Contracted Functionality */
/* void DigitalWrite(int PinNO, int Mode ){
	char ON = 0b00000001 ;
	char OFF = 0b11111111;
	if (PinNO<=7){
		if (Mode==1){
			PORTD |=ON<<(PinNO) ;
		}
		else
		{
			PORTD &=shift_and_add(OFF,PinNO);
		}
	}
	else if (PinNO>7 && PinNO <=13){
		if (Mode==1){
			PORTB |=ON<<(PinNO-8) ;
		}
		else
		{
			PORTB &=shift_and_add(OFF,PinNO-8);
		}
	}
} */


/* V1 - DigitalRead - Expanded Functionality */
int DigitalRead(int PinNO){
	switch (PinNO){
		case 0 :
		 if ( (PIND & (1 << PIND0)) == (1 << PIND0) ) {
			 return 1 ;// pin is high
			 } else {
			 return  0;// pin is low
		 }
		break ;		
		case 1 :
		 if ( (PIND & (1 << PIND1)) == (1 << PIND1) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
			 }
		break ;
		case 2 :
		 if ( (PIND & (1 << PIND2)) == (1 << PIND2) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
			 }
		break ;
		case 3 :
		 if ( (PIND & (1 << PIND3)) == (1 << PIND3) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
			 }
		
		break ;
		case 4 :
		 if ( (PIND & (1 << PIND4)) == (1 << PIND4) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
			 }
			 
		break ;
		case 5 :
		 if ( (PIND & (1 << PIND5)) == (1 << PIND5) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
			 }
			 
		break ;
		case 6 :
		 if ( (PIND & (1 << PIND6)) == (1 << PIND6) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
			 }
		break ;
		case 7 :
		 if ( (PIND & (1 << PIND7)) == (1 << PIND7) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
			 }
		break ;
		case 8 :
		 if ( (PINB & (1 << PINB0)) == (1 << PINB0) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
		 }
		break ;
		case 9 :
	    if ( (PINB & (1 << PINB1)) == (1 << PINB1) ) {
			 return 1 ;// pin is high
			 } else {
			 return 0;// pin is low
		 }
		
		break ;
		case 10 :
	    if ( (PINB & (1 << PINB2)) == (1 << PINB2) ) {
		    return 1 ;// pin is high
		    } else {
		    return 0;// pin is low
	    }
	    
		break ;
		case 11 :
	    if ( (PINB & (1 << PINB3)) == (1 << PINB3) ) {
		    return 1 ;// pin is high
		    } else {
		    return 0;// pin is low
	    }
	    
		
		break ;
		case 12 :
	    if ( (PINB & (1 << PINB4)) == (1 << PINB4) ) {
		    return 1 ;// pin is high
		    } else {
		    return 0;// pin is low
	    }
	    
		
		break ;
		case 13 :
		    if ( (PINB & (1 << PINB5)) == (1 << PINB5) ) {
			    return 1 ;// pin is high
			    } else {
			    return 0;// pin is low
		    }
		    

		
		break ;
	}
	
 return 2 ;	
}
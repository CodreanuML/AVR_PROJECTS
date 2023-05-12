/*
 * Timers.c
 *
 * Created: 3/19/2023 6:04:27 PM
 *  Author: mcodrea2
 */ 
# define F_CPU 16000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
/* Timers/Counter Descriptions
AVR got 3 Timers/Counters :
Timer/Counter0-8 Bit Timer/Counter
Timer/Counter1-16 Bit Timer/Counter
Timer/Counter2-8 Bit Timer/Counter

They are configurable :
Main registers : 

X- nr of timer/counter 0,1,2

TCNT X - This is where the uint 8-bit/16-bit counter of the timer resides. 
TCCR X - This is the register for setting up the timer/counter(prescaler and tipe of intrerupt)
TCCR register description bits :
0-CSSX0
1-CSSX1
2-CSSX2
3-WGMX1
4-COMX0
5-COMX1
6-WGMX0
7-FOCX

TIFR - is common for all 3 
TIFR register description bits :
0-TOV 0
1-OCF 0
2-TOV 1
3-OCF1B
4-OCF1A
5-ICF1
6-TOV2
7-OCF2
TIMKS - is common for all 3 
TIMSK - Timer Interrupt Mask
0- TOIE0
1- OCIE0
2- TOIE1
3- OCIE1B
4- OCIE1A
5- TICIE1
6- TOIE2
7- OCIE2

Algorithm for a timer :
1.set up TCNT register - when it overflow it will set the TOV X register to 1
2.set up the timer mode configuring the registes from TCCR (check documentation for possible config)
3.when register TOV overflow TOV flag is set, to reset the timer set it back to 1 

ATTENTION :
YOU CAN USE TIMERS WITH POLLING METHOD OR WITH INTRERUPT METHOD
*/

// POLLING METHOD TO GENERATE DELAY in MS using timer 0
void delay_ms_t0(int ms)
{
	int count=0 ;
	int ms_value=ms*10;
	TCNT0=0 ;
	TCCR0B=0x02;  // PRESCALER 8
	while (count<ms_value){
	if (TCNT0>=200){
		TCNT0=0;
		count++ ;
	}
	
	}
	
}

// POLLING METHOD TO GENERATE DELAY in MS using timer 2
void delay_ms_t2(int ms)
{
	int count=0 ;
	int ms_value=ms*10;
	TCNT2=0 ;
	TCCR2B=0x02;  // PRESCALER 8
	while (count<ms_value){
		if (TCNT2>=200){
			TCNT2=0;
			count++ ;
		}
		
	}
	
}

// POLLING METHOD TO GENERATE DELAY in MS using timer 1
void delay_ms_t1(int ms)
{
	int count=0 ;
	int ms_value=ms*10;
	TCNT1=0 ;
	TCCR1B=0x02;  // PRESCALER 8
	while (count<ms_value){
		if (TCNT1>=200){
			TCNT1=0;
			count++ ;
		}		
	}	
}




// Interrupt T0 - MS
// DO NOT FORGET WHEN IS REUSED TO REINIT TCNT0 WITH PRESCALED VALUE-overflow val 255 
void set_timer_0_ms_int()
{

	TCNT0=6 ;     // SET STARTING P TO 55 
	TCCR0B=0x03;  // PRESCALER 64
	TIMSK0 |= (1 << TOIE0);
	sei();
}

// Interrupt T2 -MS
// DO NOT FORGET WHEN IS REUSED TO REINIT TCNT0 WITH PRESCALED VALUE-overflow val 255
void set_timer_2_ms_int()
{

	TCNT2=6 ;     // SET STARTING P TO 55
	TCCR2B=0x04;  // PRESCALER 64
	TIMSK2 |= (1 << TOIE2);
	sei();	
}

// Interrupt T1 -MS
// DO NOT FORGET WHEN IS REUSED TO REINIT TCNT0 WITH PRESCALED VALUE-overflow val 65536
void set_timer_1_ms_int()
{

	TCNT1=65286 ;     // SET STARTING P TO 55
	TCCR1B=0x03;  // PRESCALER 64
	TIMSK1 |= (1 << TOIE1);
	sei();
}




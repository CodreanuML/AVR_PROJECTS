/*
 * Timers.h
 *
 * Created: 3/19/2023 6:03:44 PM
 *  Author: mcodrea2
 */ 

# define F_CPU 16000000UL
#ifndef TIMERS_H_
#define TIMERS_H_

//function to generate delay corresponding with each timers

//for all functions the general clock is 16 mHz


// generate delay in ms
void delay_ms_t0(int ms);
void delay_ms_t1(int ms);
void delay_ms_t2(int ms);




//function to activate time interrupt in 1 ms using timers 
void set_timer_0_ms_int();
void set_timer_1_ms_int();
void set_timer_2_ms_int();



#endif /* TIMERS_H_ */

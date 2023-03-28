/*
 * Timers.h
 *
 * Created: 3/19/2023 6:03:44 PM
 *  Author: mcodrea2
 */ 


#ifndef TIMERS_H_
#define TIMERS_H_

//function to generate delay corresponding with each timers

//for all functions the general clock is 16 mHz


// generate delay in us
void delay_ms_t0(int ms);
void delay_ms_t1(int ms);
void delay_ms_t2(int ms);


//generate delay in us-not very precise in C (this is V1 -without interrupt is hard to develop time delay in us,it got an eror of 0.1us) 

void delay_us_t0(int us);
void delay_us_t1(int us);
void delay_us_t2(int us);

//function to activate time interrupt in 1 ms using timers 
void set_timer_0_ms_int();
void set_timer_1_ms_int();
void set_timer_2_ms_int();

//function to activate time interrupt in 1 us using timers 
void set_timer_0_us_int();
void set_timer_1_us_int();
void set_timer_2_us_int();

#endif /* TIMERS_H_ */

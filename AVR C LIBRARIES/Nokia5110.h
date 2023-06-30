
* Nokia5110.h
*
* Created: 6/20/2023 2:02:41 PM
*  Author: mcodrea2
*/


# define F_CPU 16000000UL
#include <util/delay.h>
#include <avr/io.h>
#include <stdio.h>
#include "AvrGeneral.h"
#include "AvrTimers.h"
#include <avr/interrupt.h>



#ifndef NOKIA_H_
#define NOKIA_H_

//function used to populate the display with 6 lines of 16 char 
void write_display(char * line1 , char* line2,char* line3,char * line4,char* line5,char* line6);

//function used to shift out bits to display

void shiftOut(uint8_t dataPin, uint8_t clockPin,  uint8_t val);


//function used to write commands;
void LcdWriteCmd(char cmd);


//function used to write data;
void LcdWriteData(char dat);

//function used to init display
void LCD_INIT();

//function to write a string on a line - line between 0-6 Maximum stirng LEN 16
void write_string_line(char *line , char string[]);

#endif /* NOKIA_H_ */

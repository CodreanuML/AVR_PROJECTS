/*
 * Nokia5110.h
 *
 * Created: 6/20/2023 2:02:41 PM
 *  Author: mcodrea2
 */ 

#include <avr/io.h>
#include <stdio.h>
#define RST 9
#define CE  10
#define DC  11
#define DIN  12
#define CLK  13
#define HIGH 1
#define LOW 0
#define OUT 1
#define IN 0

//LCD init Function

void LCD_INIT(){
		 PinMode(RST, OUT);
		 PinMode(CE, OUT);
		 PinMode(DC, OUT);
		 PinMode(DIN, OUT);
		 PinMode(CLK, OUT);
		 DigitalWrite(RST, LOW);
		 DigitalWrite(RST, HIGH);
		 
		 LcdWriteCmd(0x21);  // LCD extended commands
		 LcdWriteCmd(0xB0);  // set LCD Vop (contrast)
		 LcdWriteCmd(0x04);  // set temp coefficent
		 LcdWriteCmd(0x14);  // LCD bias mode 1:40
		 LcdWriteCmd(0x20);  // LCD basic commands
		 LcdWriteCmd(0x0C);  // LCD basic commands
	
}

//function used to shift out bits to display
void shiftOut(uint8_t dataPin, uint8_t clockPin,  uint8_t val)
{
	uint8_t i;
	/// SHIFT OUT MSB FIRST
	for (i = 0; i < 8; i++)  {
		
		DigitalWrite(dataPin, !!(val & (1 << (7 - i))));
		
		DigitalWrite(clockPin, HIGH);
		DigitalWrite(clockPin, LOW);
	}
}
//function used to write commands;
void LcdWriteCmd(char cmd)
{
	DigitalWrite(DC, LOW); //DC pin is low for commands
	DigitalWrite(CE, LOW);
	shiftOut(DIN, CLK, cmd); //transmit serial commands
	DigitalWrite(CE, HIGH);
}

//function used to write data;
void LcdWriteData(char dat)
{
	DigitalWrite(DC, HIGH); //DC pin is high for data
	DigitalWrite(CE, LOW);
	shiftOut(DIN, CLK, dat); //transmit serial data
	DigitalWrite(CE, HIGH);
}

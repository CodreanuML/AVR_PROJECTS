/*
 * Nokia5110.h
 *
 * Created: 6/20/2023 2:02:41 PM
 *  Author: mcodrea2
 */ 


// NOKIA 5110 Display , CHECK DATA SHEET FOR COMMAND LIST
/*

Display Technology	Dot Matrix LCD
MCU Interface	SPI
Screen Size	1.5 Inch Across
Resolution	84×48 pixels  - 6 LINES , 84 COLUMNS
Operating Voltage	2.7V – 3.3V
Operating Current	50mA max
Viewing Angle	180°  */



//PINOUT  FROM LEFT TO RIGHT

/*
1 RST - pin is used to reset the display. It is an active low pin, which means that by pulling it low, the display can be reset. By connecting this pin to the Arduino’s reset, the screen will be automatically reset.
2 CE - Chip Enable -pin is used to select one of several connected modules that share the same SPI bus. It’s also an active low pin.
3 D/C -Data / Command - is used by the library to separate the commands (such as setting the cursor to a specific location, clearing the screen, etc.) from the data.
4 DIN - serial data pin
5 CLK - serial clock pin
6 VCC -LCD VCC
7 BL - Blacklight pin controls the backlight of the display. By connecting this pin to any PWM-capable Arduino pin or by using a potentiometer, the brightness can be controlled.
8 GND - GroundPin
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

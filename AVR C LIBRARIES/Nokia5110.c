/*
 * Nokia5110.h
 *
 * Created: 6/20/2023 2:02:41 PM
 *  Author: mcodrea2
 */ 

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

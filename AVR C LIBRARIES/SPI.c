/* SPI.C
 *
 * Created: 6/2/2023 1:03:44 PM
 *  Author: mcodrea2
 */
#include <avr/io.h>
#define SCK     5
#define MISO    4
#define MOSI    3
#define SS    2


/* AVR ATmega32 uses three registers to configure SPI communication that are SPI Control Register, SPI Status Register and SPI Data Register.

SPCR: SPI Control Register
Bit 7 – SPIE: SPI Interrupt Enable bit
1 = Enable SPI interrupt.
0 = Disable SPI interrupt.
Bit 6 – SPE: SPI Enable bit
1 = Enable SPI.
0 = Disable SPI.
Bit 5 – DORD: Data Order bit
1 = LSB transmitted first.
0 = MSB transmitted first.
Bit 4 – MSTR: Master/Slave Select bit
1 = Master mode.
0 = Slave Mode.
Bit 3 – CPOL: Clock Polarity Select bit
1 = Clock start from logical one.
0 = Clock start from logical zero.
Bit 2 – CPHA: Clock Phase Select bit
1 = Data sample on trailing clock edge.
0 = Data sample on the leading clock edge.
Bit 1:0 – SPR1: SPR0 SPI Clock Rate Select bits

SPSR: SPI Status Register
Bit 7 – SPIF: SPI interrupt flag bit
This flag gets set when the serial transfer is complete.
Also gets set when the SS pin is driven low in master mode.
It can generate an interrupt when SPIE bit in SPCR and a global interrupt is enabled.
Bit 6 – WCOL: Write Collision Flag bit
This bit gets set when SPI data register writes occurs during previous data transfer.
Bit 5:1 – Reserved Bits
Bit 0 – SPI2X: Double SPI Speed bit
When set, SPI speed (SCK Frequency) gets doubled.

SPDR: SPI Data Register
SPI Data register used to transfer data between the Register file and SPI Shift Register.
Writing to the SPDR initiates data transmission.

When the device is in master mode
Master writes data byte in SPDR. Writing to SPDR starts data transmission.
8-bit data starts shifting out towards slave and after the complete byte is shifted, SPI clock generator stops, and SPIF bit gets set.

When the device is in slave mode

THE Slave SPI interface remains in sleep as long as the SS pin is held high by the master.
It activates only when the SS pin is driven low. Data is shifted out with incoming SCK clock from master during a write operation.
SPIF is set after the complete shifting of a byte.



*/




void SPI_MASTER_Init()					/* SPI Initialize function */
{
	DDRB |= (1<<MOSI)|(1<<SCK)|(1<<SS);	/* Make MOSI, SCK, SS 
						as Output pin */
	DDRB &= ~(1<<MISO);			/* Make MISO pin 
						as input pin */
	PORTB |= (1<<SS);			/* Make high on SS pin */
	SPCR = (1<<SPE)|(1<<MSTR)|(1<<SPR0);	/* Enable SPI in master mode
						with Fosc/16 */
	SPSR &= ~(1<<SPI2X);			/* Disable speed doubler */
}




void SPI_MASTER_Write(char data)		/* SPI write data function */
{
	
	char flush_buffer;
	SPDR = data;			/* Write data to SPI data register */
	while(!(SPSR & (1<<SPIF)));	/* Wait till transmission complete */
	flush_buffer = SPDR;		/* Flush received data */
	/* Note: SPIF flag is cleared by first reading SPSR (with SPIF set) and then accessing SPDR hence flush buffer used here to access SPDR after SPSR read */

}


char SPI_MASTER_Read()				/* SPI read data function */
{
	SPDR = 0xFF;
	while(!(SPSR & (1<<SPIF)));	/* Wait till reception complete */
	return(SPDR);			/* Return received data */
}


void SPI_SLAVE_Init()					/* SPI Initialize function */
{
	DDRB &= ~((1<<MOSI)|(1<<SCK)|(1<<SS));  /* Make MOSI, SCK, SS as
 						input pins */
	DDRB |= (1<<MISO);			/* Make MISO pin as 
						output pin */
	SPCR = (1<<SPE);			/* Enable SPI in slave mode */
}


char SPI_SLAVE_Receive()			/* SPI Receive data function */
{
	while(!(SPSR & (1<<SPIF)));	/* Wait till reception complete */
	return(SPDR);		/* Return received data */
}

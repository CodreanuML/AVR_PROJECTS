/*
 * USART.c
 *
 * Created: 6/20/2023 4:03:44 PM
 * Author: mcodrea2
 */ 

/*   
AVR USART REGISTERS :

UDR :USART DATA REGISTER 
It has basically two registers, one is Tx. Byte and the other is Rx Byte. Both share the same UDR register.
Do remember that, when we write to the UDR reg. Tx buffer will get written and when we read from this register, Rx Buffer will get read. Buffer uses the FIFO shift register to transmit the data.

UCSRA : USART Control and Status Register A
  Bit 7 – RXC: USART Receive Complete
  This flag bit is set when there is unread data in UDR. The RXC Flag can be used to generate a Receive Complete interrupt.

  Bit 6 – TXC: USART Transmit Complete
  This flag bit is set when the entire frame from Tx Buffer is shifted out and there is no new data currently present in the transmit buffer (UDR). The TXC Flag bit is automatically cleared when a transmit complete interrupt is executed, or it can be cleared by writing a one to its bit location. The TXC Flag can generate a Transmit Complete interrupt.

  Bit 5 – UDRE: USART Data Register Empty
  If UDRE is one, the buffer is empty which indicates the transmit buffer (UDR) is ready to receive new data. The UDRE Flag can generate a Data Register Empty Interrupt. UDRE is set after a reset to indicate that the transmitter is ready.

  Bit 4 – FE: Frame Error
  Bit 3 – DOR: Data OverRun
  This bit is set if a Data OverRun condition is detected. A Data OverRun occurs when the receive buffer is full (two characters) and a new character is waiting in the receive Shift Register.

  Bit 2 – PE: Parity Error
  Bit 1 – U2X: Double the USART Transmission Speed
  Bit 0 – MPCM: Multi-processor Communication Mode
  
UCSRB: USART Control and Status Register B

  Bit 7 – RXCIE: RX Complete Interrupt Enable
  Writing one to this bit enables interrupt on the RXC Flag.

  Bit 6 – TXCIE: TX Complete Interrupt Enable
  Writing one to this bit enables interrupt on the TXC Flag.

  Bit 5 – UDRIE: USART Data Register Empty Interrupt Enable
  Writing one to this bit enables interrupt on the UDRE Flag.

  Bit 4 – RXEN: Receiver Enable
  Writing one to this bit enables the USART Receiver.

  Bit 3 – TXEN: Transmitter Enable
  Writing one to this bit enables the USART Transmitter.

  Bit 2 – UCSZ2: Character Size
  The UCSZ2 bits combined with the UCSZ1:0 bit in UCSRC sets the number of data bits (Character Size) in a frame the receiver and transmitter use.

  Bit 1 – RXB8: Receive Data Bit 8
  Bit 0 – TXB8: Transmit Data Bit 8
  
 UCSRC: USART Control and Status Register C 
 
  Bit 7 – URSEL: Register Select
  This bit selects between accessing the UCSRC or the UBRRH Register, as both register shares the same address. The URSEL must be one when writing the UCSRC or else data will be written in the UBRRH register.

  Bit 6 – UMSEL: USART Mode Select
  This bit selects between the Asynchronous and Synchronous mode of operation.

  0 = Asynchronous Operation

  1 = Synchronous Operation

  Bit 5:4 – UPM1:0: Parity Mode
  These bits enable and set the type of parity generation and check. If parity a mismatch is detected, the PE Flag in UCSRA will be set.

  

  UPM1	UPM0	Parity Mode
  0	0	Disabled
  0	1	Reserved
  1	0	Enabled, Even Parity
  1	1	Enabled, Odd Parity
  

  Bit 3 – USBS: Stop Bit Select
  This bit selects the number of Stop Bits to be inserted by the Transmitter. The Receiver ignores this setting.

  0 = 1-bit

  1 = 2-bit

  Bit 2:1 – UCSZ1:0: Character Size
  The UCSZ1:0 bits combined with the UCSZ2 bit in UCSRB sets the number of data bits (Character Size) in a frame the Receiver and Transmitter use.

  

  UCSZ2	UCSZ1	UCSZ0	Character Size
  0	0	0	5-bit
  0	0	1	6-bit
  0	1	0	7-bit
  0	1	1	8-bit
  1	0	0	Reserved
  1	0	1	Reserved
  1	1	0	Reserved
  1	1	1	9-bit
  

  Bit 0 – UCPOL: Clock Polarity
  This bit is used for synchronous mode only. Write this bit to zero when the asynchronous mode is used. 


UBRRL and UBRRH: USART Baud Rate Registers

Bit 15 – URSEL: Register Select
This bit selects between accessing the UCSRC or the UBRRH Register, as both register shares the same address. The URSEL must be one when writing the UCSRC or else data will be written in the UBRRH register.

Bit 11:0 – UBRR11:0: USART Baud Rate Register.
            Used to define the baud rate

\mathbf{UBBR = \frac{Fosc}{16 * Baud Rate} - 1}                   \mathbf{Baud Rate = \frac{Fosc}{16 * (UBBR + 1)}}       

Example: suppose Fosc=8 MHz and required baud rate= 9600 bps.

Then the value of UBRR= 51.088 i.e. 51.

 

We can also set this value by c code using pre-processor macro as follow.

//#define F_CPU 8000000UL		
//#define USART_BAUDRATE 9600
//#define BAUD_PRESCALE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1)
//BAUD_PRESCALE is the value that we have to load in the UBRR register to set the defined baud rate.

//MACROS DEFINITIONS

#define UCSR0A _SFR_MEM8(0xC0)
#define MPCM0 0
#define U2X0 1
#define UPE0 2
#define DOR0 3
#define FE0 4
#define UDRE0 5
#define TXC0 6
#define RXC0 7

#define UCSR0B _SFR_MEM8(0xC1)
#define TXB80 0
#define RXB80 1
#define UCSZ02 2
#define TXEN0 3
#define RXEN0 4
#define UDRIE0 5
#define TXCIE0 6
#define RXCIE0 7

#define UCSR0C _SFR_MEM8(0xC2)
#define UCPOL0 0
#define UCSZ00 1
#define UCPHA0 1
#define UCSZ01 2
#define UDORD0 2
#define USBS0 3
#define UPM00 4
#define UPM01 5
#define UMSEL00 6
#define UMSEL01 7

#define UBRR0 _SFR_MEM16(0xC4)

#define UBRR0L _SFR_MEM8(0xC4)
#define UBRR0_0 0
#define UBRR0_1 1
#define UBRR0_2 2
#define UBRR0_3 3
#define UBRR0_4 4
#define UBRR0_5 5
#define UBRR0_6 6
#define UBRR0_7 7

#define UBRR0H _SFR_MEM8(0xC5)
#define UBRR0_8 0
#define UBRR0_9 1
#define UBRR0_10 2
#define UBRR0_11 3

#define UDR0 _SFR_MEM8(0xC6)
#define UDR0_0 0
#define UDR0_1 1
#define UDR0_2 2
#define UDR0_3 3
#define UDR0_4 4
#define UDR0_5 5
#define UDR0_6 6
#define UDR0_7 7




/* POLLING METHOD   */
/*
Initialization of USART

Enable transmission and reception by using the UCSRB register.
Set data bit size to 8 bit by using the UCSRC register.
Set baud rate using the UBRR register.
*/

//INIT
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>
#include <stdlib.h>
#include <stdio.h>
#define BAUD_PRESCALE (((F_CPU / (USART_BAUDRATE * 16UL))) - 1)

void UART_init_POLLING(long USART_BAUDRATE)
{
	UCSR0B |= (1 << RXEN0) | (1 << TXEN0);	/* Turn on transmission and reception */
	UCSR0C |= (1 <<  UMSEL01) | (1 << UCSZ00) | (1 << UCSZ01);/* Use 8-bit char size */
	UBRR0L = BAUD_PRESCALE;			/* Load lower 8-bits of the baud rate */
	UBRR0H = (BAUD_PRESCALE >> 8);		/* Load upper 8-bits*/
}

//Receiving Character
unsigned char UART_RxChar()
{
	while ((UCSR0A & (1 << RXC0)) == 0);/* Wait till data is received */
	return(UDR0);		/* Return the byte */
}

//Transmitting Character
void UART_TxChar(char ch)
{
	while (! (UCSR0A & (1<<UDRE0)));  /* Wait for empty transmit buffer */
	UDR0 = ch ;
}

/* INTERRUPT METHOD*/

void UART_init_INTERRUPT(long USART_BAUDRATE)
{
	UCSR0B |= (1 << RXEN0) | (1 << RXCIE0);/* Turn on the transmission and reception */
	UCSR0C |= (1 <<  UMSEL01) | (1 << UCSZ00) | (1 << UCSZ01);/* Use 8-bit character sizes */

	UBRR0L = BAUD_PRESCALE;		/* Load lower 8-bits of the baud rate */
	UBRR0H = (BAUD_PRESCALE >> 8);	/* Load upper 8-bits */
}


///USE ISR TO READ
/*EXAMPLE
ISR(USART_RXC_vect)
{
	unsigned char a;
	a=UDR;
}
*/

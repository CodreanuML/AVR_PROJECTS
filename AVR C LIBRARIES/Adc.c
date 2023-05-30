/*
 * AdcDac.c
 *
 * Created: 3/19/2023 6:04:27 PM
 *  Author: mcodrea2
 */ 
# define F_CPU 16000000UL
#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdlib.h>
#include <util/delay.h>
/*

ATmega16/32 supports eight ADC channels, which means we can connect eight analog inputs at a time. ADC channel 0 to channel 7 are present on PORTA. i.e. Pin no.33 to 40.

The controller has 10 bit ADC, which means we will get digital output 0 to 1023.

i.e. When the input is 0V, the digital output will be 0V & when input is 5V (and Vref=5V), we will get the highest digital output corresponding to 1023 steps, which is 5V.

So controller ADC has 1023 steps and

Step size with Vref=5V :  5/1023 = 4.88 mV.
Step size with Vref=2.56 :  2.56/1023 = 2.5 mV.
So Digital data output will be Dout = Vin / step size.



ATmega16/32 ADC Features
It is 10-bit ADC
Converted output binary data is held in two special functions 8-bit register ADCL (result Low) and ADCH (result in High).
ADC gives 10-bit output, so (ADCH: ADCL) only 10-bits are useful out of 16-bits.
We have options to use this 10-bits as upper bits or lower bits.
We also have three options for Vref. 1. AVcc (analog Vcc), 2. Internal 2.56 v3. External Aref. Pin.
The total conversion time depends on crystal frequency and ADPS0: 2 (frequency devisor)
If you decided to use AVcc or Vref pin as ADC voltage reference, you can make it more stable and increase the precision of ADC by connecting a capacitor between that pin and GND.


ATmega16/32 ADC Registers
In AVR ADC, we need to understand four main register -

ADCH: Holds digital converted data higher byte
ADCL: Holds digital converted data lower byte
ADMUX: ADC Multiplexer selection register
ADCSRA: ADC Control and status register

ADMUX Register - BitMap
7 REFS1 // Combined with REFS0 to set up the reference voltage
6 REFS0
5 ADLAR // ADLAR: ADC Left Adjust Result
4 MUX4  // Setting the prescaller
3 MUX3  // Setting the prescaller
2 MUX2  // Setting the prescaller
1 MUX1  // Setting the prescaller
0 MUX0  // Setting the prescaller

ADCSRA Register - BitMap

Bit 7 – ADEN: ADC Enable Writing one to this bit enables the ADC. By writing it to zero, the ADC is turned off. Turning the ADC off while a conversion is in progress, will terminate this conversion.
Bit 6 – ADSC: ADC Start Conversion Writing one to this bit starts the conversion.
Bit 5 – ADATE: ADC Auto Trigger Enable Writing one to this bit, results in Auto Triggering of the ADC is enabled.
Bit 4 – ADIF: ADC Interrupt Flag This bit is set when an ADC conversion completes and the Data Registers are updated.
Bit 3 – ADIE: ADC Interrupt Enable Writing one to this bit, the ADC Conversion Complete Interrupt is activated.
Bits 2 : 0 – ADPS2 : 0: ADC Prescaler Select BitsThese bits determine the division factor between the XTAL frequency and the input clock to the ADC

Steps to Program ATmega16/32 ADC
Make the ADC channel pin as an input.
Set ADC enable bit in ADCSRA, select the conversion speed using ADPS2 : 0. For example, we will select devisor 128.
Select ADC reference voltage using REFS1: REFS0 in ADMUX register, for example, we will use AVcc as a reference voltage.
Select the ADC input channel using MUX4 : 0 in ADMUX, for example, we will use channel 0.
So our value in register ADCSRA = 0x87 and ADMUX = 0x40.
Start conversion by setting bit ADSC in ADCSRA. E.g.ADCSRA |= (1<<ADSC);
Wait for conversion to complete by polling ADIF bit in ADCSRA register.
After the ADIF bit gone high, read ADCL and ADCH register to get digital output.
Notice that read ADCL before ADCH; otherwise result will not be valid.

*/

void ADC_Init(){
	
		
		ADCSRA = 0x87;			/* Enable ADC, fr/128  */
		ADMUX = 0x40;			/* Vref: Avcc, ADC channel: 0 */	
}


int ADC_Read(char channel)
{
	int Ain,AinLow;
	
	ADMUX=ADMUX|(channel & 0x0f);	/* Set input channel to read */

	ADCSRA |= (1<<ADSC);		/* Start conversion */
	while((ADCSRA&(1<<ADIF))==0);	/* Monitor end of conversion interrupt */
	
	_delay_us(10);
	AinLow = (int)ADCL;		/* Read lower byte*/
	Ain = (int)ADCH*256;		/* Read higher 2 bits and 
					Multiply with weight */
	Ain = Ain + AinLow;				
	return(Ain);			/* Return digital value*/
}

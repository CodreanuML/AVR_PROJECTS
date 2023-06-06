/*
 * SPI.h
 *
 * Created: 6/2/2023 1:03:44 PM
 *  Author: mcodrea2
 */ 





# define F_CPU 16000000UL
#ifndef SPI_H_
#define SPI_H_

#define SCK     5
#define MISO    4
#define MOSI    3
#define SS    2
#define SS_Enable PORTB &= ~(1<<SS)			/* Define Slave enable */
#define SS_Disable PORTB |= (1<<SS)			/* Define Slave disable */

///initialize SPI as MASTER

void SPI_MASTER_Init();

///initializare SPI as SLAVE

void SPI_SLAVE_Init();

/// SPI Master Write 
void SPI_MASTER_Write(char data) ;

/// SPI Master Read 
char SPI_MASTER_Read();

///SPI Slave Receive

char SPI_SLAVE_Receive()	;



#endif /* SPI_H_ */

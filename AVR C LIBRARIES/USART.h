/*
 * USART.h
 *
 * Created: 6/20/2023 4:03:44 PM
 *  Author: mcodrea2
 */ 



# define F_CPU 16000000UL
#ifndef USART_H_
#define USART_H_

//POLLING METHOD
//INIT
void UART_init_POLLING(long USART_BAUDRATE);
//Receiving Character
unsigned char UART_RxChar();
//Transmitting Character
void UART_TxChar(char ch);



//INTERRUPT METHOD
//INIT
void UART_init_INTERRUPT(long USART_BAUDRATE);
#endif /* USART_H_ */

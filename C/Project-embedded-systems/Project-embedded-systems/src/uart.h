/*
 * uart.h
 *
 * Created: 04/11/2020 04:36:38
 *  Author: Richard Ringia and Robbin Kok
 */ 


#ifndef UART_H_
#define UART_H_

#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

#define UBBRVAL 51
#define F_CPU 16E6

void uart_init(uint16_t ubrr) {
	// set the baud rate
	//UBRR0H = 0;
	//UBRR0L =  UBBRVAL;
	UBRR0L = (uint8_t)(ubrr & 0xFF);
	UBRR0H = (uint8_t)(ubrr >> 8);
	
	// disable U2X mode
	// Remove the prescaler devide by 2 and will increase the speed of the UART to double
	UCSR0A = 0;
	
	// Enable transmitter and reciever
	UCSR0B = _BV(TXEN0) | (1 << RXEN0);
	
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
	
}


uint8_t usart_read(){
	loop_until_bit_is_set(UCSR0A, RXC0); // wait until the data exists
	
	return UDR0;

}

void usart_transmit(uint8_t data){
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// send the data
	UDR0 = data;
}



#endif /* ADC_H_ */
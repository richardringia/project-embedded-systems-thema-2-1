/*
 * uart.h
 *
 * Created: 04/11/2020 04:36:38
 * Author: Richard Ringia and Robbin Kok
 * 
 * http://www.rjhcoding.com/avrc-uart.php
 */ 


#ifndef UART_H_
#define UART_H_

#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

#define F_CPU 16E6

void uart_init() {
	// set the baud rate
	UBRR0H = 0;
	UBRR0L = 51;
	
	// disable U2X mode
	UCSR0A = 0;
	
	// enable transmitter and receiver
	UCSR0B = _BV(TXEN0) | (1 << RXEN0);
	
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
	
	_delay_ms(1000);
}

// Read data of arduino with uart
uint8_t uart_read(){
	// Wait until data exists
	loop_until_bit_is_set(UCSR0A, RXC0); 
	return UDR0;
}


void uart_send(int data) {
	loop_until_bit_is_set(UCSR0A,UDRE0);

	// Load data into transmit register
	UDR0 = data;
}

void uart_send_char(char data) {
	loop_until_bit_is_set(UCSR0A,UDRE0);

	// Load data into transmit register
	UDR0 = data;
}





#endif /* ADC_H_ */
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

// Send char data to arduino with uart
void uart_putc(unsigned char data)
{
	// Wait until data exists.
	loop_until_bit_is_set(UCSR0A,UDRE0);

	// Load data into transmit register
	UDR0 = data;
}

// Transmit decimal with uart
void uart_transmit(uint8_t val)
{
	uint8_t dig1 = '0', dig2 = '0';

	// count value in 100s place
	while(val >= 100)
	{
		val -= 100;
		dig1++;
	}

	// count value in 10s place
	while(val >= 10)
	{
		val -= 10;
		dig2++;
	}

	// print first digit (or ignore leading zeros)
	if(dig1 != '0') uart_putc(dig1);

	// print second digit (or ignore leading zeros)
	if((dig1 != '0') || (dig2 != '0')) uart_putc(dig2);

	// print final digit
	uart_putc(val + '0');
}



#endif /* ADC_H_ */
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
	
}


uint8_t usart_read(){
	loop_until_bit_is_set(UCSR0A, RXC0); /* Wait until data exists. */

	return UDR0;
}

void usart_transmit(uint8_t data)
{
	// wait for an empty transmit buffer
	// UDRE is set when the transmit buffer is empty
	loop_until_bit_is_set(UCSR0A,UDRE0);
	// send the data
	UDR0 = data;
}

void UART_putc(unsigned char data)
{
	// wait for transmit buffer to be empty
	//while(!(UCSR0A & (1 >> UDRE0)));

	loop_until_bit_is_set(UCSR0A,UDRE0);

	// load data into transmit register
	UDR0 = data;
}


void UART_puthex8(uint8_t val)
{
	// extract upper and lower nibbles from input value
	uint8_t upperNibble = (val & 0xF0) >> 4;
	uint8_t lowerNibble = val & 0x0F;

	// convert nibble to its ASCII hex equivalent
	upperNibble += upperNibble > 9 ? 'A' - 10 : '0';
	lowerNibble += lowerNibble > 9 ? 'A' - 10 : '0';

	// print the characters
	UART_putc(upperNibble);
	UART_putc(lowerNibble);
}

void UART_putU8(uint8_t val)
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
	if(dig1 != '0') UART_putc(dig1);

	// print second digit (or ignore leading zeros)
	if((dig1 != '0') || (dig2 != '0')) UART_putc(dig2);

	// print final digit
	UART_putc(val + '0');
}



#endif /* ADC_H_ */
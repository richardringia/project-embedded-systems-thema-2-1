/*
 * adc.h
 *
 * Created: 04/11/2020 04:43:18
 *  Author: Richard Ringia and Robbin Kok
 */ 


#ifndef ADC_H_
#define ADC_H_

#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

#define UBBRVAL 51

void uart_init() {
	// set the baud rate
	UBRR0H = 0;
	UBRR0L =  UBBRVAL;
	
	// disable U2X mode
	// Remove the prescaler devide by 2 and will increase the speed of the UART to double
	UCSR0A = 0;
	
	// Enable transmitter and reciever
	UCSR0B = _BV(TXEN0) | (1 << RXEN0);
	
	// set frame format : asynchronous, 8 data bits, 1 stop bit, no parity
	UCSR0C = _BV(UCSZ01) | _BV(UCSZ00);
	
}

// read adc value
uint16_t adc_read(uint8_t ch)
{
	// select the corresponding channel 0~7
	// ANDing with '7' will always keep the value
	// of 'ch' between 0 and 7
	ch &= 0b00000111;  // AND operation with 7
	ADMUX = (ADMUX & 0xF8)|ch;     // clears the bottom 3 bits before ORing
	
	// start single conversion
	// write '1' to ADSC
	ADCSRA |= (1<<ADSC);
	
	// wait for conversion to complete
	// ADSC becomes '0' again
	// till then, run loop continuously
	while(ADCSRA & (1<<ADSC));
	
	return (ADC);
}



#endif /* ADC_H_ */
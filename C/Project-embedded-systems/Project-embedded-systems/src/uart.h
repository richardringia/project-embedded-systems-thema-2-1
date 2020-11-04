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

void adc_init() {
	// AREF = AVcc
	ADMUX = (1<<REFS0);
	
	// ADC Enable and prescaler of 128
	// 16000000/128 = 125000
	ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
	
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
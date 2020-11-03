/**
 * \file
 *
 * \brief Empty user application template
 *
 */

/**
 * \mainpage User Application template doxygen documentation
 *
 * \par Empty user application template
 *
 * Bare minimum empty user application template
 *
 * \par Content
 *
 * -# Include the ASF header files (through asf.h)
 * -# "Insert system clock initialization code here" comment
 * -# Minimal main function that starts with a call to board_init()
 * -# "Insert application code here" comment
 *
 */

/*
 * Include header files for all drivers that have been imported from
 * Atmel Software Framework (ASF).
 */
/*
 * Support and FAQ: visit <a href="https://www.microchip.com/support/">Microchip Support</a>
 */
#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

#define UBBRVAL 51



void uart_init(){
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

uint8_t usart_read(){
	loop_until_bit_is_set(UCSR0A, RXC0); // wait until the data exists
	
	return UDR0;

}

void usart_transmit(uint8_t data){
	
	loop_until_bit_is_set(UCSR0A, UDRE0);
	// send the data
	UDR0 = data;
}

void adc_init()
{
	 // AREF = AVcc
	 ADMUX = (1<<REFS0);
	 
	 // ADC Enable and prescaler of 128
	 // 16000000/128 = 125000
	 ADCSRA = (1<<ADEN)|(1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0);
	 
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

int main (void)
{
	/* Insert system clock initialization code here (sysclk_init()). */

	board_init();
	uart_init();
	adc_init();
	DDRD = 0xff;
	
	while (1) {
		float value = adc_read(0) * 4.68;
		value /= 1024.0;
		float temperatureC = (value - 0.5) * 100;
		if (temperatureC > 16)
		{
			PORTD = 0b11100000;
		}
		else
		{
			PORTD = 0b00100000;
		}

  }
	
	
	
	/* Insert application code here, after the board has been initialized. */
}

/*
 * leds.h
 *
 * Created: 06/11/2020 17:04:35
 *  Author: Ricahrd Ringia & Robbin Kok
 */ 


#ifndef LEDS_H_
#define LEDS_H_
#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>
#include <uart.h>

void rolled_in(){
	PORTB |= 0b00000001; // Green
}

void rolled_out(){
	PORTB |= 0b00000100; // Red
}

void rolling(){
	
	PORTB |= 0b00000010;
	_delay_ms(2000);
	PORTB |= 0b00000000;
	_delay_ms(2000);
	
}

void reset(){
	PORTB = 0x00;
}

#endif /* LEDS_H_ */
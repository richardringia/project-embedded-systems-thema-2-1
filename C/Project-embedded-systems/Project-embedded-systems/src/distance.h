/*
 * distance.h
 *
 *
 * Created: 29-6-2016 14:44:43
 *  Author: Anne Pier Merkus, Robbin Kok and Richard Ringia
 */ 

/* 
 * HC-SR04
 * trigger to sensor : uno 0 (PD0) output
 * echo from sensor  : uno 3 (PD3 = INT1) input
 * 
 * DIO : uno 8  (PB0) data
 * CLK : uno 9  (PB1) clock
 * STB : uno 10 (PB2) strobe
 *
 */

#ifndef DISTANCEH
#define DISTANCEH

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

#define F_CPU 16E6
#define HIGH 0x1
#define LOW  0x0

unsigned char working;
unsigned char rising_edge;

uint16_t timer_value = 0;
uint16_t distance_cm;
uint8_t	error;

const uint8_t data=0;
const uint8_t clock=1;
const uint8_t strobe=2;

volatile uint16_t gv_counter; // 16 bit counter value
volatile uint8_t gv_echo; // a flag

ISR(TIMER1_OVF_vect)
{
	
	if(rising_edge==1)
	{
		timer_value++;
		if(timer_value > 91)
		{
			working = 0;
			rising_edge = 0;
			error = 1;
		}
	}
}

ISR (INT1_vect)
{
	if(working==1)
	{
		if(rising_edge==0)
		{
			rising_edge=1;
			TCNT1 = 0;
			timer_value = 0;
		}
		else
		{
			rising_edge = 0;
			distance_cm = (timer_value * 65536 + TCNT1)*0.5*0.0023;
			working = 0;
		}
	}
	TCCR1B = _BV(CS10);
}

//Signal to hc-sr04
void send_signal_distance()
{
	if(working==0)
	{
		
		_delay_ms(50);
		PORTD &=~ (1<<PIND0);
		_delay_us(1);
		PORTD |= (1<<PIND0);
		_delay_us(10);
		PORTD &=~ (1<<PIND0);
		working = 1;
		error = 0;
	} 
}

void init_ports(void)
{
    DDRD = 0b11110111;
	DDRB = 0xff;
}

void init_timer(void)
// prescaling : max time = 2^16/16E6 = 4.1 ms, 4.1 >> 2.3, so no prescaling required
// normal mode, no prescale, stop timer
{
    TCCR1A = 0;
    TCCR1B = 0;
	TCNT1 = 0;
	TIMSK1 = (1<<TOIE0);
}

void init_ext_int(void)
{
    // any change triggers ext interrupt 1
    EICRA |= (1 << ISC10);
    EIMSK |= (1 << INT1);
}


uint16_t calc_cm(uint16_t counter)
{
	return 0;
}

int get_distance() 
{
	return distance_cm;
}

int distance_init(void)
{
	init_ports();
	init_ext_int();
	init_timer();
	
    return 0;
}


#endif /* DISTANCEH */
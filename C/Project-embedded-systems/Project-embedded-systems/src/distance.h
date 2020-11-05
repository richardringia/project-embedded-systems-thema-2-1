/*
 * distance.h
 *
 * Created: 05/11/2020 05:06:48
 *  Author: Jaron Oun, Robbin Kok and Richard Ringia
 */ 


#ifndef DISTANCE_H_
#define DISTANCE_H_

#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

#define F_CPU 16E6
#define HIGH 0x1
#define LOW  0x0

unsigned char working;
unsigned char rising_edge;

uint16_t timer_value = 0;
uint16_t distance_cm;
uint8_t	error;

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


void Send_signal()
{
	if(working==0)
	{
		_delay_ms(50);
		PORTB &=~ (1<<PIND0);
		_delay_us(1);
		PORTB |= (1<<PIND0);
		_delay_us(10);
		PORTB &=~ (1<<PIND0);
		working = 1;
		error = 0;
	}
}


uint16_t get_distance()
{
	Send_signal();
	_delay_ms(1000);
	return distance_cm;
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


void distance_init()
{
	init_ext_int();
	init_timer();
	sei();
	
	//while(1) {
		
	//}
}

#endif /* DISTANCE_H_ */
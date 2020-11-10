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
#include <uart.h>
#include <adc.h>
#include <distance.h>
#include <lights.h>
#include <temperature.h>
#include <leds.h>
#include <stdbool.h>
#include <converter.h>


int auto_mode = 0;
int distance = 0;
int counter = 0;
int last_read = 0x31;
int data_sendend = 0;
int auto_distance = 0;
int is_reading = 0;
int read_type = 0;
int read_value = 0;

/************************************************************************/
/*	SEND DATA PROTOCOL:													*/
/*	0 0 0 = nothing														*/
/*	1 2 {value} = send temperature										*/
/*	1 3 {value} = send light											*/
/*	1 4 {value} = send distance											*/
/*	1 9 {value} = test													*/
/************************************************************************/
void send_data(int read_data)
{
	char data = 0;
		
	if (counter == 8) {
		update_temp();
	}
		
	if (counter == 3) {
		update_light();
	}
	
	if (counter == 10 && data_sendend == 0) {
		uart_send(1);
		uart_send(2);
		uart_send(get_temp());
		uart_send(1);
		uart_send(3);
		uart_send(get_light());
		data_sendend = 1;
		
		auto_distance = (temp_update_value() + light_update_value()) / 2;
		uart_send(1);
		uart_send(9);
		uart_send(auto_distance);
	}
	
	if (counter == 1) {
		data_sendend = 0;
	}

	
	
	
	uart_send(data);
}

/************************************************************************/
/*	READ DATA PROTOCOL:													*/
/*	0/1 = counter														*/
/*	2/3 = change auto modus												*/
/*	5 = min_temp
/*	6 = max_temp
/*	7 = min_light
/*	8 = max_light
/************************************************************************/
int read_data() {
	int read_data = uart_read();
	
	if (read_data == 0x23) {	
		uart_send(1);
		uart_send(9);
		uart_send(read_value);
		switch (read_type)
		{
			case 0x35:
				min_temp = read_value;
			break;
			case 0x36:
				max_temp = read_value;
			break;
			case 0x37:
				min_light = read_value;
			break;
			case 0x38:
				max_light = read_value;
			break;
			default:
			break;
		}
		
		is_reading = 0;
		read_value = 0;
		read_type = 0;
	} 
	else if (read_type == 0) {	
		if (read_data == 0x30 || read_data == 0x31) {
			if (read_data != last_read)	{
				if (counter == 10) {
					counter = 1;
					} else {
					counter = counter + 1;
				}
				last_read = read_data;
			}
		}
		
		if (read_data == 0x32) {
			auto_mode = 0;
		} else if (read_data == 0x33) {
			auto_mode = 1;
		}
		
		if (read_data == 0x34 || read_data == 0x35 || read_data == 0x36 || read_data == 0x37 || read_data == 0x38) {
			read_type = read_data;
			is_reading = 1;
		}
	} else if (is_reading) {
		PORTB = 0b00000100;
		read_value = read_value * 10 + convert_to_int(read_data);
	}
	
	return read_data;
}

/************************************************************************/
/* The change mode function is used for changing the value of the bool.	*/
/* If the bool is true it becomes false.								*/
/* If the bool is false it becomes true									*/
/************************************************************************/

void change_mode(){
	auto_mode = !auto_mode;
}


/************************************************************************/
/* The roll sunscreen function is for controlling the leds.				*/
/* 0 = Rolling the screen out and burning the corresponding led.		*/
/* 1 = Rolling the screen in and burning the corresponding led.		    */
/************************************************************************/

void roll_sunscreen(int mode)
{
	switch (mode){
		case 0:
			rolling();
			rolled_out();
			break;
		case 1:
			rolling();
			rolled_in();
			break;
		default:
			break;
	}
}


int main (void)
{
	DDRD = 0x00;
	DDRB = 0xff;
	
	// init
	board_init();
	uart_init();	
	adc_init();
	distance_init();
	
	sei();
	
	
	while (1) {
		
		if (auto_mode) {
			
		} else {
			send_signal_distance();
			_delay_ms(1000);
		}
		
		
		
		send_data(read_data());
		
		
		int new_distance = auto_mode ? auto_distance : get_distance();
		
		if (new_distance != distance) {
			roll_sunscreen(new_distance < distance);
			uart_send(1);
			uart_send(4);
			uart_send(new_distance);
		} else {
			reset();
		}
		distance = new_distance;
	}
}

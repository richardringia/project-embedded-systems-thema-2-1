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
#include <lights.h>
#include <temperature.h>
#include <distance.h>
#include <leds.h>
#include <stdbool.h>



uint16_t max_roll_distance = 300;
uint16_t min_roll_distance = 0;
bool auto_mode = true;
int distance = 0;

/************************************************************************/
/* The send data function is for sending data to the arduino.			*/
/* read_data is the value for which data it needs to send back			*/
/* 0 (0x30) = temperature sensor										*/
/* 1 (0x31) = light sensor												*/
/* 2 (0x32) = ultrazone senor                                           */
/************************************************************************/
void send_data(uint8_t read_data)
{
	uint8_t data = 0;
	
	
	switch (read_data)
	{
		case 0x30: // temperature
			data = get_temp();
		break;
		case 0x31: // light
			data = get_light();
		break;
		case 0x32: // ultrazone
			data = get_distance();
		break;
		default:
		break;
	}
	
	uart_send(data);
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
			//rolling();
			rolled_out();
			break;
		case 1:
			//rolling();
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
		send_signal_distance();
		_delay_ms(1000);
		
		
		uint8_t read_data = uart_read();
		send_data(read_data);
		
		
		int new_distance = get_distance();
		
		if (new_distance != distance) {
			rolling();
		} else {
			PORTB = 0b00000000;
		}
		distance = new_distance;	
	}
	

}

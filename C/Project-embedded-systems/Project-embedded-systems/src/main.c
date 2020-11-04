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




uint16_t max_roll_distance = 300;
uint16_t min_roll_distance = 0;



int main (void)
{
	/* Insert system clock initialization code here (sysclk_init()). */

	board_init();
	uart_init();
	adc_init();
	DDRD = 0xff;
	
	while (1) {
		
		
		if (get_light() > 100 && get_temp() > 10)
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

/*
 * lights.h
 *
 * Created: 04/11/2020 04:53:53
 *  Author: Richard Ringia & Robbin Kok
 */ 


#ifndef LIGHTS_H_
#define LIGHTS_H_


#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

#define index 10

// Lights
float avg_light = 0;
float lights[index];
uint16_t counter_light = 0;


float read_light() {
	return adc_read(5);
}

void calculate_avg_light() {
	int sum, i;
	
	for (i = 0; i < counter_light + 1; i++) {
		sum = sum + lights[i];
	}
	
	avg_light = (float) sum / i;
}

void update_light() {
	if (counter_light > (index + 1)) {
		counter_light = 0;
	}
	
	float new_light = read_light();
	lights[counter_light] = new_light;
	
	calculate_avg_light();
	
	counter_light = counter_light + 1;

	_delay_ms(1000);
}


float get_light() {
	return avg_light;
}


#endif /* LIGHTS_H_ */
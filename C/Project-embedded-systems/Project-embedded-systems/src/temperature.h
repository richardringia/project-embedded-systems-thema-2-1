/*
 * temperature.h
 *
 * Created: 04/11/2020 04:50:37
 *  Author: Richard Ringia and Robbin Kok
 */ 


#ifndef TEMPERATURE_H_
#define TEMPERATURE_H_

#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

#define index 10

float avg_temp = 0;
float temps[index];
uint16_t counter_temp = 0;

//TODO: Add array of temps and getter/filler for the temps

float read_temp() {
	float value = adc_read(0) * 4.68;
	value /= 1024.0;
	return ((value - 0.5) * 100) * 0.5;
}

void calculate_avg_temp() {
	int sum, i;
	
	for (i = 0; i < counter_temp + 1; i++) {
		sum = sum + temps[i];
	}
	
	avg_temp = (float) sum / i;
}

void update_temp() {
	if (counter_temp > (index + 1)) {
		counter_temp = 0;
	}
	
	float new_temp = read_temp();
	temps[counter_temp] = new_temp;
	
	counter_temp = counter_temp + 1;
	
}


float get_temp() {
	//calculate_avg_temp();
	//return avg_temp;
	return read_temp();
}





#endif /* TEMPERATURE_H_ */
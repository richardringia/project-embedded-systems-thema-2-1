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

// Temperatures
uint16_t inroll_temp = 15;
uint16_t outroll_temp = 20;
uint16_t avg_temp;
uint16_t temps[index];

//TODO: Add array of temps and getter/filler for the temps

void set_avarage_temp(uint16_t array[index]){
	int values = 0;
	int i = 0;
	
	for(i=0; i< index; i++){
		values + array[index];
	}
	avg_temp = values;
}

// TODO: change port number
float get_temp() {
	float value = adc_read(0) * 4.68;
	value /= 1024.0;
	return ((value - 0.5) * 100) * 0.5;
}





#endif /* TEMPERATURE_H_ */
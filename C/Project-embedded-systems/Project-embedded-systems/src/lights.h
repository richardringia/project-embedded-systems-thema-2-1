/*
 * lights.h
 *
 * Created: 04/11/2020 04:53:53
 *  Author: rring
 */ 


#ifndef LIGHTS_H_
#define LIGHTS_H_

#define index 10

#include <asf.h>
#include <avr/io.h>
#include <stdlib.h>
#include <avr/sfr_defs.h>
#include <util/delay.h>

// Lights
uint16_t outroll_light; //TODO: Add value
uint16_t inroll_light; //TODO: Add value
uint16_t lights[index];


float get_light() {
	return adc_read(5);
}


#endif /* LIGHTS_H_ */
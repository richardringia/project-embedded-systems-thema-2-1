/*
 * converter.h
 *
 * Created: 09/11/2020 16:11:41
 *  Author: rring
 */ 


#ifndef CONVERTER_H_
#define CONVERTER_H_


int convert_to_int(int value) {
	switch (value)
	{
		case 0x30:
			return 0;
		case 0x31:
			return 1;
		case 0x32:
			return 2;
		case 0x33:
			return 3;
		case 0x34:
			return 4;
		case 0x36:
			return 6;
		case 0x37:
			return 7;
		case 0x38:
			return 8;
		case 0x39:
			return 9;
		default:
			return 0;
	}
}


#endif /* CONVERTER_H_ */
#include <stdio.h>

int main(void){
	int number = 34751;	
	int reverse = 0;
	while(number > 0){
		reverse = reverse * 10 + number % 10;
		number = number / 10;
	}
	printf("reverse number = %d", reverse);
	return 0;
}
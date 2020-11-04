/* FILE    : Hex Oct Bin to Dec
 * WRITER  : NAT KANJANASIRI
 * DATE    : OCT 16, 2018
 * PURPOSE : Convert base 2, 8, 16 to base 10
 */
#include <stdio.h>
#include <string.h>
#include <math.h>

int main(void){
	int i = 0, j, y = 0, len, base, digit;
	float number = 0.0;
	char table[16] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
	char input[16];
	printf("Enter number : ");
	scanf("%s", input);
	printf("Enter base : ");
	scanf("%d", &base);
	len = strlen(input);
	for(i = len - 1; i >= 0; i--){
		for(j = 0; j < 16; j++){
			if(input[i] == table[j])
			digit = j;
		}
		number += digit * pow(base, y);
		y++;		
	}
	printf("BASE 10 is %f", number);
	return 0;
}

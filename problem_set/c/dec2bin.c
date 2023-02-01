/* FILE    : Dec to Hex Oct Bin
 * WRITER  : NAT KANJANASIRI
 * DATE    : FEB 1, 2023
 * PURPOSE : Convert base 10 to 2, 8, 16
 */
#include <stdio.h>
#include <string.h>

int main(void){
	char table[16] = "0123456789ABCDEF";
	char buffer[30], answer[30] = "";
	long number;
	int remainder, base = 2;
	scanf("%d", &number);
	if(number == 0) sprintf(answer, "0");
	while(number > 0){
		remainder = number % base;
		number = number / base;
		strcpy(buffer, answer);
		sprintf(answer, "%c%s", table[remainder], buffer);
	}
	printf("%s", answer);
	return 0;
}

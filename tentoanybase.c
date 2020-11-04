#include <stdio.h>

int main(void){
	int i = 0, j, base, number;
	char table[16] = {'0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F'};
	char out[16];
	printf("Enter number and base : ");
	scanf("%d %d", &number, &base);
	while (number > 0){
		out[i] = table[number % base];
		number = number / base;
		i++;
	}
	for(j = i - 1; j >= 0; j--){
		printf("%c", out[j]);
	}
	return 0;
}

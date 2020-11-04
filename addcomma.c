#include <stdio.h>
#include <string.h>

int main(void){
	int number, i, j, top = 0, len;
	char in[30], out[30];
	printf("Enter number : ");
	scanf("%d", &number);
	sprintf(in, "%d", number);
	len = strlen(in);
	for(i = len - 1, j = 1; i >= 0; i--, j++){
		out[top] = in[i];
		top++;
		if(j % 3 == 0 && j < len){
			out[top] = ',';
			top++;
		}		
	}	
	for(i = top - 1; i >= 0; i--){
		printf("%c",out[i]);
	}
	return 0;
}
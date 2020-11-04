/**********************
 * Program : PALINDROME
 * Writer  : NAT KANJANASIRI
 * Date    : Sep 28, 2020
 * Version : 0.14
 **********************/
#include <stdio.h>
#include <string.h>

int main(void){
    char input[10];
	int i, j, len = 0, isPALINDOME = 1;
	printf("Type your input : ");
	scanf("%s", input);
	len = strlen(input); // find number of loop by char len

	for(i = 0, j = len - 1; i < len/2; i++, j--){		// index i represented first address		
		if(input[i] != input[j]){	// index j represented last address
			isPALINDOME = 0; break;
		} 
	}
	isPALINDOME != 0 ? printf("PALINDROME") : printf("NO");
	return 0;
}
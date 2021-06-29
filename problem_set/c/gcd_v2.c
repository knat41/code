/**********************
 * Program : gcd (using loop do while)
 * Writer  : NAT KANJANASIRI
 * Date    : Sep 28, 2020
 * Version : 0.14
 **********************/
#include <stdio.h>

int main(void){
// r = remainder l = larger	s = smaller
	int r, l, s;
	printf("Enter two number : ");
	scanf("%d %d", &l, &s);	
	do{
		r = l % s;
		l = s;
		s = r;
	} while(r != 0);
	printf("GCD = %d", l);
	return 0;
}

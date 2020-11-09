/**********************
 * Program : gcd (using loop for)
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
	for(r = l % s; r > 0; r = l % s){
		l = s;
		s = r;		
	}
	
	printf("GCD = %d", s);
	return 0;
}

/**********************
 * Program : Day in Month
 * Writer  : NAT KANJANASIRI
 * Date    : Oct 1, 2020
 * Version : 0.1
 **********************/

#include <stdio.h>

int main(void){
	int month, year, ad;
	int day_in_month[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
	scanf("%d %d", &month, &year);
	ad = year - 543;
	if( ((ad % 4 == 0) && (ad % 100 != 0)) || ad % 400 == 0){
		day_in_month[1] = 29;
	}
	printf("%d", day_in_month[month - 1]);
	return 0;
}

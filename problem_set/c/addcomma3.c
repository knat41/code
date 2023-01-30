#include <stdio.h>
#include <string.h>

int main (){
  char buffer[50], answer[50] = "";  
  long remainder, number;
  int count = 0;
  scanf("%d", &number);
  while(number > 0){
	remainder = number % 10;
	number = number / 10;
	count++;
	strcpy(buffer, answer);
	sprintf (answer, "%d%s", remainder, buffer);	
	if(count % 3 == 0 && number != 0){
		strcpy(buffer, answer);
		sprintf (answer, ",%s", buffer);
	}
  }
  printf ("%s\n", answer);
  return 0;
}

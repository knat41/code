/* ****************************************
 * Program : please name your program     *
 * Purpose : what is you program do ?     *
 * Author  : who is write this code ?     *
 * Date    :                              *
 ******************************************/

#include<stdio.h>                        // # preprocessor

int a, b;                                // global  declaration statements

int sum(int x, int y);                   // function prototypes

int main()                               // function main
{                                        // begin function main   
     int c;                              // function declaration statements
     scanf("%d", &a);                    // source code (input)
     scanf("%d", &b);                    // source code (input)
     c = sum(a, b);                      // source code (process)
     printf("\n%d + %d = %d", a, b, c);  // source code (output)
     return 0;                           // source code (return of function)
}                                        // end function main

int sum(int x, int y)                    // function sum
{                                        // begin function sum
    return (x + y);                      // source code (return of function)
}                                        // end function sum

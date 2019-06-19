#include <stdio.h>

/*
    Run with gcc -o main *.c
    or with https://www.tutorialspoint.com/compile_c_online.php
*/

const int MAX = 3;

int main () {

   int  var[] = {10, 100, 200};
   int  i, *ptr;

   /* let us have array address in pointer */
   ptr = &var[MAX-1];
	
   for ( i = MAX; i > 0; i--) {

      printf("Address of var[%d] = %x\n", i-1, ptr );
      printf("Value of var[%d] = %d\n", i-1, *ptr );

      /* move to the previous location */
      ptr--;
   }
    ptr = &var[MAX-1];
	printf("ptr: %p \n", ptr );
	printf("*ptr: %d \n", *ptr );
	printf("ptr[0]: %d \n", ptr[0] );
	printf("&ptr: %p \n", &ptr );
	printf("&ptr[0]: %p \n", &ptr[0] );
	printf("*(ptr - 1): %d \n", *(ptr-1) );
	
	printf("\nptr-- \n\n");
	
	ptr--;
	printf("&ptr: %p \n", &(ptr) );
	printf("*ptr: %d \n", *ptr );
	printf("&ptr[0]: %p \n", &ptr[0] );
	printf("ptr[0]: %d \n", ptr[0] );
   return 0;
}

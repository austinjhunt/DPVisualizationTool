#include <stdio.h>
#include <stdio.h>
#include <stdlib.h>        
#include <sys/time.h>      
#include <pthread.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

#define DEBUG 0
#define TRUE 1

/**************************************************

Main Function:
	int main( int argc, char** argv )

------------------------------------------------
In this function perform the following steps:
------------------------------------------------
1. Create the following variables:
	- main_thread (pthread_t)
	- status (join status value)
2. Create a main_thread 
	- If the return value != 0, then display an error message and 
	  immediately exit program with status value 1.
3. Join the main_thread
	- If the return value != 0, then display an error message and
	  immediately exit the program with status value 2.
4. Display join status value.
5. Exit program.

*/

int main( int argc, char** argv ) {
	
	pthread_t* main_thread;
	
	int status; 

	if( pthread_create(&main_thread, NULL,(void *)th_main, NULL) != 0)
	{
		printf("Error, cannot create main_thread!");
		exit(1);
	}
	
	if ((status = pthread_join(main_thread,NULL)) != 0)
	{
		printf("Error, cannot join main_thread!");
		exit(2);
	}
	
	printf("\nJoin status: %d\n",status);
	/*
	// ---------------------------------------
	// TODO: you add your implementation here
	*/
	
	printf("\nFINISHED!\n");
	return 0;

} // end main function

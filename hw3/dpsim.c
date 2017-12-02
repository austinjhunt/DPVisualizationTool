#include <stdio.h>
#include <stdlib.h>        
#include <sys/time.h>      
#include <pthread.h>
#include <time.h>
#include <unistd.h>
#include <string.h>

#define DEBUG 0
#define TRUE 1

static const unsigned int NUM_PHILOSOPHERS = 5;
static const unsigned int NUM_CHOPSTICKS = 5;

static int chopsticks[5];
static pthread_mutex_t mutex[5];
static pthread_t philosophers[5];


void* th_main( void* th_main_args ) {
	
	// ---------------------------------------
	// TODO: you add your implementation here
	//initialize all element values in chopsticks array to -1
	int i; 
	for (i = 0; i < NUM_CHOPSTICKS ; i ++) 
	{	chopsticks[i] = -1; } //end initialization
		
	printf("\nchopsticks initialized\n");

	//create a thread for each philosopher
	for (i = 0; i < NUM_PHILOSOPHERS ; i++) 
	{	
		if (pthread_create(&philosophers[i], NULL, th_phil, (void *) i) != 0)//if not success
		{ printf("\nError with pthread_create!"); pthread_exit(1);}
		//printf("\nth main i = %d",i);
	}
	
	printf("\nthread created for each philosopher!\n");

	//infinite loop
	
	int p0Eating, p1Eating,p2Eating,p3Eating,p4Eating;
	p0Eating = 0;
	p1Eating = 0; 
	p2Eating = 0;
	p3Eating = 0;
	p4Eating = 0;

	while (TRUE) 
	{
		//make a copy of chopsticks to use for iteration (because threads will be constantly changing original)
		int chopsticksCopy[5];
		memcpy(chopsticksCopy,chopsticks,NUM_CHOPSTICKS * sizeof(int));
		/*printf("Chopsticks array: ");
		for (int m = 0; m < NUM_CHOPSTICKS; m++)
		{
			printf(" %d ", chopsticksCopy[m]); 
		}
		
		printf("\n");*/

		if (chopsticksCopy[0] == 0 && chopsticksCopy[1] == 0) p0Eating = 1;
		else { p0Eating = 0;}

		if (chopsticksCopy[1] == 1 && chopsticksCopy[2] == 1) p1Eating = 1;
		else { p1Eating = 0;}

		if (chopsticksCopy[2] == 2 && chopsticksCopy[3] == 2) p2Eating = 1;
		else { p2Eating = 0;}

		if (chopsticksCopy[3] == 3 && chopsticksCopy[4] == 3) p3Eating = 1;
		else { p3Eating = 0;}

		if (chopsticksCopy[4] == 4 && chopsticksCopy[0] == 4) p4Eating = 1;
		else { p4Eating = 0;}
		

		//which philosophers are eating? whichever ones are holding one of the chopsticks? 
	
		
		printf("\nPhilosopher(s) ");
		if (p0Eating) printf("%d,",0);
		if (p1Eating) printf("%d,",1);
		if (p2Eating) printf("%d,",2);
		if (p3Eating) printf("%d,",3);
		if (p4Eating) printf("%d,",4);
		printf(" are eating.\n");
		
		if (chopsticksCopy[0]==0 && chopsticksCopy[1]==1 && chopsticksCopy[2]==2 && chopsticksCopy[3]==3 && chopsticksCopy[4]==4 )
		{	//deadlock 
			printf("\nDeadlock condition (0,1,2,3,4) ... terminating");
			break;//from loop
		}
		delay(1000);
	
	}

	
	

	for (i = 0; i < NUM_PHILOSOPHERS ; i++) 
	{	
		if (pthread_kill(philosophers[i], 0) != 0)//if not success
		{ 
			printf("\nError with pthread_kill! No signal sent"); exit(1);
		}
	}	
		

		
	
	pthread_exit(0);
	
	
	

} // end th_main function


void* th_phil( void* th_phil_args ) {

	// ---------------------------------------
	// TODO: you add your implementation here
	
	long phil_id = (long) th_phil_args; 
	
	while(1)
	{
		delay(2000);//philosopher thinks
		eat((int)phil_id); //philosopher eats
	}
		
	

} // end th_phil function


void delay( long nanosec ) {

	struct timespec t_spec;

	t_spec.tv_sec = 0;
	t_spec.tv_nsec = nanosec;

	nanosleep( &t_spec, NULL );

} // end think function


void eat( int phil_id ) {
	
	
	// ---------------------------------------
	// TODO: you add your implementation here
	

	//lock first, then pick up right chopstick
	pthread_mutex_lock(&mutex[phil_id]);
	chopsticks[phil_id] = phil_id; 


	//printf("\nPhil%d got the right one!\n",phil_id);
	//delay(1);
		
	//if(chopsticks[(phil_id+1)%NUM_CHOPSTICKS] == -1)

	//lock first, pick up left
	pthread_mutex_lock(&mutex[(phil_id+1)%NUM_CHOPSTICKS]);
	chopsticks[(phil_id+1)%NUM_CHOPSTICKS] = phil_id;
		
	
	//eating 
	//printf("\nphilosopher %d is eating!\n",phil_id);
	delay(10000) ;
	

	//set down left
	chopsticks[(phil_id+1)%NUM_CHOPSTICKS] = -1; 
	pthread_mutex_unlock(&mutex[(phil_id+1)%NUM_CHOPSTICKS]);
	//wait
	//delay(1000);		
	//set down right
	chopsticks[phil_id] = -1; 
	pthread_mutex_unlock(&mutex[phil_id]);
	
	

	
	//printf("\nPhil%d finished eating!\n", phil_id);
	

} // end eat function

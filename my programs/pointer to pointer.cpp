#include<stdio.h>
int  main()
{
	int var;
	int *ptr;
	int **ptr1;
	int ***ptr2;
	var=3000;
	ptr=&var; 
	ptr1=&ptr;
	ptr2=&ptr1;
	printf("\"hello\"");
	printf("\"valur of var=%d\"\n",var);
	printf("vale avaiolble at *ptr =%d\n",*ptr);
	printf("value avialble at **ptr1=%d\n",**ptr1);
	printf("address of ptr=%d",ptr1);
	
	printf("address of ptr=%d",&ptr);
	
}

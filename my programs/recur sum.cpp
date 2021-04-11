#include<stdio.h>
main()
{

int n=50,i;
 void display(int);
 display(n);}
 
 void display(int num)
 {
 	if (num>=1)
 	{
 		printf("%d ",num);
 		display(num-1);
	 }
 }
 


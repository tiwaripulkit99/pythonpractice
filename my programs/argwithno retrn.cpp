#include<stdio.h>
main()
{
 void sum(float,float);
 float x,y;
 printf("enter 2 number to add");
 scanf("%f%f",&x,&y);
 	sum(x,y);
}
void sum(float a,float b)
{ 
 printf("%f",a+b);
	
}

#include<stdio.h>
main()
{ void even();
void odd();
even();	
odd();
}
even()
{ int i;
printf("the even numbers between  1 to 50 are ");
	for(i=2;i<=50;i+=2)
{
		printf("%d ",i);}
		printf("\n");	
}
odd()
{ int i;
printf("the odd numbers between  1 to 50 are ");
	for(i=1;i<=50;i+=2)
{
		printf("%d ",i);}	
}


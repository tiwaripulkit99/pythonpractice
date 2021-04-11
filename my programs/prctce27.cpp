#include<stdio.h>
main()
{ int n;
	int factorial(int);
	printf("enter a number");
	scanf("%d",&n);
	factorial(n);
printf("factorial of %d is =%d",n,factorial(n));}
int factorial(int n1)
{
	if (n1==0)
	return 1;
	else
	return n1*factorial(n1-1);
	
}

#include<stdio.h>
main()
{
	int fib(int);
	int n,i;
	printf("enter the number");
	scanf("%d",&n);
	for(i=1;i<=100;i++)
	printf("%d  ",fib(i));
	
}
fib( int n)
{
if (n==1||n==2)
return 1;
else 
return fib(n-1)+fib(n-2);
}


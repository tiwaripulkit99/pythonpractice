#include<stdio.h>
main()
{
	int fact(int);
	int n;
	printf("enter a number for fact:");
	scanf("%d",&n);
	printf("%d",fact(n));
	
}
fact(int n)
{
	if (n>0)
	return (n*fact(n-1));
	else
	return 1;
}

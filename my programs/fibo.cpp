#include<stdio.h>
main()
{
	static int n;
	int i;
	printf("ENTER THE NO");
	scanf("%d",&n);
	for(i=(n-1);i>=10;i++)
	{
	
	n=(n-1) +(n-2);
	printf("%d",n);
}}

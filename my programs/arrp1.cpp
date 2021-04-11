#include<stdio.h>
main()
{
	int A[10],i,sum=0;
	printf("enter 10 numbers:");
	for(i=0;i<=9;i++)
	 scanf("%d",&A[i]);
	for(i=0;i<=9;i++)
	{
	sum=sum+A[i];}
	printf("%d",sum);
	
}

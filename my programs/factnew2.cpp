#include<stdio.h>
main()
{
    int n,i;
	 
	printf("ENTER THE NO");
	scanf("%d",&n);
	for(i=(n-1);i>=1;i--)
	{
	
	n=n*i;}
	printf("%d",n);
}


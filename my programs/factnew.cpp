#include<stdio.h>
main()
{
	int i,n,fact=1;
	printf("no.");
	scanf("%d",&n);
	for(i=n;i>=1;i--)
	fact=fact*i;
	printf("%d",fact);
}

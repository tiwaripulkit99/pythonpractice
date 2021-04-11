#include<stdio.h>
main()
{
	int a[5];
	int i;
	for(i=0;i<=4;i++)
{
		printf("enter the number");
    	scanf("%d",&a[i]);}
    
		for(i=0;i<=4;i++)
		{
			printf("[%d]=%d ",i,a[i]);
			
		} printf("\n");
		
		for(i=4;i>=0;i--)
		{
			printf("[%d]=%d ",i,a[i]);
			
		}
}

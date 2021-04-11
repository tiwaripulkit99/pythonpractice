#include<stdio.h>
main()
{
	int i,j;
	for(i=1;i<=3;i++)
	{
	
	for(j=1;j<=5;j++)
	{
	if(i==2)
	{
	
		if(j==2||j==3||j==4)
		{
		
				printf(" ");
			continue;}
		}
		
		printf("*");
	}
	printf("\n");
}
}


#include<stdio.h>
#include<conio.h>
main()
{
	int i,j;
	for(i=1;i<=3;i++)
	{
		for (j=1;j<=5;j++)
		{
			if (j>=4-i&& j<=i+2)
				printf("*");
			 else
			printf(" ");
			
			
		}printf("\n");
	
		
	}
}

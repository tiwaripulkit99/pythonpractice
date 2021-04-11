#include<stdio.h>
main ()
{
	int tdarr[3][3]={{1,2,3},{4,5,6},{7,8,9}};
	int i,j,r=3,c=3;
	printf("\ntdarray[i][j]=element\n");
	for(i=0;i<r;i++)
	{
		for(j=0;j<c;j++)
		{
			printf("[%d][%d]=%d ",i,j,tdarr[i][j]);
			
		}
		printf("\n");
	}
	
	
	
	}

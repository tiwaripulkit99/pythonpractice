#include<stdio.h>
main()
{
	int arr[3][3],i,j,sum;
	for(i=0;i<=2;i++)
		for(j=0;j<=2;j++)
		scanf("%d",&arr[i][j]);
	
	for(i=0;i<=2;i++)
		for(j=0;j<=2;j++)
		if(i+j==2)
		{
			sum=sum+arr[i][j]; 
		}
		printf("%d",sum);
	
}

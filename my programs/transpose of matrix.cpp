#include<stdio.h>
main()
{
	int arr[3][3],i,j;
	for(i=0;i<=2;i++)
	 {
	 for(j=0;j<=2;j++)
	 scanf("%d",&arr[i][j]);
	 }

		for(i=0;i<=2;i++)
{
	 	 for(j=0;j<=2;j++)
	 printf("%d",arr[i][j]);
	 	printf("\n");
	 }
	 printf("\t");
	 printf("transpose of matrix is =\n\t");
		for(i=0;i<=2;i++)
{
	 	 for(j=0;j<=2;j++)
{
		 printf("%d",arr[j][i]);}
	 
	 	printf("\t\n\t");
}
}

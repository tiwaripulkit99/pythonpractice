#include<stdio.h>
main()
{
	int arr[2][2]={{1,2},{3,4}};
	void fun(int[2][2]);
	fun(arr);	
}
void fun(int c[2][2])
{
	int i,j;
	for(i=0;i<=1;i++)
	{
		for(j=0;j<=1;j++){
		
		printf("%d ",c[i][j]);
	} 
	printf("\n");}
}


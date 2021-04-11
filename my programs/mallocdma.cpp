#include<stdio.h>
#include<stdlib.h>
main()
{
	int *ptr;
	int n;
	printf("enter the size of array you want to create\n");
	scanf("%d",&n);
	ptr=(int*) malloc(3*sizeof(int));
	for(int i=0;i<4;i++)
	{
		printf("enter the value no of %d of this array\n",i);
		scanf("%d",&ptr[i]);}
	
		for(int i=0;i<n;i++)
	{
		printf(" the value no of %d of this array is %d\n",i,ptr[i]);
		
	
	
	}
}

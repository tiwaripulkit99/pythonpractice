#include<stdio.h>
#include<stdlib.h>
main()
{
	int *ptr;
	int n;
	printf("enter the size of arrayb you want to create\n");
	scanf("%d",&n);
	ptr=(int*) malloc(10* sizeof(int));	
	for(int i=0;i<n;i++)
	{
		printf("enter the value no of %d of this array\n",i);
		scanf("%d",&ptr[i]);
	}
		for(int i=0;i<n;i++)
	{
		printf(" the value no of %d of this array is %d\n",i,ptr[i]);
		
	
	
	}
}

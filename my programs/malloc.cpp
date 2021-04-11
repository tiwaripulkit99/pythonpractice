#include<stdio.h>
#include<stdlib.h>
#include<cstdlib>
main()
{ system("color 7c");
	int n,i,*ptr,sum=0;
	printf("enter number of element:");
	scanf("%d",&n);
	ptr=(int*)malloc(n*sizeof(int));
	if(ptr==NULL)
	{
		printf("sorry!unable to allocate memory");
		exit(0);
	}
	printf("enter the element of array:");
	for(i=0;i<n;i++)
{
	scanf("%d",ptr+i);
	sum+=*(ptr+i);
}
printf("sum=%d",sum);
free(ptr);
}

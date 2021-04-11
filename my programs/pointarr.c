//pointer array
#include<stdio.h>
main()
{
	int arr[3]={10,200,3000 };
	int *ptr[3];
	int i;
	for(i=0;i<=2;i++)
	{
		ptr[i]=&arr[i];
		
	}
		for(i=0;i<=2;i++)
	printf("%d  ",*ptr[i]);
	
}

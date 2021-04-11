#include<stdio.h>
main()
{
	union number
	{
		int n1;
		float n2;
		
	};
	union number x;

	printf("enter value of n1:");
	scanf("%d",&x.n1);
		printf("\nvalue of n1=%d\n",x.n1);
	printf("\nenter value of n2:");
	scanf("%d",&x.n2);

	printf("\nvalue of n2=%f\n",x.n2);
		printf("\nvalue of n1=%d\n",x.n1);
	
}


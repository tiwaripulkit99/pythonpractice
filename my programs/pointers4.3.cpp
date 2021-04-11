#include<stdio.h>
main()
{
	int *ptr1,n=5;
	int *nptr=NULL;
	
	printf("nptr=%d\n",nptr);
	
	printf("%d\n",ptr1);
		ptr1=&n;
			printf("%d\n",ptr1);
			ptr1=ptr1+1;
		printf("%d\n",ptr1);
	
}


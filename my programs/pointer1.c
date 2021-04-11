#include<stdio.h>
main()
{
	int a =5;
	int *p;
	p=&a;
	printf("%d\n",a);
	printf("%u\n",&a);
	printf("%u\n",p);
	printf("%d\n",&p);
	}

#include<stdio.h>
main()
{    char pt;
   pt='hhsxk';
	float fvar=4.8;
	float *ptr;
	float **ptr1;
	
	ptr=&fvar;
	ptr1=&ptr;
	printf("%f\n",*ptr);
		printf("%u\n",*ptr1);
		printf("%u\n",&ptr1);
		printf("%u\n",&fvar);
		printf("%c",pt);    
}

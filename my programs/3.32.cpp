#include<stdio.h>
main()
{
	int a,b,*p1,*p2;
	printf("enter any 2 numbr");
	p1=&a;
	p2=&b;
	scanf("%d%d",p1,p2);
	if(*p1>*p2)
	{
		printf("a is greater ");
		
	}else 
	printf("b is greater");
}

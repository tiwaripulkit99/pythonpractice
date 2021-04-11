#include<stdio.h>
main()
{ int add();


 printf("%d",add());
}
int add()
{int a,b,c;
	printf("ENTER TWO NUMBERS");
	scanf("%d%d",&a,&b);
c=a+b;
return c;
}

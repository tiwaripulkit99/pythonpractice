#include<stdio.h>
main()
{
	int *p1,*p2,a,b;
	int add(int*,int*);
	printf( "enter 2 numbers to add\n");
	p1=&a;
	p2=&b;
	scanf("%d%d",&a,&b);
	printf("%d",add(&a,&b));

} 
int add(int*n1,int*n2)
{ int c;

c=*n1+*n2;
}

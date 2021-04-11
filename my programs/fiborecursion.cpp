#include<stdio.h>
main()
{
	int fibo(int);
	int n,s;
	printf("enter number upto u want ");
	scanf("%d",&n);
 s=	fibo(n);
	printf("%d",s);

	
}
fibo(int n1)
{ 
int a=0,b=1,c,i;
if(i==0)
return 0;
else
for (i=1;i<=n1;i++)
return (fibo (a+b));
b=a;


	
}

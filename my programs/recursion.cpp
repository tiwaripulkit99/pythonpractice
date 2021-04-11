#include<stdio.h>
main()
{ int x;
int fun1(int);
x=fun1(3);
printf("%d",x);
}
fun1(int a)
{

int s;
if(a==1)
return a;
s=a+fun1(a-1);
return s;
}

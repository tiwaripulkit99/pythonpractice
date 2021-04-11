#include<stdio.h>
main()
{ int fun(int,float);
 int (*pfn)(int,float);
 pfn=&fun;
 printf("address of function=%d\n",pfn);
 printf("result=%d\n",fun(3,3.14));
 printf("result=%d",pfn(3,3.14));
}
int fun(int a,float b)
{

return a*b;}

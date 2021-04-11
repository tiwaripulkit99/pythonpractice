#include <stdio.h>
main()
{ int a,b;
 int sum(int,int);
 printf("enter 2 number");
 scanf("%d%d",&a,&b);
 printf("%d%d",sum(a,b));
}
int sum(int x ,int y)
{
return  x+y;
}

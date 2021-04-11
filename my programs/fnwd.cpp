#include"stdio.h"
main()
{  int sum(int *,int *);
int (*ptr)(int *,int *);
int a,b;
ptr=&sum;
printf("enter 2 number");
scanf("%d%d",&a,&b);
printf("%d",ptr(&a,&b));

}
 int sum(int *x,int *y)
 {
 	return *x+*y;
 }


#include<stdio.h>
main()
{int n,x,b=1;
printf("enter numbr");
scanf("%d",&n);
x=n;
 while(n>=1)
 {
 	b=n*b;
 	n--;}
 	printf("%d",b);
 
}

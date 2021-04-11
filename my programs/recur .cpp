#include<stdio.h>
main()
{ int n,r;
int sum(int);
printf("sum of first 10 natural number is\n");
r=sum(n);
printf("%d",r);
}

int sum(int n1)
{


 if (n1<=10){
	
	n1=n1+sum(n1+1);
	return n1;
	}
	else
     return 0 ;
}


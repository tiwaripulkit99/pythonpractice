#include<stdio.h>
main()
{ int x,n;
  void expo(int,int);
	printf("enter number");
	scanf("%d",&x);
	printf("enter exponent value");
	scanf("%d",&n);
	expo(x,n);
	}
	
	expo(int x1,int n1)
	{ int pow=1,i;
	for(i=1;i<=n1;i++)
	pow=pow*x1;
	printf("%d^%d=%d",x1,n1,pow);
	}
	
	

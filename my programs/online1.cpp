#include<stdio.h>
main()
{
	int num1,num2;
	void swap(int,int);
	printf("enter 2 numbers");
	scanf("%d%d",&num1,&num2);
	printf("num1=%d\nnum2=%d",num1,num2);
	swap(num1,num2);
	
}
void swap(int n1,int n2)
{int temp;
temp=n1;
n1=n2;
n2=temp;
printf("num1=%d\nnum2=%d",n1,n2);
}

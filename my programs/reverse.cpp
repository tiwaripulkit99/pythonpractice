#include<stdio.h>
main()
{int n,rev=0,r;
printf("enter the number");
scanf("%d",&n);
while(n>0){

r=n%10;
rev=rev*10+r;


n=n/10;

}printf("reverse number is %d",rev);}

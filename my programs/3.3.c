#include<stdio.h>
main()
{
int m=29,*ab;

printf("address of m=%d\n",&m);
printf("value of m=%d\n",m);
ab=&m;
printf("now ab is assinged with address of m \n");
printf("address of pointer ab=%d\n",&ab);
printf("content of pointer ab is %d\n",*ab);
m=34;
printf("value of m assigned to 34 now\n");
printf("address of pointer ab=%d\n",&ab);
printf("content of pointer ab=%d\n",*ab);
*ab=7;
printf("pointer variable ab is assigned with value 7 now\n");
printf("address of m=%d\n",&m);
printf("value of m=%d\n",m);





}


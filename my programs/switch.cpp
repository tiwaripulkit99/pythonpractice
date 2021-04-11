#include<stdio.h>
main()
{ int a,b,ch;
printf("enter the value of a and b:\n");
scanf("%d%d",&a,&b);
printf("menu\n");
printf("1.add\n");
printf("2.subtract\n");
printf("3.division\n");
printf("4.mutliplication\n");
printf("enter your choice:");
scanf("%d",&ch);
switch(ch)
{case 1:
	printf("addtion is %d",a+b);
	break;
	 case 2:
	printf("subratction is %d",a-b);
	break; 
	 case 3:
	printf("division is %d",a/b);
	break;
	 case 4:
	printf("multiplicaion is %d",a*b);
	break; 
	default:
		printf("value is unaccesible");
	}}




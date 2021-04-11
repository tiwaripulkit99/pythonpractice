#include<stdio.h>
main()
{
	float salary;
	int en;
	void data(int,float);
	printf("enter the employe numbr");
	scanf("%d",&en);
	printf("enter the salary");
	scanf("%f",&salary);
	

	data(en,salary);
}
void data(int empn,float sal)
{ int incent;
if( sal>=30000)
 {
 incent=1000;}
 else if(sal>=20000 && sal<30000)
 {
 incent=500;}
 else if(sal<=10000)
{
  incent=300;}
else

 {
 printf("invalid incentive");}
 printf("\n\n");
 printf("\nempno\temp salary\tincentives\n");
 printf("\n%0.2d\t%0.2f\t%0.2d");
}


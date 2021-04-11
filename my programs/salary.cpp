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
{
if( sal>=30000)
 {
 printf("1000\t");}
 else if(sal>=20000 && sal<30000)
 {
 printf("500\t");}
 else if(sal<=10000)
{
  printf("300\t");}
else

 {
 printf("invalid incentive");}}


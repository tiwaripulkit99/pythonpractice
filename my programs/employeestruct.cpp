#include<stdio.h>
struct employee 
{
	int eno;
	char name[20];
	float salary;
};
main()
{
	struct employee e[5];
	int i;
	printf("enter the information");
	for(i=0;i<=4;i++)
	{
	
	printf("\nEmployee Id:");
	scanf("%d",&e[i].eno);
	printf("\nEmployee Name :");
	scanf("%s",&e[i].name);
	printf("\nSalary :");
	scanf("%f",&e[i].salary);
	}
	
	printf("Employee Information:\n");
	printf("EmpNo\tNAme\tSalary\n");
	printf("-----------------------------------\n");
	for(i=0;i<=4;i++)
	{
		printf("%d\t%s\t%0.2f\n",e[i].eno,e[i].name,e[i].salary);
	}
}

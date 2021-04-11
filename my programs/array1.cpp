#include<stdio.h>
main()
{
	int marks[5];
	int i;
	for(i=0;i<=4;i++)
{
		printf("address of marks [%d]=%u\n",i,&marks[i]);}
	

 for(i=0;i<=4;i++)
{
	printf("\nenter marks");
	scanf("%d",&marks[i]);
	
}
for(i=0;i<=4;i++)
{
	printf("\nvalues of marks[%d]=%d",i,marks[i]);
}
}

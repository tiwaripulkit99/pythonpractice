//program to print multiplicaton table
/*#include<stdio.h>
main()
{ int x,i,z;
printf("enter the number for which u want table");
scanf("%d",&x);
for (i=1;i<=10;i++){

z=x*i;
printf("%d\n",z);}
}*/

//program to print factorial of given number
#include<stdio.h>
main()
{
	int f,n,i=1;
	
	printf("enter the numbr for which u want factorial");
	scanf("%d",&n);

    while(i<n){
	
	
   f=f*i;
   
   	i++;
}printf("%d",f);}


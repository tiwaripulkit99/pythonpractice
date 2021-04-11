#include<stdio.h>
main()
{
int arr[3][3],i,j,sum;

printf("enter number");
for(i=0;i<=2;i++)
  
 for(j=0;j<=2;j++)
 {
 scanf("%d",&arr[i][j]);}
 printf("\n");
 for(i=0;i<=2;i++)

 {
 for(j=0;j<=2;j++)
 {
 printf("%d  ",arr[i][j]);
 sum=sum+arr[i][j];
   }
   printf("=%d ",sum);
   printf("\n");
   sum=0;
   


 }

 printf("\n");
  for(i=0;i<=2;i++)
 {
 sum=sum+arr[i][i];}
 printf("sum of main diagnol is =%d",sum);
 }

 


 
	

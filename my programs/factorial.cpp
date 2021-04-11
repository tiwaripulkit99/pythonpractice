#include<stdio.h>
main()

   {int f=1,n,x;
     
      printf("enter the number");
      scanf("%d",&n);
      x=n;
      while(n>=1){
	  
	  f=f*n;
      n--;}
      printf("factorial of %d is %d",x,f);
  } 
      

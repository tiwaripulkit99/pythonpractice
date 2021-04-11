#include<stdio.h>
main() 
{	int fact(int);
	int i,z,n;

	printf("entr number");
	scanf("%d",&n);
	z=fact(n);
	printf("%d",z);
			}
				
	fact(int x)
	
	{ int facto=1,i;
     for(i=1;i<=x;i++)
	 {    
      facto=facto*i;    
  }    return facto;}
  
  

#include<stdio.h>
main()
{int r,ch;
printf("enter the radius of cicirle");
scanf("%d",r);
printf("\nmenu");
printf("1 for area");
printf("2 for perimeter");
scanf("%d",ch);
switch(ch)
{ case 1:
	{printf("area of circle is %d",3.14*r*r);
	}
case 2:
     {printf("perimter of circle is %d",2*3.14*r);
	 }
		 }	
}

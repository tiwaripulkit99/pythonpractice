#include<stdio.h>
main(){
	int sq(int);
	int cube(int);
	int s,z,i;
	for (i=1;i<=10;i++)
{
		
	s=sq(i);
	printf("sqaure of given numbr is %d\n",s);}
	for (i=1;i<=10;i++)
	
	{
	z=cube(i);
	
	
	printf("cube of given numbr is %d\n",z);}

}

sq(int a)
{ int c;
c=a*a;
return c;
}
cube(int b)
{
int d;
d=b*b*b;
return d;}


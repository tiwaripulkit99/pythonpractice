#include<stdio.h>
main()
{ 
void sq(int);
void cube(int);
int a,i;

for (i=1;i<=10;i++)
sq(i);
for (i=1;i<=10;i++)
cube(i);


	
}
sq(int num)
{ int s;
s=num*num;
printf("the square of %d is %d\t\n",num,s);


}


cube(int num)
{
	int c;
	c=num*num*num;
	printf("the cube of the %d is %d\n",num,c);

}

#include<stdio.h>
  main()
{ 
  int add(int,int),a,b,s;
 printf("enter 2 numbrs");
 scanf("%d%d",&a,&b);
  s=add(a,b);
  printf("%d",s);
}
 int add(int x,int y)
{ int c;


	c=x+y;
	return(c);
}

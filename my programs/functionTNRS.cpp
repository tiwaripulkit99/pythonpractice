#include<stdio.h>
  main()
{ 
  int add(),s;
 printf("enter 2 numbrs");
  s=add();
  printf("%d",s);
}
add()
{ int a,b,c;

	printf("enter two numbers");
	scanf("%d%d",&a,&b);
	c=a+b;
	return(c);
}

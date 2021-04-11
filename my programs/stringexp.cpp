#include<stdio.h>
main()
{
	char s[3][10],i;
	printf("enter three name");
	for(i=0;i<=2;i++)
gets(&s[i][0]);
	for(i=0;i<=2;i++)
	printf("%s",s[i]);
	
}

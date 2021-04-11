#include<stdio.h>
#include<string.h>
main()
{
	char s1[10],s2[10];
	int r;
	printf("enter the string:");
	gets(s1);
	printf("enter the string:");
	gets(s2);
	r=strcmp(s1,s2);
	printf("r=%d",r);
	if(r==0)
	{
		printf("two string are equal");
		
	}
	else
	printf("two string are not equal");

}

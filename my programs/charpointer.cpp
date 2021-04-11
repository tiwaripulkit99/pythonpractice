#include<stdio.h>
main()
{
char *p,*pc,c1='a';
pc=&c1;
p="hello!how are you?";
while(*p!='\0')
{
	if(*p==' ')
	{
		printf("\n");
		p++;
		continue;
	}
	printf("%c",*p);
	p++; 
}
}

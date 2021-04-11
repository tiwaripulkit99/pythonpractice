#include<stdio.h>
main()
{
	int name[30],ch;
	int i=0;
	printf("enter full name:");
	while(ch!='\n')

{
	ch=getchar();
	printf("%c",ch);
	name[i]=ch;
	i++;
	
}
name[i]='\0';
printf("\name:%s,name");
}

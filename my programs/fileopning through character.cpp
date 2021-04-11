#include<stdio.h>
main()
{
FILE *fptr;
char ch;
fptr=fopen("a.txt","r");
if(fptr==NULL)
{
	printf("file doesn't Exists:");
}
else
{
	printf("file is opened for reading:\n");
	while(ch!=EOF)
{
		ch=fgetc(fptr);
	printf("%c",ch);
}
	
}fclose(fptr);
}

#include<stdio.h>
main()
{
	FILE *fptr;
	char ch;
	long ptrpos;


	fptr=fopen("a.txt","r");
	if(fptr==NULL)
	{
		printf("File opening error\n");
		
	}
	fseek(fptr,15l,SEEK_SET);
	while((ch=fgetc(fptr))!=EOF)
	{
		printf("%c",ch);
	}
}

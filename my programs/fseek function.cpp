#include<stdio.h>
main()
{
	FILE *fptr;
	long ptrpos;
	char filename[20];
	printf("Enter Filename to be opened\n");
	scanf("%s",filename);
	fptr=fopen(filename,"r");
	if(fptr==NULL)
	{
		printf("File opening error\n");
		
	}
	fseek(fptr,10l,SEEK_SET);
	ptrpos=ftell(fptr);
	printf("file pointer is pointing at %ldth  byte in the file\n",ptrpos);
	fseek(fptr,-5l,SEEK_CUR);
	ptrpos=ftell(fptr);
	printf("file pointer is pointing at %ldth byte in the file\n",ptrpos);
}

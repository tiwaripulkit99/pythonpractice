#include<stdio.h>
#include<string.h>
 int main()
 {
 	FILE *fptr;
 	int i;
 	char s[100]="hello students kese ho";
 	fptr=fopen("a.txt","w");
 	if(fptr==NULL)
 	{
 		printf("file not opened");
 		return(1);
 	
	 }
	 for(i=0;i<strlen(s);i++)
	
	 	fputc(s[i],fptr);
	 	fclose(fptr);
	 
 }

#include<stdio.h>
#include<string.h>
main()
{
	char str[20],str1[10]="tiwari";
	int length;
		printf("\nenter the string:");
		gets(str);
	  
		printf("\nlength of string:%d",strlen(str));
		printf("\n%s",strcpy(str1,str));
}

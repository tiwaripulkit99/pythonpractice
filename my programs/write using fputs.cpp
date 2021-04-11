#include<stdio.h>
main()/*
{
	FILE *fp;
	
	fp=fopen("hi.txt","w");
	fputs("hello beta",fp);
}//and if we want to take input from user than*/
 {
	FILE *fp;
	char str[10];
	
	
	fp=fopen("hi.txt","w");
	printf("enter the string which u want to write::");
	gets(str);
	fputs(str,fp);}

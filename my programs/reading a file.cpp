#include<stdio.h>
main()
{
	char str[10];
	FILE *fp;
	fp=fopen("a.txt","r");
	if(fp==NULL){
		printf("file not found");
		return(1);
	}
	while(fgets(str,9,fp)!=NULL){
		printf("%s",str);
	}fclose(fp);
}

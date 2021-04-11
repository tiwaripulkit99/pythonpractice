#include<stdio.h>

struct book
{
	char name[20];
	int pages;
	char author[20];

}bookdata;
main()
{ struct book *ptr,bd2;

  ptr=&bookdata;
	printf("enter book name:");
	scanf("%s",ptr->name);
	printf("enter Pages:");
	scanf("%d",& ptr->pages);
	printf("enter author name:")
	scanf("%s",ptr->author); 


printf("-----------Book information-------------\n");
printf("Book name\tbookpages\tBookauthor\n");
printf("%s\t\t%d\t\t %s",ptr->name,ptr->pages,ptr->author);
printf("\n");


  ptr=&bd2;
	printf("enter book name:");
	scanf("%s",ptr->name);
	printf("enter Pages:");
	scanf("%d",& ptr->pages);
	printf("enter author name:");
	scanf("%s",ptr->author); 


printf("-----------Book information-------------\n");
printf("Book name\tbookpages\tBookauthor\n");
printf("%s\t\t%d\t\t %s",ptr->name,ptr->pages,ptr->author);
}

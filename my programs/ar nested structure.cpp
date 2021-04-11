#include<stdio.h>
struct book
{
	char bname[20];
	char author[20];
	int pages;
	struct date{
		int day;
		int month;
		int year;
		 
	}pdate;

};
main()
{
	struct book b={"c++","balguruswamy",234,{12,3,1992}};
	struct book *ptr;
	struct book b1[2];
	int i;
	ptr=&b;
	printf("\n%s %s %d %d %d %d",b.bname,b.author,b.pages,b.pdate.day,b.pdate.month,b.pdate.year);
	printf("\n%s %s  %d %d %d %d",ptr->bname,ptr->author,ptr->pages,ptr->pdate.day,ptr->pdate.month,ptr->pdate.year);
	printf("enter the book info:\n");
	for(i=0;i<=1;i++)
	{
		printf("\n Book name:");
		scanf("%s",&b1[i].bname);
		
		printf("\n Book author:");
		scanf("%s",&b1[i].author);
		
		printf("\n Book pages:");
		scanf("%d",&b1[i].pages);
		printf("\nPublication date[dd mm yy]:");
		scanf("%d %d %d",&b1[i].pdate.day,&b1[i].pdate.month,&b1[i].pdate.year);
	
	
}
printf("Book info:");
for(i=0;i<=1;i++)
{
printf("name=%s\n",b1[i].bname);
printf("author=%s\n",b1[i].author);
printf("pages=%d\n",b1[i].pages);
printf("date:%d- %d -%d\n",b1[i].pdate.day,b1[i].pdate.month,b1[i].pdate.year);}
}

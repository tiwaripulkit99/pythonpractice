#include<stdio.h>

struct book{
	char bname[20];
	int pages;
	
};
void display(struct book*);
main()
{
	struct book b={"c",500},b1={"C++",600
	};
	display(&b);
	display(&b1);
	
	
}
void display(struct book *ptr)
{
	printf("\nBook name:%s",ptr->bname);
	printf("\nBook pages:%d\n",ptr->pages);
}

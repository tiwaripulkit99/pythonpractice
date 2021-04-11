#include<stdio.h>
	struct supermarket
	{
	char name[20];
	float price;
	int quantity;
	}e[2];
main()
{  
int i;

	for(i=0;i<=1;i++)
{
		
	printf("\nenter the item name:");
	scanf("%s",&e[i].name);
	printf("\nenter the item price:");
	scanf("%f",&e[i].price);
	printf("\nenter the item quantity:");
	scanf("%d",&e[i].quantity);}
	printf("Supermarket Information:\n");
	printf("itemname\tprice\tquantity\n");
	printf("-----------------------------------------\n");
	
for(i=0;i<=1;i++)
{
 printf("%s\t b\t%f\t\t%d\n",e[i].name,e[i].price,e[i].quantity);	
}
} 

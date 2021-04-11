#include<stdio.h>
main()
{
	int arr[3]={1,2,3};
	void fun(int);
	int i;
	for(i=0;i<=2;i++)
	{ fun (arr[i]);
		
	}
} 
void fun(int element)
{
	printf("%d",element);
}

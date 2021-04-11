#include<stdio.h>
main()
{
	int n=3;
	void fun(int);
	printf("n=%d\n",n);
	fun(n);
	printf("\nin main after calling recursive calls completion");
}
void fun(int n1)
{
	printf("at teh beginning of the function n1=%d\n",n1);
	if(n1==0)
	return;
	else
	{
		printf("in else before function calling n1:=%d\n",n1);
		fun(n1-1);
		printf("in the else after function calling:n1=%d\n",n1);
		
		
		
		
		
	}
	
}

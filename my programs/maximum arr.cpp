#include<stdio.h>
main()
{
	int arr[]={ 23,45,78,56,100,134};
	int i,max=arr[0],temp;
	for(i=0;i<=5;i++)
	{
		if(arr[i]<max)
		{
			max=arr[i];
		}
	}printf(" maximum=%d",max);
}

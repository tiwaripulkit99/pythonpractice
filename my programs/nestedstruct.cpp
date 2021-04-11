#include<stdio.h>
struct country{
	char name[20];
	char weather[20];
	int year;
	struct date{
		int dat;
		int month;
		int year;
	}d;
	
}cn;
main()
	{
	
	printf("\ncountry name:");
	scanf("%s",&cn.name);
	printf("\nweather :");
	scanf("%s",&cn.weather);
	printf("\nyear :");
	scanf("%d",&cn.year);
	printf("\nenter date month and year");
	scanf("%d%d%d",&cn.d.dat,&cn.d.month,&cn.d.year);
	
	
		
	printf("Country Information:\n");
	printf("name\tWeather\t\t\tyear\n");
	printf("-----------------------------------\n");
	
		printf("%s\t%s\t%d\n",cn.name,cn.weather,cn.year);
			printf("date is: %d-%d-%d",cn.d.dat,cn.d.month,cn.d.year); 
	}



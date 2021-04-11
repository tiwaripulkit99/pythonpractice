#include<stdio.h>
#include<conio.h>
main(int argc,char *argv[])
{
	int i;
	if(argc>=2)
	{
		printf("the argument supplied:\n");
		for(i=1;i<argc;i++)
		{
			printf("%s",argv[i]);
			
				}
			}
				else
				{
					printf("argument list is empty\n");
				}
			}

#include<stdio.h>
main()
{int i,j,k,n;
n=2;
for(i=1;i<=3;i++,n--)
{ for(k=1;k<=n;k++){
	printf(" ");
}
for(j=1;j<=i;j++)

{

printf("* ");
}
printf("\n");
}
}

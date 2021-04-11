#include<stdio.h>
main()
{
      int sec,hh,mm,ss;
printf("input second :");
scanf("%d",&sec);
mm=sec/60;
ss=sec%60;
hh=mm/60;
mm=mm%60;
printf(" HH=%02d:MM=%02d:SS=%02d",hh,mm,ss);
}

  #include <stdio.h>

 
int main()
{   int add(int *, int *);
   int first, second, sum;
 
   printf("Input two integers to add\n");
   scanf("%d%d", &first, &second);
 
   sum = add(&first, &second);
 
   printf("(%d) + (%d) = (%d)\n", first, second, sum);
 
   return 0;
}

int add(int *x, int *y) {
   int sum;
   
   sum = *x + *y;
   
   return sum;
}

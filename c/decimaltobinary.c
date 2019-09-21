#include<stdio.h>    
int main(){  
int a[10],n,i=0;    
printf("Enter the number to convert: ");    
scanf("%d",&n);    
while(n>0)    
{    
    a[i]=n%2;    
    n=n/2;    
    i++;
}
    printf("\nBinary of Given Number is=");  
    i=i-1;  
while(i>=0)    
{   printf("%d",a[i]);    
    i--;
}    
printf("\n");

return 0;  
}  

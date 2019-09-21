#include<stdio.h>
int main(){
    int count=0;
    char a[100],b[100];
    printf("Enter String to reverse: ");
    gets(a);
    
    while(a[count] != '\0')
        count++;
    
    for(int i=0;i<count;i++)
        b[i] = a[count - 1 - i];
    
    // strrev(a);
    puts(b);
    return 0;
}
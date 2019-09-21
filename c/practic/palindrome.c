#include<stdio.h>
int main(){
    int n,temp,check,rev=0;
    
    // printf("%d",temp);
    printf("Enter no\n");
    scanf("%d",&n);
    temp = n;
    while(n>0){
        check = n%10;
        rev=(rev*10)+check;
        n = n/10;
    }
    if(rev == temp){
        printf("%d is palindrome\n",rev);
    }else{
        printf("Not Palindrome %d %d\n",temp,rev);
    }
    return 0;
}
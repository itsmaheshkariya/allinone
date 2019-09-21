#include<stdio.h>

long recursive(int n){
    
    if(n == 0){
        return 1;
    }else{
        return n * recursive(n - 1);
    }

}
int main(){
    int n,fact;
    printf("Enter no\n");
    scanf("%d",&n);
    fact = recursive(n);
    printf("Recursive of %d id %d\n",n,fact);
    return 0; 
}

//palindrome
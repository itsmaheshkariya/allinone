#include<stdio.h>
int main(){
    int n = 0,f1=0,f2=1,f3=0;
    printf("Enter no: ");
    scanf("%d",&n);
    printf("%3d%3d",f1,f2);
    for(int i=2;i<n;i++){
        f3 = f1+f2;
        f1 = f2;
        f2 = f3;
        printf("%3d",f3);
    }
    printf("\n");
    return 0;
}
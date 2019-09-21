#include<iostream>
using namespace std;
void swap(int* a, int* b) //pass bye reference
{
 int z = *a;
 *a = *b;
 *b = z;
}
int main(){
    int a= 90;
    int b= 80;
    cout<<"before swap"<<a<<b;
    swap(&a,&b); //call bye reference
    cout<<"after swap"<<a<<b;

    return 0;
}





#include<stdio.h>
int main(){
    char c , isLowerVowel, isUpperVowel;
    printf("Enter Char to check vowel or not: ");
    scanf("%c",&c);
    isLowerVowel = (c == 'a'||c == 'e'|| c == 'i'||c == 'o'|| c == 'u');
    isUpperVowel = (c == 'A'||c == 'E'|| c == 'I'||c == 'O'|| c == 'U');
    if(isLowerVowel || isUpperVowel){
        printf("%c is vowel\n",c);
    }else{
        printf("%c is not vowel\n",c);
    }
    

} 
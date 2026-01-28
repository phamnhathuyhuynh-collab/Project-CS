#include <stdio.h>
#include <string.h>

int main(){
    char s[] = " huy"; 
    for(unsigned int i =0; i < strlen(s); i++){
        printf("%c", s[i]);
    }
    return 0;
}
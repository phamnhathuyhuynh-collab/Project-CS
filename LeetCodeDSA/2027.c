#include <stdio.h>
#include <string.h>

int main(){
    char* s = "XXX"; 
    int lenght = strlen(s); 
    int count = 0; 
    int i = 0; 
    while(i < lenght){
        if(s[i] == 'X'){
            count += 1; 
            i += 3; 
        }else{
            i += 1;
        }
    }
    printf("%d", count); 
    return 0;
}
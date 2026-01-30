#include <stdio.h>
#include <malloc.h>
#include <math.h>
#include <string.h>
#include <stdbool.h>

void swap(char *a, char *b){
    char temp = *a; 
    *a = *b; 
    *b = temp;
}

void reverseChar(char *s, int start, int end){
    while(start < end){
        swap(&(s[start]), &(s[end]));
        start++; 
        end--;
    }
}

bool isVowel(char *a){
    if( *a == 'a' || *a == 'u' || *a == 'o' || *a == 'e' || *a == 'i') return true;
    return false;
}

int main(){
    char s[] = "ae aei aeiou eio uoia";
    unsigned length = strlen(s);
    printf("%s", s);
    int chuanDem =0; 
    unsigned dem = 0; 

    for(unsigned int i =0; i < length; i++){
        if(isVowel(&(s[i]))){
            chuanDem++;
        }
        if(s[i] != ' '){
            dem++; 
        }else{ 
            break; 
        }
    }

    // printf("\n%d %d", dem, chuanDem); 


    while(s[dem] != '\0'){
        int nb =0; 
        unsigned int i = dem +1;
        while(1){
            if(s[i] != ' ' && i < length){
                if(isVowel(&(s[i]))){
                    // printf("\n%c", s[i]);
                    nb++;
                }
            }else{
                break;
            }
            i++;
        }   
        // printf("\n%c", s[i - 1]);
        if(nb == chuanDem){
            reverseChar(s, dem + 1, i - 1);
        }

        printf("\n%d", nb);
        dem = i;
    }

    printf("\n%s", s);
    return 0;
}
#include <stdio.h>
#include <string.h>
#include <ctype.h>

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

// void *strstrip(char *s, size_t size){
//     char *end; 

//     end = s + size - 1; 
//     while(end >= s && isspace((unsigned char)*end)) end--;
//     *(end + 1) = '\0';
//     while(*s && isspace((unsigned char)*s)) s++;
    
// }

int main(){
    char s[] = "  hello world  ";

    size_t size = strlen(s); 

    unsigned int start = 0; 
    for(unsigned int  i =0 ; i < size; i++){
        if(isspace((unsigned char)s[i])){
            start++; 
        }else{
            break;
        }
    }

    int i =0; 
    int dem = 0; 
    printf("\n%s", s);
    if(start == size){
        s[0] = '\0';
    }
    while(start < size){
        if(!isspace((unsigned char)s[start])){
            swap(&(s[i]), &(s[start]));
            i++;
            dem = 0; 
            if(start == size -1){
                i++;
            }
        }else{
            dem++;
            if(dem == 1){
                i++;
            }
        }
        start++; 
    }
    s[i - 1] = '\0'; 
    
    unsigned a = 0; 
    unsigned b = i - 2; 

    while(a < b){
        swap(&(s[a]), &(s[b])); 
        a++; 
        b--;
    }


    int startReverse = 0; 
    int finReverse = 0;
    while(s[finReverse] != '\0'){
        if(s[finReverse] != ' '){
            finReverse++;
        }else{
            int temp = finReverse;
            reverseChar(s, startReverse, temp -1);
            finReverse++; 
            startReverse = finReverse;
        }
    }
    reverseChar(s, startReverse, finReverse -1);
    printf("\n%s", s);
    printf("1");

    return 0;
}
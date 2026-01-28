#include <stdio.h>
#include <string.h>
char findDifference(char* s, char* t){
    int results = 0; 
    int resultt = 0;
    for(int i =0; i< strlen(s) ; i++ ){
        results += s[i];
    }
    for(int i =0; i < strlen(t) ; i++){
        resultt += t[i];
    }
    if(results > resultt){
        return (char)(results - resultt);
    }else{
        return (char)(resultt - results);

    }
}

int main(){
    char* t = "huynh";
    char* s = "huyn";
    printf("%c", findDifference(s, t));
    
    return 0;
}
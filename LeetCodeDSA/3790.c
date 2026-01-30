#include <stdio.h>

int main(){
    int k = 99901; 
    int i =1; 
    int num = 1; 
    if(k %2 ==0 || k % 5 == 0){
        printf("-1");
        return 1;
    }
    if(k == 1){
        printf("-1");
        return 1;
    }
    while(1){
        i++;
        num = num*10 +1;
        if(num % k == 0){
            printf("%d", i);
            break;
        }
    }
    return 0;
}
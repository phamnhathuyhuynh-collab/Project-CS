#include <stdio.h>
#include <stdlib.h>
int hamingWeight(int n){
    int count = 0; 
    while(n > 0){
        if(n&1){
            count++;
        }
        n >>= 1;
    }
    return count;
}

int main(){
    printf("%d", hamingWeight(5));
}
#include <stdio.h>
#include <math.h>

int main(){
    int n; 
    printf("Nhap so n: ");
    scanf("%d", &n); 

    int result = 0;

    int i = 1;
    for(;; i++){
        if(n - (pow(10, i)) <= 0){ 
            break;
        }
    }
    printf("%d\n", i);
    while(n > 0){
        result += (n%10*(pow(10, i -1))); 
        i--; 
        n/=10;
    }
    printf("%d", result);
    return 0;
}
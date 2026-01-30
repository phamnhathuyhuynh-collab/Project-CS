#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>


bool isPrime(int n){
    if(n == 2) return false; 
    for(int i = 3 ; i*i <= (n); i+= 2){
        if(n % i == 0){
            return false;
        }
    }
    return true;
}

int main(){
    int n; 
    printf("Nhap so n: "); 
    scanf("%d", &n); 

    int ans = 2, m =3, sum = 2; 
    while(sum + m <= n){
        if(isPrime(m)){
            sum += m; 
            if(isPrime(sum)) ans = sum;
        }
        m += 2;
    }

    printf("%d", ans);
}
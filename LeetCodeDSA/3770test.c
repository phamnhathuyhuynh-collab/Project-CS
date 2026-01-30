#include <stdio.h> 
#include <malloc.h> 

int isPrime(int n){
    if(n <= 1){
        return 0;
    }
    for(int i =2; i < n; i++){
        if(n % i == 0){
            return 0;
        }
    }
    return 1;
}

int main(){
    // int k; 
    // printf("Nhap so k: "); 
    // scanf("%d", &k); 
    if(isPrime(2)){
        printf("Yes"); 
    }else{
        printf("No");
    }

    // int somme = 0;
    // for(int i =0, j =0; i < 750;j++){
    //     if(isPrime(j)){
    //         i++;
    //         if(i >= 746 && i <= 750){
    //             somme += j;
    //         }
    //         printf("%d ", j);
    //     }
    // }
    // printf("\n%d", somme);
    return 0;
}
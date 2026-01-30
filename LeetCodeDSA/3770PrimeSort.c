#include <stdio.h> 
// #include <stdlib.h>
#include <malloc.h>
#include <math.h>

int isPrime(int n){
    if(n <= 1){
        return 0;
    }
    for(int i =2; i <= sqrt(n); i++){
        if(n % i == 0){
            return 0;
        }
    }
    return 1;
}

int isSomme(int tableau[], int n, int k){
    if(n == 2){
        return 1;
    }
    int somme = 0;

    for(int i = 0; i < k -1 ; i++){
            somme += tableau[i];
            if(somme == n){
                printf("\n%d %d", somme, i);
                printf("\n%d", tableau[i]);
                return 1;
            }    
    }  
    return 0;
}

void sieveAlgo(int tableau[], int n){
    tableau[0] = tableau[1] = 0;
    int p = 2; 

    while(p*p <= n){
        if(tableau[p]){
            for(int i = p*p ; i <= n; i+= p){
                tableau[i] = 0;
            }
        }
        p++;
    }
    
    for(int i = 2 ;i <= n; i++){
        if(tableau[i]){
            tableau[i]= i;
        }
    }
}


int main(){
    int k;
    
    printf("Nhap so k de kiem tra: "); 
    scanf("%d", &k);
    
    int* tableau = malloc((k+1)*sizeof(int));
    for(int i =0 ; i <= k; i++){
        tableau[i] = 1;
    }
    if(k == 2){
        printf("2");
        return 1;
    }
    sieveAlgo(tableau, k);
    printf("\n");
    for(int i =0; i <= k; i++){
        printf("%d ", tableau[i]);
    }
    // tableau[0] = tableau[1] = 0;
    
// Cach nay duoc nhung voi case nho 

    // int interieurK; 
    // for(int i = k; i >= 0 ; i--){
    //     if(isPrime(i)){
    //         interieurK = i;
    //         if(isSomme(tableau, interieurK, k)){
    //             printf("\n%d", interieurK);
    //             return 1;
    //         }
    //     }
    // }

// Thu nghiem cach moi de han che time limit

  

    int somme = 0;
    int max = 0;
    int i =0;
    while(somme <= k && i < k){
        // printf("\n%d", somme);
        if(tableau[i] != 0){
            somme += tableau[i];
            if(tableau[somme] && somme <= k){
                max = somme;
                // printf("\n\n%d", max);
            }
        }
        i++;
    }  
    
    printf("\n%d" , max);
    

    // printf("%d", isPrime(49));
    // if(isSomme(tableau, 2)){
    //     printf("Yeah!!");
    // }else{
    //     printf("No!!");
    // }
    free(tableau); 
    return 0;
}
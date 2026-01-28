#include <stdio.h>
#include <stdlib.h>
int* countBits(int n){
    int* arr_bits = (int*)malloc((n+1)*sizeof(int));
    arr_bits[0] = 0;
    for(int i =0; i< n; i++){
        if(i != 0){
            if(i&(i-1) == 0){
                arr_bits[i] = 1;
            }else{
                arr_bits[i] = arr_bits[i&(i-1)] + 1;
            }
        }
    }
    return arr_bits;
}
int* countBitsAdvances(int n){
    int* arr_bits = (int*)malloc((n+1)*sizeof(int));
    arr_bits[0] = 0;
    for(int i =0; i<= n; i++){
        arr_bits[i] = arr_bits[i >> 1] + (i&1);
    }
    return arr_bits;
}

int main(){
    int n = 20; 
    int* arr = countBits(20);
    for(int i =0; i<= n; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
    free(arr);
    return 0;
}
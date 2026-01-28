#include <stdio.h>

int missingNumber(int n, int arr[n]){
    int missing = n; 
    for(int i =0; i< n; i++){
        missing ^= i ^ arr[i];
    }
    return missing;
}

int main(){
    int n = 6;
    int arr[] = {0,1,2,3,5, 6};
    printf("%d", missingNumber(n, arr));
}
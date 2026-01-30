#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


int intComparator ( const void * first, const void * second ) {
    int firstInt = * (const int *) first;
    int secondInt = * (const int *) second;
    return secondInt - firstInt;
}


int main(){
    int reward1[] = {1,4,4,6,4}; 
    int reward1Size = 5;
    int reward2[] = {6,3,5,6,1}; 
    int reward2Size = 5;
    int k = 1;

    if(k == reward1Size){
        int total = 0; 
        for(int i = 0 ; i < reward1Size; i++){
            total += reward1[i];
        }
        printf("%d", total); 
        return 1;
    }
    int total = 0;
    for(int i =0;i < reward1Size; i++){
        total += reward2[i];
    }
    int gain[reward1Size];
    for(int i =0 ; i < reward1Size; i++){
        gain[i] = reward1[i] - reward2[i]; 
    }
    for(int i =0 ;i < reward1Size;i++){
        printf("%d ", gain[i]);
    }
    qsort(gain, reward1Size, sizeof(int),  intComparator);
    printf("\n");
    
    for(int i =0; i < k; i++){
        total += gain[i];
    }
    printf("%d", total);
    return 0;
}
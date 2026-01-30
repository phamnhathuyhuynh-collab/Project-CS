#include <stdio.h>
#include <malloc.h>

void setTable(int reservedTable[], int sourceTable[], int numsSize, int *count){

    for(int i =0; i < numsSize && reservedTable[sourceTable[i]] == 0; i++ ){
        reservedTable[sourceTable[i]]++;
        (*count)++;
    }
}

int countElement(int reservedTable[], int k, int *count){
    int totalCount = 0; 
    for(int i = 0; *count - k > 0 ; i++){
        if(reservedTable[i] != 0){
            (*count)--;
            totalCount += reservedTable[i];
        }
    }
    return totalCount; 
}

void swap(int *a, int *b){
    int temp = *a; 
    *a = *b; 
    *b = temp; 
}

int main(){
    int k;
    int numsSize; 
    int sourceTable[100000];
    int reservedTable[100000];
    int count = 0;
    printf("Nhap numsSize cua day: "); 
    scanf("%d", &numsSize); 
    printf("\nNhap gioi han cua day: "); 
    scanf("%d", &k); 
    printf("\nNhap so trong day: "); 
    for(int i =0; i < numsSize; i++){
        scanf("%d", &(sourceTable[i]));
    }
    for(int i =0; i < 100000; i++){
        reservedTable[i] = 0; 
    }
    // setTable(reservedTable, sourceTable, numsSize, &count); 
    // int result = countElement(reservedTable, k, &count); 
    


    for(int i =0 ; i < numsSize; i++){
        int indexMax = i;
        for(int j = i + 1; j < numsSize; j++){
            if(sourceTable[indexMax] < sourceTable[j]){
                indexMax = j;
            }    
        }
        swap(&sourceTable[indexMax], &sourceTable[i]);
    }
    int totalCount = 0; 
    if(numsSize == 1){
        if(k == 0){
            printf("1"); 
            return 1;
        }else{
            printf("0"); 
            return 1;
        }
    }
    for(int i =0; i < numsSize - 1; i++){
        if(sourceTable[i] != sourceTable[i+1] && k >= 1){
            if(i == numsSize - 2 && k == 0){
                totalCount++;
            }
            k--;
        }else{
            if(k == 0 ){
            totalCount++;

            }
            if(i == numsSize - 2 && k == 0){
                totalCount++;
            }
        }
    }
    for(int i =0 ; i < numsSize; i++){
        printf("%d", sourceTable[i]);
    }  
    printf("\n");
    printf("%d", totalCount);
    // printf("%d", count);
    return 0; 
}
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int cmp(const void* a, const void* b){
    return (*(int*)a - *(int*)b); 
}
int bisect_right(int *nums, int numsSize, int q){
    int left = 0 ; 
    int right = numsSize - 1; 
    int middle = 0;
    if(q >= nums[right]){
        return numsSize;
    }
    while(left < right){
        middle = (right + left) / 2;
        if(nums[middle] <= q){
            left = middle + 1; 
        }else{
            right = middle; 
        }
    }
    return left;
}
void answerQueries(int *acc, int* nums, int numsSize, int* queries, int queriesSize) {
    qsort(nums, numsSize, sizeof(int), cmp);
    for(int i = 1; i < numsSize; i++){
        nums[i] += nums[i - 1]; 
    }
    for(int i = 0; i < queriesSize; i++){
        acc[i] = bisect_right(nums, numsSize, queries[i]); 
    }
}

int main(){
    int numsSize = 4;
    int nums[] = {4,5,2,1};
    int queriesSize = 3; 
    int queries[] = {3,10,21};
    int *acc = malloc(queriesSize*sizeof(int)); 
    if(acc == NULL){
        return 0;
    }
    answerQueries(acc, nums, numsSize, queries, queriesSize); 
    for(int i = 0; i < numsSize; i++){
        printf("%d ", nums[i]); 
    }
    printf("\n");
    for(int i = 0; i < queriesSize;i++){
        printf("%d ",acc[i]);
    }
    return 0;
}
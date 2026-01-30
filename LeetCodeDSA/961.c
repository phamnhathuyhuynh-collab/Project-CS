#include <stdio.h>
#include <stdlib.h>
int comp(const void* a, const void* b){
    return (*(int*)a- *(int*)b);
}
int repeatedNTimes(int* nums, int numsSize) {
    int res = 0;
    qsort(nums, numsSize, sizeof(int), comp); 
    for(int i =0; i <numsSize -1; i++){
        if(nums[i] == nums[i+ 1]){
            res = nums[i];
            break;
        }
    }
    return res;
}
int main(){
    int nums[] = {2,1,2,5,3,2};
    printf("%d", repeatedNTimes(nums, 6));
    return 0;
}
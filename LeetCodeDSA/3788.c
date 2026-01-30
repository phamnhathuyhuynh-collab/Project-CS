#include <stdio.h>
#include <limits.h>

int main(){
    int numsSize = 5; 
    int nums[] = {10,-1,3,-4,-5};
    int sum_nums= 0;
    for(int i =0; i < numsSize; i++){
        sum_nums += nums[i];
    }

    int max_sum = INT_MIN;   
    int min_value = INT_MAX; 

    for(int i = numsSize - 2; i >= 0; i--){
        sum_nums -= nums[i + 1]; 
        if(nums[i + 1] < min_value){
            min_value = nums[i + 1]; 
        }
        if(sum_nums - min_value > max_sum){
            max_sum = sum_nums - min_value ;
        }
    }
    printf("%d", max_sum);
    return 0;
}
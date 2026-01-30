#include <stdio.h>
#include <math.h>
#include <stdlib.h>



void swap(int *a, int *b){
    int temp = *a;
    *a = *b; 
    *b = temp; 
}

void reverseArr(int arr[], int start, int end){
    while(start < end){
        swap(&(arr[start]), &(arr[end])); 
        start++; 
        end--; 
    }
}

int main(){
    int balanceSize = 3;
    int balance[] = {-6, 6, 5}; 

    int test = 0; 
    for(int i =0; i < balanceSize ; i++){
        test += balance[i]; 
    }
    
    if(test < 0){
        printf("-1"); 
        return 1;
    }

    int target = 0; 
    for(int i = 0; i < balanceSize; i++){
        if(balance[i] < 0){
            target = i; 
            break; 
        }
        if(i == balanceSize){
            printf("Minium step: 0"); 
        }
    }
    printf("%d\n", target);
    int sumLeft = 0;
    int countLeft = 0; 
    int sumRight = 0;
    int countRight = 0; 

    for(int i =0; i < balanceSize; i++){
        if(i < target){
            sumLeft += balance[i];
            countLeft++;
        }else if(i > target){
            sumRight += balance[i];
            countRight++;
        }
    }
    printf("%d\n", countLeft);
    printf("%d", countRight);

    int sumPositive = 0;
    for(int i = 0 ; i < balanceSize; i++){
        if(balance[i] > 0){
            sumPositive += balance[i];
        }
    }

    int vongXoay = 0; 
    // lệnh if đầu tiên với trường hợp bên trái của số âm không có só nào 
    if(countLeft == 0 && sumLeft == 0){
        if(balanceSize == 2){
            if(balance[target] + balance[target + 1] >= 0){
                printf("\n%d", abs(balance[target]));
                return 1;
            }
        }else{
            int temp = (balanceSize - 1) / 2;
            reverseArr(balance, 0, temp); 
            reverseArr(balance, temp + 1, balanceSize -1); 
            for(int i =0; i < balanceSize ; i++){
                printf("%d ", balance[i]); 
            }
        }
    }else if(countRight == 0 && sumRight == 0){
        if(balanceSize == 2){
            if(balance[target] + balance[target - 1] >= 0){
                printf("\n%d ", abs(balance[target])); 
                return 1;
            }
        }else{
            int temp = (balanceSize - 1) / 2; 
            reverseArr(balance, 0, temp - 1); 
            reverseArr(balance, temp, balanceSize -1); 
            for(int i =0; i < balanceSize ; i++){
                printf("%d ", balance[i]); 
            }
        }
    }else{
        for(int i = 0; i < target; i++){
            if(sumLeft - balance[i] > sumRight){
                sumLeft -= balance[i];
                sumRight += balance[i];
                vongXoay++; 
            }
        }
        

        if(vongXoay != 0){
            reverseArr(balance, vongXoay, balanceSize - 1);
        }
        reverseArr(balance, 0, balanceSize -1);
        printf("\n");
        for(int i =0; i < balanceSize ; i++){
                printf("%d ", balance[i]); 
            }
    }

    for(int i = 0; i < balanceSize; i++){
        if(balance[i] < 0){
            target = i; 
            break; 
        }
        if(i == balanceSize - 1){
            return 0;
        }
    }


    int count = 0;
    int i = target + 1;
    int j = target -1;
    
        while(j >= 0 && i <= balanceSize - 1){
            if((i - target <= target - j && balance[i] >= 0) || balance[j] == 0){
                if(balance[i] == 0 && i < balanceSize -1){
                    i++;
                    continue;
                }
                (balance[i])--;
                (balance[target])++;
                count += (i - target);
                if(balance[i] == 0 && i < balanceSize -1){
                    i++;
                }
                if(balance[target] == 0){
                    goto jump_here;
                }
            }else{
                    if(balance[j] == 0 && j > 0){
                        j--;
                    }
                    (balance[j])--;
                    (balance[target])++;
                    count += (target - j);
                    
                    if(balance[target] == 0){
                        goto jump_here;
                    }
            }
            
        }
        
    
    jump_here:
    printf("\n");
    for(int i =0; i < balanceSize; i ++){
        
        printf("%d ", balance[i]); 
    }
    printf("\n%d", count);

    
    return 0;

}
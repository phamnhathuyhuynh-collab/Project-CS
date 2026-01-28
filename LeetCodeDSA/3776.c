#include <stdio.h>
typedef long long ll;


// dùng để đổi 2 số a, b
void swap(ll *a, ll *b){
    ll temp = *a;
    *a = *b; 
    *b = temp; 
}

// dùng để đổi 1 subarray trong 1 dãy 
void reverseArr(ll arr[], int start, int end){
    while(start < end){
        swap(&(arr[start]), &(arr[end])); 
        start++; 
        end--; 
    }
}

int main(){
    int balanceSize = 4;
    ll balance[] = {1,2,-5,2}; 

    // dùng để tính tổng dãy nếu < 0 thì trả về -1 còn không thì tiếp tục
    int test = 0; 
    for(int i =0; i < balanceSize ; i++){
        test += balance[i]; 
    }
    
    if(test < 0){
        printf("-1"); 
        return 1;
    }

    // kiểm tra xem giá trị âm nằm ở đâu, nếu có thì break, nếu không thì tức cả dãy dương và trả về 0
    int target = 0; 
    for(int i = 0; i < balanceSize; i++){
        if(balance[i] < 0){
            target = i; 
            break; 
        }
        if(i == balanceSize - 1 ){
            printf("Minium step: 0"); 
        }
    }
    printf("%d\n", target);

    // so sánh tổng phía trái và phía phải của giá trị âm
    int sumLeft = 0; 
    int sumRight = 0; 

    for(int i =0; i < balanceSize; i++){
        if(i < target){
            sumLeft += balance[i];
        }else if(i > target){
            sumRight += balance[i];
        }
    }

    // đang thắc mắc rằng phần này làm gì ???
    int sumPositive = 0;
    for(int i = 0 ; i < balanceSize; i++){
        if(balance[i] > 0){
            sumPositive += balance[i];
        }
    }

    // định nghĩa là vòng xoay, đoán xem nên chia đều hai bên như nào 
    int vongXoay = 0; 
    for(int i = 0; i < target; i++){
        if(sumLeft - balance[i] >= sumRight){
            sumLeft -= balance[i];
            sumRight += balance[i];
            vongXoay++; 
        }
    }
    if(vongXoay == 0){
        for(int i = balanceSize - 1; i > target; i--){
            if(sumRight - balance[i] >= sumLeft){
                sumLeft += balance[i];
                sumRight -= balance[i];
                vongXoay++; 
            }
        }
        
        reverseArr(balance, 0, vongXoay);
        goto rotate;
    }
    printf("%d\n",vongXoay);

    if(vongXoay != 0){
        reverseArr(balance, vongXoay, balanceSize - 1);
    }
    rotate:
    reverseArr(balance, 0, balanceSize -1);

    printf("%d\n%d\n", sumLeft, sumRight);
    for(int i = 0 ; i< balanceSize; i++){
        printf("%lld ", balance[i]);
    }
    for(int i = 0; i < balanceSize; i++){
        if(balance[i] < 0){
            target = i; 
            break; 
        }
        if(i == balanceSize - 1){
            printf("Minium step: 0"); 
        }
    }
    int count = 0;
    int i = target + 1;
    int j = target -1;
    
    while(i > balanceSize - 1 && j >= 0){
        (balance[j])--; 
                    printf("\n%lld ", balance[j]);  
                    (balance[target])++;
                    count +=( target - j);
                    // printf("%d", count);
                    if(balance[j] == 0 && j >= 0){
                        j--;
                    }
                    if(balance[target] == 0){
                        goto jump_here;
                    }  
    }

    while(j < 0 && i <= balanceSize - 1){
        (balance[i])--;
                // printf("\n%lld ", balance[i]);
                (balance[target])++;
                count += (i - target);
                // printf("%d", count);
                if(balance[i] == 0 && i < balanceSize -1){
                    i++;
                }
                if(balance[target] == 0){
                    goto jump_here;
                }
    }

        while(j >= 0 && i <= balanceSize - 1){
            // printf("%d %d\n", i, j); 
            if( i - target >= target - j){
                (balance[i])--;
                // printf("\n%lld ", balance[i]);
                (balance[target])++;
                count += (i - target);
                // printf("%d", count);
                if(balance[i] == 0 && i < balanceSize -1){
                    i++;
                }
                if(balance[target] == 0){
                    goto jump_here;
                }
            }else{
                    (balance[j])--; 
                    // printf("\n%lld ", balance[j]);  
                    (balance[target])++;
                    count +=( target - j);
                    // printf("%d", count);
                    if(balance[j] == 0 && j >= 0){
                        j--;
                    }
                    if(balance[target] == 0){
                        goto jump_here;
                    }       
            }
        }
    
    jump_here:
    printf("\n");
    for(int i = 0 ; i< balanceSize; i++){
        printf("%lld ", balance[i]);
    }
    printf("\n%d", count);
    return 0;

}
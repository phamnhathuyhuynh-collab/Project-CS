#include <stdio.h>

int maxProfit(int* prices, int pricesSize) {
    if(pricesSize == 1){
        return 0;
    }

    int total = 0; 
    int profit = 0; 
    int i = 0; 
    int j = 1; 
    while(i < pricesSize && j < pricesSize){
        while(j < pricesSize && prices[j] - prices[i] > profit){
            profit = prices[j] - prices[i]; 
            j++;
        }
        total += profit; 
        i = j; 
        j++; 
        profit = 0;
    }
    return total;
}
// huong di khac cua bai nay 
int maxProfit2(int* prices, int pricesSize){
    int total = 0; 
    for(int i = 1; i < pricesSize; i++){
        if(prices[i] > prices[i - 1]){ 
            total += prices[i] - prices[i - 1];
        }
    }
    return total;
}

int main(){
    int pricesSize = 6; 
    int prices[] = {3, 2, 6, 5, 0, 3};
    printf("%d", maxProfit(prices, pricesSize));
    return 0;
}
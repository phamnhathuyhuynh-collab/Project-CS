#include <stdio.h>
int min_value(int a, int b){
    if(a >= b){
        return b;
    }else{
        return a;
    }
}

int main(){
    int cost1 = 85, cost2 = 14, costBoth =31, need1 = 49, need2 = 0;
    int result = min_value(costBoth, cost1+ cost2)*min_value(need1, need2); 
    if(need1 > need2){
        result += min_value(costBoth, cost1)*(need1- need2);
    }else{
        result += min_value(costBoth, cost2)*(need2- need1);
    }
    printf("%d", result);
    return 0;
}
#include <stdio.h>
#include <stdbool.h>

bool lemonadeChange(int* bills, int billsSize){
    int fiveDollarBill = 0; 
    int tenDollarBill = 0; 
    
    for(int i = 0; i < billsSize; i++){
        if(bills[i] == 5){
            fiveDollarBill++; 
        }else{ 
            if(bills[i] == 10){
                if(fiveDollarBill - 1 < 0){
                    return false;
                }else{
                    fiveDollarBill--; 
                    tenDollarBill++;
                }
            }
            if(bills[i] == 20){ 
                if(fiveDollarBill > 0 && tenDollarBill > 0){
                    fiveDollarBill--; 
                    tenDollarBill--; 
                }else{
                    fiveDollarBill -= 3;
                    if(fiveDollarBill < 0){
                        return false;
                    }
                }
            }
        }
    }
    return true;
}

int main(){
    int billsSize = 5;
    int bills[] = {5,5,5,10,20}; 
    if(lemonadeChange(bills, billsSize)){
        printf("True");
    }else{
        printf("False");
    }
    return 0;
}
#include <stdio.h>

int min(int a, int b){
    if(a < b){
        return a;
    }else{
        return b;
    }
}


int main(){
    int heightSize = 9;
    int height[] = {1,8,6,2,5,4,8,3,7};
    int max = 0;
    int j = heightSize - 1;
    int i =0;
    while(i < j){
        if((j - i)*min(height[i], height[j]) > max){
            max =(j - i)*min(height[i], height[j]);
        }
        if(height[i] < height[j]){
            i++;
        }else{
            j--;
        }
    }
    
    printf("%d", max);
    return 0;
}
#include <stdio.h>
#include <stdlib.h> 




int main(){
    int arr[] = {2,2,3,4,5,3,4};
    int res = 0;
     
    for(int i =0; i< sizeof(arr)/4; i++){
        res ^= arr[i];
    }
    printf("%d", res);
    return 0;
}
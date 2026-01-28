#include <stdio.h>
#include <stdlib.h>


int cmp(const void *a, const void *b){
    return (*(int*)a - *(int*)b);
}

int findContentChildren(int* g, int gSize, int* s, int sSize) {
    qsort(g, gSize, sizeof(g[0]), cmp); 
    qsort(s, sSize, sizeof(s[0]), cmp); 

    int count = 0; 
    int i = 0; 
    int j = 0; 
    while(i < gSize && j < sSize){ 
        if(g[i] <= s[j]){
            count++; 
            i++; 
            j++;
        }else{
            j++;
        }
    }
    return count;
}

int main(){
    int gSize = 3;
    int g[] ={1, 2, 3};
    int sSize = 2; 
    int s[] = {1, 1};

    printf("%d", findContentChildren(g, gSize, s, sSize));
    return 0;
}
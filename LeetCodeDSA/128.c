#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define SIZE 1007

typedef struct node{
    int key; 
    struct node *next;
}Node; 

Node* table[SIZE]; 

int hash(int x){
    return (x%SIZE + SIZE)%SIZE; 
}

int contains(int x){
    int h = hash(x); 
    Node* cur = table[h]; 
    while(cur){
        if(cur->key == x) return 1; 
        cur = cur->next;
    }
    return 0; 
}

void add(int x){
    if(contains(x)) return; 
    int h = hash(x); 
    Node* node = malloc(sizeof(Node)); 
    node->key = x; 
    node->next = table[h]; 
    table[h] = node; 
}

void clear_table() {
    for (int i = 0; i < SIZE; i++) {
        Node *cur = table[i];
        while (cur) {
            Node *tmp = cur;
            cur = cur->next;
            free(tmp);
        }
        table[i] = NULL;
    }
}

int longestConsecutive(int* nums, int numsSize) {
    for(int i =0; i < numsSize; i++){
        add(nums[i]); 
    }
    int best = 0; 
    int i = 0; 
    while(i < numsSize){
        int count = 0; 
        if(!contains(nums[i] - 1)){
            int x = nums[i];
            while(contains(x)){
                count++; 
                x++; 
            }
        }
        if(count > best){
            best = count; 
        }
        i++;
    }
    return best;
}


int main(){
    int numsSize = 4;
    int nums[] = {1,0,1,2}; 
    printf("%d" , longestConsecutive(nums, numsSize)); 
    
    return 0; 
}
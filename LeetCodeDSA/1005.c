#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

typedef struct Heap
{
    int *array; 
    int size; 
    int capacity; 
} Heap;

Heap *createHeap(int capacity){
    Heap *heap = (Heap*)malloc(sizeof(Heap));
    heap->size = 0; 
    heap->capacity = capacity; 
    heap->array = (int *)malloc(sizeof(int)); 
    return heap;
}

void swap(int *a, int *b){
    int temp = *a; 
    *a = *b; 
    *b = temp;
}

// Function to heapify the node at index i
void heapify(Heap *heap, int i){
    int largest = i; 
    int left = 2*i + 1; 
    int right = 2*i + 2; 
    if(left < heap->size && heap->array[left] > heap->array[largest])
        largest = left;
    
    if(right < heap->size && heap->array[right] > heap->array[largest])
        largest = right;

    if(largest != i){
        swap(heap->array[left], heap->array[largest]); 
        heapify(heap, largest);
    }
}

void builHeap(Heap *heap){
    int n = heap->size; 
    for(int i = (n -1) /2; i>=0; i --)
        heapify(heap, i);
}

void insertHeap(Heap *heap, int value){
    if(heap->size == heap->capacity){
        return;
    }
    heap->size++; 
    int i = (heap->size - 1); 
    heap->array[i] = value;
    while(i> 0 && heap->array[(i-1)/2] < heap->array[i]){
        swap(&heap->array[i], &heap->array[(i- 1)/2]); 
        i = (i -1)/2;
    }
}

int extractHeap(Heap *heap){
    if(heap->size <= 0){
        return INT_MIN;
    }
    if(heap->size == 1){
        heap->size--; 
        return heap->array[0]; 
    }

    int root = heap->array[0]; 
    heap->array[0] = heap->array[heap->size -1]; 
    heap->size--;
    heapify(heap, 0); 
    return root;
}

int deleteKey(Heap *heap, int index){
    if(index >= heap->size){
        return;
    }
    if(index == heap->size - 1){
        heap->size--; 
        return;
    }
    heap->array[index] = heap->array[heap->size - 1]; 
    heapify(heap, index); 
}

int comp(const void *a, const void *b){
    return (*(int *)a - *(int *)b); 
}

int largestSumAfterKNegations(int* nums, int numsSize, int k) {
    qsort(nums, numsSize, sizeof(int), comp); 
    int i =0; 
    while(k > 0 && i < numsSize && nums[i] < 0){
        nums[i] = -nums[i];
        k--; 
        i++;
    }
    if(k % 2 != 0){
        qsort(nums, numsSize, sizeof(int), comp);
        nums[0] = -nums[0];
    }
    int total = 0; 
    for(int j = 0; j < numsSize; j++){
        total += nums[j];
    }
    return total;
}



int main(){
    int nums[] = {-2,5,0,2,-2};
    Heap *heap = createHeap(5); 
    
    return 0;
}
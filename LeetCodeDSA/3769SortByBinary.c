#include <stdio.h>
#include <malloc.h>
int reverseBit(int n){
    int result = 0; 
    while(n){
        result = (result << 1) | (n&1); 
        n >>= 1;
    }
    return result; 
}

// void sort(int tableau[], int start,int middle, int end){
//     int tableau1[middle - start  +1]; 
//     int tableau2[end - middle]; 
//     int tableauTemp[end - start + 1];

//     for(int i = 0; i < middle - start + 1 ; i++){
//         tableau1[i] = tableau[start + i]; 
//     }

//     for(int i =0; i < end - middle; i++){
//         tableau2[i] = tableau[middle + i + 1]; 
//     }

//     int i = 0, j = 0, t = 0; 
//     for(;i < middle - start + 1 && j < end - middle ; t++){
//         if(tableau1[i] < tableau2[j]){
//             tableauTemp[t] = tableau1[i]; 
//             i++;
//         }else{
//             tableauTemp[t] = tableau2[j]; 
//             j++;
//         }
//     }

//     while(i < middle - start  +1){
//         tableauTemp[t] = tableau1[i]; 
//         t++; 
//         i++;
//     }
    
//     while(j < end - middle){
//         tableauTemp[t] = tableau2[j]; 
//         t++; 
//         j++; 
//     }
//     int dem = start; 
//     for(int i =0; i < end - start + 1; i++){
//         tableau[dem] = tableauTemp[i];
//         dem++; 
//     }
// }

// void mergeSort(int tableau[], int start, int end){
//     if(start < end){
//         int middle = (end + start) / 2; 
//         mergeSort(tableau, start, middle); 
//         mergeSort(tableau, middle + 1, end);
//         sort(tableau, start, middle , end); 
//     }
// }

void sortBinary(int tableau[], int reserved[], int start,int middle, int end){
    int tableau1[middle - start  +1]; 
    int tableau2[end - middle]; 
    int reserved1[middle - start + 1]; 
    int reserved2[end - middle];
    int tableauTemp[end - start + 1];
    int reservedTemp[end - start  +1];

    for(int i = 0; i < middle - start + 1 ; i++){
        tableau1[i] = tableau[start + i]; 
        reserved1[i] = reserved[start + i];
    }

    for(int i =0; i < end - middle; i++){
        tableau2[i] = tableau[middle + i + 1]; 
        reserved2[i] = reserved[middle + i + 1]; 
    }

    int i = 0, j = 0, t = 0; 
    for(;i < middle - start + 1 && j < end - middle ; t++){
        if(reserved1[i] < reserved2[j]){
            tableauTemp[t] = tableau1[i];
            reservedTemp[t] = reserved1[i];  
            i++;
        }else if(reserved1[i] == reserved2[j]){
            if(tableau1[i] < tableau2[j]){
                tableauTemp[t] = tableau1[i];
                reservedTemp[t] = reserved1[i];  
                i++;
            }else{
                tableauTemp[t] = tableau2[j];
                reservedTemp[t] = reserved2[j];  
                j++;
            }
        }else{
            tableauTemp[t] = tableau2[j]; 
            reservedTemp[t] = reserved2[j];
            j++;
        }
    }

    while(i < middle - start  +1){
        tableauTemp[t] = tableau1[i]; 
        reservedTemp[t] = reserved1[i];
        t++; 
        i++;
    }
    
    while(j < end - middle){
        tableauTemp[t] = tableau2[j]; 
        reservedTemp[t] = reserved2[j];

        t++; 
        j++; 
    }
    int dem = start; 
    for(int i =0; i < end - start + 1; i++){
        tableau[dem] = tableauTemp[i];
        reserved[dem] = reservedTemp[i];
        dem++; 
    }
}

void mergeSortBinary(int tableau[], int reserved[], int start, int end){
    if(start < end){
        int middle = (end + start) / 2; 
        mergeSortBinary(tableau, reserved, start, middle); 
        mergeSortBinary(tableau, reserved, middle + 1, end);
        sortBinary(tableau, reserved, start, middle , end); 
    }
}



int main(){
    int k;
    printf("Nhap so luong cua day tableau: "); 
    scanf("%d", &k); 
    int* tableau = (int*)malloc(k*sizeof(int)); 
    int* tableauCopy = (int*)malloc(k*sizeof(int)); 

    printf("Nhap cac phan tu cua day: "); 
    for(int i =0; i <k; i++){
        scanf("%d", &(tableau[i])); 
    }
    for(int i =0; i < k; i++){
        tableauCopy[i] = tableau[i];
    }
    // mergeSortBinary(tableau, tableauCopy, 0, k - 1);
    for(int i =0; i <k; i++){
        printf("%d ", (tableau[i])); 
    }
    int* reserved = (int*)malloc(k*sizeof(int));

    for(int i =0; i < k;i++){
        int a = tableau[i];
        reserved[i] = reverseBit(a); 
    }
    
    // mergeSort(reserved, 0, k - 1);
    // for(int i =1; i < k; i++){
    //     int temp = reverseBit(tableau[i]); 
        
    // }
    mergeSortBinary(tableau, reserved, 0, k -1);
    printf("\n");
    for(int i =0; i < k; i++){
        printf("%d ", reserved[i]); 
    }
    printf("\n");

    for(int i =0; i <k; i++){
        printf("%d ", (tableau[i])); 
    }

    free(tableau); 
    free(reserved);
    return 0;
}


// /**
// LEETCODE VERSION
//  * Note: The returned array must be malloced, assume caller calls free().
//  */
// void sortBinary(int tableau[], int reserved[], int start,int middle, int end){
//     int tableau1[middle - start  +1]; 
//     int tableau2[end - middle]; 
//     int reserved1[middle - start + 1]; 
//     int reserved2[end - middle];
//     int tableauTemp[end - start + 1];
//     int reservedTemp[end - start  +1];

//     for(int i = 0; i < middle - start + 1 ; i++){
//         tableau1[i] = tableau[start + i]; 
//         reserved1[i] = reserved[start + i];
//     }

//     for(int i =0; i < end - middle; i++){
//         tableau2[i] = tableau[middle + i + 1]; 
//         reserved2[i] = reserved[middle + i + 1]; 
//     }

//     int i = 0, j = 0, t = 0; 
//     for(;i < middle - start + 1 && j < end - middle ; t++){
//         if(reserved1[i] < reserved2[j]){
//             tableauTemp[t] = tableau1[i];
//             reservedTemp[t] = reserved1[i];  
//             i++;
//         }else if(reserved1[i] == reserved2[j]){
//             if(tableau1[i] < tableau2[j]){
//                 tableauTemp[t] = tableau1[i];
//                 reservedTemp[t] = reserved1[i];  
//                 i++;
//             }else{
//                 tableauTemp[t] = tableau2[j];
//                 reservedTemp[t] = reserved2[j];  
//                 j++;
//             }
//         }else{
//             tableauTemp[t] = tableau2[j]; 
//             reservedTemp[t] = reserved2[j];
//             j++;
//         }
//     }

//     while(i < middle - start  +1){
//         tableauTemp[t] = tableau1[i]; 
//         reservedTemp[t] = reserved1[i];
//         t++; 
//         i++;
//     }
    
//     while(j < end - middle){
//         tableauTemp[t] = tableau2[j]; 
//         reservedTemp[t] = reserved2[j];

//         t++; 
//         j++; 
//     }
//     int dem = start; 
//     for(int i =0; i < end - start + 1; i++){
//         tableau[dem] = tableauTemp[i];
//         reserved[dem] = reservedTemp[i];
//         dem++; 
//     }
// }

// void mergeSortBinary(int tableau[], int reserved[], int start, int end){
//     if(start < end){
//         int middle = (end + start) / 2; 
//         mergeSortBinary(tableau, reserved, start, middle); 
//         mergeSortBinary(tableau, reserved, middle + 1, end);
//         sortBinary(tableau, reserved, start, middle , end); 
//     }
// }

// int reverseBit(int n){
//     int result = 0; 
//     while(n){
//         result = (result << 1) | (n&1); 
//         n >>= 1;
//     }
//     return result; 
// }

// int* sortByReflection(int* nums, int numsSize, int* returnSize) {
//     int* reserved = (int*)malloc(numsSize*sizeof(int));

//     for(int i =0; i < numsSize;i++){
//         int a = nums[i];
//         reserved[i] = reverseBit(a); 
//     }
//     mergeSortBinary(nums, reserved, 0, numsSize -1);
//     *returnSize = numsSize; 
//     return nums;
// }
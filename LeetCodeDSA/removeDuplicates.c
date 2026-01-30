#include <stdio.h> 
#include <malloc.h>


typedef struct node *ref; 
struct node{
    int key; 
    ref next;
};

ref getNode(int k){
    ref p; 
    p = (ref)malloc(sizeof(struct node));
    if(p == NULL){
        printf("Khoi tao khong thanh cong!!");
    }
    p->key = k; 
    p->next = NULL;
    return p;
}

void addAfter(ref *head, int k){
    ref p, q; 
    p = getNode(k);
    if(*head == NULL){
        *head = p;
    }else{
        for(q = *head; q->next; q=q->next);
        q->next = p; 
        p->next = NULL;
    }
}

void printList(ref head){
    ref p; 
    for(p = head; p; p=p->next){
        printf("%d -->  ", p->key);
    }

}

int main(){
    ref head = NULL;
    int k;
    
    while(1){
        printf("Nhap so k de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &k);
        if(k == 0){
            break;
        }
        addAfter(&head, k);
    }
    ref dummyNode = malloc(sizeof(struct node)); 
    dummyNode->key = 0; 
    dummyNode->next = head; 
    ref prev = dummyNode; 
    ref current = head; 
    ref tempNext =head->next; 
    int count = 0;
    if(tempNext == NULL){
        printList(head);
        return 1;
    }
    while(tempNext){
        if(current->key != tempNext->key){
            if(count == 0){
                if(tempNext->next == NULL){
                    break;
                }
                tempNext = tempNext->next; 
                current = current->next; 
                prev = prev->next;
            }else{
                prev->next =NULL;
                prev->next = tempNext; 
                
                current = tempNext;
                if(current == NULL){
                    break;
                }
                tempNext = tempNext->next;
                count = 0;
            }
        }else{
            count++; 
            tempNext = tempNext->next;
            
        }
    }
    prev->next =NULL;
    prev->next = tempNext; 
                
    current = tempNext;
    printf("%d", prev->key);
    printf("\n");
    printList(dummyNode->next);
    return 0;
}
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

    ref dummyNode = (ref)malloc(sizeof(struct node)); 
    dummyNode->key = 0; 
    dummyNode->next = head; 

    ref evenNode = (ref)malloc(sizeof(struct node)); 
    evenNode->key = 0;  
    evenNode->next =NULL;
    ref headEven = evenNode;

    ref prev = dummyNode; 
    ref current = head;


    while(current){
        if(current->key % 2 == 0){
            while(current && current->key % 2 == 0){
                if(current->next){
                    prev->next = current->next; 
                    headEven->next = current; 
                    headEven=headEven->next;
                    current->next = NULL;
                    current = prev->next;
                }else{
                    prev->next = current->next; 
                    headEven->next = current; 
                    headEven=headEven->next; 
                    current = NULL;
                    break;
                }
            }
        }else{
            prev=prev->next;
            current =current->next;
        }
    }
    printList(evenNode->next);
    printf("\n");
    headEven->next = dummyNode->next;
    dummyNode->next = evenNode->next;
    printList(dummyNode->next);
    return 0; 
    


}
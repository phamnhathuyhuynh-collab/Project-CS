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
    while(head){
        if(head->next && head->key == head->next->key){
            while(head->next && head->key == head->next->key){
                head=head->next;
            }
            prev->next= head->next;
        }else{
            prev=prev->next;
        }
        head=head->next;
    }
    printList(dummyNode->next);
    return 0;
}
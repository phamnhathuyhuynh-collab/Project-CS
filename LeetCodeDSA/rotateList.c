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
    int h;
    int k;
    while(1){
        printf("Nhap so h de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &h);
        if(h == 0){
            break;
        }
        addAfter(&head, h);
    }
    printf("Nhap so k la so lan xoay: "); 
    scanf("%d", &k);

    ref tail; 
    int count = 1; 
    ref dummyNode = malloc(sizeof(struct node)); 
    dummyNode->key = 0; 
    dummyNode->next= head; 
    for(tail = head; tail->next; tail=tail->next){
        count++; 
    }
    

    if( k % count == 0){
        printList(head);
        return 1; 
    }else{
        ref prev = head;
        ref current = head;
        for(int i = count - (k % count) ; i > 1; i--){
            prev = prev->next;
            current = current->next;
        }
        current = current->next;

        dummyNode->next = current;
        tail->next = head;
        prev->next =NULL;
    }
    printf("%d", tail->key);
    printf("\n");
    printList(dummyNode->next);
    return 0;



}
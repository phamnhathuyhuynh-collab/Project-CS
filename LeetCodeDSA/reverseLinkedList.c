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
    int left, right;
    while(1){
        printf("Nhap so k de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &k);
        if(k == 0){
            break;
        }
        addAfter(&head, k);
    }
    printf("\n");
    printf("Nhap hai so dau va cuoi de dao: ");
    scanf("%d %d", &left, &right); 
    ref dummyNode; 
    dummyNode = malloc(sizeof(struct node));
    dummyNode->key = 0; 
    dummyNode->next = head; 

    ref leftPrev = dummyNode; 
    ref current = head; 
    for(int i = left -1; i > 0; i--){
        leftPrev= current; 
        current = current->next;
    }

    ref prev = NULL; 
    ref tempNext; 
    for(int i = right - left + 1; i > 0; i--){
        tempNext = current->next;
        current->next = prev; 
        prev = current ;
        current = tempNext;
    }

    leftPrev->next->next = current; 
    leftPrev->next = prev; 
    printList(dummyNode->next);
    printf("\n"); 
    printf("%d", current->key);
    return 0;
}



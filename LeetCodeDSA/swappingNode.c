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
    int k, i, count = 0; 
    while(1){
        printf("Nhap so k de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &k);
        if(k == 0){
            break;
        }
        addAfter(&head, k);
    }
    printf("Nhap vao so i: "); 
    scanf("%d", &i);
    ref tail; 
    ref p, q; 
    for(tail = head; tail; tail=tail->next){
        count++;
    }
    int n = count - i ; 
    for(p =head; n > 0; n--, p=p->next);
    for(q=head; i > 1; i--, q=q->next);
    int temp = p->key; 
    p->key = q->key; 
    q->key = temp; 
    printList(head);

}
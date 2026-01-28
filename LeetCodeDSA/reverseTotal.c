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
    ref p, q, tail;
    int k;
    int count = 1;
    while(1){
        printf("Nhap so k de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &k);
        if(k == 0){
            break;
        }
        addAfter(&head, k);
    }
    for(tail =head; tail->next; tail=tail->next){
        count++;
    }
    if(count == 1){
        printList(head);
        return 1;
    }
    p= head;
    if(count == 2){
        head = tail; 
        head->next = p;
        p->next = NULL;   
        printList(head);
        return 1;
    }
    q= head;
    q=q->next;
    head=head->next->next;
    p->next = q->next;
    q->next = p;
    
    while(1){
        p->next= head->next; 
        head->next = q;
        q=head;
        if(head == tail){
            break;
        }
        head = p->next;
    } 
    printf("%d\n", count);
    printList(head);
    return 0;

}
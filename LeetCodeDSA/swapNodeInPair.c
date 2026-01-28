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
    ref p, q , t;
    int k;
    while(1){
        printf("Nhap so k de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &k);
        if(k == 0){
            break;
        }
        addAfter(&head, k);
    }

    p = head; 
    q = head->next;

    p->next=q->next; 
    q->next = p;
    head = q;

    
    for(t =p, p = p->next;  p != NULL && p->next != NULL; ){
            q = p->next;

            if(q->next != NULL){
            
            p->next=q->next; 
            q->next = p;
            t->next = q;
            t = p; 
            p = p->next; 
        }else{
            
            t->next = q; 
            q->next = p; 
            p->next = NULL;
        }
            
        printf("%d -->  %d -->  %d -->  %d\n",t->key, p->key, q->key, t->next->key);
    }
    
    
    printf("%d -->  %d -->  %d -->  %d\n",t->key, p->key, q->key, t->next->key);
    
    printList(head);
    printf("\n"); 

    return 0;
}
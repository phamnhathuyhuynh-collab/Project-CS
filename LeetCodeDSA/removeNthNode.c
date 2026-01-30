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
    ref head = NULL, p, q; 
    ref tail; 

    int k, i, count = 0; 
    while(1){
        printf("Nhap so k de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &k);
        if(k == 0){
            break;
        }
        addAfter(&head, k);
    }
    printf("Nhap vao vi tri tu duoi ban muon xoa: "); 
    scanf("%d", &i);
    for(tail = head ; tail; tail=tail->next){
        count++;
    }
    int t = count - i;
    for(p = head, q = head ; t > 1;t--, p=p->next, q=q->next){
        printf("%d  %d -->  ", p->key, q->key);
    }
    if(count == i){
        
        head = head->next;
        free(q);

    }else{
        printf("\n");
        p=p->next; 
        printf("%d -->", p->key);
        printf("%d", q->key);
        q->next = p->next; 
    
        free(p);

    }
    
    printf("\n");
    
    printList(head);
    printf("\n");
    printf("%d", count);
    return 0; 
}
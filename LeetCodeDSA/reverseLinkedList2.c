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
    ref p, q , tenirLeftt, tenirRightt, tail;
    int k;
    ref debut, fin;
    int left, right;
    while(1){
        printf("Nhap so k de them vao day(nhap 0 de thoat): "); 
        scanf("%d", &k);
        if(k == 0){
            break;
        }
        addAfter(&head, k);
    }
    printf("Nhap hai vi tri left va right : ");
    scanf("%d %d", &left, &right);
    for(tail=head; tail->next; tail=tail->next);
    if(head->next == tail){
        p = head;
        head= tail; 
        head->next = p; 
        p->next = NULL;
        printList(head);
        return 1;
    }
    if(head == tail){
        printList(head); 
        return 1;
    }
    for(debut = head, tenirLeftt = head; left > 2; left-- ,tenirLeftt=tenirLeftt->next, debut=debut->next); 
    debut=debut->next;
    
    for(fin = head, tenirRightt = head; right > 1; right--, tenirRightt=tenirRightt->next, fin=fin->next); 
    tenirRightt=tenirRightt->next;
    if(left == right){
        printList(head);
        return 1;
    }
    p= debut;
    if((right - left) == 1){
        debut = fin; 
        debut->next = p;
        printList(head);
        return 1;
    }
    
    q= debut;
    q=q->next;
    debut=debut->next->next;
    p->next = q->next;
    q->next = p;
    
    while(1){
        p->next= debut->next; 
        debut->next = q;
        q=debut;
        if(debut == fin){
            break;
        }
        debut = p->next;
    } 
    
    printf("\n");

    printList(debut);
    printf("\n");
    tenirLeftt->next=debut; 
    
    
    printList(head);

}
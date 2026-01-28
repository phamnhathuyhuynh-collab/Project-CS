def merge(n, p, q, r): 
    arr1 = n[p: q + 1]
    arr2 = n[q + 1: r + 1]
    
    i = 0
    j = 0
    k = p
    while i < len(arr1) and j < len(arr2): 
        if arr1[i] <= arr2[j]:
            n[k] = arr1[i]
            i += 1
        else: 
            n[k] = arr2[j]
            j += 1
        k += 1
    while i < len(arr1):
        n[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        n[k] =  arr2[j]
        j += 1
        k += 1

    return n 

def merge_sort(n, p ,r):
    if p < r: 
        q = (r + p) // 2
        merge_sort(n, p, q)
        merge_sort(n, q + 1, r)
        merge(n, p, q, r)
    return n


        
def b_search(n, start, finish, y):
    middle = (start + finish) // 2
    if y == n[middle]:
        return middle
    else:
            if y < n[middle]:
                return b_search(n, start, middle -1, y)
            else:
                return b_search(n, middle + 1, finish, y)


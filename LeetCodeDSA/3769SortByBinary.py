def sort(tableau, start , middle , end):
    tableau1 = tableau[start: middle]
    tableau2 = tableau[middle: end]
    tableauTemp = tableau[start:end]

    
    
def mergeSort(tableau, start, end):
    if start < end: 
        middle = (start + end ) // 2
        mergeSort(tableau, start, middle)
        mergeSort(tableau, middle + 1, end) 
        sort(tableau, start, middle, end)
       


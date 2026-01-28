from collections import Counter
def minCostToMoveChips(position):
    cnt = Counter(position)
    minEven = float('inf')
    minOdd = float('inf')
    for i in cnt: 
        if i % 2 == 0 and i < minEven: 
            minEven = i 
        if i % 2 == 1 and i < minOdd: 
            minOdd = i 
    print(minEven, minOdd)
    totalEven = 0
    totalOdd = 0
    for i in cnt: 
        if i % 2 == 0: 
            totalEven += cnt[i]
        if i % 2 != 0: 
            totalOdd += cnt[i]
            
    return totalEven if totalEven < totalOdd else totalOdd
        

print(minCostToMoveChips(position = [1,1000000000]))

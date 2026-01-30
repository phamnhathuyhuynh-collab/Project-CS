def kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k):
    if numOnes >= k: 
        return k
    else: 
        if numOnes + numZeros >= k: 
            return numOnes
        else: 
            return numOnes + (k - numOnes - numZeros)*(-1)
print(kItemsWithMaximumSum(numOnes = 3, numZeros = 2, numNegOnes = 0, k = 4))
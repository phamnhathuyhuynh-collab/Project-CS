def maxMatrixSum(matrix):
    count = 0
    total = 0
    maxNev = float('-inf')
    minPos = float('inf')
    lenI = len(matrix)
    
    for i in range(lenI): 
        for j in range(lenI): 
            if matrix[i][j] < 0: 
                count += 1
                if matrix[i][j] > maxNev: 
                    maxNev = matrix[i][j]
            else: 
                if matrix[i][j] < minPos:
                    minPos = matrix[i][j]
            total += abs(matrix[i][j])
    if count % 2 != 0: 
        if minPos > abs(maxNev):
            total += 2*(maxNev)
        else: 
            total -= 2*(minPos)
    return total

def maxMatrixSumAdvance(matrix):
    count = 0
    total = 0
    min_abs = float('inf')
    for i in range(len(matrix)): 
        for j in range(len(matrix[0])): 
            if matrix[i][j] < 0: 
                count += 1
            total += abs(matrix[i][j])
            min_abs = min(abs(matrix[i][j]), min_abs)
    if count %2 != 0: 
        total -= 2*min_abs
    return total
print(maxMatrixSum(matrix = [[10,-6,-6,-8],[-3,-7,-8,-9],[-4,-8,-5,-8],[-9,-9,-6,-8]]))
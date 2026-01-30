from collections import Counter
def minimumAbsDifference(arr):
    arr.sort() 
    res = [] 
    m = float('inf')
    n = len(arr)
    L, R = 0, 1
    while R < n: 
        if arr[R] - arr[L] < m:
            m = arr[R] - arr[L]
            res = [[arr[L], arr[R]]]
        elif arr[R] - arr[L] == m:
            res.append([arr[L], arr[R]])
        R += 1
        L += 1
    return res
print(minimumAbsDifference(arr = [4,2,1,3]))
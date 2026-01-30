from collections import Counter, defaultdict
from heapq import heapify, heappop, heappush
def isPossible(nums):
    cnt = Counter(nums)
    cntKeys = cnt.keys()
    max_amount = 0 
    count = 0
    for i in range(1, len(cntKeys),1): 
        if cnt[cntKeys[i]] > max_amount:
            max_amount = cnt[cntKeys[i]]
        if cnt[cntKeys[i]]
            
print(isPossible(nums = [1,2,3,3,4,4,5,5]))
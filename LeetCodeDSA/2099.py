from collections import Counter
from heapq import heappop, heappush, heapify

def maxSubsequence(nums, k): 
    
    heapNums = []
    res = []
    for i in nums: 
        heapNums.append(i)
    heapNums.sort()
    
    heapNums = heapNums[len(heapNums)- k:]
    print(heapNums)
    cnt =Counter(heapNums)
    
    print(cnt)
    for i in nums:
        if i in heapNums and k > 0 and cnt[i] > 0:
            res.append(i)
            cnt[i] -= 1
            k -= 1
    return res
print(maxSubsequence(nums = [-16,-13,8,16,35,-17,30,-8,34,-2,-29,-35,15,13,-30,-34,6,15,28,-23,34,28,-24,15,-17,10,31,32,-3,-36,19,31,-5,-21,-33,-18,-23,-37,-15,12,-28,-40,1,38,38,-38,33,-35,-28,-40,4,-15,-29,-33,-18,-9,-29,20,1,36,-8,23,-34,16,-7,13,39,38,7,-7,-10,30,9,26,27,-37,-18,-25,14,-36,23,28,-15,35,-9,1], k = 8))
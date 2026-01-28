from collections import defaultdict
from sortedcontainers import SortedList
from heapq import heappop, heappush, heapify

def largestSumAfterKNegations(nums, k):
    nums.sort()
    i = 0
    while k > 0 and nums[i] < 0 and i < len(nums): 
        nums[i] = -nums[i]
        k -= 1
        i += 1
    if k % 2 != 0: 
        nums.sort()
        nums[0] = -nums[0]
    return sum(nums)
            
def largestSumAfterKNegationsSortedList(nums, k):
    numsReserved = SortedList(nums)
    
    while k > 0:
        temp = numsReserved[0]
        numsReserved.remove(numsReserved[0])
        numsReserved.add((-1)*temp)
        k -= 1
            

    return sum(numsReserved)
   
def largestSumAfterKNegationsHeap(nums, k):
    heapify(nums)
    print(nums)
    while k > 0: 
        temp = -heappop(nums)
        heappush(nums, temp)
        k -= 1
        
    return sum(nums)
    
print(largestSumAfterKNegations(nums =[5,6,9,-3,3], k =3))
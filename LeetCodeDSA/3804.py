from collections import defaultdict
def centeredSubarrays(nums): 
    count = 0 
    longeur = len(nums)
    hashmap = defaultdict()
    for i in nums: 
        hashmap[i] = True
    
    for i in range(longeur):
        hashmap[i] = False 
        total = nums[i]
        for j in range(i + 1, longeur + 1, 1):
            total += nums[j]
            hashmap[nums[j]] = False
            if 
                
    return hashmap
print(centeredSubarrays(nums = [2,-3]))
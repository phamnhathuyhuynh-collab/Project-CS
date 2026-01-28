def absDifference(nums, k):
    nums.sort()  
    kLargest = 0
    kSmallest = 0  
    for i in range(k):
        kLargest += nums[len(nums) - i - 1]
        kSmallest += nums[i]
    
    print(kLargest - kSmallest)
    
absDifference([100], 1)    
    
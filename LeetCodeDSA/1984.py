def minimumDifference(nums, k):
    nums.sort()
    i = 0
    minNums = float('inf')
    if len(nums) == 1 or k == 1: 
        return 0
    while i + k - 1 < len(nums): 
        if nums[i + k - 1] - nums[i] < minNums: 
            minNums = nums[i + k - 1] - nums[i]
        i += 1
    
    return minNums

# loi giai chuan leetcode
def minimumDifferenceChatGpt(nums, k):
    if k <= 1:
        return 0
        
    nums.sort()
    minDiff = float('inf')
        
    for i in range(len(nums) - k + 1):
        minDiff = min(minDiff, nums[i+k-1] - nums[i])
        
    return minDiff
print(minimumDifference(nums = [10, 1, 7, 5], k = 2))
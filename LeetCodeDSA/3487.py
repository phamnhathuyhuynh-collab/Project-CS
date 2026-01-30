def maxSum(nums):
    unique_nums = set(nums)
    total = 0
    posCount = 0
    for i in unique_nums: 
        if i >= 0: 
            total += i
            posCount += 1
    
    return total if posCount != 0 else min(unique_nums)
    
print(maxSum(nums = [-100]))
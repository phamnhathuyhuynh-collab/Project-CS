def maximumScore(nums):
    sumNums = sum(nums)
        # print(sumNums)
    max = float('-inf')
    min = float('inf')
    for i in range(len(nums) - 2, -1, -1):
        sumNums -= nums[i + 1]
        if nums[i + 1] < min:
            min = nums[i + 1]
        if sumNums - min > max:
            max = sumNums - min 
    return max
    
print(maximumScore(nums = [-7,-5,3]))
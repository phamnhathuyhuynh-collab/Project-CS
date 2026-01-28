def missing_number(nums):
    arr = []
    for i in range(max(nums) + 1):
        arr.append(0)
    for i in range(len(nums)):
       arr[nums[i]] = 1
    for i in range(len(nums)):
        if arr[i] == 0:
            return i
    return max(nums) + 1
def missingNumber(nums):
    missing = len(nums)  
    for i, num in enumerate(nums):
        missing ^= i ^ num
    
    return missing

print(missing_number([0,1,2,3,4,5,6,7])) 
print(missingNumber([0,1,2]))
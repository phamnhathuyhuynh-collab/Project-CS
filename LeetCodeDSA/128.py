def longestConsecutive(nums):
    s = set(nums)
    best = 0 
    for x in s: 
        
        if x - 1 not in s: 
            y = x 
            while y in s: 
                y += 1
 
            best = max(best, y- x)
                
    return best
print(longestConsecutive(nums = [100,4,200,1,3,2]))
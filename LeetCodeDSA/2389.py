from _bisect import bisect_right
def answerQueries(nums, queries):
    nums.sort()

    m = len(nums)
    
    for i in range(1, m):
        nums[i] += nums[i - 1]
    
    return [bisect_right(nums, q) for q in queries]
    
                 
                
                
print(answerQueries(nums = [4,5,2,1], queries = [3,10,21]))
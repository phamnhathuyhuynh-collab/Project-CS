def rotateElements(nums, k):
    t = [] 
    p = []
    n = len(nums)
    for i in range(n): 
        if nums[i] >= 0: 
            t.append(nums[i])
            p.append(i)
    s = set(p)
    m = len(t)
    if m == 0: 
        return nums
    for i in range(k % m):
        temp = t[0]
        t = t[1: m]
        t.append(temp)
    cnt = 0
    for i in range(n):
        if i in s:
           nums[i] = t[cnt]
           cnt += 1
    return nums 
        
print(rotateElements(nums = [1,-2,3,-4], k = 3))
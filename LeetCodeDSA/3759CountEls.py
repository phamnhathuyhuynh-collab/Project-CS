def countElements(nums, k): 
    reserved = {}
    for i in nums:
        value = reserved.get(i, 0) 
        if value != 0:
            (reserved[i]) += 1
        else: 
            (reserved[i]) = 1
            

    
    while k > 0 : 
        if(not reserved):
            break
        reserved.pop(max(reserved))
        k -= 1
    totalCount = 0;
    for i in reserved:        
        totalCount += reserved[i]
    return totalCount
 

print(countElements([5, 5, 5], 0))
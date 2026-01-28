def single_number(nums):
    
    if len(nums) == 1:
            return nums[0]
    count_diction = {}
    for i in nums: 
        count_diction[i] = 0
    for i in nums: 
        count_diction[i] +=1
    for i in count_diction.keys():
        if count_diction[i] == 1:
            return i
print(single_number([1,1,2,4,4,5,5,6,6]))

        
   
           





        
from collections import defaultdict, Counter
def minLength(nums, k):
    left = 0 
    right= 0
    count = float('inf')
    cnt = Counter(nums)
    cnt_reserved = defaultdict()
    
    for i in cnt: 
        cnt_reserved[i] = [cnt[i], cnt[i]]
    
    total = nums[left]
    cnt_reserved[nums[left]][1] -=1
    print(cnt_reserved)
    do_dai = len(nums)
    while right < do_dai: 
        if total >= k : 
            if right + 1 - left <= count:
                count = right + 1 - left
            if cnt_reserved[nums[left]][1] + 1 == cnt_reserved[nums[left]][0]:
                total -= nums[left]
            cnt_reserved[nums[left]][1] += 1
            left += 1
            if left >= do_dai: 
                break
        else: 
            right += 1
            if right >= do_dai :
                break
            if abs(cnt_reserved[nums[right]][1] - 1 - cnt_reserved[nums[right]][0]) == 1:
                total += nums[right]
            cnt_reserved[nums[right]][1] -= 1
        print(total)
        print(count)
        print(left, right)
    return count if count != float('inf') else -1
            
            
            
        
print(minLength(nums = [6, 6, 11], k = 12))
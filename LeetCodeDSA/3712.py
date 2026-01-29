from collections import Counter
def sumDivisibleByK(nums, k):
    cnt = Counter(nums)
    sum = 0
    for i in cnt:
        if cnt[i] % k == 0:
            sum += cnt[i]*i
    return sum
print(sumDivisibleByK(nums = [1,2,2,3,3,3,3,4], k = 2))
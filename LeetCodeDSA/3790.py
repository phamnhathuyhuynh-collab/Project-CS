def minAllOneMultiple(k):
    i = 1
    num = 1
    if k % 2 == 0 or k % 5 == 0:
        return -1
    if k == 1:
        return 1
    while(1):
        i += 1
        num = (num*10 +1) % k
        print(num)
        if num == 0:
            return i

print(minAllOneMultiple(27))


def hamingWieght(n):
    count = 0 
    while n > 0: 
        if n&1:
            count += 1
        n = n >> 1
    return count 

def hamingWieght2(n):
    return n&(n-1)

def hammingWeight3(n):
        count = 0
        while n != 0:
            n &= (n - 1)
            count += 1
        return count
print(hammingWeight3(3))
n = 4
n &=(n-1)
print(n)


        
    
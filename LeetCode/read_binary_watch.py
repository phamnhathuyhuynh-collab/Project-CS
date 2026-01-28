tunred_on = 2

def counts_bit(n):
    res = 0
    while n > 0: 
        res += n&1 
        n >>= 1
    return res

result = []
for i in range(12):
    for j in range(60):
        if counts_bit(i) + counts_bit(j) == tunred_on:
            hour = str(i)
            min = ((2-len(str(j)))*'0'+str(j))
            result.append(hour+':'+min) 
    
print(result)

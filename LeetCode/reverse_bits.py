def reverse_bits_classic(n):
    arr = []
    while n > 0: 
        if n % 2 == 0:
            arr.append(0)
        else: 
            arr.append(1)
            n -= 1
        n /= 2
    while len(arr) < 32:
        arr.append(0)
    result = 0 
    for i, n in enumerate(arr[::-1]):
        if n == 1:
            result += 2**i
    return result 

def reverse_bit_advanced(n):
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n = n >> 1
    return result
        
print(reverse_bits_classic(43261596) == reverse_bit_advanced(43261596))
print(reverse_bit_advanced(43261596))

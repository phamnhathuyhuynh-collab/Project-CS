def count_bits(n):
    arr_bit = []
    for i in range(n +1):
        temp = i
        count = 0
        while temp > 0: 
            if temp&1:
                count += 1
            temp >>= 1
        arr_bit.append(count)
    return arr_bit

def count_bits_n(n):
    arr_bits = [0]
    for i in range(n + 1):
        if i != 0: 
            if i&(i-1) == 0:
                arr_bits.append(1)
            else: 
                arr_bits.append(arr_bits[i&(i-1)] + 1)
    return arr_bits
print(count_bits(20))
print(count_bits_n(20))
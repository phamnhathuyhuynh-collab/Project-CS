def residuePrefixes(s):
    i = 1
    amount = len(s)
    if amount == 1:
        return 1
    count = 0
    while i <= amount: 
        if i % 3 == len(set(s[:i])):
            count += 1
        i += 1
    return count
    return s[:0]
        
print(residuePrefixes(s = "bob"))
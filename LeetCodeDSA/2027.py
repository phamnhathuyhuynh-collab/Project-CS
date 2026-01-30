def minimumMoves(s):
    lenght = len(s) - 1
    count = 0
    i = 0
    while i <= lenght:
        if s[i] == 'X':
            count += 1
            i += 3
        else: 
            i += 1
    return count    
print(minimumMoves(s = "XXOX"))
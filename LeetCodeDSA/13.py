def revertRomanToInt(s):
    match s: 
        case "I":
            return 1
        case "V":
            return 5
        case "X":
            return 10
        case "L":
            return 50
        case "C":
            return 100
        case "D":
            return 500 
        case _:
            return 1000
def romanToInt(s): 
    res = 0
    i = len(s) - 1
    while i > 0:
        if revertRomanToInt(s[i]) > revertRomanToInt(s[i - 1]): 
            res += revertRomanToInt(s[i]) - revertRomanToInt(s[i - 1])
            i -= 2
        else: 
            res += revertRomanToInt(s[i])
            i -= 1
    if i == 0: 
        res += revertRomanToInt(s[i])
    return res
        
print(romanToInt(s = "MMMDCCXXIV"))
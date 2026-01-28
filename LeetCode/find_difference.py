def find_difference(s, t):
    results = 0
    resultt = 0
    for i in s: 
        results += ord(i)
    for i in t:
        resultt += ord(i)
    return chr(abs(results - resultt))

s = 'huy'
t = 'huyt'
print(find_difference(s, t))
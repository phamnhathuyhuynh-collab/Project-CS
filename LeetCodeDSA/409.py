def longest_palindrome(c):
    tableau = {}
    count = 0
    odd = True
    for i in c: 
        if i in tableau: 
            tableau[i] += 1
        else: 
            tableau[i] =1
    for i in tableau:
        if tableau[i] % 2 == 0: 
            count += tableau[i]
        else : 
            if odd :
                count += 1
                odd = False
            
            count += tableau[i] - 1
    return count
    
print(longest_palindrome("d"))
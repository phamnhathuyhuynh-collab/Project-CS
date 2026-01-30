
def swap(a, b):
    temp = a 
    a = b
    b = temp

def reverseChar(s, start , end):
    while start < end: 
        swap(s[start], s[end])
        start += 1
        end -= 1
    
    
def isVowel(s):
    match s: 
        case 'a' | 'i' | 'e' | 'o' | 'u':
            return True
        case _:
            return False

def reverseWords(s):
    start = 0
    demVowel = 0
    for i in s: 
        if i != ' ':
            start += 1
            if isVowel(i):
                demVowel += 1
        else: 
            break
    
    
    i = 0
    while start < len(s):
        nb = 0
        i = start + 1
        while 1: 
            if s[i] != ' ' and i < len(s): 
                if isVowel(s[i]):
                    nb += 1
            else: 
                break
            i += 1
        if nb == demVowel:
            reverseChar(s, start + 1, i- 1)
        start = i
    
    print(s)
        
    
    
reverseWords("Huynh Pham Nhat Huy")
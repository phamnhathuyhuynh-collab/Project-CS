def decrypt(code, k):
    lenght = len(code)
    res = [0]*lenght
    
    if k > 0: 
        i = 0
        while i < lenght: 
            sumI = 0
            j = i + 1
            count = 0
            while count < k: 
                if j >= lenght: 
                    j = 0
                
                sumI += code[j]
                print(code[j])
                j += 1
                count += 1
            
            res[i] = sumI
            i += 1
    if k < 0: 
        i = 0
        while i < lenght: 
            sumI = 0
            j = i - 1
            count = 0
            while count > k: 
                if j < 0 : 
                    j = lenght - 1
                sumI += code[j]
                print(code[j])
                j -= 1
                count -= 1
            res[i] = sumI
            i += 1
    return res
    
                    
        
        
    
print(decrypt(code = [2,4,9,3], k = -2))
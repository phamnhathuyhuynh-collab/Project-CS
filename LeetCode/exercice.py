def moyenne_minimum():
    tableau = [1,2,3,4]
    result = 0
    taille = 0
    for i in tableau:
        taille += 1 
        result += i
        
    moyen = result / taille
    min = tableau[0]
    for i in tableau: 
        if i < min: 
            min = i
    return  moyen, min

def trier():
    tableau = [1,2,4,5]
    taille = 0
    for i in tableau:
        taille += 1
    i = 0 
    j =1
    while j < taille: 
        if tableau[i] > tableau[j]:
            return False
        i += 1
        j += 1 
    return True
print(moyenne_minimum())
print(trier())
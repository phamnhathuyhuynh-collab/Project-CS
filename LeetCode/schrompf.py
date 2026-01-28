def schompf():
    tableau1 = [4, 8, 7, 12]
    tableau2 = [3, 6]
    result = 0
    for i in range(len(tableau2)):
        for j in range(len(tableau1)):
            result += tableau2[i]*tableau1[j]
    return result
print(schompf())
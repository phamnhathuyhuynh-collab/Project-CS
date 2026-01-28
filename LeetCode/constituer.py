def constituer():
    tableau1 = [1,2,3,4,5,6]
    tableau2 = [2,3,4,5,6,7]
    tableau_constitue = []
    for i in range(len(tableau1)):
        somme = tableau1[i] + tableau2[i]
        tableau_constitue.append(somme)
    return tableau_constitue
print(constituer())
        
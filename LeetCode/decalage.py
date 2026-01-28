def decalage(): 
    tableau = [1,2,3,4]
    nombre_de_decale = 2
    for i in range(nombre_de_decale):
        tableau.append(tableau[i])
    for i in range(nombre_de_decale):
        tableau.remove(tableau[0])
    return tableau

def declage_classic():
    tableau = [1,2,3,4]
    nombre_de_decale = 2 
    tableau_vrai = []
    for i in range(nombre_de_decale):
        tableau.append(tableau[i])
    for i in range(len(tableau)):
        if i > nombre_de_decale - 1:
            tableau_vrai.append(tableau[i])
    return tableau_vrai
def deplacer_gauche_en_place(tableau, nombre_de_decale):
    n = len(tableau)
    tableau_reserve = []
    if n <= 1:
        return tableau
    for i in range(nombre_de_decale - 1):
        tableau_reserve.append(tableau[i])
    while i + nombre_de_decale + 1 <= n -1:
        tableau[i + nombre_de_decale] = tableau[i + 1 + nombre_de_decale]
        i += 1
    for i in range(nombre_de_decale - 1):
        tableau.append(tableau[i])
    return tableau
print(decalage())
print(declage_classic())

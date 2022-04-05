from Generique import *


def bd_number(li: list) -> list:
    newLi = []
    dico = create_Dictionnaire(li)
    for i in range(len(li)):
        subTab = []
        for j in range(len(li[i])):
            subTab += [dico.index(li[i][j])]
        newLi += [subTab]
    return newLi


def bd_str(li: list, dico: list) -> list:
    newLi = []
    for i in range(len(li)):
        subTab = []
        for j in range(len(li[i])):
            subTab += [dico[li[i][j]]]
        newLi += [subTab]
    return newLi

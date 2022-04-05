from dbScan.generique import *

def bd_number(li: list) -> list:
    dico = createdico(li)
    for i in range(len(li)):
        for j in range(len(li[i])):
            li[i][j] = dico.index(li[i][j])
    return li

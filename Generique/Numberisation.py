from Generique import create_Dictionnaire


def bd_number(li: list) -> list:
    """
    :param li: list à numériser.
    :return:
    """
    newLi = []
    dico = create_Dictionnaire(li)
    for i in range(len(li)):
        subTab = []
        for j in range(len(li[i])):
            subTab += [dico.index(li[i][j])]
        newLi += [subTab]
    return newLi


def bd_str(li: list, dico: list) -> list:
    """
    :param li: list à dénumériser.
    :param dico: Dictionnaire
    :return:
    """
    newLi = []
    for i in range(len(li)):
        subTab = []
        for j in range(len(li[i])):
            subTab += [dico[li[i][j]]]
        newLi += [subTab]
    return newLi

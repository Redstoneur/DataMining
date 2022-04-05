def yn(intitule: str) -> bool:
    """Question oui/non"""
    r = ""
    y = ['y', 'yes', 'o', 'oui']
    n = ['n', 'no', 'non']
    while r not in y + n:
        r = input(intitule).lower()
    if r in y:
        return True
    return False


def enleve_Duplicatat(tab: list) -> list:
    newT = []
    for i in tab:
        if i not in newT:
            newT += [i]
    return newT


def create_Dictionnaire(tab: list) -> list:
    superT = []
    for i in tab:
        if type(i) is list:
            superT += i
        else:
            superT += [i]
    return enleve_Duplicatat(superT)

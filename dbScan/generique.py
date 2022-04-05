def enleveDuplicatat(tab: list) -> list:
    newT = []
    for i in tab:
        if i not in newT:
            newT += [i]
    return newT


def createdico(tab: list) -> list:
    superT = []
    for i in tab:
        if type(i) is list:
            superT += i
        else:
            superT += [i]
    return enleveDuplicatat(superT)

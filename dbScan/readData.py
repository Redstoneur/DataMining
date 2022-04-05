def readtxt(link: str) -> [str, ValueError]:
    try:
        file = open(link, "r")
        txt = file.read()
        file.close()
        return txt
    except ValueError:
        return ValueError


def readLinesTable(link: str) -> [list, ValueError]:
    try:
        file = open(link, "r")
        tablinestab = []
        for line in file.readlines():
            tablinestab += [line.replace(" \n", "").split(" ")]
        file.close()
        return tablinestab
    except ValueError:
        return ValueError




def superReadLinesTable(link:str) -> [list, ValueError]:
    try:
        file = open(link, "r")
        tablinestab = []
        for line in file.readlines():
            tablinestab += [line.replace(" \n", "").split(" ")]
        file.close()
        return tablinestab
    except ValueError:
        return ValueError

from Generique import enleve_Duplicatat


def haveLinkFile(message: str = "Donnez le lien : ", link: str = "") -> str:
    while 1:
        if link == "":
            link: str = input(message)
        try:
            f = open(link)
        except IOError:
            print("Il y a un problème avec le lien :\n")
            link: str = ""
        else:
            f.close()
            return link


def read_txt(link: str) -> [str, IOError]:
    try:
        file = open(link, "r")
    except IOError:
        return IOError
    else:
        txt = file.read()
        file.close()
        return txt


def readLinesTable(link: str) -> [list, IOError]:
    try:
        file = open(link, "r")
    except IOError:
        return IOError
    else:
        tablinestab = []
        for line in file.readlines():
            tablinestab += [line.replace(" \n", "").split(" ")]
        file.close()
        return tablinestab


def superReadLinesTable(link: str) -> [list, IOError]:
    try:
        file = open(link, "r")
    except IOError:
        return IOError
    else:
        tablinestab = []
        lines = file.readlines()
        for i in range(len(lines)):
            tab = lines[i].split(" ")
            if i != len(lines) - 1:
                tab.pop()
            tablinestab += [enleve_Duplicatat(tab)]
        file.close()
        return tablinestab

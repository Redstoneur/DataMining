from dbScan.generique import *


def haveLinkFile(message: str = "Donnez le lien : ", link: str = "") -> str:
    while 1:
        link = input(message)
        try:
            f = open(link)
        except ValueError:
            print("Il y a un problème avec le lien :\n" + str(ValueError) + "\n")
        else:
            f.close()
            return link


def read_txt(link: str) -> [str, ValueError]:
    try:
        file = open(link, "r")
    except ValueError:
        return ValueError
    else:
        txt = file.read()
        file.close()
        return txt


def readLinesTable(link: str) -> [list, ValueError]:
    try:
        file = open(link, "r")
    except ValueError:
        return ValueError
    else:
        tablinestab = []
        for line in file.readlines():
            tablinestab += [line.replace(" \n", "").split(" ")]
        file.close()
        return tablinestab


def superReadLinesTable(link: str) -> [list, ValueError]:
    try:
        file = open(link, "r")
    except ValueError:
        return ValueError
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

from dbScan.generique import *


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


def superReadLinesTable(link: str) -> [list, ValueError]:
    try:
        file = open(link, "r")
        tablinestab = []
        lines = file.readlines()
        for i in range(len(lines)):
            tab = lines[i].split(" ")
            if i != len(lines) - 1:
                tab.pop()
            tablinestab += [enleveDuplicatat(tab)]
        file.close()
        return tablinestab
    except ValueError:
        return ValueError
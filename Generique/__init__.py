from Generique.HaveNumber import *
from Generique.Numberisation import *


def yn(intitule: str) -> bool:
    """
    Question oui/non
    :param intitule: intitulé de question
    :return:
    """
    r: str = ""
    y: list[str] = ['y', 'yes', 'o', 'oui']
    n: list[str] = ['n', 'no', 'non']
    while r not in y + n:
        r: str = input(intitule).lower()
    if r in y:
        return True
    return False


def enleve_Duplicata(tab: list) -> list:
    """
    Enlève les duplicata de la list fournit en paramètre
    :param tab: liste avec duplicata
    :return:
    """
    newT: list = []
    for i in tab:
        if i not in newT:
            newT += [i]
    return newT


def create_Dictionnaire(tab: list) -> list:
    """
    Crée un dictionnaire de toutes les valeurs rencontrées
    dans la liste en paramètre et ses sous-lists
    :param tab:
    :return:
    """
    superT: list = []
    for i in tab:
        if type(i) is list:
            superT += i
        else:
            superT += [i]
    superT: list = enleve_Duplicata(superT)
    superT.sort()
    return superT

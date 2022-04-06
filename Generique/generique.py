def yn(intitule: str) -> bool:
    """
    Question oui/non
    :param intitule: intitulé de question
    :return:
    """
    r: str = ""  # initialisation de la variable de réponse
    y: list[str] = ['y', 'yes', 'o', 'oui']  # Création de la liste des valeurs de réponse positive
    n: list[str] = ['n', 'no', 'non']  # Création de la liste des valeurs de réponse négative

    while r not in y + n:  # boucle pour avoir une réponse conforme aux réponses possible
        r: str = input(intitule).lower()

    if r in y:
        return True  # si réponse positive
    return False  # si réponse négative


def enleve_Duplicata(tab: list) -> list:
    """
    Enlève les duplicata de la list fournit en paramètre
    :param tab: liste avec duplicata
    :return:
    """
    newT: list = []
    for i in tab:  # récupération des valeurs de façon unique
        if i not in newT:
            newT += [i]
    return newT


def create_Dictionnaire(tab: list) -> list:
    """
    Crée un dictionnaire de toutes les valeurs rencontrées
    dans la liste en paramètre (et ses sous-lists si nécessaire)
    :param tab:
    :return:
    """
    superT: list = []

    for i in tab:  # récupération de toutes les valeurs possible sans se soucier des duplicatas
        if type(i) is list:
            superT += i
        else:
            superT += [i]

    superT: list = enleve_Duplicata(superT)  # suppression des Duplicatas
    superT.sort()  # Trie des valeurs dans l'ordre alphabétique
    return superT

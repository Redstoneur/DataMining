from Generique import enleve_Duplicata


def haveLinkFile(message: str = "Donnez le lien : ", link: str = "") -> str:
    """
    Permet de demander à l'utilisateur un lien vers des données.
    :param message: intitulé de question
    :param link: permet de donner un lien par défaut (facultatif)
    :return:
    """
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


def ReadLinesData(link: str) -> [list, IOError]:
    """
    Permet de lire les données.
    Nécessite un fichier txt
    :param link: lien vers le fichier
    :return:
    """
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
            tablinestab += [enleve_Duplicata(tab)]
        file.close()
        return tablinestab

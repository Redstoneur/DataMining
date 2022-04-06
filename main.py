from Generique import *
from WorkSpace import *


def main(Link: str = "./Document/NoSql.txt", eps: float = 0.5, minPts: int = 4, DevMod: bool = False,
         DebugMod: bool = False):
    """
    :param Link: Le lien par défaut
    :param minPts:
    :param eps:
    :param DevMod: Si en True permet d'utiliser Link sinon False et demande un lien
    :param DebugMod: Si en True permet d'utiliser eps et minPts par défaut sinon False et demande un lien
    :return:
    """

    if not DevMod:  # récupérer un lien vers des données
        Link: str = haveLinkFile("Donnez le lien des données : ")
        print()

    if not DebugMod:  # les valeurs de "eps" et "minPts"
        eps: float = -1
        minPts: int = -1
        while not (0 <= eps <= 1):
            eps: float = haveFloatant("eps = ")
        while not (0 <= minPts <= 10):
            minPts: int = haveInteger("minPts = ")
        print()

    Data = ReadLinesData(Link)  # générer les données
    DBSCAN_cluster = dbscan(Data, eps, minPts)  # créer les Clusters

    print("Les données récupérer : \n" +
          "     --> " + str(Data) + "\n\n" +
          "Les différents Clusters générés : \n" +
          "     --> " + str(DBSCAN_cluster) + "\n")

    if len(Data) == len(DBSCAN_cluster):  # création et affichage des Clusters
        table_cluster = Table_cluster()
        for i in range(len(Data)):
            table_cluster.__add__(DBSCAN_cluster[i], Data[i])
        table_cluster.affichage()


if __name__ == '__main__':
    main(Link="./Document/NoSql.txt", eps=0.5, minPts=4, DevMod=False, DebugMod=False)

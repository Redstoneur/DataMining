from Generique import *
from WorkSpace import *


def main(Link: str = "", DevMod: bool = False, DebugMod: bool = False):
    if not DevMod:
        Link: str = haveLinkFile("Donnez le lien des données : ")
    Data = superReadLinesTable(Link)
    print(Data)

    if DebugMod:
        eps = 0.5
        minPts = 4
    else:
        eps, minPts = -1, -1
        while not (0 <= eps <= 1):
            eps = haveFloatant("eps = ")
        while not (0 <= minPts <= 10):
            minPts = haveFloatant("minPts = ")

    DBSCAN_cluster = dbscan(Data, eps, minPts)
    print(DBSCAN_cluster)

    if len(Data) == len(DBSCAN_cluster):
        table_cluster = Table_cluster()
        for i in range(len(Data)):
            table_cluster.__add__(DBSCAN_cluster[i], Data[i])
        table_cluster.affichage()


if __name__ == '__main__':
    main(Link="./NoSql.txt", DevMod=True, DebugMod=True)

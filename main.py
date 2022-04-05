from dbScan import *


def main(Link: str = "", DevMod: bool = False):
    if not DevMod:
        Link: str = haveLinkFile("Donnez le lien des données : ")
    Data = superReadLinesTable(Link)
    print(Data)
    if DevMod:
        Dictionnaire = create_Dictionnaire(Data)
        Data_Nb = bd_number(Data)
        Data_Str = bd_str(Data_Nb, Dictionnaire)
        print(Dictionnaire)
        print(Data_Nb)
        print(Data_Str)

    DBSCAN_cluster = dbscan(Data, eps=10, minPts=5)
    print(DBSCAN_cluster)


if __name__ == '__main__':
    link = "./NoSql.txt"
    devMod = yn("Mode Dévelopeur ? ")
    main(link, devMod)

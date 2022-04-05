from dbScan import *


def main(Link: str = "", DevMod: bool = False):
    if not DevMod:
        Link: str = haveLinkFile("Donnez le lien des données : ")
    Data = superReadLinesTable(Link)
    Dictionnaire = create_Dictionnaire(Data)
    Data_Nb = bd_number(Data)
    Data_Str = bd_str(Data_Nb, Dictionnaire)
    print(Data)
    print(Dictionnaire)
    print(Data_Nb)
    print(Data_Str)

    # dataArray = np.array(data)
    # dataArray = np.array([["1", "4", "2"], ["0", "2", "4"], ["1", "4", "8"]])
    # print(data)
    # print(dataArray)
    DBSCAN_cluster = dbscan(Data, eps=10, min_samples=5)
    print(DBSCAN_cluster)
    # print(DBSCAN_cluster.labels_)
    # label, core_sample_mask = DBSCAN(eps=0.3, min_samples=10).fit(data)


if __name__ == '__main__':
    link = "./NoSql.txt"
    devMod = yn("Mode Dévelopeur ? ")
    main(link, devMod)

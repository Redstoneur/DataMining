from dbScan import *

if __name__ == '__main__':
    # link = input("link : ")
    link = "C:/Alipio/DataMinig/NoSql.txt"
    # date = readtxt(link)
    # date = readLinesTable(link)
    data = superReadLinesTable(link)
    dico = createdico(data)
    print(data)
    print(dico)
    dataNb = (bd_number(data))
    print(data)
    print(dataNb)
    #dataArray = np.array(data)
    # dataArray = np.array([["1", "4", "2"], ["0", "2", "4"], ["1", "4", "8"]])
    # print(data)
    # print(dataArray)

    # DBSCAN_cluster = DBSCAN(eps=10, min_samples=5).fit(dataArray)
    #
    # print(DBSCAN_cluster)
    # print(DBSCAN_cluster.labels_)

    # label, core_sample_mask = DBSCAN(eps=0.3, min_samples=10).fit(data)

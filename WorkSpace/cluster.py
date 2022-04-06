from Generique import create_Dictionnaire, enleve_Duplicata


class Cluster:
    ID: int = None  # ID du Cluster
    Titre: str = ""  # Titre du Cluster
    Properties: list = []  # Liste des propriétés du Cluster
    Generic_Property = []  # Liste Variable Commune

    def __init__(self, numID: int, titre: str = "") -> None:
        """
        Permet d'initier le Cluster.
        :param numID: ID du Cluster
        :param titre: Titre du Cluster (si non fournit met un titre par défaut)
        :return:
        """
        if titre == "":
            self.Titre = "Cluster Numéro " + str(numID)
        self.ID = numID

    def addProperty(self, property: list) -> None:
        """
        Permet d'ajouter une Propriété au Cluster.
        :param property: Propriété à ajouter
        :return:
        """
        self.Properties += [property]
        self.update_Generic_Property()

    def update_Generic_Property(self) -> None:
        """
        Permet de mettre à jour les Propriétés Génériques
        :return:
        """
        if not self.Generic_Property:
            self.Generic_Property = self.Properties[0]
        else:
            dico = create_Dictionnaire(self.Properties)
            self.Generic_Property = dico
            toDel = []
            for i in dico:
                for j in self.Properties:
                    if i not in j:
                        toDel += [i]
            if len(toDel) != 0:
                toDel = enleve_Duplicata(toDel)
                for i in toDel:
                    self.Generic_Property.remove(i)
        self.Generic_Property.sort()

    def Text(self) -> str:
        """
        Permet de récupérer un texte résumé des données du Cluster
        :return:
        """
        return str(self.ID) + ") " + str(self.Titre) + " " + str(self.Generic_Property) + " : \n" + \
               "    ==> List Properties : " + str(self.Properties) + "\n"

    def affichage(self) -> None:
        """
        Permet d'afficher les données du Cluster
        :return:
        """
        print(self.Text())


class Table_cluster:
    tableau: list[Cluster]  # Tableau de Clusters

    def __init__(self) -> None:
        """
        Permet d'initialiser le Tableau de Cluster
        :return:
        """
        self.tableau: list[Cluster] = []

    def __add__(self, numID: int, property: list) -> None:
        """
        Permet d'ajouter des Clusters et leurs propriétés
        :param numID: ID du Cluster
        :param property: Propriété du Cluster
        :return:
        """
        isInTab: bool = False
        if len(self.tableau) != 0:
            for i in range(len(self.tableau)):
                if self.tableau[i].ID == numID:
                    self.tableau[i].addProperty(property)
                    isInTab: bool = True
        if not isInTab:
            cl = Cluster(numID)
            cl.addProperty(property)
            self.tableau += [cl]

    def Text(self) -> str:
        """
        Permet de récupérer un texte résumé des données des Clusters du Tableau
        :return:
        """
        text: str = "Liste des Clusters :\n"
        for i in self.tableau:
            text += i.Text()
        return text

    def affichage(self) -> None:
        """
        afficher les Clusters du tableau
        :return:
        """
        print(self.Text())

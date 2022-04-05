from Generique import create_Dictionnaire, enleve_Duplicatat


class Cluster:
    ID: int = None
    Titre: str = ""
    Properties: list = []
    Generic_Property = []

    def __init__(self, numID: int, titre: str = ""):
        if titre == "":
            self.Titre = "Cluster Numéro " + str(numID)
        self.ID = numID

    def addProperty(self, property: list):
        self.Properties += [property]
        self.update_Generic_Property(property)

    def update_Generic_Property(self, property: list):
        if not self.Generic_Property:
            self.Generic_Property = property
        else:
            dico = create_Dictionnaire(self.Properties)
            self.Generic_Property = dico
            toDel = []
            for i in dico:
                for j in self.Properties:
                    if i not in j:
                        toDel += [i]
            if len(toDel) != 0:
                toDel = enleve_Duplicatat(toDel)
                for i in toDel:
                    self.Generic_Property.remove(i)

    def Text(self) -> str:
        return str(self.ID) + ") " + str(self.Titre) + " " + str(self.Generic_Property) + " : \n" + \
               "    - List Properties : " + str(self.Properties) + "\n"

    def affichage(self):
        print(self.Text())


class Table_cluster:
    tableau: list[Cluster]

    def __init__(self):
        self.tableau = []

    def __add__(self, numID: int, property: list):
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
        text: str = "Liste des Clusters :\n"
        for i in self.tableau:
            text += i.Text()
        return text

    def affichage(self):
        print(self.Text())

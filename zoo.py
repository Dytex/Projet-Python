class animaux:

    def __init__(self, regime, qt_nourit, nombre):
        self.regime = regime
        self.qt_nourit = qt_nourit
        self.nombre = nombre

class domestiques(animaux):

    def __init__(self, regime, qt_nourit, nombre, nb_pattes, mammifere, marin):
        super().__init__(regime, qt_nourit, nombre)
        self.nb_pattes = nb_pattes
        self.mammifere = mammifere
        self.marin = marin

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}".format(self.regime, self.qt_nourit, self.nombre, self.nb_pattes, self.mammifere, self.marin)

class mammiferes(animaux):

    def __init__(self, regime, qt_nourit, nombre, nb_pattes, marin, domestique):
        super().__init__(regime, qt_nourit, nombre)
        self.nb_pattes = nb_pattes
        self.marin = marin
        self.domestique = domestique

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}, {5}".format(self.regime, self.qt_nourit, self.nombre, self.nb_pattes, self.marin, self.domestique)

class marins(animaux):

    def __init__(self, regime, qt_nourit, nombre, domestique, mammifere):
        super().__init__(regime, qt_nourit, nombre)
        self.domestique = domestique
        self.mammifere = mammifere

    def __str__(self):
        return "{0}, {1}, {2}, {3}, {4}".format(self.regime, self.qt_nourit, self.nombre, self.domestique, self.mammifere)

if (__name__ == '__main__'):
    mon_dictionnaire = {}
    mon_dictionnaire["Humain"] = mammiferes('omnivore', 600, 2, 2, "Non", "Non")
    mon_dictionnaire["Lion"] = mammiferes('carnivore', 3000, 1, 4, "Non", "Non")
    mon_dictionnaire["Lapin"] = mammiferes('vegetarien', 100, 7, 4, "Non", "Oui")
    mon_dictionnaire["Mouton"] = mammiferes('vegetarien', 500, 5, 4, "Non", "Oui")
    mon_dictionnaire["Chien"] = mammiferes('omnivore', 500, 2, 4, "Non", "Oui")
    mon_dictionnaire["Pieuvre"] = marins('carnivore', 200, 1, "Non", "Non")
    mon_dictionnaire["Poule"] = domestiques('omnivore', 200, 8, 2, "Non", "Oui")

    print ("Humain : ", mon_dictionnaire["Humain"],"\n", "Lion : ", mon_dictionnaire["Lion"],"\n","Lapin : ", mon_dictionnaire["Lapin"],"\n","Mouton : ", mon_dictionnaire["Mouton"],"\n","Chien : ", mon_dictionnaire["Chien"],"\n","Pieuvre : ", mon_dictionnaire["Pieuvre"],"\n","Poule : ", mon_dictionnaire["Poule"])

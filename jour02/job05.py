class Voiture:
    def __init__(self):
        self.__marque = "Renault"
        self.__modele = "Clio 4"
        self.__annee = 2016
        self.__kilometrage = 74_154
        self.__en_marche = False
        self.__reservoir = 45

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("Voiture en marche")
        else:
            print("En réseerve")

    def arreter(self):
        if self.__en_marche:
            self.__en_marche = False
            print("Voiture arrêtée")

    def __verifier_plein(self):
        return self.__reservoir

    def __set_marque(self):
        self.__marque = "Ford"
        return self.__marque

    def __set_modele(self):
        self.__modele = "Puma ST"
        return self.__modele

    def __set_annee(self):
        self.__annee = 2020
        return self.__annee

    def __set_kilometrage(self):
        self.__kilometrage = 22_172
        return self.__kilometrage

    def get_marque(self):
        self.__set_marque()
        print(f"Marque : {self.__marque}")

    def get_modele(self):
        self.__set_modele()
        print(f"Modèle : {self.__modele}")

    def get_annee(self):
        self.__set_annee()
        print(f"Année : {self.__annee}")

    def get_kilometrage(self):
        self.__set_kilometrage()
        print(f"Kilométrage : {self.__kilometrage}")


voiture = Voiture()

voiture.get_marque()
voiture.get_modele()
voiture.get_annee()
voiture.get_kilometrage()

voiture.demarrer()
voiture.arreter()


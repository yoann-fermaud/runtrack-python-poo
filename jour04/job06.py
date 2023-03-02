class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def demarrer(self):
        print("Attention, je roule !")

    def informations_vehicule(self):
        print("\n[Informations véhicule]"
              "\nMarque:", self.marque,
              "\nModèle:", self.modele,
              "\nAnnée:", self.annee,
              "\nPrix:", self.prix, "euros")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.nb_portes = 4

    def demarrer(self):
        print(f"{self.marque} {self.modele} en marche.")

    def informations_vehicule(self):
        super().informations_vehicule()
        print("Nombre de portes:", self.nb_portes)


class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.nb_roues = 2

    def demarrer(self):
        print(f"{self.marque} {self.modele} en marche.")

    def informations_vehicule(self):
        super().informations_vehicule()
        print("Nombre de roues:", self.nb_roues)


voiture_00 = Voiture("Ford", "Puma ST", 2020, 35_699)
moto_00 = Moto("Yamaha", "R1", 2022, 20_499)

voiture_00.informations_vehicule()
voiture_00.demarrer()

moto_00.informations_vehicule()
moto_00.demarrer()

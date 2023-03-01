class Ville:
    def __init__(self, ville, nb_habitants):
        self.__ville = ville
        self.__nb_habitants = nb_habitants

    def set_nb_habitants(self):
        self.__nb_habitants += 1
        return self.__nb_habitants

    def get_nb_habitant(self):
        return self.__nb_habitants


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouter_population()

    def ajouter_population(self):
        self.__ville.set_nb_habitants()


ville_paris = Ville("Paris", 1_000_000)
ville_marseille = Ville("Marseille", 861_635)

print("Population de la ville de Paris :", ville_paris.get_nb_habitant(), "habitants")
print("Population de la ville de Marseille :", ville_marseille.get_nb_habitant(), "habitants")

personne_00 = Personne("John", 45, ville_paris)
personne_01 = Personne("Myrtille", 4, ville_paris)
personne_02 = Personne("Chloé", 18, ville_marseille)

print("Mise à jour de la population de la ville de Paris :", ville_paris.get_nb_habitant(), "habitants")
print("Mise à jour de la population de la ville de Marseille :", ville_marseille.get_nb_habitant(), "habitants")

class Personne:
    def __init__(self):
        self.age = 14

    def modifier_age(self, age):
        self.age = age
        return self.age

    def afficher_bonjour(self):
        print("Hello !")

    def afficher_age(self):
        print(self.age)


class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def aller_en_cours(self):
        print("Je vais en cours.")

    def affichage_age(self):
        print(f"J'ai {self.age} ans.")


class Professeur:
    def __init__(self, matiere_enseignee):
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print("Le cours va commencer.")


personne_00 = Personne()
eleve_00 = Eleve()

personne_00.afficher_age()
eleve_00.afficher_age()
eleve_00.affichage_age()

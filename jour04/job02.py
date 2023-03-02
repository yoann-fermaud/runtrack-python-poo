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


class Professeur(Personne):
    def __init__(self, matiere_enseignee):
        Personne.__init__(self)
        self.__matiere_enseignee = matiere_enseignee

    def enseigner(self):
        print(f"Le cours de {self.__matiere_enseignee} va commencer.")


professeur_00 = Professeur("mathématiques")
eleve_00 = Eleve()

professeur_00.enseigner()
eleve_00.afficher_bonjour()
eleve_00.aller_en_cours()

professeur_00.modifier_age(40)
eleve_00.modifier_age(15)

professeur_00.afficher_age()
eleve_00.affichage_age()

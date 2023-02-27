class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def se_presenter(self):
        return print("Je suis", self.nom, self.prenom)


personne_01 = Personne("John", "Doe")
personne_02 = Personne("Jean", "Dupond")

personne_01.se_presenter()
personne_02.se_presenter()

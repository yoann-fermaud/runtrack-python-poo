import random


class Personnage:
    def __init__(self, nom: str, vie: int):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        ennemi.vie -= random.randint(2, 20)
        return ennemi.vie


class Jeu:
    def __init__(self):
        self.niveau = None
        self.vie_multiplicateur = None

    def choisir_niveau(self):
        while self.niveau is None:
            try:
                match int(input("1. Facile\n2. Moyen\n3. Difficile"
                                "\nChoisissez votre niveau de difficulté: ")):
                    case 1:
                        self.niveau = "Facile"
                        return self.niveau
                    case 2:
                        self.niveau = "Moyen"
                        return self.niveau
                    case 3:
                        self.niveau = "Difficile"
                        return self.niveau
                    case _:
                        print("\nNiveau de difficulté invalide.")
            except ValueError:
                print("\nNiveau de difficulté invalide.")

    def victoire(self):
        if self.joueur_00.vie <= 0 <= self.joueur_01.vie:
            print(f"{self.joueur_00.nom} est vaincu !")
        elif self.joueur_01.vie <= 0 <= self.joueur_00.vie:
            print(f"Le {self.joueur_01.nom} est vaincu !")

    def lancer_jeu(self):
        self.choisir_niveau()
        if self.niveau == "Facile" or self.niveau == "Moyen":
            self.vie_multiplicateur = 1
        elif self.niveau == "Difficile":
            self.vie_multiplicateur = 2

        self.joueur_00 = Personnage("DOOM", self.vie_multiplicateur * 50)
        self.joueur_01 = Personnage("BOSS", self.vie_multiplicateur * 60)

        print(f"\n{self.joueur_00.nom} VERSUS {self.joueur_01.nom} !")
        tour = 1
        while self.joueur_00.vie > 0 and self.joueur_01.vie > 0:
            print(f"\n[Tour {tour}] - "
                  f"{self.joueur_00.nom} : {self.joueur_00.vie} PV, "
                  f"{self.joueur_01.nom} : {self.joueur_01.vie} PV")
            try:
                match int(input("Choisissez une option - [1]: attaquer ou [2]: fuir ? ")):
                    case 1:
                        self.joueur_00.attaquer(self.joueur_01)
                        if self.niveau != "Facile":
                            self.joueur_01.attaquer(self.joueur_00)
                    case 2:
                        print("Vous avez fui le combat ???")
                        break
                    case _:
                        self.joueur_01.attaquer(self.joueur_00)
                        print("Choix invalide, vous subissez des dommages !")
                tour += 1
            except ValueError:
                self.joueur_01.attaquer(self.joueur_00)
                print("Choix invalide, vous subissez des dommages !")

        self.victoire()


if __name__ == '__main__':
    jeu = Jeu()
    jeu.lancer_jeu()

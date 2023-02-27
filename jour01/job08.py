import math


class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changer_rayon(self, rayon):
        self.rayon = rayon
        return self.rayon

    def aire(self):
        return (self.rayon ** 2) * math.pi

    def circonference(self):
        return self.diametre() * math.pi

    def diametre(self):
        return self.rayon * 2

    def afficher_infos(self):
        return print(f"Rayon du cercle : {self.rayon}\n"
                     f"Diamètre du cercle : {self.diametre()}\n"
                     f"Aire du cercle : {self.aire()}\n"
                     f"Circonférence du cercle : {self.circonference()}")


cercle = Cercle(12)

print("Avant changement de rayon :")
cercle.afficher_infos()

print("\nAprès changement de rayon :")
cercle.changer_rayon(22)
cercle.afficher_infos()


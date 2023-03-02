class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return (2 * self.__longueur) + (2 * self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur

    def __set_longeur(self, longueur):
        self.__longueur = longueur
        return self.__longueur

    def __set_largeur(self, largeur):
        self.__largeur = largeur
        return self.__largeur

    def get_longueur(self, longueur):
        self.__set_longeur(longueur)
        return self.__longueur

    def get_largeur(self, largeur):
        self.__set_largeur(largeur)
        return self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.surface() * self.__hauteur


rect = Rectangle(12, 22)
para = Parallelepipede(12, 22, 10)

print("[Avant modification]")
print("Périmètre du rectangle:", rect.perimetre())
print("Surface du rectangle:", rect.surface())
print("Volume du parallélépipède:", para.volume())

rect.get_longueur(10)
rect.get_largeur(20)
para.get_longueur(10)
rect.get_largeur(20)

print("\n[Après modification]")
print("Périmètre du rectangle:", rect.perimetre())
print("Surface du rectangle:", rect.surface())
print("Volume du parallélépipède:", para.volume())

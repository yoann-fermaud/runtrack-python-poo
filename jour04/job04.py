class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        Forme.__init__(self)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur


rect = Rectangle(12, 22)
print("Aire du rectangle:", rect.aire())

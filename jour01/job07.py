class Personnage:
    def __init__(self):
        self.x = 22
        self.y = 12

    def gauche(self):
        self.x -= 1
        return self.x

    def droite(self):
        self.x += 1
        return self.x

    def haut(self):
        self.y += 1
        return self.y

    def bas(self):
        self.y -= 1
        return self.y

    def position(self):
        my_tuple = (self.x, self.y)
        return print(my_tuple)


personnage = Personnage()
personnage.position()
personnage.gauche()
personnage.haut()
personnage.position()

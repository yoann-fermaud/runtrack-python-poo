class Rectangle:
    def __init__(self):
        self.__longueur = 10
        self.__largeur = 5

    #  Mutateur
    def __set_rectangle(self):
        self.__longueur = 22
        self.__largeur = 12

    #  Assesseur
    def get_rectangle(self):
        print("Avant appelle du setter :", self.__longueur, self.__largeur)
        self.__set_rectangle()
        print("Après appelle du setter :", self.__longueur, self.__largeur)


rect = Rectangle()
rect.get_rectangle()

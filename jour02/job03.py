class Livre:
    def __init__(self):
        self.__titre = "Les Misérables"
        self.__auteur = "Victor Hugo"
        self.__nombre_pages = 2598
        self.__old_nombre_pages = self.__nombre_pages
        self.__disponible = True

    def emprunter(self):
        if self.verification():
            self.__disponible = False
        return True

    def rendre(self):
        if self.emprunter():
            self.__disponible = True

    def verification(self):
        if self.__disponible:
            return True
        return False

    def __set_livre(self):
        self.__titre = "La photo qui tue"
        self.__auteur = "Anthony Horowitz"
        self.__nombre_pages = 224
        if self.__nombre_pages < 0:
            self.__nombre_pages = self.__old_nombre_pages
            print("ValueError: __nombre_pages")

    def get_livre(self):
        self.__set_livre()
        print(f"Informations :'{self.__titre}' de {self.__auteur}, "
              f"{self.__nombre_pages} pages, {self.__disponible}")


livre = Livre()
#  Livre Disponible
livre.verification()
livre.get_livre()
#  Emprunt
livre.emprunter()
livre.get_livre()
#  Livre rendu
livre.rendre()
livre.get_livre()


class Livre:
    def __init__(self):
        self.__titre = "Les Misérables"
        self.__auteur = "Victor Hugo"
        self.__nombre_pages = 2598
        self.__old_nombre_pages = self.__nombre_pages

    def __set_livre(self):
        self.__titre = "La photo qui tue"
        self.__auteur = "Anthony Horowitz"
        self.__nombre_pages = 224

        if self.__nombre_pages < 0:
            self.__nombre_pages = self.__old_nombre_pages
            print("ValueError: __nombre_pages")

    def get_livre(self):
        print(f"Avant appelle du setter : '{self.__titre}' de {self.__auteur}, {self.__nombre_pages} pages")
        self.__set_livre()
        print(f"Après appelle du setter : '{self.__titre}' de {self.__auteur}, {self.__nombre_pages} pages")


livre = Livre()
livre.get_livre()

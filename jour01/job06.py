class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""
        print(f"L'age de l'animal est de {self.age} ans")

    def vieillir(self):
        self.age += 1
        return print(f"L'age de l'animal est de {self.age} ans")

    def nommer(self, prenom):
        self.prenom = prenom
        return print(f"L'animal se nomme {self.prenom}")


animal = Animal()
animal.vieillir()
animal.nommer("Luna")

class Point:
    def __init__(self):
        self.x = 22
        self.y = 12

    def afficher_les_points(self):
        return print(f"Valeur des points x, y : {self.x}, {self.y}")

    def afficher_x(self):
        return print(f"Valeur du points x : {self.x}")

    def afficher_y(self):
        return print(f"Valeur du point y : {self.y}")

    def changer_x(self):
        self.x = 12
        return self.x

    def changer_y(self):
        self.y = 22
        return self.y


point = Point()

print("Avant changement des valeurs de x et y")
point.afficher_les_points()
point.afficher_x()
point.afficher_y()

print("\nAprès changement des valeurs de x et y")
point.changer_x()
point.changer_y()

point.afficher_les_points()
point.afficher_x()
point.afficher_y()

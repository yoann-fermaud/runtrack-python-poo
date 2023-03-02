import math


class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius

    def aire(self):
        return (self.radius ** 2) * math.pi


cercle = Cercle(12)
print("Aire du cercle:", cercle.aire())

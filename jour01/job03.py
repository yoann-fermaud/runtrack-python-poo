class Operation:
    def __init__(self):
        self.nombre1 = 22
        self.nombre2 = 12

    def addition(self):
        return print("Addition de nombre1 + nombre2 :", self.nombre1 + self.nombre2)


op = Operation()
op.addition()

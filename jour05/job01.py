# --| 1 |-- #
class Factorial:
    def __init__(self):
        self.__integer = None
        self.__factorial = self.__integer

    def take_input(self):
        self.__integer = int(input("Enter an integer: "))
        self.__factorial = self.__integer - 1
        return self.__integer

    def show_input(self):
        print("Calculate the factorial of", self.take_input())

    def calculate(self):
        if self.__factorial > 0:
            self.__integer *= self.__factorial
            self.__factorial -= 1
            self.calculate()
        else:
            print("Result:", self.__integer)

    def run(self):
        self.show_input()
        self.calculate()


factorial = Factorial()
factorial.run()


# --| 2 |-- #


# def take_input():
#     return int(input("Enter an integer: "))
#
#
# def factorial(value):
#     if value > 0:
#         return value * factorial(value - 1)
#     else:
#         return 1
#
#
# print("Result of the factorial:", factorial(take_input()))

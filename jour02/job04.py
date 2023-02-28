class Student:
    def __init__(self, first_name, last_name, identification_number):
        self.__first_name, self.__last_name = first_name, last_name
        self.__identification_number = identification_number
        self.__credit_numbers = 0
        self.__level = self.__student_eval()

    def __add_credits(self, credit):
        if credit > 0:
            self.__credit_numbers += credit
            self.__level = self.__student_eval()

    def __student_eval(self):
        if self.__credit_numbers >= 90:
            return "Excellent"
        elif self.__credit_numbers >= 80:
            return "Très Bien"
        elif self.__credit_numbers >= 70:
            return "Bien"
        elif self.__credit_numbers >= 60:
            return "Passable"
        else:
            return "insuffisant"

    def get_student(self):
        self.__add_credits(40)
        self.__add_credits(50)
        print(f"Le nombre de crédits de {self.__first_name} {self.__last_name} est de {self.__credit_numbers}")

    def get_student_info(self):
        print(f"Nom : {self.__last_name}"
              f"\nPrénom : {self.__first_name}"
              f"\nId : {self.__identification_number}"
              f"\nNiveau : {self.__level}")


student_01 = Student("John", "Doe", 145)
student_01.get_student()
student_01.get_student_info()

class StudentNotaDTO:

    def __init__(self, nume_student, nota_student):
        self.__nume_student = nume_student
        self.__nota_student = nota_student

    def __str__(self):
        return f"Studentul {self.__nume_student} cu nota {self.__nota_student}"

    def __lt__(self, other):
        if self.__nume_student == other.__nume_student:
            return self.__nota_student > other.__nota_student
        else:
            return self.__nume_student < other.__nume_student

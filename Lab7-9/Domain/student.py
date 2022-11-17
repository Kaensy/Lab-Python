class Student:

    def __init__(self, id_student, nume):
        self.__id_student = id_student
        self.__nume = nume
        self.__sters = False

    def sterge(self):
        self.__sters = True

    def getID_student(self):
        return self.__id_student

    def getNume(self):
        return self.__nume

    def setNume(self, nume):
        self.__nume = nume

    def get_sters(self):
        return self.__sters

    def __eq__(self, other):
        return self.__id_student == other.__id_student

    def __str__(self):
        return f"{self.__id_student} {self.__nume}"
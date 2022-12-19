class NotaDTO():

    def __init__(self, id_nota, id_student, id_materie, nota):
        self.__id_nota = id_nota
        self.__id_student = id_student
        self.__id_materie = id_materie
        self.__nota = nota

    def get_id_nota(self):
        return self.__id_nota

    def get_id_student(self):
        return self.__id_student

    def get_id_materie(self):
        return self.__id_materie

    def get_nota(self):
        return self.__nota

    def __str__(self):
        return f"{self.__student.getNume()} {self.__materie.get_nume_materie()} {self.__nota} {self.__id_nota}"

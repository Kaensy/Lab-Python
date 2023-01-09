
class Nota:
    """
    Clasa Nota care contine elemente cu id-ul unic de tip int id_nota, studentul de tip Student student,
    materia de tip Materie materie si nota de tip int nota
    """
    def __init__(self, id_nota, id_student, id_materie, nota):
        self.__id_nota = id_nota
        self.__id_student = id_student
        self.__id_materie = id_materie
        self.__nota = nota

    def get_id_nota(self):
        """
        returneaza id-ul unic de tip int din __id_nota
        :return: rez : int - __id_nota
        """
        return self.__id_nota

    def get_id_student(self):
        """
        returneaza studentul de tip Student din __student
        :return: rez : Student - __student
        """
        return self.__id_student


    def get_nota(self):
        """
        returneaza valoarea de tip int din __nota
        :return: rez : int - __nota
        """
        return self.__nota

    def get_id_materie(self):
        """
        returneaza materia de tip Materie din __materie
        :return: rez : Materie - __materie
        """
        return self.__id_materie

    def set_nota(self, nota):
        """
        schimba nota de tip int din __nota cu nota nota
        :param nota: int
        :return: - ( __nota = nota )
        """
        self.__nota = nota

    def __eq__(self, other):
        return self.__id_nota == other.__id_nota

    def __str__(self):
        return f"{self.__id_nota} {self.__id_student} {self.__id_materie} {self.__nota}"

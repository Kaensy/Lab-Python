class Nota:
    """
    Clasa Nota care contine elemente cu id-ul unic de tip int id_nota, studentul de tip Student student,
    materia de tip Materie materie si nota de tip int nota
    """
    def __init__(self, id_nota, student, materie, nota):
        self.__id_nota = id_nota
        self.__student = student
        self.__materie = materie
        self.__nota = nota
        self.__sters = False

    def get_id_nota(self):
        """
        returneaza id-ul unic de tip int din __id_nota
        :return: rez : int - __id_nota
        """
        return self.__id_nota

    def get_student(self):
        """
        returneaza studentul de tip Student din __student
        :return: rez : Student - __student
        """
        return self.__student

    def get_sters(self):
        """
        returneaza valoarea de tip bool a campului __sters
        :return: rez : bool - True ( __sters == True )
                            - False ( __sters == False )
        """
        return self.__sters

    def get_nota(self):
        """
        returneaza valoarea de tip int din __nota
        :return: rez : int - __nota
        """
        return self.__nota

    def get_materie(self):
        """
        returneaza materia de tip Materie din __materie
        :return: rez : Materie - __materie
        """
        return self.__materie

    def set_nota(self, nota):
        """
        schimba nota de tip int din __nota cu nota nota
        :param nota: int
        :return: - ( __nota = nota )
        """
        self.__nota = nota
    def sterge(self):
        """
        Marcheaza nota ca find stearsa
        :return: - ( __sters = True )
        """
        self.__sters = True

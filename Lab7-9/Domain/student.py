class Student:
    """
    Clasa Student care contine elemente cu id-ul unic de tip int id_student
    si numele de tip string nume
    """
    def __init__(self, id_student, nume):
        self.__id_student = id_student
        self.__nume = nume
        self.__sters = False

    def sterge(self):
        """
        Marcheaza studentul ca find sters
        :return: - ( __sters = True )
        """
        self.__sters = True

    def getID_student(self):
        """
        returneaza id-ul unic al studentull Student
        :return: rez : int - __id_student
        """
        return self.__id_student

    def getNume(self):
        """
        returneaza numele __nume al studentului
        :return: rez : string - __nume
        """
        return self.__nume

    def setNume(self, nume):
        """
        schimba numele __nume al studentului Student in noul nume nume
        :param nume: string
        :return: - ( __nume = nume )
        """
        self.__nume = nume

    def get_sters(self):
        """
        returneaza valoarea de tip bool a campului __sters
        :return: rez : bool - True ( __sters == True )
                            - False ( __sters == False )
        """
        return self.__sters

    def __eq__(self, other):
        return self.__id_student == other.__id_student

    def __str__(self):
        return f"{self.__id_student} {self.__nume}"

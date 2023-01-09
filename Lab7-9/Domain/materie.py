class Materie:

    """
    Clasa Materie care contine elemente cu id-ul unic de tip int id_materie,
    numele materiei de tip string nume_materie si
    numele profesorului de tip string nume_profesor
    """

    def __init__(self, id_materie, nume_materie, nume_profesor):
        self.__id_materie = id_materie
        self.__nume_materie = nume_materie
        self.__nume_profesor = nume_profesor


    def get_id_materie(self):
        """
        returneaza id-ul unic al materiei materie
        :return: rez : int - id_materie
        """
        return self.__id_materie

    def get_nume_materie(self):
        """
        returneaza numele materiei nume_materie al materiei materie
        :return: rez : string - nume_materie
        """
        return self.__nume_materie

    def get_nume_profesor(self):
        """
        returneaza numele profesorului nume_profesor al materiei materie
        :return: rez : string - nume_profesor
        """
        return self.__nume_profesor

    def set_nume_materie(self, nume_materie):
        """
        schimba numele materiei __nume_materie in noul nume materie nume_materie
        :param nume_materie: string
        :return: - ( __nume_materie = nume_materie )
        """
        self.__nume_materie = nume_materie

    def set_nume_profesor(self, nume_profesor):
        """
        schimba numele profesorului __nume_profesor in noul nume profesor nume_profesor
        :param nume_profesor: string
        :return: - ( __nume_profesor = nume_profesor )
        """
        self.__nume_profesor = nume_profesor

    def __str__(self):
        return f"{self.__id_materie} {self.__nume_materie} {self.__nume_profesor}"

    def __eq__(self, other):
        return self.__id_materie == other.__id_materie

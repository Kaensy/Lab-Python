class Materie:

    def __init__(self, id_materie, nume_materie, nume_profesor):
        self.__id_materie = id_materie
        self.__nume_materie = nume_materie
        self.__nume_profesor = nume_profesor
        self.__sters = False

    def sterge(self):
        self.__sters = True

    def get_id_materie(self):
        return self.__id_materie

    def get_nume_materie(self):
        return self.__nume_materie

    def get_nume_profesor(self):
        return self.__nume_profesor

    def get_sters(self):
        return self.__sters

    def set_nume_materie(self, nume_materie):
        self.__nume_materie = nume_materie

    def set_nume_profesor(self, nume_profesor):
        self.__nume_profesor = nume_profesor

    def __str__(self):
        return f"{self.__id_materie} {self.__nume_materie} {self.__nume_profesor}"

    def __eq__(self, other):
        return self.__id_materie == other.__id_materie

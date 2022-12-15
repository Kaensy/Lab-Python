class Costum:
    """
    Clasa Costum formata din id-ul unic int id_costum, denumirea string denumire_costum, tematica string tematica_costum,
    pretul int pret_costum, disponibilitatea string disponibilitate_costum
    """

    def __init__(self, id_costum, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum):
        self.__id_costum = id_costum
        self.__denumire_costum = denumire_costum
        self.__tematica_costum = tematica_costum
        self.__pret_costum = pret_costum
        self.__disponibilitate_costum = disponibilitate_costum

    def get_id_costum(self):
        return self.__id_costum

    def get_denumire_costum(self):
        return self.__denumire_costum

    def get_tematica_costum(self):
        return self.__tematica_costum

    def get_pret_costum(self):
        return self.__pret_costum

    def get_disponibilitate_costum(self):
        return self.__disponibilitate_costum

    def set_denumire_costum(self, denumire_costum_noua):
        self.__denumire_costum = denumire_costum_noua

    def set_tematica_costum(self, tematica_costum_noua):
        self.__tematica_costum = tematica_costum_noua

    def set_pret_costum(self, pret_costum_nou):
        self.__pret_costum = pret_costum_nou

    def set_disponibilitate_costum(self, disponibilitate_costum):
        self.__disponibilitate_costum = disponibilitate_costum

    def __str__(self):
        return (f"{self.__id_costum},{self.__denumire_costum},{self.__tematica_costum},{self.__pret_costum},{self.__disponibilitate_costum}")

    def __eq__(self, other):
        return self.__id_costum == other.__id_costum

    def __lt__(self, other):
        return self.__pret_costum < other.__pret_costum

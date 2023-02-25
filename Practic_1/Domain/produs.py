class Produs:

    def __init__(self, id_produs, denumire, pret):
        self.__id = id_produs
        self.__denumire = denumire
        self.__pret = pret

    def get_id_produs(self):
        return self.__id

    def get_denumire_produs(self):
        return self.__denumire

    def get_pret_produs(self):
        return self.__pret

    def set_denumire_produs(self, denumire_alta):
        self.__denumire = denumire_alta

    def set_pret_produs(self, pret_altul):
        self.__pret = pret_altul

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return f"{self.__id} {self.__denumire} {self.__pret}"

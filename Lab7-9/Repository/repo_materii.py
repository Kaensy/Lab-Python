from Erori.repo_error import RepoError


class RepoMaterii:
    """
    Clasa RepoMaterii contine un dictionar de materii de tip Materie
    """
    def __init__(self):
        self.__materii = {}

    def adauga_materie(self, materie):
        """
        Incearca adaugarea materiei materie in dictionarul __materii daca  id-ul acestuia nu apare
        deja in dictionar
        :param materie: Materie
        :return: - ( materia materie este adaugat in dictionar )
        :raises : RepoError cu mesajul "materie existenta!" - daca id_ul materiei materie apare in dictionar
        """
        if materie.get_id_materie() in self.__materii and self.__materii[materie.get_id_materie()].get_sters()==False:
            raise RepoError("materie existenta!")
        self.__materii[materie.get_id_materie()] = materie

    def stergere_materie(self, id_materie):
        """
        Verifica daca id-ul id_materie se afla in dictionarul de materii
        Daca se afla materia se marcheaza ca find sters
        Daca nu gaseste id-ul va tipari mesaj eroare corespunzator
        :param id_materie: int
        :return: - ( materia cu id id_materie din dictionar este marchat ca si sters )
        :raises: RepoError cu mesajul "materie inexistenta!" - daca id-ul nu se afla in dictionar
        """
        if id_materie not in self.__materii or self.__materii[id_materie].get_sters()==True:
            raise RepoError("materie inexistenta!")
        self.__materii[id_materie].sterge()

    def cauta_materie(self, id_materie):
        """
        Cauta id-ul unic id_materie in dictionar
        Daca nu il gaseste va tipari mesaj "materie inexistenta!"
        Daca il gaseste returneaza materia Materie
        :param id_materie: int
        :return: rez : Materie - ( materia cu id id_materie din dictionar )
        :raises: RepoError cu mesajul "materie inexistenta!" - daca id_materie nu se afla in dictionar
        """
        if id_materie not in self.__materii or self.__materii[id_materie].get_sters():
            raise RepoError("materie inexistenta!")
        return self.__materii[id_materie]

    def modifica_materie(self, materie):
        """
        Verifica daca id-ul unic al materiei smaterie se afla in dictionarul de materii
        Daca se afla atunci materiea cu id-ul materiei materie se modifica cu elem materiei materie
        Daca nu se afla tipareste mesaj "materie inexistent"
        :param materie: Materie
        :return: - ( materia cu id-ul materiei materie se schimba in materia materie )
        :raises: RepoError : "materie inexistent"
        """
        if materie.get_id_materie() not in self.__materii or self.__materii[materie.get_id_materie()].get_sters()==True:
            raise RepoError("materie inexistenta!")
        self.__materii[materie.get_id_materie()] = materie

    def get_all(self):
        """
        returneaza lista materii de materii de tip Materie formata din materile din dictionar
        :return: rez : list - lista de materii de tip materie
        """
        materii = []
        for materie_id in self.__materii:
            if not self.__materii[materie_id].get_sters():
                materii.append(str(self.__materii[materie_id]))
        return materii

    def __len__(self):
        nr = 0
        for materie in self.__materii:
            if not self.__materii[materie].get_sters():
                nr += 1
        return nr

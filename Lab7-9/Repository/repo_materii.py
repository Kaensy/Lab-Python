from Erori.repo_error import RepoError


class RepoMaterii:
    """
    Clasa RepoMaterii contine un dictionar de materii de tip Materie
    """
    def __init__(self):
        self.__materii = {}

    def adauga_materie(self, materie):
        if materie.get_id_materie() in self.__materii and self.__materii[materie.get_id_materie()].get_sters()==False:
            raise RepoError("materie existenta!")
        self.__materii[materie.get_id_materie()] = materie

    def stergere_materie(self, id_materie):
        if id_materie not in self.__materii or self.__materii[id_materie].get_sters()==True:
            raise RepoError("materie inexistenta!")
        self.__materii[id_materie].sterge()

    def cauta_materie(self, id_materie):
        if id_materie not in self.__materii:
            raise RepoError("materie inexistenta!")
        return self.__materii[id_materie]

    def modifica_materie(self, materie):
        if materie.get_id_materie() not in self.__materii or self.__materii[materie.get_id_materie()].get_sters()==True:
            raise RepoError("materie inexistenta")
        self.__materii[materie.get_id_materie()] = materie

    def get_all(self):
        materii = []
        for materie_id in self.__materii:
            if not self.__materii[materie_id].get_sters():
                materii.append(self.__materii[materie_id])
        return materii

    def __len__(self):
        nr = 0
        for materie in self.__materii:
            if not self.__materii[materie].get_sters():
                nr += 1
        return nr

from Erori.repo_error import RepoError


class RepoNote:
    """
    Clasa RepoNote care contine un dictionar de note de tip Nota
    """
    def __init__(self):
        self.__note = {}

    def adauga_nota(self, nota):
        if nota.get_id_nota() in self.__note and not self.__note[nota.get_id_nota()].get_sters():
            raise RepoError("nota existenta!")
        self.__note[nota.get_id_nota()] = nota


    def sterge_nota(self,id_nota):
        if id_nota not in self.__note or self.__note[id_nota].get_sters():
            raise RepoError("nota inexistenta!")
        self.__note[id_nota].sterge()

    def get_all(self):
        note = []
        for nota_id in self.__note:
            if not self.__note[nota_id].get_sters():
                note.append(self.__note[nota_id])
        return note


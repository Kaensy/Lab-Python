from Erori.repo_error import RepoError


class RepoNote:

    def __init__(self):
        self.__note = {}

    def adauga_nota(self, nota):
        if nota.get_id_nota() in self.__note:
            raise RepoError("nota existent!")
        self.__note[nota.get_id_nota()] = nota


    def get_all(self):
        note = []
        for nota_id in self.__note:
            if not self.__note[nota_id].get_sters():
                note.append(self.__note[nota_id])
        return note


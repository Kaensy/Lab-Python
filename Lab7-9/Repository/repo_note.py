from Erori.repo_error import RepoError


class RepoNote:
    """
    Clasa RepoNote care contine un dictionar de note de tip Nota
    """
    def __init__(self):
        self._note = {}

    def adauga_nota(self, nota):
        if nota.get_id_nota() in self._note and not self._note[nota.get_id_nota()].get_sters():
            raise RepoError("nota existenta!")
        self._note[nota.get_id_nota()] = nota


    def sterge_nota(self,id_nota):
        if id_nota not in self._note or self._note[id_nota].get_sters():
            raise RepoError("nota inexistenta!")
        self._note[id_nota].sterge()

    def get_all(self):
        note = []
        for nota_id in self._note:
            if not self._note[nota_id].get_sters():
                note.append(self._note[nota_id])
        return note


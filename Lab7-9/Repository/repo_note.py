from Erori.repo_error import RepoError


class RepoNote:
    """
    Clasa RepoNote care contine un dictionar de note de tip Nota
    """
    def __init__(self):
        self._note = {}

    def adauga_nota(self, nota):
        if nota.get_id_nota() in self._note:
            raise RepoError("nota existenta!")
        self._note[nota.get_id_nota()] = nota

    def sterge_nota(self, id_nota):
        if id_nota not in self._note:
            raise RepoError("nota inexistenta!")
        del self._note[id_nota]

    def get_all(self):
        note = []
        for nota_id in self._note:
            note.append(self._note[nota_id])
        return note

    def __len__(self):
        return len(self._note)

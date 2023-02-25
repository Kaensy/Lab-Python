from Erori.repo_error import RepoError

class RepoProduse:

    def __init__(self):
        self._produse = {}

    def adauga_produs(self, produs):
        if produs.get_id_produs() in self._produse:
            raise RepoError("Produs Existent!")
        self._produse[produs.get_id_produs()] = produs

    def sterge_produs(self, id_produs):
        if id_produs not in self._produse:
            raise RepoError("Produs Inexistent!")
        del self._produse[id_produs]

    def cauta_produs(self, id_produs):
        if id_produs not in self._produse:
            raise RepoError("Produs Inexistent!")
        return self._produse[id_produs]

    def get_all(self):
        produse = []
        for id_produs in self._produse:
            produse.append(self._produse[id_produs])
        return produse

    def __len__(self):
        return len(self._produse)

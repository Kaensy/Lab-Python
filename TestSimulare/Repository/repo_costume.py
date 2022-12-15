from Erori.repo_error import RepoError

class RepoCostume:
    """
    Clasa RepoCostume contine un dictionar format din costume de tip Costum
    """

    def __init__(self):
        self._costume = {}

    def adauga_costum(self, costum):
        """
        introduce costumul de tip Costum costum in dictionarul de costume _costume daca id-ul costumului costum nu se
        afle deja in dictionar
        :param costum: Costum
        :return: - ( costumul costum se adauga in dictionarul _costume )
        :raise: RepoError cu mesajul "costum existent!"- daca id-ul costumului costum se afla in dictionar
        """
        if costum.get_id_costum() in self._costume:
            raise RepoError("costum existent!")
        self._costume[costum.get_id_costum()] = costum

    def cauta_costum_dupa_id(self, id_costum):
        """
        returneaza costumul costum cu id-ul id_costum
        :param id_costum: int
        :return: rez - costum ( costumul cu id-ul id_costum )
        :raises: RepoError cu mesajul "costum inexistent!" - daca id-ul costumului nu se afla in dictionar
        """
        if id_costum not in self._costume:
            raise RepoError("costum inexistent!")
        return self._costume[id_costum]

    def get_all(self):
        """
        returneaza lista formata din toate costumele din dictionar
        :return: rez - list ( lista de costume )
        """
        costume = []
        for costum in self._costume:
            costume.append(self._costume[costum])
        return costume

    def __len__(self):
        return len(self._costume)

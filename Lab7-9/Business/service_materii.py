from Domain.materie import Materie


class ServiceMaterii:
    """
    Clasa ServiceMaterii contine clasele ValidatorMaterie si RepoMaterii
    """
    def __init__(self, validator_materie, repo_materii):
        self.__validator_materie = validator_materie
        self.__repo_materii = repo_materii

    def adauga_materie(self, id_materie, nume_materie, nume_profesor):
        """
        Construieste materia de tip materie cu id-ul int unic id_materie, numele string nume_materie si numele string nume_profesor
        Valideaza materia materie si daca e valid il adauga in RepoMaterii doar daca acesta nu apare deja in RepoMaterii
        :param id_materie: int
        :param nume_materie: string
        :param nume_profesor: string
        :return: - ( RepoMaterii' = RepoMaterii U materie daca validarea si adaugarea se fac cu succes )
        :raises: ValidError - cu mesajele de validare daca materia creata e invalida
                 RepoError - cu mesajul "materie existenta!" daca materia apare deja in RepoMaterii
        """
        materie = Materie(id_materie, nume_materie, nume_profesor)
        self.__validator_materie.valideaza(materie)
        self.__repo_materii.adauga_materie(materie)

    def modifica_materie(self, id_materie, nume_materie, nume_profesor):
        """
        Construieste materia de tip materie cu id-ul int unic id_materie, numele string nume_materie si numele string nume_profesor
        Valideaza materia materie si daca e valid il cauta materia cu id id_materie din RepoMaterii si il modifica cu noua materie creata
        :param id_materie: int
        :param nume_materie: string
        :param nume_profesor: string
        :return: - ( materia cu id-ul id_materie se va schimba in noua materie cu id-ul id_materie, numele nume_materie si numele nume_profesor )
        :raises: ValidError - cu mesajele de validare daca materia creata e invalida
                 RepoError - cu mesajul "materie inexistenta!" daca materia nu apare in RepoMaterii
        """
        materie = Materie(id_materie, nume_materie, nume_profesor)
        self.__validator_materie.valideaza(materie)
        self.__repo_materii.modifica_materie(materie)

    def get_all_materii(self):
        """
        returneaza lista materii de materii de tip materie formata din materile din dictionarul din RepoMaterii
        :return: rez : list - lista de materii de tip materie
        """
        return self.__repo_materii.get_all()

    def cauta_materie(self, id_materie):
        """
        Valideaza id-ul id_materiei si daca e valid il cauta in dictionarul RepoMaterii
        daca il gaseste returneaza materia Materie cu id-ul id_materie
        :param id_materie: int
        :return: rez : Materie - materia Materie cu id-ul __id_materie = id_materie
        :raises: ValidError - cu mesajul "id invalid!\n" daca id-ul e invalid
                 RepoError - cu mesajul "materie inexistent!" daca id-ul id_materie nu apare in RepoMaterii
        """
        self.__validator_materie.valideaza_id_materie(id_materie)
        return self.__repo_materii.cauta_materie(id_materie)



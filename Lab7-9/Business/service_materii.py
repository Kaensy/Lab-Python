from Domain.materie import Materie


class ServiceMaterii:

    def __init__(self, validator_materie, repo_materii):
        self.__validator_materie = validator_materie
        self.__repo_materii = repo_materii

    def adauga_materie(self, id_materie, nume_materie, nume_profesor):
        materie = Materie(id_materie, nume_materie, nume_profesor)
        self.__validator_materie.valideaza(materie)
        self.__repo_materii.adauga_materie(materie)

    def modifica_materie(self, id_materie, nume_materie, nume_profesor):
        materie = Materie(id_materie, nume_materie, nume_profesor)
        self.__validator_materie.valideaza(materie)
        self.__repo_materii.modifica_materie(materie)

    def get_all_materii(self):
        return self.__repo_materii.get_all()



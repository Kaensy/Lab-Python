from Domain.produs import Produs

class ServiceProduse:

    def __init__(self, validator_produs, repo_produse):
        self.__validator_produs = validator_produs
        self.__repo_produse = repo_produse

    def adauga_produs_service(self, id_produs, denumire_produs, pret_produs):
        produs = Produs(id_produs, denumire_produs, pret_produs)
        self.__validator_produs.valideaza(produs)
        self.__repo_produse.adauga_produs(produs)

    def get_all_service(self):
        return self.__repo_produse.get_all()

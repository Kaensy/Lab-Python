from Domain.costum import Costum

class ServiceCostume():
    """
    
    """

    def __init__(self, repo_costume):
        self.__repo_costume = repo_costume

    def adauga_costum_service(self, id_costum, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum):
        """

        :param id_costum:
        :param denumire_costum:
        :param tematica_costum:
        :param pret_costum:
        :param disponibilitate_costum:
        :return:
        """
        costum = Costum(id_costum, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum)
        self.__repo_costume.adauga_costum(costum)

    def get_all_costume(self):
        return self.__repo_costume.get_all()

    def all_costume_tematica_service(self, tematica_costum):
        costume = self.__repo_costume.get_all()
        costume_tematica = []
        for costum in costume:
            if costum.get_tematica_costum() == tematica_costum and costum.get_disponibilitate_costum() == "True":
                costume_tematica.append(costum)
        costume_tematica.sort()
        return costume_tematica

    def cauta_costum(self, id_costum):
        return self.__repo_costume.cauta_costum_dupa_id(id_costum)

    def inchiriere_costum(self, id_costum):
        mesaj = []
        costume = self.__repo_costume.get_all()
        for costum in costume:
            if costum.get_id_costum() == id_costum:
                if costum.get_disponibilitate_costum() == "True":
                    mesaj.append("1")
                    mesaj.append(costum)
                else:
                    mesaj.append("2")
        if not mesaj:
            mesaj.append("3")
        costume.sort()
        mesaj.append(costume[0])
        return mesaj


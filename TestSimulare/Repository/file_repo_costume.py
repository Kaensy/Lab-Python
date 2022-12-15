from Repository.repo_costume import RepoCostume
from Domain.costum import Costum

class FileRepoCostume(RepoCostume):
    """

    """

    def __init__(self, cale_fisier):
        RepoCostume.__init__(self)
        self.__cale_fisier = cale_fisier

    def __real_all_from_file(self):
        with open(self.__cale_fisier, "r") as f:
            lines = f.readlines()
            self._costume.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split(",")
                    id_costum = int(parts[0])
                    denumire_costum = parts[1]
                    tematica_costum = parts[2]
                    pret_costum = int(parts[3])
                    disponibilitate_costum = parts[4]
                    costum = Costum(id_costum,denumire_costum,tematica_costum,pret_costum,disponibilitate_costum)
                    self._costume[id_costum] = costum

    def __write_all_to_file(self):
        with open(self.__cale_fisier, "w") as f:
            for costum in self._costume.values():
                f.write(str(costum)+"\n")

    def adauga_costum(self, costum):
        self.__real_all_from_file()
        RepoCostume.adauga_costum(self, costum)
        self.__write_all_to_file()

    def cauta_costum_dupa_id(self,id_costum):
        self.__real_all_from_file()
        return RepoCostume.cauta_costum_dupa_id(self, id_costum)

    def get_all(self):
        self.__real_all_from_file()
        return RepoCostume.get_all(self)


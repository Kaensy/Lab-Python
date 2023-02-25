from Repository.repo_produse import RepoProduse
from Domain.produs import Produs

class FileRepoProduse(RepoProduse):

    def __init__(self, cale_fisier):
        RepoProduse.__init__(self)
        self.__cale_catre_fisier = cale_fisier

    def __read_all_from_file(self):
        with open(self.__cale_catre_fisier,"r") as f:
            lines = f.readlines()
            self._produse.clear()
            for line in lines:
                line = line.strip()
                if line!="":
                    parts = line.split()
                    id_produs = int(parts[0])
                    denumire_produs = parts[1]
                    pret_produs = int(parts[2])
                    produs = Produs(id_produs,denumire_produs,pret_produs)
                    self._produse[id_produs] = produs

    def __write_all_to_file(self):
        with open(self.__cale_catre_fisier, "w") as f:
            for produs in self._produse.values():
                f.write(str(produs)+"\n")

    def adauga_produs(self, produs):
        self.__read_all_from_file()
        RepoProduse.adauga_produs(self,produs)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoProduse.get_all(self)

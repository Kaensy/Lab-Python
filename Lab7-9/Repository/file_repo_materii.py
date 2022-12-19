from Repository.repo_materii import RepoMaterii
from Domain.materie import Materie


class FileRepoMaterii(RepoMaterii):

    def __init__(self, cale_catre_fisier):
        RepoMaterii.__init__(self)
        self.__cale_catre_fisier = cale_catre_fisier

    def __read_all_from_file(self):
        with open(self.__cale_catre_fisier, "r") as f:
            lines = f.readlines()
            self._materii.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split()
                    id_materie = parts[0]
                    nume_materie = parts[1]
                    nume_profesor = parts[2]
                    materie = Materie(id_materie, nume_materie, nume_profesor)
                    self._materii[id_materie] = materie

    def __write_all_to_file(self):
        with open(self.__cale_catre_fisier, "w") as f:
            for materie in self._materii.values():
                if not materie.get_sters():
                    f.write(str(materie)+"\n")

    def adauga_materie(self, materie):
        self.__read_all_from_file()
        RepoMaterii.adauga_materie(self, materie)
        self.__write_all_to_file()

    def modifica_materie(self,materie):
        self.__read_all_from_file()
        RepoMaterii.modifica_materie(self,materie)
        self.__write_all_to_file()

    def stergere_materie(self, id_materie):
        self.__read_all_from_file()
        RepoMaterii.stergere_materie(self,id_materie)
        self.__write_all_to_file()

    def cauta_materie(self,id_materie):
        self.__read_all_from_file()
        return RepoMaterii.cauta_materie(self,id_materie)

    def get_all(self):
        self.__read_all_from_file()
        return RepoMaterii.get_all(self)

    def size(self):
        self.__read_all_from_file()
        return RepoMaterii.__len__(self)

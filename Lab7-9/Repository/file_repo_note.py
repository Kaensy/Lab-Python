from Repository.repo_note import RepoNote
from Domain.nota_dto import NotaDTO
from Domain.nota import Nota


class FileRepoNote(RepoNote):

    def __init__(self, cale_catre_fisier):
        RepoNote.__init__(self)
        self.__cale_catre_fisier = cale_catre_fisier

    def __read_all_from_file(self):
        with open(self.__cale_catre_fisier, "r") as f:
            lines = f.readlines()
            self._note.clear()
            for line in lines:
                line = line.strip()
                if line != "":
                    parts = line.split()
                    id_nota = parts[0]
                    id_student = parts[1]
                    id_materie = parts[2]
                    valoare_nota = parts[3]
                    nota = Nota(id_nota, id_student, id_materie, valoare_nota)
                    self._note[id_nota] = nota

    def __write_all_to_file(self):
        with open(self.__cale_catre_fisier, "w") as f:
            for nota in self._note.values():
                if not nota.get_sters():
                    f.write(str(nota)+"\n")

    def adauga_nota(self, nota):
        self.__read_all_from_file()
        RepoNote.adauga_nota(self, nota)
        self.__write_all_to_file()

    def sterge_nota(self, id_nota):
        self.__read_all_from_file()
        RepoNote.sterge_nota(self,id_nota)
        self.__write_all_to_file()

    def get_all(self):
        self.__read_all_from_file()
        return RepoNote.get_all(self)

    def size(self):
        self.__read_all_from_file()
        return RepoNote.__len__(self)

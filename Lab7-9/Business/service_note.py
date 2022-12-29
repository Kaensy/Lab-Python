from Domain.sef_promotie_dto import SefPromotieDTO
from Domain.nota import Nota
from Domain.student_nota_dto import StudentNotaDTO


class ServiceNote:
    """
    Clasa ServiceNote contine clasele ValidatorNota, RepoNote, RepoStudenti si RepoMaterii
    """
    def __init__(self, validator_nota, repo_note, repo_studenti, repo_materii):
        self.__validator_nota = validator_nota
        self.__repo_note = repo_note
        self.__repo_studenti = repo_studenti
        self.__repo_materii = repo_materii

    def sterge_student_si_notele_lui(self, id_student):
        """
        sterge studentul cu id-ul id_student si notele corespunzatoare acestuia
        :param id_student: int
        :return: - ( sterge studentul cu id-ul id_student si notele acestuia la toate materile )
        """
        student = self.__repo_studenti.cauta_student(id_student)
        note = self.__repo_note.get_all()
        note_student = [x for x in note if x.get_student() == student]
        for nota_student in note_student:
            self.__repo_note.sterge_nota(nota_student.get_id_nota())
        self.__repo_studenti.sterge_student(id_student)

    def sterge_materie_si_note(self, id_materie):
        """
        sterge materia cu id_ul id_materie si notele corespunzatoare acesteia
        :param id_materie: int
        :return: - ( sterge materia de id id_materie si toate notele acesteia )
        """
        materie = self.__repo_materii.cauta_materie(id_materie)
        note = self.__repo_note.get_all()
        note_materie = [x for x in note if x.get_materie() == materie]
        for nota_materie in note_materie:
            self.__repo_note.sterge_nota(nota_materie.get_id_nota())
        self.__repo_materii.stergere_materie(id_materie)


    def get_sefi_promotie(self):
        """
        creeaza un dictionar de studenti cu toate notele acestuia
        creeaza o lista de obiecte de tip SefPromotieDTO formata din numele unui student impreuna cu media acestuia
        ordoneaza descrescator lista si returneaza primi 20%
        :return: rez - list ( primele 20% elemente din lista ordonata descrescator a studentilor dupa medie )
        """
        info_studenti = {}
        note = self.__repo_note.get_all()
        for nota in note:
            id_student_nota = nota.get_student()
            valoare_nota = nota.get_nota()
            if id_student_nota not in info_studenti:
                info_studenti[id_student_nota] = []
            info_studenti[id_student_nota].append(valoare_nota)
        sefi_promotie = []
        for id_student in info_studenti:
            student = self.__repo_studenti.cauta_student(id_student)
            nume_student = student.getNume()
            medie_student = sum(info_studenti[id_student])/len(info_studenti[id_student])
            sef_promotie_dto = SefPromotieDTO(nume_student, medie_student)
            sefi_promotie.append(sef_promotie_dto)
        sefi_promotie.sort(reverse=True)
        nr = int(len(sefi_promotie)/5)
        if not nr:
            return sefi_promotie[:1]
        else:
            return sefi_promotie[:nr]

    def asignare_nota(self, id_nota, id_student, id_materie, valoare_nota):
        """
        creeaza o nota de tip Nota cu id-ul id_nota, studentul de tip Student cu id_ul id_student, materia de
        tip Materie cu id-ul id_materie si valoarea int a note valoare_nota
        :param id_nota: int
        :param id_student: int
        :param id_materie: int
        :param valoare_nota: float
        :return: - ( RepoNote' = RepoNote U Nota )
        """
        nota = Nota(id_nota, self.__repo_studenti.cauta_student(id_student), self.__repo_materii.cauta_materie(id_materie), valoare_nota)
        self.__validator_nota.valideaza(nota)
        self.__repo_note.adauga_nota(nota)

    def get_all_note(self):
        """
        returneaza lista de note de tip Nota din RepoNote
        :return: rez = list ( lista de note de tip Nota )
        """
        return self.__repo_note.get_all()

    def lista_studenti_note(self, id_materie):
        """
        creeaza un dictionar de studenti cu notele acestuia la materia Materie cu id-ul id_materie
        creeaza o lista de obiecte de tip student_nota_dto formata din numele unui student impreuna cu nota acestuia
        ordoneaza alfabetic si dupa descrescator dupa note si returneaza lista
        :param id_materie: int
        :return: rez - list ( lista ordonata alfabetic si descrescator dupa note a studentilor cu note la materia Materie id_materie )
        """
        lista_studenti_note = {}
        note = self.__repo_note.get_all()
        for nota in note:
            materie = nota.get_materie()
            if id_materie == materie.get_id_materie():
                lista_studenti_note[nota.get_id_nota()] = nota
        lista_studenti = []
        for nota in lista_studenti_note.values():
            nume_student = nota.get_student().getNume()
            nota_student = nota.get_nota()
            student_dto = StudentNotaDTO(nume_student, nota_student)
            lista_studenti.append(student_dto)
        lista_studenti.sort()
        return lista_studenti

    def nota_frecventa_minima(self):
        lista_note = {}
        note = self.__repo_note.get_all()
        for nota in note:
            valoare_nota = nota.get_nota()
            if valoare_nota not in lista_note:
                lista_note[valoare_nota] = 0
            lista_note[valoare_nota] += 1
        lista_note = sorted(lista_note.items(),key=lambda x:x[1])
        return lista_note[0]

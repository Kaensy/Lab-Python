from Domain.student import Student
import random


class ServiceStudenti:
    """
    Clasa ServiceStudenti contine clasele ValidatorStudent si RepoStudenti
    """
    def __init__(self, validator_student, repo_studenti):
        self.__validator_student = validator_student
        self.__repo_studenti = repo_studenti

    def adauga_student(self, id_student, nume):
        """
        Construieste studentul de tip Student cu id-ul unic id_student si numele nume
        Valideaza studentul student si daca e valid il adauga in RepoStudenti doar daca acesta nu apare deja in RepoStudenti
        :param id_student: int
        :param nume: string
        :return: - ( RepoStudenti' = RepoStudenti U student daca validarea si adaugarea se fac cu succes
        :raises: ValidError - cu mesajele de validare daca studentul creat e invalid
                 RepoError - cu mesajul "student existent!" daca studentul apare deja in RepoStudenti
        """
        student = Student(id_student, nume)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.adauga_student(student, )

    def modifica_student(self, id_student, nume):
        """
        Construieste studentul de tip Student cu id-ul unic id_student si numele nume
        Valideaza studentul student si daca e valid cauta studentul cu id id_student din RepoStudenti si il modifica cu noul Student creat
        :param id_student: int
        :param nume: string
        :return: - ( studentul cu id-ul id_student se va schimba in noul student cu id-ul id_student si numele nume )
        :raises: ValidError - cu mesajele de validare daca studentul creat e invalid
                 RepoError - cu mesajul "student inexistent!" daca studentul nu apare in RepoStudenti
        """
        student = Student(id_student, nume)
        self.__validator_student.valideaza(student)
        self.__repo_studenti.modifica_student(student)

    def get_all_studenti(self):
        """
        returneaza lista studenti de studenti de tip student formata din studentii din dictionarul din RepoStudenti
        :return: rez : list - lista de studenti de tip student
        """
        return self.__repo_studenti.get_all()

    def cauta_student(self, id_student):
        """
        Valideaza id-ul id_student si daca e valid il cauta in dictionarul RepoStudenti si daca il gaseste il returneaza
        :param id_student: int
        :return: rez : Student - studentul Student cu id-ul __id_student = id_student
        :raises: ValidError - cu mesajul "id invalid!\n" daca id-ul e invalid
                 RepoError - cu mesajul "student inexistent!" daca id-ul id_student nu apare in RepoStudenti
        """
        self.__validator_student.valideaza_id_student(id_student)
        return self.__repo_studenti.cauta_student(id_student)

    def adaugare_studenti_random(self, times):
        """
        adauga times nr de studenti cu id id_student random si nume nume_student random in dictionarul RepoStudenti
        :param times: int
        :return: - ( adauga times studenti in RepoStudenti )
        """
        for d in range(times):
            while True:
                id = random.randint(0, 100+times+len(self.get_all_studenti()))
                nume_student = ""
                nr_lit = random.randint(5, 16)
                for i in range(nr_lit):
                    nume_student += chr(random.randint(67, 122))
                try:
                    self.adauga_student(id, nume_student)
                    break
                except:
                    pass

    def adaugare_studenti_random_recursiv(self, times):
        """
        adauga times studenti cu id id_student random si nume nume_student random in dictionarul RepoStudenti
        :param times: int
        :return: - ( adauga student random in RepoStudenti si apeleaza functia de times-1 daca times > 0)
        """

        if times:
            self.adaugare_studenti_random_recursiv(int(times-1))
            id = random.randint(0, 100+times+len(self.get_all_studenti()))
            nume_student = ""
            nr_lit = random.randint(5, 16)
            for i in range(nr_lit):
                nume_student += chr(random.randint(67, 122))
            try:
                self.adauga_student(id, nume_student)
            except:
                self.adaugare_studenti_random_recursiv(1)
        return
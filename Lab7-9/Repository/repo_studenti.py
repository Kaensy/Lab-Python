from Erori.repo_error import RepoError
import random


class RepoStudenti:
    """
    Clasa RepoStudenti care contine un dictionar de studenti de tip Student
    """
    def __init__(self):
        self.__studenti = {}

    def adauga_student(self, student):
        """
        Incearca adaugarea studentului student in dictionarul __studenti daca  id-ul acestuia nu apare
        deja in dictionar sau daca apare dar este sters
        :param student: student
        :return: - ( studentul student este adaugat in dictionar )
        :raises : RepoError cu mesajul "student existent" - daca id_ul studentului student apare in dictionar
        """
        if student.getID_student() in self.__studenti and self.__studenti[student.getID_student()].get_sters()==False:
            raise RepoError("student existent!")
        self.__studenti[student.getID_student()] = student

    def sterge_student(self, id_student):
        """
        Verifica daca id-ul id_student se afla in dictionarul de studentu
        Daca se afla studentul se marcheaza ca find sters
        Daca nu gaseste id-ul va tipari mesaj eroare corespunzator
        :param id_student: int
        :return: - ( studentul cu id id_student din dictionar este marchat ca si sters )
        :raises: RepoError cu mesajul "student inexistent!" - daca id-ul nu se afla in dictionar
        """
        if id_student not in self.__studenti or self.__studenti[id_student].get_sters()==True:
            raise RepoError("student inexistent!")
        self.__studenti[id_student].sterge()

    def cauta_student(self, id_student):
        """
        Cauta id-ul unic id_student in dictionar
        Daca nu il gaseste va tipari mesaj "student inexistent"
        Daca il gaseste returneaza studentul Student
        :param id_student: int
        :return: rez : Student - ( studentul cu id id_student din dictionar )
        :raises: RepoError cu mesajul "student inexistent" - daca id_student nu se afla in lista
        """
        if id_student not in self.__studenti or self.__studenti[id_student].get_sters():
            raise RepoError("student inexistent!")
        return self.__studenti[id_student]

    def modifica_student(self, student):
        """
        Verifica daca id-ul unic al studentului student se afla in dictionarul de studenti
        Daca se afla atunci studentul cu id-ul studentului student se modifica cu elem studentului student
        Daca nu se afla tipareste mesaj "student inexistent!"
        :param student: student
        :return: - ( studentul cu id-ul studentului student se schimba in studentul student )
        :raises: RepoError : "student inexistent"
        """
        if student.getID_student() not in self.__studenti or self.__studenti[student.getID_student()].get_sters()==True:
            raise RepoError("student inexistent!")
        self.__studenti[student.getID_student()] = student

    def get_all(self):
        """
        returneaza lista studenti de studenti de tip student formata din studentii din dictionar
        :return: rez : list - lista de studenti de tip student
        """
        studenti = []
        for student_id in self.__studenti:
            if not self.__studenti[student_id].get_sters():
                studenti.append(str(self.__studenti[student_id]))
        return studenti

    def __len__(self):
        nr = 0
        for student in self.__studenti:
            if not self.__studenti[student].get_sters():
                nr += 1
        return nr

from Erori.repo_error import RepoError


class RepoStudenti:

    def __init__(self):
        self.__studenti = {}

    def adauga_student(self, student):
        if student.getID_student() in self.__studenti and self.__studenti[student.getID_student()].get_sters()==False:
            raise RepoError("student existent!")
        self.__studenti[student.getID_student()] = student

    def sterge_student(self, id_student):
        if id_student not in self.__studenti or self.__studenti[id_student].get_sters()==True:
            raise RepoError("student inexistent!")
        self.__studenti[id_student].sterge()

    def cauta_student(self, id_student):
        if id_student not in self.__studenti:
            raise RepoError("student inexistent!")
        return self.__studenti[id_student]

    def modifica_student(self, student):
        if student.getID_student() not in self.__studenti or self.__studenti[student.getID_student()].get_sters()==True:
            raise RepoError("student inexistent!")
        self.__studenti[student.getID_student()] = student

    def get_all(self):
        studenti = []
        for student_id in self.__studenti:
            if not self.__studenti[student_id].get_sters():
                studenti.append(self.__studenti[student_id])
        return studenti

    def __len__(self):
        nr = 0
        for student in self.__studenti:
            if not self.__studenti[student].get_sters():
                nr += 1
        return nr

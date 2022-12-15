from Domain.student import Student
from Repository.file_repo_studenti import FileRepoStudenti

class TesteFileRepo:

    def __init__(self):
        pass

    def __goleste_fisier(self, cale_fisier):
        with open(cale_fisier, "w") as f:
            pass

    def run_all_tests(self):
        self.__run_repo_tests()
        print("file_repo tests trecute cu success ")

    def __run_repo_tests(self):
        cale_fisier = "Teste/test_studenti.txt"
        self.__goleste_fisier(cale_fisier)
        repo = FileRepoStudenti(cale_fisier)
        assert repo.size() == 0
        student = Student(1, "Lau")
        repo.adauga_student(student)
        assert repo.size() == 1


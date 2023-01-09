from Validator.validator_student import ValidatorStudent
from Validator.validator_materie import ValidatorMaterie
from Validator.validator_nota import ValidatorNota
from Repository.file_repo_studenti import FileRepoStudenti
from Repository.file_repo_materii import FileRepoMaterii
from Repository.file_repo_note import FileRepoNote
from Business.service_studenti import ServiceStudenti
from Business.service_materii import ServiceMaterii
from Business.service_note import ServiceNote
from Domain.student import Student
from Domain.materie import Materie
from Domain.nota import Nota
from Domain.nota_dto import NotaDTO
from Erori.validation_error import ValidError
from Erori.repo_error import RepoError


class Teste:

    def __init__(self):
        pass

    def __goleste_fisier(self, cale_fisier):
        with open(cale_fisier, "w") as f:
            pass

    def teste_domain(self):
        id = 1
        nume = "Didi"
        self.__student1 = Student(id, nume)
        assert (self.__student1.getID_student() == id)
        assert (self.__student1.getNume() == nume)
        nume_altul = "Altul"
        self.__student1.setNume(nume_altul)
        assert (self.__student1.getNume() == nume_altul)

        nume_materie = "Mate"
        nume_profesor = "Matei"
        self.__materie1 = Materie(id, nume_materie, nume_profesor)
        assert (self.__materie1.get_id_materie() == id)
        assert (self.__materie1.get_nume_materie() == nume_materie)
        assert (self.__materie1.get_nume_profesor() == nume_profesor)
        nume_materie_alta = "Algebra"
        self.__materie1.set_nume_materie(nume_materie_alta)
        assert (self.__materie1.get_nume_materie() == nume_materie_alta)
        nume_profesor_altul = "Altul"
        self.__materie1.set_nume_profesor(nume_profesor_altul)
        assert (self.__materie1.get_nume_profesor() == nume_profesor_altul)
        nota = 10
        self.__nota1 = Nota(id, self.__student1.getID_student(), self.__materie1.get_id_materie(), nota)
        assert (self.__nota1.get_nota() == nota)
        assert (self.__nota1.get_id_nota() == id)
        assert (self.__nota1.get_id_student() == self.__student1.getID_student())
        assert (self.__nota1.get_id_materie() == self.__materie1.get_id_materie())
        nota_alta = 9
        self.__nota1.set_nota(nota_alta)
        assert (self.__nota1.get_nota() == nota_alta)

    def teste_validare(self):
        id_invalid = -5
        nume_invalid = ""
        self.__studentinvalid = Student(id_invalid, nume_invalid)
        ValidatorStudent.valideaza(ValidatorStudent, self.__student1)
        try:
            ValidatorStudent.valideaza(ValidatorStudent, self.__studentinvalid)
            assert False
        except ValidError as ve:
            assert(str(ve) == "id invalid!\nnume invalid!\n")

        ValidatorMaterie.valideaza(ValidatorMaterie, self.__materie1)
        self.__materieinvalida = Materie(id_invalid, nume_invalid, nume_invalid)
        try:
            ValidatorMaterie.valideaza(ValidatorStudent, self.__materieinvalida)
            assert False
        except ValidError as ve:
            assert (str(ve) == "id invalid!\nnume materie invalid!\nnume profesor invalid!\n")

        nota_invalida = 15
        self.__notainvalida = Nota(id_invalid, self.__student1.getID_student(), self.__materie1.get_id_materie(), nota_invalida)
        ValidatorNota.valideaza(ValidatorNota, self.__nota1)
        try:
            ValidatorNota.valideaza(ValidatorNota, self.__notainvalida)
            assert False
        except ValidError as ve:
            assert (str(ve) == "id invalid!\nnota invalida!\n")

    def teste_repo(self):
        student_unu = Student(1, "Gabi")
        student_modifica = Student(1, "Lau")
        student_modifica_invalid = Student(2, "Lau")
        cale_fisier_studenti = "Teste/test_studenti.txt"
        repo_studenti = FileRepoStudenti(cale_fisier_studenti)
        self.__goleste_fisier(cale_fisier_studenti)
        assert (repo_studenti.__len__() == 0)
        repo_studenti.adauga_student(student_unu)
        assert (repo_studenti.__len__() == 1)
        assert (repo_studenti.get_all()[0].__str__() == "1 Gabi")
        student_invalid = Student(1, "Lau")
        try:
            repo_studenti.adauga_student(student_invalid)
            assert False
        except RepoError as re:
            assert (str(re) == "student existent!")
        try:
            repo_studenti.modifica_student(student_modifica_invalid)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        try:
            repo_studenti.sterge_student(2)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        assert (repo_studenti.cauta_student(1) == student_unu)
        try:
            repo_studenti.cauta_student(2)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        repo_studenti.modifica_student(student_modifica)
        assert (repo_studenti.cauta_student(1) == student_modifica)
        repo_studenti.sterge_student(1)
        assert (repo_studenti.__len__() == 0)

        materie_unu = Materie(1, "Mate", "Matei")
        materie_modificare = Materie(1, "Algebra", "Altcineva")
        materie_modificare_invalida = Materie(2, "Algebra", "Altcineva")
        cale_fisier_materii = "Teste/test_materii.txt"
        repo_materii = FileRepoMaterii(cale_fisier_materii)
        self.__goleste_fisier(cale_fisier_materii)
        assert (repo_materii.__len__() == 0)
        repo_materii.adauga_materie(materie_unu)
        assert (repo_materii.__len__() == 1)
        assert (repo_materii.get_all()[0].__str__() == "1 Mate Matei")
        try:
            repo_materii.adauga_materie(materie_modificare)
            assert False
        except RepoError as re:
            assert (str(re) == "materie existenta!")
        materie_invalida = Materie(1, "Mate", "Altul")
        try:
            repo_materii.modifica_materie(materie_modificare_invalida)
            assert False
        except RepoError as re:
            assert (str(re) == "materie inexistenta!")
        repo_materii.modifica_materie(materie_modificare)
        assert (repo_materii.cauta_materie(1) == materie_modificare)
        try:
            repo_materii.stergere_materie(2)
            assert False
        except RepoError as re:
            assert (str(re) == "materie inexistenta!")
        try:
            repo_materii.adauga_materie(materie_invalida)
            assert False
        except RepoError as re:
            assert (str(re) == "materie existenta!")
        repo_materii.stergere_materie(1)
        assert (repo_materii.__len__() == 0)


        cale_fisier_note = "Teste/test_note.txt"
        repo_note = FileRepoNote(cale_fisier_note)
        self.__goleste_fisier(cale_fisier_note)
        repo_studenti.adauga_student(student_unu)
        repo_materii.adauga_materie(materie_unu)
        nota_unu = NotaDTO(1, student_unu.getID_student(), materie_unu.get_id_materie(), 9.0)
        assert (len(repo_note.get_all()) == 0)
        repo_note.adauga_nota(nota_unu)
        assert (len(repo_note.get_all()) == 1)
        try:
            repo_note.adauga_nota(nota_unu)
            assert False
        except RepoError as re:
            assert (str(re) == "nota existenta!")

        assert(str(repo_note.get_all()[0]) == str(nota_unu))

        repo_note.sterge_nota(1)
        assert (len(repo_note.get_all()) == 0)
        try:
            repo_note.sterge_nota(1)
            assert False
        except RepoError as re:
            assert (str(re) == "nota inexistenta!")


    def teste_service(self):
        validatorstudent = ValidatorStudent()
        cale_fisier_studenti = "Teste/test_studenti.txt"
        self.__goleste_fisier(cale_fisier_studenti)
        repostudenti = FileRepoStudenti(cale_fisier_studenti)
        service_studenti = ServiceStudenti(validatorstudent,repostudenti)
        student_unu = Student(1, "Lau")
        student_modificat = Student(1, "Didi")
        assert(len(service_studenti.get_all_studenti())==0)
        service_studenti.adauga_student(1, "Lau")
        assert (service_studenti.cauta_student(1) == student_unu)
        assert (len(service_studenti.get_all_studenti()) == 1)
        service_studenti.modifica_student(1,"Didi")
        assert (service_studenti.cauta_student(1) == student_modificat)
        try:
            service_studenti.modifica_student(2, "Cineva")
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        try:
            service_studenti.adauga_student(1, "Lau")
            assert False
        except RepoError as re:
            assert (str(re) == "student existent!")

        validatormaterie = ValidatorMaterie()
        cale_fisier_materii = "Teste/test_materii.txt"
        self.__goleste_fisier(cale_fisier_materii)
        repomaterii = FileRepoMaterii(cale_fisier_materii)
        service_materii = ServiceMaterii(validatormaterie, repomaterii)
        materie_unu = Materie(1, "Mate", "Matei")
        materie_modificata = Materie(1, "Algebra", "Altul")
        assert (len(service_materii.get_all_materii()) == 0)
        service_materii.adauga_materie(1, "Mate", "Matei")
        assert(service_materii.cauta_materie(1) == materie_unu)
        assert (len(service_materii.get_all_materii()) == 1)
        service_materii.modifica_materie(1, "Algebra" , "Altul")
        assert (service_materii.cauta_materie(1) == materie_modificata)
        try:
            service_materii.modifica_materie(2, "a", "a")
            assert False
        except RepoError as re:
            assert (str(re) == "materie inexistenta!")
        try:
            service_materii.adauga_materie(1, "AltaMaterie", "AltNume")
            assert False
        except RepoError as re:
            assert (str(re) == "materie existenta!")

        validatornota = ValidatorNota()
        cale_fisier_note = "Teste/test_note.txt"
        self.__goleste_fisier(cale_fisier_note)
        reponote = FileRepoNote(cale_fisier_note)
        service_note = ServiceNote(validatornota, reponote, repostudenti, repomaterii)
        assert (len(service_note.get_all_note()) == 0)
        service_note.asignare_nota(1,1,1,10)
        try:
            service_note.asignare_nota(1,1,1,10)
            assert False
        except RepoError as re:
            assert (str(re) == "nota existenta!")
        assert(len(service_note.get_all_note()))
        assert(service_note.get_sefi_promotie()[0].__str__() == "studentul Didi cu media 10.0")
        assert(service_note.lista_studenti_note_descresc(1)[0].__str__() == "Studentul Didi cu nota 10.0")
        service_note.sterge_student_si_notele_lui(1)
        assert (len(service_studenti.get_all_studenti()) == 0)
        try:
            service_note.sterge_student_si_notele_lui(1)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        try:
            service_studenti.cauta_student(1)
            assert False
        except RepoError as re:
            assert (str(re) == "student inexistent!")
        service_note.sterge_materie_si_note(1)
        assert (len(service_materii.get_all_materii()) == 0)
        try:
            service_note.sterge_materie_si_note(1)
            assert False
        except RepoError as re:
            assert (str(re) == "materie inexistenta!")
        try:
            service_materii.cauta_materie(1)
            assert False
        except RepoError as re:
            assert (str(re) == "materie inexistenta!")

        assert (len(service_studenti.get_all_studenti()) == 0)
        service_studenti.adaugare_studenti_random(20)
        assert (len(service_studenti.get_all_studenti()) == 20)
        service_studenti.adaugare_studenti_random_recursiv(20)
        assert (len(service_studenti.get_all_studenti()) == 40)

        assert (len(service_materii.get_all_materii()) == 0)
        service_materii.adaugare_materii_random(20)
        assert (len(service_materii.get_all_materii()) == 20)
        service_materii.adaugare_materii_random_recursiv(20)
        assert (len(service_materii.get_all_materii()) == 40)

    def run(self):
        self.teste_domain()
        print("Ruleaza teste domain cu succes")
        self.teste_validare()
        print("Ruleaza teste validator cu succes")
        self.teste_repo()
        print("Ruleaza teste repo cu succes")
        self.teste_service()
        print("Ruleaza teste service cu succes")
from Validator.validator_student import ValidatorStudent
from Validator.validator_materie import ValidatorMaterie
from Validator.validator_nota import ValidatorNota
from Repository.repo_studenti import RepoStudenti
from Repository.repo_materii import RepoMaterii
from Repository.repo_note import RepoNote
from Business.service_studenti import ServiceStudenti
from Business.service_materii import ServiceMaterii
from Business.service_note import ServiceNote
from Domain.student import Student
from Domain.materie import Materie
from Domain.nota import Nota
from Erori.validation_error import ValidError
from Erori.repo_error import RepoError
class Teste:

    def __init__(self):
        pass

    def teste_domain(self):
        id = 1
        nume = "Didi"
        self.__student1 = Student(id, nume)
        assert (self.__student1.getID_student() == id)
        assert (self.__student1.getNume() == nume)
        assert (not self.__student1.get_sters())
        nume_altul = "Altul"
        self.__student1.setNume(nume_altul)
        assert (self.__student1.getNume() == nume_altul)
        self.__student1.sterge()
        assert (self.__student1.get_sters())

        nume_materie = "Mate"
        nume_profesor = "Matei"
        self.__materie1 = Materie(id, nume_materie, nume_profesor)
        assert (self.__materie1.get_id_materie() == id)
        assert (self.__materie1.get_nume_materie() == nume_materie)
        assert (self.__materie1.get_nume_profesor() == nume_profesor)
        assert (not self.__materie1.get_sters())
        nume_materie_alta = "Algebra"
        self.__materie1.set_nume_materie(nume_materie_alta)
        assert (self.__materie1.get_nume_materie() == nume_materie_alta)
        nume_profesor_altul = "Altul"
        self.__materie1.set_nume_profesor(nume_profesor_altul)
        assert (self.__materie1.get_nume_profesor() == nume_profesor_altul)
        self.__materie1.sterge()
        assert (self.__materie1.get_sters())

        nota = 10
        self.__nota1 = Nota(id, self.__student1, self.__materie1, nota)
        assert (self.__nota1.get_nota() == nota)
        assert (self.__nota1.get_id_nota() == id)
        assert (self.__nota1.get_student() == self.__student1)
        assert (self.__nota1.get_materie() == self.__materie1)
        assert (not self.__nota1.get_sters())
        nota_alta = 9
        self.__nota1.set_nota(nota_alta)
        assert (self.__nota1.get_nota() == nota_alta)
        self.__nota1.sterge()
        assert (self.__nota1.get_sters())

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
        self.__notainvalida = Nota(id_invalid, self.__student1, self.__materie1, nota_invalida)
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
        repo_studenti = RepoStudenti()
        assert (repo_studenti.__len__() == 0)
        repo_studenti.adauga_student(student_unu)
        assert (repo_studenti.__len__() == 1)
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
        repo_materii = RepoMaterii()
        assert (repo_materii.__len__() == 0)
        repo_materii.adauga_materie(materie_unu)
        assert (repo_materii.__len__() == 1)
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
            assert (str(re) == "materie inexistenta")
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

    def teste_service(self):
        validatorstudent = ValidatorStudent()
        repostudenti = RepoStudenti()
        service_studenti = ServiceStudenti(validatorstudent,repostudenti)
        assert(len(service_studenti.get_all_studenti())==0)
        service_studenti.adauga_student(1, "Lau")
        assert (len(service_studenti.get_all_studenti()) == 1)
        service_studenti.modifica_student(1,"Didi")
        try:
            service_studenti.adauga_student(1,"Lau")
            assert False
        except RepoError as re:
            assert (str(re) == "student existent!")

        validatormaterie = ValidatorMaterie()
        repomaterii = RepoMaterii()
        service_materii = ServiceMaterii(validatormaterie, repomaterii)
        assert (len(service_materii.get_all_materii()) == 0)
        service_materii.adauga_materie(1, "Mate", "Matei")
        assert (len(service_materii.get_all_materii()) == 1)
        service_materii.modifica_materie(1, "Algebra" , "Altul")

        validatornota = ValidatorNota()
        reponote = RepoNote()
        service_note = ServiceNote(validatornota, reponote, repostudenti, repomaterii)


    def run(self):
        self.teste_domain()
        print("Ruleaza teste domain cu succes")
        self.teste_validare()
        print("Ruleaza teste validator cu succes")
        self.teste_repo()
        print("Ruleaza teste repo cu succes")
        self.teste_service()
        print("Ruleaza teste service cu succes")
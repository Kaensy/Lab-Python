import unittest
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
from Erori.validation_error import ValidError
from Erori.repo_error import RepoError

class UnitTestDomainTests(unittest.TestCase):

    def setUp(self):
        self.student_valid = Student(1, "Lau")
        self.student_valid_altul = Student(2, "Dragos")
        self.student_acelasi_id = Student(1, "Didi")
        self.student_invalid = Student(-1, "")

        self.materie_valida = Materie(1, "Mate" , "Prof")
        self.materie_valida_alta = Materie(2, "Info", "Mugurel")
        self.materie_acelasi_id = Materie(1, "Romana", "AltProf" )
        self.materie_invalida = Materie(-1, "", "")

        self.nota_valida = Nota(1, 1, 1, 9.0)
        self.nota_valida_alta = Nota(2, 2, 2, 7.0)
        self.nota_acelasi_id = Nota(1, 1, 1, 5.0)
        self.nota_invalida = Nota(-1, -2, -3, 11)

    def tearDown(self):
        pass

    def test_student(self):
        self.assertEqual(self.student_valid.getID_student(), 1)
        self.assertEqual(self.student_valid.getNume(), "Lau")

        self.assertEqual(self.student_valid, self.student_acelasi_id)
        self.assertNotEqual(self.student_valid, self.student_valid_altul)
        self.assertEqual(str(self.student_valid), "1 Lau")

        self.student_valid.setNume("Didi")
        self.assertEqual(self.student_valid.getNume(), "Didi")

    def test_materie(self):
        self.assertEqual(self.materie_valida.get_id_materie(),1)
        self.assertEqual(self.materie_valida.get_nume_materie(), "Mate")
        self.assertEqual(self.materie_valida.get_nume_profesor(), "Prof")

        self.assertEqual(self.materie_valida, self.materie_acelasi_id)
        self.assertNotEqual(self.materie_valida, self.materie_valida_alta)
        self.assertEqual(str(self.materie_valida), "1 Mate Prof")

        self.materie_valida.set_nume_materie("AltNumeMaterie")
        self.materie_valida.set_nume_profesor("AltNumeProf")
        self.assertEqual(self.materie_valida.get_nume_materie(), "AltNumeMaterie")
        self.assertEqual(self.materie_valida.get_nume_profesor(), "AltNumeProf")

    def test_nota(self):
        self.assertEqual(self.nota_valida.get_id_nota(), 1)
        self.assertEqual(self.nota_valida.get_id_student(), 1)
        self.assertEqual(self.nota_valida.get_id_materie(), 1)
        self.assertEqual(self.nota_valida.get_nota(), 9.0)

        self.assertEqual(self.nota_valida, self.nota_acelasi_id)
        self.assertNotEqual(self.nota_valida, self.nota_valida_alta)
        self.assertEqual(str(self.nota_valida), "1 1 1 9.0")

        self.nota_valida.set_nota(8.0)
        self.assertEqual(self.nota_valida.get_nota(), 8.0)

    def test_validators(self):
        ValidatorStudent.valideaza(ValidatorStudent(), self.student_valid)
        ValidatorStudent.valideaza_id_student(ValidatorStudent(), 1)
        self.assertRaisesRegex(ValidError, "id invalid!\nnume invalid!\n" ,ValidatorStudent.valideaza, ValidatorStudent, self.student_invalid)
        self.assertRaisesRegex(ValidError, "id invalid!\n" ,ValidatorStudent.valideaza_id_student, ValidatorStudent, self.student_invalid.getID_student())

        ValidatorMaterie.valideaza(ValidatorMaterie(), self.materie_valida)
        ValidatorMaterie.valideaza_id_materie(ValidatorMaterie(), 1)
        with self.assertRaisesRegex(ValidError,"id invalid!\nnume materie invalid!\nnume profesor invalid!\n"):
            ValidatorMaterie.valideaza(ValidatorMaterie(), self.materie_invalida)
        with self.assertRaisesRegex(ValidError,"id invalid"):
            ValidatorMaterie.valideaza_id_materie(ValidatorMaterie(), self.materie_invalida.get_id_materie())

        ValidatorNota.valideaza(ValidatorNota(), self.nota_valida)
        with self.assertRaisesRegex(ValidError, "id invalid!\nid student invalid!\nid materie invalid!\nnota invalida!\n"):
            ValidatorNota.valideaza(ValidatorNota(), self.nota_invalida)

class UnitTestRepoTests(unittest.TestCase):

    def setUp(self):
        self.student_1 = Student(1, "Lau")
        self.student_2 = Student(2, "Dragos")
        self.student_3 = Student(3, "Raja")
        self.student_4 = Student(4, "David")
        self.student_5 = Student(5, "Philip")
        self.student_invalid = Student(-1, "")
        self.student_acelasi_id = Student(1, "Didi")
        self.cale_fisier_studenti = "test_studenti.txt"
        self.repo_studenti = FileRepoStudenti(self.cale_fisier_studenti)
        self.validatorstudent = ValidatorStudent()
        self.service_studenti = ServiceStudenti(self.validatorstudent, self.repo_studenti)

        self.materie_1 = Materie(1, "Mate" , "Prof")
        self.materie_2 = Materie(2, "Info", "Mugurel")
        self.materie_3 = Materie(3, "Romana", "Varga")
        self.materie_invalida = Materie(-2, "", "")
        self.materie_acelasi_id = Materie(1, "NuConteaza", "AltProf" )
        self.cale_fisier_materii = "test_materii.txt"
        self.repo_materii = FileRepoMaterii(self.cale_fisier_materii)
        self.validatormaterie = ValidatorMaterie()
        self.service_materii = ServiceMaterii(self.validatormaterie, self.repo_materii)

        self.nota_1 = Nota(1, 1, 1, 9.4)
        self.nota_2 = Nota(2, 2, 2, 5.3)
        self.nota_3 = Nota(3, 3, 3, 7.2)
        self.nota_4 = Nota(4, 1, 2, 9.9)
        self.nota_5 = Nota(5, 2, 2, 6.9)
        self.nota_6 = Nota(6, 3, 1, 7.2)
        self.nota_7 = Nota(7, 4, 2, 9.4)
        self.nota_8 = Nota(8, 5, 1, 4.4)
        self.nota_invalida = Nota(-3, -4, -5, 12)
        self.nota_acelasi_id = Nota(1, 1, 1, 5.0)
        self.cale_fisier_note = "test_note.txt"
        self.repo_note = FileRepoNote(self.cale_fisier_note)
        self.validatornote = ValidatorNota()
        self.service_note = ServiceNote(self.validatornote, self.repo_note, self.repo_studenti, self.repo_materii)

    def tearDown(self):
        with open(self.cale_fisier_studenti, "w") as f:
            pass
        with open(self.cale_fisier_materii, "w") as f:
            pass
        with open(self.cale_fisier_note, "w") as f:
            pass

    def test_repo_studenti(self):
        self.assertEqual(self.repo_studenti.__len__(), 0)
        self.assertEqual(self.repo_studenti.size(), 0)
        self.repo_studenti.adauga_student(self.student_1)
        self.assertEqual(self.repo_studenti.__len__(), 1)
        self.assertEqual(self.repo_studenti.size(), 1)
        with self.assertRaisesRegex(RepoError, "student existent!"):
            self.repo_studenti.adauga_student(self.student_acelasi_id)
        self.repo_studenti.adauga_student(self.student_2)
        self.repo_studenti.adauga_student(self.student_3)
        self.assertEqual(self.repo_studenti.__len__(), 3)
        self.assertEqual(self.repo_studenti.size(), 3)
        self.assertEqual(self.repo_studenti.cauta_student(1), self.student_1)
        self.repo_studenti.modifica_student(self.student_acelasi_id)
        self.assertEqual(str(self.repo_studenti.cauta_student(1)), str(self.student_acelasi_id))
        self.assertEqual(str(self.repo_studenti.get_all()[0]), str(self.repo_studenti.cauta_student(1)))
        self.assertEqual(str(self.repo_studenti.get_all()[1]), str(self.repo_studenti.cauta_student(2)))
        self.assertEqual(str(self.repo_studenti.get_all()[2]), str(self.repo_studenti.cauta_student(3)))
        self.repo_studenti.sterge_student(self.student_1.getID_student())
        self.assertEqual(self.repo_studenti.__len__(), 2)
        with self.assertRaisesRegex(RepoError, "student inexistent!"):
            self.repo_studenti.sterge_student(self.student_1.getID_student())

    def test_repo_materii(self):
        self.assertEqual(self.repo_materii.__len__(), 0)
        self.assertEqual(self.repo_materii.size(), 0)
        self.repo_materii.adauga_materie(self.materie_1)
        self.assertEqual(self.repo_materii.__len__(), 1)
        self.assertEqual(self.repo_materii.size(), 1)
        with self.assertRaisesRegex(RepoError, "materie existenta!"):
            self.repo_materii.adauga_materie(self.materie_acelasi_id)
        self.repo_materii.adauga_materie(self.materie_2)
        self.repo_materii.adauga_materie(self.materie_3)
        self.assertEqual(self.repo_materii.__len__(), 3)
        self.assertEqual(self.repo_materii.size(), 3)
        self.assertEqual(self.repo_materii.cauta_materie(1), self.materie_1)
        self.repo_materii.modifica_materie(self.materie_acelasi_id)
        self.assertEqual(str(self.repo_materii.cauta_materie(1)), str(self.materie_acelasi_id))
        self.assertEqual(str(self.repo_materii.get_all()[0]), str(self.repo_materii.cauta_materie(1)))
        self.assertEqual(str(self.repo_materii.get_all()[1]), str(self.repo_materii.cauta_materie(2)))
        self.assertEqual(str(self.repo_materii.get_all()[2]), str(self.repo_materii.cauta_materie(3)))
        self.repo_materii.stergere_materie(self.materie_1.get_id_materie())
        self.assertEqual(self.repo_materii.__len__(), 2)
        with self.assertRaisesRegex(RepoError, "materie inexistenta!"):
            self.repo_materii.stergere_materie(self.materie_1.get_id_materie())

    def test_repo_note(self):
        self.assertEqual(self.repo_note.__len__(), 0)
        self.assertEqual(self.repo_note.size(), 0)
        self.repo_note.adauga_nota(self.nota_1)
        self.assertEqual(self.repo_note.__len__(), 1)
        self.assertEqual(self.repo_note.size(), 1)
        with self.assertRaisesRegex(RepoError, "nota existenta!"):
            self.repo_note.adauga_nota(self.nota_acelasi_id)

        self.repo_note.adauga_nota(self.nota_2)
        self.repo_note.adauga_nota(self.nota_3)
        self.assertEqual(self.repo_note.__len__(), 3)
        self.assertEqual(self.repo_note.size(), 3)

        self.repo_note.sterge_nota(self.nota_1.get_id_nota())
        self.assertEqual(self.repo_note.__len__(), 2)
        with self.assertRaisesRegex(RepoError, "nota inexistenta"):
            self.repo_note.sterge_nota(self.nota_1.get_id_nota())

        self.assertEqual(str(self.repo_note.get_all()[0]), str(self.nota_2))
        self.assertEqual(str(self.repo_note.get_all()[1]), str(self.nota_3))

    def test_service_studenti(self):
        self.assertEqual(len(self.service_studenti.get_all_studenti()), 0)
        self.service_studenti.adauga_student(self.student_1.getID_student(), self.student_1.getNume())
        self.assertEqual(len(self.service_studenti.get_all_studenti()), 1)
        with self.assertRaisesRegex(RepoError, "student existent!"):
            self.service_studenti.adauga_student(self.student_1.getID_student(), self.student_1.getNume())
        with self.assertRaisesRegex(ValidError, "id invalid!\nnume invalid!\n"):
            self.service_studenti.adauga_student(self.student_invalid.getID_student(), self.student_invalid.getNume())

        self.service_studenti.adauga_student(self.student_2.getID_student(), self.student_2.getNume())
        self.assertEqual(len(self.service_studenti.get_all_studenti()), 2)

        #White Box testing pentru functia de modificare student din ServiceStudenti
        #-------------------------------------------------------------------------------------------------------------#
        self.service_studenti.modifica_student(self.student_acelasi_id.getID_student(), self.student_acelasi_id.getNume())
        self.assertEqual(self.service_studenti.cauta_student(self.student_acelasi_id.getID_student()), self.student_acelasi_id)
        id_invalid = -1
        id_tip_gresit = ""
        nume_tip_gresit = int(1)
        nume_invalid = ""
        id_valid = self.student_2.getID_student()
        nume_valid = self.student_1.getNume()
        with self.assertRaisesRegex(ValidError, "id invalid!\n"):
            self.service_studenti.modifica_student(id_invalid, nume_valid)
        with self.assertRaisesRegex(ValidError, "nume invalid!\n"):
            self.service_studenti.modifica_student(id_valid, nume_invalid)
        with self.assertRaisesRegex(ValidError, "id invalid!\nnume invalid!\n"):
            self.service_studenti.modifica_student(self.student_invalid.getID_student(), self.student_invalid.getNume())
        with self.assertRaisesRegex(RepoError, "student inexistent!"):
            self.service_studenti.modifica_student(self.student_3.getID_student(), self.student_3.getNume())
        with self.assertRaises(TypeError):
            self.service_studenti.modifica_student(id_tip_gresit, nume_valid)
        self.service_studenti.modifica_student(id_valid, nume_tip_gresit)
        self.assertEqual(self.service_studenti.cauta_student(id_valid).getNume(),str(nume_tip_gresit))
        #-------------------------------------------------------------------------------------------------------------#

        with self.assertRaisesRegex(ValidError, "id invalid!\n"):
            self.service_studenti.cauta_student(self.student_invalid.getID_student())
        with self.assertRaisesRegex(RepoError, "student inexistent!"):
            self.service_studenti.cauta_student(self.student_3.getID_student())

        self.assertEqual(self.service_studenti.get_all_studenti()[0], self.service_studenti.cauta_student(self.student_acelasi_id.getID_student()))
        self.assertEqual(self.service_studenti.get_all_studenti()[1], self.service_studenti.cauta_student(self.student_2.getID_student()))

    def test_service_studenti_blackbox(self):
        self.service_studenti.adauga_student(self.student_1.getID_student(), self.student_1.getNume())
        self.service_studenti.adauga_student(self.student_2.getID_student(), self.student_2.getNume())

        # Black Box testing pentru functia de modificare student din ServiceStudenti
        # -------------------------------------------------------------------------------------------------------------#
        self.service_studenti.modifica_student(self.student_acelasi_id.getID_student(),self.student_acelasi_id.getNume())
        self.assertEqual(self.service_studenti.cauta_student(self.student_acelasi_id.getID_student()),self.student_acelasi_id)
        with self.assertRaisesRegex(ValidError, "id invalid!\nnume invalid!\n"):
            self.service_studenti.modifica_student(self.student_invalid.getID_student(), self.student_invalid.getNume())
        with self.assertRaisesRegex(RepoError, "student inexistent!"):
            self.service_studenti.modifica_student(self.student_3.getID_student(), self.student_3.getNume())
        # -------------------------------------------------------------------------------------------------------------#
    def test_service_materii(self):
        self.assertEqual(len(self.service_materii.get_all_materii()), 0)
        self.service_materii.adauga_materie(self.materie_1.get_id_materie(), self.materie_1.get_nume_materie(),self.materie_1.get_nume_profesor())
        self.assertEqual(len(self.service_materii.get_all_materii()), 1)
        with self.assertRaisesRegex(RepoError, "materie existenta!"):
            self.service_materii.adauga_materie(self.materie_1.get_id_materie(), self.materie_1.get_nume_materie(),self.materie_1.get_nume_profesor())
        with self.assertRaisesRegex(ValidError, "id invalid!\nnume materie invalid!\nnume profesor invalid!\n"):
            self.service_materii.adauga_materie(self.materie_invalida.get_id_materie(), self.materie_invalida.get_nume_materie(),self.materie_invalida.get_nume_profesor())

        self.service_materii.adauga_materie(self.materie_2.get_id_materie(), self.materie_2.get_nume_materie(),self.materie_2.get_nume_materie())
        self.assertEqual(len(self.service_materii.get_all_materii()), 2)

        self.service_materii.modifica_materie(self.materie_acelasi_id.get_id_materie(),self.materie_acelasi_id.get_nume_materie(),self.materie_acelasi_id.get_nume_profesor())
        self.assertEqual(self.service_materii.cauta_materie(self.materie_acelasi_id.get_id_materie()),self.materie_acelasi_id)
        with self.assertRaisesRegex(ValidError, "id invalid!\nnume materie invalid!\nnume profesor invalid!\n"):
            self.service_materii.modifica_materie(self.materie_invalida.get_id_materie(), self.materie_invalida.get_nume_materie(), self.materie_invalida.get_nume_profesor())
        with self.assertRaisesRegex(RepoError, "materie inexistenta!"):
            self.service_materii.modifica_materie(self.materie_3.get_id_materie(), self.materie_3.get_nume_materie(), self.materie_3.get_nume_profesor())

        with self.assertRaisesRegex(ValidError, "id invalid!\n"):
            self.service_materii.cauta_materie(self.materie_invalida.get_id_materie())
        with self.assertRaisesRegex(RepoError, "materie inexistenta!"):
            self.service_materii.cauta_materie(self.materie_3.get_id_materie())

        self.assertEqual(self.service_materii.get_all_materii()[0],self.service_materii.cauta_materie(self.materie_acelasi_id.get_id_materie()))
        self.assertEqual(self.service_materii.get_all_materii()[1],self.service_materii.cauta_materie(self.materie_2.get_id_materie()))

    def test_service_note(self):
        self.repo_studenti.adauga_student(self.student_1)
        self.repo_studenti.adauga_student(self.student_2)
        self.repo_studenti.adauga_student(self.student_3)
        self.repo_studenti.adauga_student(self.student_4)
        self.repo_studenti.adauga_student(self.student_5)
        self.repo_materii.adauga_materie(self.materie_1)
        self.repo_materii.adauga_materie(self.materie_2)

        self.assertEqual(len(self.service_note.get_all_note()), 0)
        self.service_note.asignare_nota(self.nota_1.get_id_nota(), self.nota_1.get_id_student(), self.nota_1.get_id_materie(), self.nota_1.get_nota())
        self.assertEqual(len(self.service_note.get_all_note()), 1)
        with self.assertRaisesRegex(ValidError, "id invalid!\nid student invalid!\nid materie invalid!\nnota invalida!\n"):
            self.service_note.asignare_nota(self.nota_invalida.get_id_nota(), self.nota_invalida.get_id_student(),self.nota_invalida.get_id_materie(), self.nota_invalida.get_nota())
        with self.assertRaisesRegex(RepoError, "nota existenta!"):
            self.service_note.asignare_nota(self.nota_1.get_id_nota(), self.nota_1.get_id_student(),self.nota_1.get_id_materie(), self.nota_1.get_nota())

        self.service_note.asignare_nota(self.nota_2.get_id_nota(), self.nota_2.get_id_student(),self.nota_2.get_id_materie(), self.nota_2.get_nota())
        self.service_note.asignare_nota(self.nota_4.get_id_nota(), self.nota_4.get_id_student(),self.nota_4.get_id_materie(), self.nota_4.get_nota())
        self.service_note.asignare_nota(self.nota_5.get_id_nota(), self.nota_5.get_id_student(),self.nota_5.get_id_materie(), self.nota_5.get_nota())
        self.service_note.asignare_nota(self.nota_6.get_id_nota(), self.nota_6.get_id_student(),self.nota_6.get_id_materie(), self.nota_6.get_nota())
        self.service_note.asignare_nota(self.nota_7.get_id_nota(), self.nota_7.get_id_student(),self.nota_7.get_id_materie(), self.nota_7.get_nota())
        self.service_note.asignare_nota(self.nota_8.get_id_nota(), self.nota_8.get_id_student(),self.nota_8.get_id_materie(), self.nota_8.get_nota())
        self.assertEqual(len(self.service_note.get_all_note()), 7)

        self.assertEqual(self.service_note.get_all_note()[0], self.nota_1)
        self.assertEqual(self.service_note.get_note_afisare()[0],"Lau - Mate : 9.4 cu id-ul 1")
        self.assertEqual(self.service_note.get_all_note()[1], self.nota_2)
        self.assertEqual(self.service_note.get_note_afisare()[1],"Dragos - Info : 5.3 cu id-ul 2")

        self.assertEqual(str(self.service_note.get_sefi_promotie()[0]),"studentul Lau cu media 9.65")

        self.assertEqual(str(self.service_note.lista_studenti_note_descresc_quicksort(self.materie_1.get_id_materie())[0]),"Studentul Lau cu nota 9.4")
        self.assertEqual(str(self.service_note.lista_studenti_note_descresc_quicksort(self.materie_1.get_id_materie())[1]),"Studentul Raja cu nota 7.2")
        self.assertEqual(str(self.service_note.lista_studenti_note_descresc_quicksort(self.materie_1.get_id_materie())[2]),"Studentul Philip cu nota 4.4")

        self.assertEqual(str(self.service_note.lista_studenti_note_alfabetic_gnomesort(self.materie_1.get_id_materie())[0]),"Studentul Lau cu nota 9.4")
        self.assertEqual(str(self.service_note.lista_studenti_note_alfabetic_gnomesort(self.materie_1.get_id_materie())[1]),"Studentul Philip cu nota 4.4")
        self.assertEqual(str(self.service_note.lista_studenti_note_alfabetic_gnomesort(self.materie_1.get_id_materie())[2]),"Studentul Raja cu nota 7.2")

        self.assertEqual(self.service_note.nota_frecventa_minima(),(5.3, 1))

        self.assertEqual(len(self.service_note.get_all_note()), 7)
        self.assertEqual(len(self.repo_studenti.get_all()),5)
        self.service_note.sterge_student_si_notele_lui(self.student_1.getID_student())
        self.assertEqual(len(self.service_note.get_all_note()),5)
        self.assertEqual(len(self.repo_studenti.get_all()), 4)
        with self.assertRaisesRegex(RepoError, "student inexistent!"):
            self.service_note.sterge_student_si_notele_lui(self.student_1.getID_student())

        self.assertEqual(len(self.service_note.get_all_note()), 5)
        self.assertEqual(len(self.repo_materii.get_all()), 2)
        self.service_note.sterge_materie_si_note(self.materie_1.get_id_materie())
        self.assertEqual(len(self.service_note.get_all_note()), 3)
        self.assertEqual(len(self.repo_materii.get_all()), 1)
        with self.assertRaisesRegex(RepoError, "materie inexistenta!"):
            self.service_note.sterge_materie_si_note(self.materie_1.get_id_materie())

unittest.main()
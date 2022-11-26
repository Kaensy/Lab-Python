from Erori.repo_error import RepoError
from Erori.validation_error import ValidError


class UI:

    def __init__(self, service_studenti, service_materii, service_note):
        self.__service_studenti = service_studenti
        self.__service_materii = service_materii
        self.__service_note = service_note
        self.__comenzi = {
            "adauga_student": self.__ui_adauga_student,
            "print_studenti": self.__ui_print_studenti,
            "sterge_student": self.__ui_sterge_student_si_note,
            "modifica_student": self.__ui_modifica_student,
            "cauta_student": self.__ui_cauta_student,
            "adauga_studenti_random": self.__ui_adauga_studenti_random,
            "sefi_promotie": self.__ui_sefi_promotie,
            "adauga_materie": self.__ui_adauga_materie,
            "print_materii": self.__ui_print_materii,
            "sterge_materie": self.__ui_sterge_materie,
            "modifica_materie": self.__ui_modifica_materie,
            "cauta_materie": self.__ui_cauta_materie,
            "adauga_materii_random": self.__ui_adauga_materii_random,
            "comenzi": self.__ui_afisare_comenzi
            }

    def __ui_adauga_materii_random(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        times = int(self.__params[0])
        self.__service_materii.adaugare_materii_random(times)

    def __ui_adauga_studenti_random(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        times = int(self.__params[0])
        self.__service_studenti.adaugare_studenti_random(times)


    def __ui_afisare_comenzi(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        for comanda in self.__comenzi:
            print(comanda)
        print("exit")
    def __ui_cauta_materie(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        id_materie = int(self.__params[0])
        print(str(self.__service_materii.cauta_materie(id_materie)))

    def __ui_cauta_student(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        print(str(self.__service_studenti.cauta_student(id_student)))

    def __ui_modifica_materie(self):
        if len(self.__params) != 3:
            print("Numar parametri invalid!")
            return
        id_materie = int(self.__params[0])
        nume_materie = self.__params[1]
        nume_profesor = self.__params[2]
        self.__service_materii.modifica_materie(id_materie, nume_materie, nume_profesor)
        print("Materie modificata cu succes")

    def __ui_modifica_student(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        self.__service_studenti.modifica_student(id_student, nume)
        print("Student modificat cu succes")

    def __ui_sterge_materie(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        id_materie = int(self.__params[0])
        self.__service_note.sterge_materie_si_note(id_materie)
        print(f"Materia cu id-ul {id_materie} si notele acesteia au fost sterse")

    def __ui_print_materii(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        materii = self.__service_materii.get_all_materii()
        if len(materii) == 0:
            print("Nu exista materii in aplicatie")
            return
        for materie in materii:
                print(materie)

    def __ui_adauga_materie(self):
        if len(self.__params) != 3:
            print("Numar parametri invalid")
            return
        id_materie = int(self.__params[0])
        nume_materie = self.__params[1]
        nume_profesor = self.__params[2]
        self.__service_materii.adauga_materie(id_materie, nume_materie, nume_profesor)
        print("Materie adaugata cu succes")

    def __ui_sefi_promotie(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid")
            return
        sefi_promotie = self.__service_note.get_sefi_promotie()
        for sef_promotie in sefi_promotie:
            print(sef_promotie)

    def __ui_sterge_student_si_note(self):
        if len(self.__params) != 1:
            print("Numar parametri invalid!")
            return
        id_student = int(self.__params[0])
        self.__service_note.sterge_student_si_notele_lui(id_student)
        print(f"Studentul cu id-ul {id_student} si notele lui sterse cu succes")

    def __ui_print_studenti(self):
        if len(self.__params) != 0:
            print("Numar parametri invalid!")
            return
        studenti = self.__service_studenti.get_all_studenti()
        if len(studenti) == 0:
            print("Nu exista studenti in aplicatie")
            return
        for student in studenti:
            print(student)

    def __ui_adauga_student(self):
        if len(self.__params) != 2:
            print("Numar parametri invalid")
            return
        id_student = int(self.__params[0])
        nume = self.__params[1]
        self.__service_studenti.adauga_student(id_student, nume)
        print("Student adaugat cu succes")

    def run(self):
        for comenzi in self.__comenzi:
            print(comenzi)
        print("exit")
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split()
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("UI error: tip numeric invalid")
                except ValidError as ve:
                    print(f"Valid Error :{ve}")
                except RepoError as re:
                    print(f"Repo Error:{re}")
            else:
                print("Comanda Invalida!")

from Erori.repo_error import RepoError
from Erori.valid_error import ValidError

class UI:

    def __init__(self, service_produse):
        self.__service_produse = service_produse
        self.__comenzi = {
            "adauga_produs": self.__ui_adauga_produs,
            "print_produse": self.__ui_print_produse
        }

    def __ui_print_produse(self):
        if len(self.__params) != 0:
            print("nr params invalid!")
            return
        produse = self.__service_produse.get_all_service()
        for produs in produse:
            print(produs)

    def __ui_adauga_produs(self):
        if len(self.__params) != 3:
            print("nr params invalid!")
            return
        id_produs = int(self.__params[0])
        denumire_produs = self.__params[1]
        pret_produs = int(self.__params[2])
        self.__service_produse.adauga_produs_service(id_produs, denumire_produs, pret_produs)
        print("Produs adaugat cu succes")

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
                    print("UI Error : tip numeric invalid")
                except ValidError as ve:
                    print(f"Valid Error : {ve}")
                except RepoError as re:
                    print(f"Repo Error : {re}")
            else:
                print("Comanda invalida")

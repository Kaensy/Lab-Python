class UI:

    def __init__(self, service_costume):
        self.__service_costume = service_costume
        self.__comenzi = {
            "adauga_costum" : self.__ui_adauga_costum,
            "print_costume_tematica" : self.__ui_print_costume_tematica,
            "inchiriere" : self.__ui_inchiriere
             }

    def __ui_inchiriere(self):
        if len(self.__params) != 1:
            print("Nr parametrii invalid!")
            return
        id_costum = int(self.__params[0])
        mesaj = self.__service_costume.inchiriere_costum(id_costum)
        if mesaj[0] == "1":
            print(str(mesaj[1]))
        elif mesaj[0] == "2":
            print("Ne pare rau. Costumul este inchiriat de catre alta persoana")
        elif mesaj[0] == "3":
            print(f"Costumul cu id-ul {id_costum} nu exista")
        print("Sugestie:",mesaj[-1])

    def __ui_adauga_costum(self):
        if len(self.__params) != 5:
            print("Nr parametrii invalid!")
            return
        id_student = int(self.__params[0])
        denumire_costum = self.__params[1]
        tematica_costum = self.__params[2]
        pret_costum = int(self.__params[3])
        disponibilitate_costum = self.__params[4]
        self.__service_costume.adauga_costum_service(id_student, denumire_costum, tematica_costum, pret_costum, disponibilitate_costum)
        print("Costum adaugat cu succes")

    def __ui_print_costume_tematica(self):
        if len(self.__params) != 1:
            print("Nr parametrii invalid!")
            return
        tematica_costum = self.__params[0]
        costume = self.__service_costume.all_costume_tematica_service(tematica_costum)
        for costum in costume:
            print(costum)


    def run(self):
        for comanda in self.__comenzi:
            print(comanda)
        print("exit")
        while True:
            comanda = input(">>>")
            comanda = comanda.strip()
            if comanda == "":
                continue
            if comanda == "exit":
                return
            parti = comanda.split(",")
            nume_comanda = parti[0]
            self.__params = parti[1:]
            if nume_comanda in self.__comenzi:
                try:
                    self.__comenzi[nume_comanda]()
                except ValueError:
                    print("UI Error : tip numeric invalid!")
            else:
                print("comanda invalida")

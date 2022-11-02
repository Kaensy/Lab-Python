from datetime import date
from business.service_pachete import adauga_pachet_service, creeare_lista_interval_service, \
    creeare_lista_destinatie_pret_service, creeare_lista_datasfarsit_service, nr_pachete_destinatie_service, \
    creeare_lista_interval_crescator_service, medie_pret_destinatie_service, numar_pachete_service, \
    get_datainceput_pachet_service, get_datasfarsit_pachet_service, get_destinatie_pachet_service, \
    get_pret_pachet_service, modificare_pachet_service, stergere_destinatie_pachete_service, \
    stergere_durata_pachete_service, stergere_pret_pachete_service
from domain.pachet import to_string_pachet


def adauga_persoane_ui(l, params):
    if len(params) != 8:
        raise ValueError("Numar parametri invalid!")
    data_inceput = date(int(params[2]), int(params[1]), int(params[0]))
    data_sfarsit = date(int(params[5]), int(params[4]), int(params[3]))
    destinatie = str(params[6])
    pret = int(params[7])
    adauga_pachet_service(l, data_inceput, data_sfarsit, destinatie, pret)


def print_pachet_ui(l):
    for i, pachet in enumerate(l):
        print(i + 1, ". ", to_string_pachet(pachet))

def print_pachet_fara_index_ui(l):
    for pachet in l:
        print(to_string_pachet(pachet))
def run_ui():
    pachete = []
    interfata_baza = """
1.Adaugare
2.Stergere 
3.Cautare 
4.Rapoarte 
5.Undo ( x )
6.Exit 
7.Tiparire Lista Pachete"""
    interfata_adaugare = """
1.Adauga pachet de calatorie
2.Modifica pachet de calatorie 
3.Inapoi"""
    interfata_modificare ="""
1.Data de inceput
2.Data de sfarsit
3.Destinatie
4.Pret"""
    interfata_alegere ="""
1.Da
2.Nu"""
    interfata_stergere ="""
1.Sterge toate pachetele dintr-o destinatie
2.Sterge toate pachetele cu o durata mai scurta decat o valoare introdusa
3.Sterge toate pachetele cu un pret mai mare decat un pret introdus
4.Inapoi"""
    interfata_cautare = """
1.Tiparirea pachetelor dintr-un interval
2.Tiparirea pachetelor dintr-o locatie si cu pret mai mic decat o suma 
3.Tiparirea pachetelor cu o anumita data de sfarsit 
4.Inapoi"""
    interfata_rapoarte = """
1.Nr pachete pentru o destinatie
2.Pachete dintr-o perioada ordonate crescator 
3.Media de pret pentru o destinatie 
4.Inapoi"""
    while True:
        print(interfata_baza)
        command = input(">>>")
        command = command.strip()
        if command == "":
            continue
        elif command == "exit":
            return
        elif command == "1":
            while command:
                print(interfata_adaugare)
                command = input(">>>")
                command = command.strip()
                if command == "1":
                    parts = input("Introduce-ti datele pachetului : ")
                    parts = parts.split(" ")
                    try:
                        adauga_persoane_ui(pachete, parts)
                    except ValueError as ve:
                        print(ve)
                elif command == "2":
                    print("Pe care pachet doriti sa il modificati")
                    print_pachet_ui(pachete)
                    index_pachet_modificare = int(input(">>>"))
                    if index_pachet_modificare > numar_pachete_service(pachete) or index_pachet_modificare < 1:
                        print("Index invalid")
                    else:
                        data_inceput_noua = get_datainceput_pachet_service(pachete[index_pachet_modificare-1])
                        data_sfarsit_noua = get_datasfarsit_pachet_service(pachete[index_pachet_modificare-1])
                        destinatie_noua = get_destinatie_pachet_service(pachete[index_pachet_modificare-1])
                        pret_nou = get_pret_pachet_service(pachete[index_pachet_modificare-1])
                        lista_modificare=[]
                        adauga_pachet_service(lista_modificare, data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
                        modificare = True
                        schimbare = False
                        while modificare:
                            print("Ce doriti sa modificati")
                            print(interfata_modificare)
                            if schimbare:
                                print("5.Terminat\n6.Inapoi")
                            else:
                                print("5.Inapoi")
                            modificare = input(">>>")
                            if modificare == "1":
                                data_inceput_mod = input("Data inceput noua : ")
                                data_inceput_mod = data_inceput_mod.split()
                                if not (len(data_inceput_mod) == 3 and all([item.isdigit() for item in data_inceput_mod])):
                                    print("Data Invalida")
                                else:
                                    data_inceput_noua = date(int(data_inceput_mod[2]), int(data_inceput_mod[1]), int(data_inceput_mod[0]))
                                    schimbare = True
                            elif modificare == "2":
                                data_sfarsit_mod = input("Data sfarsit noua : ")
                                data_sfarsit_mod = data_sfarsit_mod.split()
                                if not (len(data_sfarsit_mod) == 3 and all([item.isdigit() for item in data_sfarsit_mod])):
                                    print("Data Invalida")
                                else:
                                    data_sfarsit_noua = date(int(data_sfarsit_mod[2]), int(data_sfarsit_mod[1]), int(data_sfarsit_mod[0]))
                                    schimbare = True
                            elif modificare == "3":
                                destinatie_mod = input("Destinatie noua : ")
                                destinatie_mod = destinatie_mod.strip()
                                if not destinatie_mod:
                                    print("Destinatie Invalida")
                                else:
                                    destinatie_noua = destinatie_mod
                                    schimbare = True
                            elif modificare == "4":
                                pret_mod = input("Pret nou : ")
                                pret_mod = pret_mod.strip()
                                if not (pret_mod.isdigit() and int(pret_mod) > -1):
                                    print("Pret Invalid")
                                else:
                                    pret_nou = pret_mod
                                    schimbare = True
                            elif modificare == "5" and schimbare == False:
                                modificare = False
                            elif modificare == "5" and schimbare:
                                pusca = False
                                try:
                                    adauga_pachet_service(lista_modificare, data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
                                except ValueError as ve:
                                    print(str(ve))
                                    pusca = True
                                if not pusca:
                                    print("Doriti sa faceti urmatoarea modificare ?")
                                    print_pachet_fara_index_ui(lista_modificare)
                                    alegere = True
                                    while alegere :
                                        print(interfata_alegere)
                                        alegere = input(">>>")
                                        if alegere == "1":
                                            modificare_pachet_service(pachete[index_pachet_modificare-1], data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
                                            alegere = False
                                            modificare = False
                                        elif alegere =="2":
                                            modificare = False
                                            alegere = False
                                        else:
                                            print("Comanda Invalida")
                            elif modificare == "6" and schimbare == True:
                                modificare = False
                            else:
                                print("Comanda Invalida")
                elif command == "3":
                    command = False
                else:
                    print("Comanda invalida")
        elif command == "2":
            while command:
                print(interfata_stergere)
                command = input(">>>")
                command = command.strip()
                if command == "1":
                    destinatie = input("Introduceti destinatia dorita : ")
                    destinatie = destinatie.strip()
                    if not destinatie:
                        print("Destinatie invalida")
                    else:
                        stergere_destinatie_pachete_service(pachete, destinatie)
                elif command == "2":
                    durata = input("Introduceti durata : ")
                    durata = durata.strip()
                    if not(durata.isdigit() and int(durata) >0):
                        print("Durata invalida")
                    else:
                        stergere_durata_pachete_service(pachete, int(durata))
                elif command == "3":
                    pret = input("Introduceti pretul : ")
                    pret = pret.strip()
                    if not(pret.isdigit() and int(pret) > -1):
                        print("Pret invalid")
                    else:
                        stergere_pret_pachete_service(pachete, int(pret))
                elif command == "4":
                    command = False
                else:
                    print("Comanda invalida")
        elif command == "3":
            lista_cautata = []
            while command:
                print(interfata_cautare)
                if lista_cautata:
                    print("5.Filtrare")
                command = input(">>>")
                command = command.strip()
                if command == "1":
                    lista_cautata = []
                    interval = input("Introduceti intervalul de timp dorit : ")
                    interval = interval.split()
                    if len(interval) == 6:
                        data_inceput_interval = date(int(interval[2]), int(interval[1]), int(interval[0]))
                        data_sfarsit_interval = date(int(interval[5]), int(interval[4]), int(interval[3]))
                        creeare_lista_interval_service(lista_cautata, pachete, data_inceput_interval, data_sfarsit_interval)
                        try:
                            print_pachet_ui(lista_cautata)
                        except ValueError as ve:
                            print(ve)
                        if not lista_cautata:
                            print("Nu sa gasit niciun pachet")
                    else:
                        print("Interval Invalid ")
                elif command == "2":
                    lista_cautata = []
                    params = input("Introduceti Destinatia cautata si pretul maxim : ")
                    params = params.split()
                    if len(params) == 2 and params[1].isdigit():
                        destinatie_cautata = str(params[0])
                        pret_cautat = int(params[1])
                        creeare_lista_destinatie_pret_service(lista_cautata, pachete, destinatie_cautata, pret_cautat)
                        try:
                            print_pachet_ui(lista_cautata)
                        except ValueError as ve:
                            print(ve)
                        if not lista_cautata:
                            print("Nu sa gasit niciun pachet")
                    elif len(params) != 2:
                        print("Nr de parametri invalid")
                    elif not (params[1].isdigit()):
                        print("Pret invalid")
                elif command == "3":
                    lista_cautata = []
                    params = input("Introduceti Data de Sfarsit cautata : ")
                    params = params.split()
                    data_sfarsit_cautata = date(int(params[2]), int(params[1]), int(params[0]))
                    creeare_lista_datasfarsit_service(lista_cautata, pachete, data_sfarsit_cautata)
                    try:
                        print_pachet_ui(lista_cautata)
                    except ValueError as ve:
                        print(ve)
                    if not lista_cautata:
                        print("Nu sa gasit niciun pachet")
                elif command == "4":
                    command = False
                elif command == "5" and lista_cautata:
                    print("To Be Implemented")
                else:
                    print("Comanda invalida")
        elif command == "4":
            while command:
                print(interfata_rapoarte)
                command = input(">>>")
                command = command.strip()
                if command == "1":
                    destinatie_raport = input("Introduceti Destinatia cautata : ")
                    destinatie_raport = destinatie_raport.strip()
                    print(nr_pachete_destinatie_service(pachete, destinatie_raport))
                elif command == "2":
                    interval = input("Introduceti intervalul de timp dorit : ")
                    interval = interval.strip()
                    interval = interval.split()
                    if len(interval) == 6:
                        data_inceput_interval = date(int(interval[2]), int(interval[1]), int(interval[0]))
                        data_sfarsit_interval = date(int(interval[5]), int(interval[4]), int(interval[3]))
                        lista_cautata = creeare_lista_interval_crescator_service(pachete, data_inceput_interval, data_sfarsit_interval)
                        try:
                            print_pachet_ui(lista_cautata)
                        except ValueError as ve:
                            print(ve)
                    else:
                        print("Interval Invalid ")
                elif command == "3":
                    destinatie = input("Introduceti destinatia cautata : ")
                    print("Media preturilor din", destinatie, "este de :", medie_pret_destinatie_service(pachete, destinatie),"de lei")
                elif command == "4":
                    command = False
                else:
                    print("Comanda invalida")
        elif command == "7":
            try:
                print_pachet_ui(pachete)
            except ValueError as ve:
                print(ve)
            if not pachete:
                print("Lista goala")
        elif command == "6":
            return
        else:
            print("Comanda invalida")

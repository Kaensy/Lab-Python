from datetime import date
from business.service_pachete import adauga_pachet_service, creeare_lista_interval_service, \
    creeare_lista_destinatie_pret_service, creeare_lista_datasfarsit_service, nr_pachete_destinatie_service, \
    creeare_lista_interval_crescator_service, medie_pret_destinatie_service, numar_pachete_service, \
    get_datainceput_pachet_service, get_datasfarsit_pachet_service, get_destinatie_pachet_service, \
    get_pret_pachet_service, modificare_pachet_service, stergere_destinatie_pachete_service, \
    stergere_durata_pachete_service, stergere_pret_pachete_service, filtrare_pret_destinatie, filtrare_luna, undoundo
from domain.pachet import to_string_pachet


def adauga_persoane_ui(l, undo, params):
    if len(params) != 8:
        raise ValueError("Numar parametri invalid!")
    data_inceput = date(int(params[2]), int(params[1]), int(params[0]))
    data_sfarsit = date(int(params[5]), int(params[4]), int(params[3]))
    destinatie = str(params[6])
    pret = int(params[7])
    adauga_pachet_service(l, undo, data_inceput, data_sfarsit, destinatie, pret)


def print_pachet_ui(l):
    for key, value in l.items():
        print(key, to_string_pachet(value))

def print_pachet_fara_index_ui(l):
    for key in l:
        print(to_string_pachet(l[key]))

def adaugare(pachete, undo, params):
    try:
        adauga_persoane_ui(pachete, undo, params)
    except ValueError as ve:
        print(ve)

def stergere(pachete, undo, params):
    if params[0] == "1":
        if not params[1]:
            print("Destinatie invalida")
        else:
            stergere_destinatie_pachete_service(pachete, undo, params[1])
    elif params[0] == "2":
        if not (params[1].isdigit() and int(params[1]) > 0):
            print("Durata invalida")
        else:
            stergere_durata_pachete_service(pachete, undo, int(params[1]))
    elif params[0] == "3":
        if not (params[1].isdigit() and int(params[1]) > -1):
            print("Pret invalid")
        else:
            stergere_pret_pachete_service(pachete, undo, int(params[1]))

def print_pachete(l, undo, params):
    for key, value in l.items():
        print(key, to_string_pachet(value))

def cautare(pachete, undo, params):
        if params[0] == "1":
            lista_cautata = {}
            if len(params) == 7:
                data_inceput_interval = date(int(params[3]), int(params[2]), int(params[1]))
                data_sfarsit_interval = date(int(params[6]), int(params[5]), int(params[4]))
                creeare_lista_interval_service(lista_cautata, pachete, data_inceput_interval, data_sfarsit_interval)
                try:
                    print_pachet_ui(lista_cautata)
                except ValueError as ve:
                    print(ve)
                if not lista_cautata:
                    print("Nu sa gasit niciun pachet")
            else:
                print("Interval Invalid ")
        elif params[0] == "2":
            lista_cautata = {}
            if len(params) == 3 and params[2].isdigit():
                destinatie_cautata = str(params[1])
                pret_cautat = int(params[2])
                creeare_lista_destinatie_pret_service(lista_cautata, pachete, destinatie_cautata, pret_cautat)
                try:
                    print_pachet_ui(lista_cautata)
                except ValueError as ve:
                    print(ve)
                if not lista_cautata:
                    print("Nu sa gasit niciun pachet")
            elif len(params) != 3:
                print("Nr parametrii invalid")
            elif not (params[2].isdigit()):
                print("Pret invalid")
        elif params[0] == "3":
            lista_cautata = {}
            data_sfarsit_cautata = date(int(params[3]), int(params[2]), int(params[1]))
            creeare_lista_datasfarsit_service(lista_cautata, pachete, data_sfarsit_cautata)
            try:
                print_pachet_ui(lista_cautata)
            except ValueError as ve:
                print(ve)
            if not lista_cautata:
                print("Nu sa gasit niciun pachet")

def rapoarte(pachete, undo, params):
    if params[0] == "1":
        print(nr_pachete_destinatie_service(pachete, params[1]))
    elif params[0] == "2":
        if len(params) == 7:
            data_inceput_interval = date(int(params[3]), int(params[2]), int(params[1]))
            data_sfarsit_interval = date(int(params[6]), int(params[5]), int(params[4]))
            lista_cautata = creeare_lista_interval_crescator_service(pachete, data_inceput_interval,data_sfarsit_interval)
            try:
                print_pachet_ui(lista_cautata)
            except ValueError as ve:
                print(ve)
        else:
            print("Interval Invalid ")
    elif params[0] == "3":
        medie = medie_pret_destinatie_service(pachete, params[1])
        if medie:
            print("Media preturilor din", params[1], "este de :", medie, "de lei")
        else:
            print("Nu exista nici un pachet disponibil pentru destinatia introdusa")

def filtrare(pachete, undo, params):
    if params[0] == "1":
        if len(params) == 3 and params[1].isdigit():
            pret_filtrare = int(params[1])
            destinatie_filtrare = str(params[2])
            filtrare_pret_destinatie(pachete, undo, pret_filtrare, destinatie_filtrare)
            print_pachet_ui(pachete)
        elif len(params) != 3:
            print("Nr parametrii invalid")
        elif not (params[1].isdigit()):
            print("Pret invalid")
    elif params[0] == "2":
        if params[1].isdigit():
            filtrare_luna(pachete, undo, int(params[1]))
            print_pachet_ui(pachete)
        else:
            print("Luna invalida")

def modificare_ui(pachete, undo, params):
    data_inceput_noua = get_datainceput_pachet_service(pachete[int(params[0])])
    data_sfarsit_noua = get_datasfarsit_pachet_service(pachete[int(params[0])])
    destinatie_noua = get_destinatie_pachet_service(pachete[int(params[0])])
    pret_nou = get_pret_pachet_service(pachete[int(params[0])])
    data_inceput = date(int(params[3]), int(params[2]), int(params[1]))
    data_sfarsit = date(int(params[6]), int(params[5]), int(params[4]))
    destinatie = params[7]
    pret = int(params[8])
    undo.append(lambda: modificare_pachet_service(pachete[int(params[0])], data_inceput_noua, data_sfarsit_noua, destinatie_noua,pret_nou))
    modificare_pachet_service(pachete[int(params[0])], data_inceput, data_sfarsit, destinatie, pret)

def undo_ui(pachete, undo, params):
    undoundo(pachete, undo)

def run_ui():
    pachete = {}
    undo = []
    comenzi = {
        'Adaugare': adaugare,
        'Stergere': stergere,
        'Afisare': print_pachete,
        'Cautare': cautare,
        'Rapoarte': rapoarte,
        'Filtrare': filtrare,
        'Modificare': modificare_ui,
        'Undo': undo_ui
    }
    interfata_baza = """---------------------MENIU---------------------
1.Adaugare
2.Stergere 
3.Cautare 
4.Rapoarte 
5.Filtrare
6.Undo 
7.Exit 
8.Tiparire Lista Pachete
-----------------------------------------------"""
    interfata_adaugare = """-------------------ADAUGARE--------------------
1.Adauga pachet de calatorie
2.Modifica pachet de calatorie 
3.Inapoi
-----------------------------------------------"""
    interfata_modificare = """-------------------MODIFICARE-------------------
1.Data de inceput
2.Data de sfarsit
3.Destinatie
4.Pret"""
    interfata_alegere = """-----------------------------------------------
1.Da
2.Nu
-----------------------------------------------"""
    interfata_stergere = """-------------------STERGERE--------------------
1.Sterge toate pachetele dintr-o destinatie
2.Sterge toate pachetele cu o durata mai scurta decat o valoare introdusa
3.Sterge toate pachetele cu un pret mai mare decat un pret introdus
4.Inapoi
-----------------------------------------------"""
    interfata_cautare = """-------------------CAUTARE---------------------
1.Tiparirea pachetelor dintr-un interval
2.Tiparirea pachetelor dintr-o locatie si cu pret mai mic decat o suma 
3.Tiparirea pachetelor cu o anumita data de sfarsit 
4.Inapoi
-----------------------------------------------"""
    interfata_filtrare = """------------------FILTRARE--------------------
1.Filtrare dupa Pret Maxim si o Destinatie
2.Filtrare pachete care nu apar intr-o luna
3.Inapoi
-----------------------------------------------"""
    interfata_filtrare_cautare = """------------------FILTRARE---------------------
1.Filtrare dupa Pret Maxim si o Destinatie
2.Filtrare pachete care nu apar intr-o luna
3.Undo
4.Inapoi
-----------------------------------------------"""
    interfata_rapoarte = """------------------RAPOARTE---------------------
1.Nr pachete pentru o destinatie
2.Pachete dintr-o perioada ordonate crescator 
3.Media de pret pentru o destinatie 
4.Inapoi
-----------------------------------------------"""
    modalitate = input("1 - Optiuni\n2 - Linie de comanda\n")
    while modalitate == "1":
        print(interfata_baza)
        command = input(">>>")
        command = command.strip()
        if command == "":
            continue
        elif command == "1":
            while command:
                print(interfata_adaugare)
                command = input(">>>")
                command = command.strip()
                if command == "1":
                    parts = input("Introduce-ti datele pachetului : ")
                    parts = parts.split(" ")
                    try:
                        adauga_persoane_ui(pachete, undo, parts)
                    except ValueError as ve:
                        print(ve)
                elif command == "2":
                    print("Pe care pachet doriti sa il modificati")
                    print_pachet_ui(pachete)
                    index_pachet_modificare = int(input(">>>"))
                    if pachete.get(index_pachet_modificare) == None:
                        print("Index invalid")
                    else:
                        data_inceput_noua = get_datainceput_pachet_service(pachete[index_pachet_modificare])
                        data_sfarsit_noua = get_datasfarsit_pachet_service(pachete[index_pachet_modificare])
                        destinatie_noua = get_destinatie_pachet_service(pachete[index_pachet_modificare])
                        pret_nou = get_pret_pachet_service(pachete[index_pachet_modificare])
                        lista_modificare={}
                        adauga_pachet_service(lista_modificare, undo, data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
                        modificare = True
                        schimbare = False
                        while modificare:
                            print("Ce doriti sa modificati")
                            print(interfata_modificare)
                            if schimbare:
                                print("5.Terminat\n6.Inapoi\n-----------------------------------------------")
                            else:
                                print("5.Inapoi\n-----------------------------------------------")
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
                                    pret_nou = int(pret_mod)
                                    schimbare = True
                            elif modificare == "5" and schimbare == False:
                                modificare = False
                            elif modificare == "5" and schimbare:
                                pusca = False
                                try:
                                    adauga_pachet_service(lista_modificare, undo, data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
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
                                            undo.append(lambda: modificare_pachet_service(pachete[index_pachet_modificare], get_datainceput_pachet_service(lista_modificare[1]), get_datasfarsit_pachet_service(lista_modificare[1]), get_destinatie_pachet_service(lista_modificare[1]), get_pret_pachet_service(lista_modificare[1])))
                                            modificare_pachet_service(pachete[index_pachet_modificare], data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
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
                        stergere_destinatie_pachete_service(pachete, undo, destinatie)
                elif command == "2":
                    durata = input("Introduceti durata : ")
                    durata = durata.strip()
                    if not(durata.isdigit() and int(durata) >0):
                        print("Durata invalida")
                    else:
                        stergere_durata_pachete_service(pachete,undo, int(durata))
                elif command == "3":
                    pret = input("Introduceti pretul : ")
                    pret = pret.strip()
                    if not(pret.isdigit() and int(pret) > -1):
                        print("Pret invalid")
                    else:
                        stergere_pret_pachete_service(pachete,undo, int(pret))
                elif command == "4":
                    command = False
                else:
                    print("Comanda invalida")
        elif command == "3":
            lista_cautata = {}
            while command:
                print(interfata_cautare)
                if lista_cautata:
                    print("5.Filtrare")
                command = input(">>>")
                command = command.strip()
                if command == "1":
                    lista_cautata = {}
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
                    lista_cautata = {}
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
                        print("Nr parametrii invalid")
                    elif not (params[1].isdigit()):
                        print("Pret invalid")
                elif command == "3":
                    lista_cautata = {}
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
                    command_filtrare = True
                    undo_cautare = []
                    while command_filtrare:
                        print(interfata_filtrare_cautare)
                        command_filtrare = input(">>>")
                        command_filtrare = command_filtrare.strip()
                        if command_filtrare == "1":
                            params = input("Introduceti Pretul maxim si Destinatia Dorita : ")
                            params = params.split()
                            if len(params) == 2 and params[0].isdigit():
                                pret_filtrare = int(params[0])
                                destinatie_filtrare = str(params[1])
                                filtrare_pret_destinatie(lista_cautata,undo_cautare, pret_filtrare, destinatie_filtrare)
                                print_pachet_ui(lista_cautata)
                            elif len(params) != 2:
                                print("Nr parametrii invalid")
                            elif not (params[0].isdigit()):
                                print("Pret invalid")
                        elif command_filtrare == "2":
                            params = input("Introduceti Luna : ")
                            params = params.strip()
                            if params.isdigit():
                                filtrare_luna(lista_cautata,undo_cautare, params)
                                print_pachet_ui(lista_cautata)
                            else:
                                print("Luna invalida")
                        elif command_filtrare == "3":
                            if undo_cautare:
                                undoundo(lista_cautata, undo_cautare)
                                print_pachet_ui(lista_cautata)
                        elif command_filtrare == "4":
                            command_filtrare = False
                        else:
                            print("Comanda invalida")
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
                    medie = medie_pret_destinatie_service(pachete, destinatie)
                    if medie:
                        print("Media preturilor din", destinatie, "este de :", medie,"de lei")
                    else:
                        print("Nu exista nici un pachet disponibil pentru destinatia introdusa")
                elif command == "4":
                    command = False
                else:
                    print("Comanda invalida")
        elif command == "5":
            while command:
                print(interfata_filtrare)
                command = input(">>>")
                command = command.strip()
                if command == "1":
                    params = input("Introduceti Pretul maxim si Destinatia Dorita : ")
                    params = params.split()
                    if len(params) == 2 and params[0].isdigit():
                        pret_filtrare = int(params[0])
                        destinatie_filtrare = str(params[1])
                        filtrare_pret_destinatie(pachete,undo, pret_filtrare, destinatie_filtrare)
                        print_pachet_ui(pachete)
                    elif len(params) != 2:
                        print("Nr parametrii invalid")
                    elif not (params[0].isdigit()):
                        print("Pret invalid")
                elif command == "2":
                    params = input("Introduceti Luna : ")
                    params = params.strip()
                    if params.isdigit():
                        filtrare_luna(pachete,undo, params)
                        print_pachet_ui(pachete)
                    else:
                        print("Luna invalida")
                elif command == "3":
                    command = False
                else:
                    print("Comanda invalida")
        elif command == "6":
            undoundo(pachete, undo)
        elif command == "8":
            try:
                print_pachet_ui(pachete)
            except ValueError as ve:
                print(ve)
            if not pachete:
                print("Lista goala")
        elif command == "7":
            return
        else:
            print("Comanda invalida")
    while modalitate == "2":
        for keys in comenzi:
            print(keys)
        params = input(">>>")
        params = params.split(" ")
        while params[0] in comenzi:
            comenzi[params[0]](pachete, undo, params[1:])
            params = input(">>>")
            params = params.split()
            if params[0] == "Exit":
                return


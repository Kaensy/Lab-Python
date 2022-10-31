from datetime import date
from business.service_pachete import adauga_pachet_service
from domain.pachet import to_string_pachet
from infrastructura.repository_persoane import creeare_lista_interval, creeare_lista_destinatie_pret, \
    creeare_lista_datasfarsit, nr_pachete_destinatie


# Creeaza functii de service pt functile de creare
# Valideaza parametrii in functile de creare

def adauga_persoane_ui(l, params):
    if len(params) != 8:
        raise ValueError("Numar parametri invalid!\n")
    data_inceput = date(int(params[2]), int(params[1]), int(params[0]))
    data_sfarsit = date(int(params[5]), int(params[4]), int(params[3]))
    destinatie = str(params[6])
    pret = int(params[7])
    adauga_pachet_service(l, data_inceput, data_sfarsit, destinatie, pret)


def print_pachet_ui(l):
    for i, pachet in enumerate(l):
        print(i + 1, ". ", to_string_pachet(pachet))


def run_ui():
    pachete = []
    interfata_baza = """
1.Adaugare
2.Stergere ( x )
3.Cautare 
4.Rapoarte ( x )
5.Undo ( x )
6.Exit 
7.Tiparire Lista Pachete"""
    interfata_adaugare = """
1.Adauga pachet de calatorie
2.Modifica pachet de calatorie (x)
3.Inapoi"""
    interfata_cautare = """
1.Tiparirea pachetelor dintr-un interval
2.Tiparirea pachetelor dintr-o locatie si cu pret mai mic decat o suma 
3.Tiparirea pachetelor cu o anumita data de sfarsit 
4.Inapoi"""
    interfata_rapoarte = """
1.Nr pachete pentru o destinatie
2.Pachete dintr-o perioada ordonate crescator ( x )
3.Media de pret pentru o destinatie ( x )
4.Inapoi
"""
    while True:
        print(interfata_baza)
        command = input(">>>")
        command = command.strip()
        if command == "":
            continue
        elif command == "exit":
            return
        elif command == "1":
            print(interfata_adaugare)
            command = input(">>>")
            command = command.strip()
            while command:
                if command == "1":
                    parts = input("Introduce-ti datele pachetului : ")
                    parts = parts.split(" ")
                    try:
                        adauga_persoane_ui(pachete, parts)
                    except ValueError as ve:
                        print(ve)
                    print(interfata_adaugare)
                    command = input(">>>")
                    command = command.strip()
                elif command == "2":
                    print("To Be Implemented\n", interfata_adaugare)
                    command = input(">>>")
                    command = command.strip()
                elif command == "3":
                    command = False
                else:
                    print("Comanda invalida")
                    print(interfata_adaugare)
                    command = input(">>>")
                    command = command.strip()
        elif command == "3":
            print(interfata_cautare)
            command = input(">>>")
            command = command.strip()
            lista_cautata = []
            while command:
                if command == "1":
                    lista_cautata = []
                    interval = input("Introduceti intervalul de timp dorit : ")
                    interval = interval.split()
                    if len(interval) == 6:
                        data_inceput_interval = date(int(interval[2]), int(interval[1]), int(interval[0]))
                        data_sfarsit_interval = date(int(interval[5]), int(interval[4]), int(interval[3]))
                        creeare_lista_interval(lista_cautata, pachete, data_inceput_interval, data_sfarsit_interval)
                        try:
                            print_pachet_ui(lista_cautata)
                        except ValueError as ve:
                            print(ve)
                        if lista_cautata:
                            print(interfata_cautare, "\n5.Filtrare")
                        else:
                            print("Nu sa gasit niciun pachet\n", interfata_cautare)
                        command = input(">>>")
                        command = command.strip()
                    else:
                        print("Interval Invalid ")
                elif command == "2":
                    lista_cautata = []
                    params = input("Introduceti Destinatia cautata si pretul maxim : ")
                    params = params.split()
                    if len(params) == 2 and params[1].isdigit():
                        destinatie_cautata = str(params[0])
                        pret_cautat = int(params[1])
                        creeare_lista_destinatie_pret(lista_cautata, pachete, destinatie_cautata, pret_cautat)
                        try:
                            print_pachet_ui(lista_cautata)
                        except ValueError as ve:
                            print(ve)
                        if lista_cautata:
                            print(interfata_cautare, "\n5.Filtrare")
                        else:
                            print("Nu sa gasit niciun pachet\n", interfata_cautare)
                        command = input(">>>")
                        command = command.strip()
                    elif len(params) != 2:
                        print("Nr de parametri invalid")
                    elif not (params[1].isdigit()):
                        print("Pret invalid")
                elif command == "3":
                    lista_cautata = []
                    params = input("Introduceti Data de Sfarsit cautata : ")
                    params = params.split()
                    data_sfarsit_cautata = date(int(params[2]), int(params[1]), int(params[0]))
                    creeare_lista_datasfarsit(lista_cautata, pachete, data_sfarsit_cautata)
                    try:
                        print_pachet_ui(lista_cautata)
                    except ValueError as ve:
                        print(ve)
                    if lista_cautata:
                        print(interfata_cautare, "\n5.Filtrare")
                    else:
                        print("Nu sa gasit niciun pachet\n", interfata_cautare)
                    command = input(">>>")
                elif command == "4":
                    command = False
                elif command == "5" and lista_cautata:
                    print("To Be Implemented")
                    print(interfata_cautare)
                    command = input(">>>")
                    command = command.strip()
                else:
                    print("Comanda invalida")
                    print(interfata_cautare)
                    if lista_cautata:
                        print("5.Filtrare")
                    command = input(">>>")
                    command = command.strip()
        elif command == "4":
            print(interfata_rapoarte)
            command = input(">>>")
            command = command.strip()
            while command:
                if command == "1":
                    destinatie_raport = input("Introduceti Destinatia cautata : ")
                    destinatie_raport = destinatie_raport.strip()
                    print(nr_pachete_destinatie(pachete, destinatie_raport))
                    print(interfata_rapoarte)
                    command = input(">>>")
                    command = command.strip()
                if command == "4":
                    command = False
                else:
                    print("Comanda invalida")
                    print(interfata_rapoarte)
                    command = input(">>>")
                    command = command.strip()
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

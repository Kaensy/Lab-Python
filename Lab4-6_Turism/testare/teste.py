from datetime import date

from business.service_pachete import numar_pachete_service, adauga_pachet_service, creeare_lista_interval_service, \
    creeare_lista_destinatie_pret_service, creeare_lista_datasfarsit_service, nr_pachete_destinatie_service, \
    creeare_lista_interval_crescator_service, medie_pret_destinatie_service, modificare_pachet_service, \
    stergere_destinatie_pachete_service, stergere_durata_pachete_service, stergere_pret_pachete_service, \
    filtrare_pret_destinatie, filtrare_luna, undoundo
from domain.pachet import creeaza_pachet, get_datainceput_pachet, get_datasfarsit_pachet, get_destinatie_pachet, \
    get_pret_pachet, set_datainceput_pachet, set_datasfarsit_pachet, set_destinatie_pachet, set_pret_pachet, \
    egal_pachete
from infrastructura.repository_persoane import numar_pachete_lista, adauga_pachet_lista, get_all_pachete, \
    modificare_pachet, stergere_pachet_index
from validare.validator_pachet import valideaza_pachet


def ruleaza_teste_pachet():
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)
    pachet = creeaza_pachet(data_inceput,data_sfarsit,destinatie,pret)
    assert(data_inceput == get_datainceput_pachet(pachet))
    assert(data_sfarsit == get_datasfarsit_pachet(pachet))
    assert(destinatie == get_destinatie_pachet(pachet))
    assert(pret == get_pret_pachet(pachet))

    data_inceput_noua = date(2023,11,17)
    set_datainceput_pachet(pachet,data_inceput_noua)
    assert(data_inceput_noua == get_datainceput_pachet(pachet))
    data_sfarsit_noua = date(2023,12,1)
    set_datasfarsit_pachet(pachet,data_sfarsit_noua)
    assert(data_sfarsit_noua == get_datasfarsit_pachet(pachet))
    destinatie_noua = "Dej"
    set_destinatie_pachet(pachet,destinatie_noua)
    assert(destinatie_noua == get_destinatie_pachet(pachet))
    pret_nou = 40
    set_pret_pachet(pachet,pret_nou)
    assert(pret_nou == get_pret_pachet(pachet))

def ruleaza_teste_validare_pachet():
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)
    pachet = creeaza_pachet(data_inceput, data_sfarsit, destinatie, pret)
    valideaza_pachet(pachet)

    data_inceput_gresita = date(2021, 10, 11)
    data_sfarsit_gresita = date(2020, 10, 15)
    destinatie_gresita = ""
    pret_gresit = int(-1)
    pachet_gresit = creeaza_pachet(data_inceput_gresita, data_sfarsit_gresita, destinatie_gresita, pret_gresit)
    try:
        valideaza_pachet(pachet_gresit)
        assert False
    except ValueError as ve:
        assert(str(ve)=="data_inceput invalida!\ndata_sfarsit invalida!\ndestinatie invalida!\npret invalid!\n")

def ruleaza_egal():
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)
    pachet_a = creeaza_pachet(data_inceput, data_sfarsit, destinatie, pret)
    pachet_b = creeaza_pachet(data_inceput, data_sfarsit, destinatie, pret)
    assert(egal_pachete(pachet_a,pachet_b)==True)
    data_inceput_c = date(2023, 12, 15)
    data_sfarsit_c = date(2023, 12, 17)
    destinatie_c = "Kolozsvaristan"
    pret_c = int(30)
    pachet_c = creeaza_pachet(data_inceput_c,data_sfarsit_c,destinatie_c,pret_c)
    assert(egal_pachete(pachet_a,pachet_c)==False)

def ruleaza_teste_repository_pachete():
    pachete={}
    undo = []
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)
    pachet = creeaza_pachet(data_inceput, data_sfarsit, destinatie, pret)
    assert (numar_pachete_lista(pachete) == 0)
    adauga_pachet_lista(pachete, undo, pachet)
    assert (numar_pachete_lista(pachete) == 1)

    data_inceput_acelasi = date(2023, 10, 11)
    data_sfarsit_acelasi = date(2023, 10, 15)
    destinatie_acelasi = "Kolozsvar"
    pret_acelasi = int(25)
    pachet_acelasi = creeaza_pachet(data_inceput_acelasi, data_sfarsit_acelasi, destinatie_acelasi, pret_acelasi)
    try:
        adauga_pachet_lista(pachete,undo, pachet_acelasi)
        assert False
    except ValueError as ve:
        assert(str(ve) == "pachet invalid!\n")
    assert (numar_pachete_lista(pachete) == 1)

    lista_pachete = get_all_pachete(pachete)
    assert(len(lista_pachete) == 1)
    assert (get_destinatie_pachet(lista_pachete[1]) == get_destinatie_pachet(pachet))

    data_inceput_noua = date(2024, 12, 12)
    data_sfarsit_noua = date(2025, 1, 1)
    destinatie_noua = "Cluj"
    pret_nou = int(50)
    modificare_pachet(lista_pachete[1], data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
    assert (get_datainceput_pachet(lista_pachete[1]) == data_inceput_noua)
    assert (get_datasfarsit_pachet(lista_pachete[1]) == data_sfarsit_noua)
    assert (get_destinatie_pachet(lista_pachete[1]) == destinatie_noua)
    assert (get_pret_pachet(lista_pachete[1]) == pret_nou)

    stergere_pachet_index(lista_pachete, 1)
    assert (len(lista_pachete) == 0)

def ruleaza_teste_service_pachete():
    pachete = {}
    undo = []
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)

    data_inceput_gresita = date(2021, 10, 11)
    data_sfarsit_gresita = date(2020, 10, 15)
    destinatie_gresita = ""
    pret_gresit = int(-1)

    data_inceput_acelasi = date(2023, 10, 11)
    data_sfarsit_acelasi = date(2023, 10, 15)
    destinatie_acelasi = "Kolozsvar"
    pret_acelasi = int(25)

    assert (numar_pachete_service(pachete) == 0)
    adauga_pachet_service(pachete,undo,data_inceput,data_sfarsit,destinatie,pret)
    assert (numar_pachete_service(pachete) == 1)

    try:
        adauga_pachet_service(pachete,undo,data_inceput_gresita,data_sfarsit_gresita,destinatie_gresita,pret_gresit)
        assert False
    except ValueError as ve:
        assert(str(ve) == "data_inceput invalida!\ndata_sfarsit invalida!\ndestinatie invalida!\npret invalid!\n")

    try:
        adauga_pachet_service(pachete,undo,data_inceput_acelasi,data_sfarsit_acelasi,destinatie_acelasi,pret_acelasi)
        assert False
    except ValueError as ve:
        assert(str(ve) == "pachet invalid!\n")

    assert (numar_pachete_service(pachete)==1)

    data_inceput_noua = date(2024, 12, 12)
    data_sfarsit_noua = date(2025, 1, 1)
    destinatie_noua = "Cluj"
    pret_nou = int(50)
    modificare_pachet_service(pachete[1], data_inceput_noua, data_sfarsit_noua, destinatie_noua, pret_nou)
    assert (get_datainceput_pachet(pachete[1]) == data_inceput_noua)
    assert (get_datasfarsit_pachet(pachete[1]) == data_sfarsit_noua)
    assert (get_destinatie_pachet(pachete[1]) == destinatie_noua)
    assert (get_pret_pachet(pachete[1]) == pret_nou)

    data_inceput_gresita = date(2021, 10, 11)
    data_sfarsit_gresita = date(2020, 10, 15)
    destinatie_gresita = ""
    pret_gresit = int(-1)
    try:
        modificare_pachet_service(pachete[1], data_inceput_gresita, data_sfarsit_gresita, destinatie_gresita, pret_gresit)
        assert False
    except ValueError as ve:
        assert (str(ve) == "data_inceput invalida!\ndata_sfarsit invalida!\ndestinatie invalida!\npret invalid!\n")

    lista_pachete = {}
    data_inceput_unu = date(2023, 12, 12)
    data_sfarsit_unu = date(2024, 1, 1)
    destinatie_unu = "Cluj"
    pret_unu = int(50)

    data_inceput_doi = date(2023, 12, 12)
    data_sfarsit_doi = date(2023, 12, 15)
    destinatie_doi = "Cluj"
    pret_doi = int(75)

    data_inceput_trei = date(2024, 1, 1)
    data_sfarsit_trei = date(2024, 1, 5)
    destinatie_trei = "Dej"
    pret_trei = int(15)

    adauga_pachet_service(lista_pachete,undo, data_inceput_unu, data_sfarsit_unu, destinatie_unu, pret_unu)
    adauga_pachet_service(lista_pachete,undo, data_inceput_doi, data_sfarsit_doi, destinatie_doi, pret_doi)
    adauga_pachet_service(lista_pachete,undo, data_inceput_trei, data_sfarsit_trei, destinatie_trei, pret_trei)

    assert (numar_pachete_service(lista_pachete) == 3)
    stergere_destinatie_pachete_service(lista_pachete,undo, "Dincolo")
    assert (numar_pachete_service(lista_pachete) == 3)
    stergere_durata_pachete_service(lista_pachete,undo,1)
    assert (numar_pachete_service(lista_pachete) == 3)
    stergere_pret_pachete_service(lista_pachete,undo,100)
    assert (numar_pachete_service(lista_pachete) == 3)

    stergere_destinatie_pachete_service(lista_pachete,undo, destinatie_trei)
    assert (numar_pachete_service(lista_pachete) == 2)
    stergere_durata_pachete_service(lista_pachete,undo, 4)
    assert (numar_pachete_service(lista_pachete) == 1)
    stergere_pret_pachete_service(lista_pachete,undo, 40)
    assert (numar_pachete_service(lista_pachete) == 0)

    lista_filtrare = {}
    # 11 10 2023 -> 15 10 2023 ;"Kolozsvar" ; 25
    # 12 12 2023 -> 1 1 2024 ; "Cluj" ; 50
    # 12 12 2023 -> 15 12 2023 ; "Cluj" ; 75
    # 1 1 2024 -> 5 1 2024 ; "Dej" ; 15
    # 5 5 2024 -> 5 5 2025 ; "Cluj" ; 65
    adauga_pachet_service(lista_filtrare,undo, data_inceput, data_sfarsit, destinatie, pret)
    adauga_pachet_service(lista_filtrare,undo, data_inceput_unu, data_sfarsit_unu, destinatie_unu, pret_unu)
    adauga_pachet_service(lista_filtrare,undo, data_inceput_doi, data_sfarsit_doi, destinatie_doi, pret_doi)
    adauga_pachet_service(lista_filtrare,undo, data_inceput_trei, data_sfarsit_trei, destinatie_trei, pret_trei)
    adauga_pachet_service(lista_filtrare,undo, date(2024, 5, 5), date(2025, 5, 5), "Cluj", int(65))

    assert (numar_pachete_service(lista_filtrare) == 5)
    filtrare_pret_destinatie(lista_filtrare,undo, 70, "Cluj")
    assert (numar_pachete_service(lista_filtrare) == 2)
    filtrare_luna(lista_filtrare,undo, 12)
    assert (numar_pachete_service(lista_filtrare) == 0)

def ruleaza_teste_creare_lista_noua():
    pachete={}
    pachete_interval={}
    undo = []
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)
    adauga_pachet_service(pachete,undo,data_inceput,data_sfarsit,destinatie,pret)

    data_inceput_doi = date(2023, 10, 12)
    data_sfarsit_doi = date(2023, 10, 16)
    destinatie_doi = "Kolozsvar2"
    pret_doi = int(30)
    adauga_pachet_service(pachete,undo,data_inceput_doi,data_sfarsit_doi,destinatie_doi,pret_doi)

    data_inceput_interval_gresit = date(2024, 1, 1)
    data_sfarsit_interval_gresit = date(2025, 12, 12)
    assert (numar_pachete_service(pachete_interval)==0)
    creeare_lista_interval_service(pachete_interval,pachete,data_inceput_interval_gresit,data_sfarsit_interval_gresit)
    assert (numar_pachete_service(pachete_interval)==0)

    data_inceput_interval_corect = date(2022, 1, 1)
    data_sfarsit_interval_corect = date(2024, 12, 12)
    creeare_lista_interval_service(pachete_interval,pachete,data_inceput_interval_corect,data_sfarsit_interval_corect)
    assert (numar_pachete_service(pachete_interval)==2)
    # ^^^ Testare cautare dupa Interval

    pachete_destinatie_pret = {}

    destinatie_cautata_corecta = "Kolozsvar"
    pret_cautat_corect = 100
    creeare_lista_destinatie_pret_service(pachete_destinatie_pret,pachete,destinatie_cautata_corecta,pret_cautat_corect)
    assert(numar_pachete_service(pachete_destinatie_pret)==1)
    destinatie_cautata_gresita = "Florestini"
    pret_cautat_gresit = 1
    creeare_lista_destinatie_pret_service(pachete_destinatie_pret,pachete,destinatie_cautata_gresita,pret_cautat_corect)
    assert (numar_pachete_service(pachete_destinatie_pret) == 1)
    creeare_lista_destinatie_pret_service(pachete_destinatie_pret,pachete,destinatie_cautata_corecta,pret_cautat_gresit)
    assert (numar_pachete_service(pachete_destinatie_pret) == 1)
    destinatie_cautata_corecta_doi = "Kolozsvar2"
    creeare_lista_destinatie_pret_service(pachete_destinatie_pret,pachete,destinatie_cautata_corecta_doi,pret_cautat_corect)
    assert (numar_pachete_service(pachete_destinatie_pret) == 2)
    # ^^^ Testare cautare dupa Destinatie - Pret

    pachete_datasfarsit = {}

    data_sfarsit_corecta = date(2023, 10, 15)
    creeare_lista_datasfarsit_service(pachete_datasfarsit, pachete, data_sfarsit_corecta)
    assert (numar_pachete_service(pachete_datasfarsit) == 1)
    data_sfarsit_gresita = date(2030, 12, 12)
    creeare_lista_datasfarsit_service(pachete_datasfarsit, pachete, data_sfarsit_gresita)
    assert (numar_pachete_service(pachete_datasfarsit) == 1)
    data_sfarsit_corecta_doi = date(2023, 10, 16)
    creeare_lista_datasfarsit_service(pachete_datasfarsit, pachete, data_sfarsit_corecta_doi)
    assert (numar_pachete_service(pachete_datasfarsit) == 2)

def ruleaza_teste_rapoarte():
    pachete = {}
    undo = []
    data_inceput_unu = date(2022, 12, 12)
    data_sfarsit_unu = date(2023, 1, 12)
    destinatie = "Cluj"
    pret_unu = int(30)
    assert (nr_pachete_destinatie_service(pachete, destinatie)==0)
    adauga_pachet_service(pachete,undo, data_inceput_unu, data_sfarsit_unu, destinatie, pret_unu)
    assert (nr_pachete_destinatie_service(pachete, destinatie)==1)

    data_inceput_doi = date(2023, 5, 5)
    data_sfarsit_doi = date(2023, 6, 6)
    pret_doi = int(50)
    adauga_pachet_service(pachete,undo, data_inceput_doi, data_sfarsit_doi, destinatie, pret_doi)
    assert (nr_pachete_destinatie_service(pachete, destinatie)==2)

    interval_inceput_unu = date(2022, 12, 15)
    interval_sfarsit = date(2023, 8, 8)
    interval_inceput_doi = date(2022, 11, 11)
    lista_cautata = creeare_lista_interval_crescator_service(pachete, interval_inceput_unu, interval_sfarsit)
    assert (numar_pachete_service(lista_cautata) == 1)
    lista_cautata = creeare_lista_interval_crescator_service(pachete, interval_inceput_doi, interval_sfarsit)
    assert (numar_pachete_service(lista_cautata) == 2)

    destinatie_inexistenta = "Dincolo"
    medie_pret = medie_pret_destinatie_service(pachete, destinatie_inexistenta)
    assert (medie_pret == 0)
    medie_pret = medie_pret_destinatie_service(pachete, destinatie)
    assert (medie_pret == 40)

def ruleaza_undo():
    pachete = {}
    undo = []
    data_inceput_unu = date(2022, 12, 12)
    data_sfarsit_unu = date(2023, 1, 12)
    destinatie = "Cluj"
    pret_unu = int(30)
    assert (nr_pachete_destinatie_service(pachete, destinatie) == 0)
    adauga_pachet_service(pachete, undo, data_inceput_unu, data_sfarsit_unu, destinatie, pret_unu)
    assert (nr_pachete_destinatie_service(pachete, destinatie) == 1)
    undoundo(pachete, undo)
    assert (nr_pachete_destinatie_service(pachete, destinatie) == 0)
    adauga_pachet_service(pachete, undo, data_inceput_unu, data_sfarsit_unu, destinatie, pret_unu)
    assert (nr_pachete_destinatie_service(pachete, destinatie) == 1)
    stergere_destinatie_pachete_service(pachete, undo, destinatie)
    assert (nr_pachete_destinatie_service(pachete, destinatie) == 0)
    undoundo(pachete, undo)
    assert (nr_pachete_destinatie_service(pachete, destinatie) == 1)

def ruleaza_toate_testele():
    ruleaza_teste_pachet()
    print("teste pachet trecute cu success poggers!")
    ruleaza_teste_validare_pachet()
    print("teste validare pachet trecute cu success poggers!")
    ruleaza_egal()
    print("merge egalu")
    ruleaza_teste_repository_pachete()
    print("teste repository pachete trecute cu success")
    ruleaza_teste_service_pachete()
    print("teste service trecute cu success")
    ruleaza_teste_creare_lista_noua()
    print("teste cautare trecute cu success")
    ruleaza_teste_rapoarte()
    print("teste rapoarte trecute cu success")
    ruleaza_undo()
    print("Undo works")

from datetime import date

from business.service_pachete import numar_pachete_service, adauga_pachet_service
from domain.pachet import creeaza_pachet, get_datainceput_pachet, get_datasfarsit_pachet, get_destinatie_pachet, \
    get_pret_pachet, set_datainceput_pachet, set_datasfarsit_pachet, set_destinatie_pachet, set_pret_pachet, \
    egal_pachete
from infrastructura.repository_persoane import numar_pachete_lista, adauga_pachet_lista, get_all_pachete, \
    creeare_lista_interval, creeare_lista_destinatie_pret, creeare_lista_datasfarsit, nr_pachete_destinatie
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
    pachete=[]
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)
    pachet = creeaza_pachet(data_inceput,data_sfarsit,destinatie,pret)
    assert (numar_pachete_lista(pachete)==0)
    adauga_pachet_lista(pachete,pachet)
    assert (numar_pachete_lista(pachete)==1)

    data_inceput_acelasi = date(2023, 10, 11)
    data_sfarsit_acelasi = date(2023, 10, 15)
    destinatie_acelasi = "Kolozsvar"
    pret_acelasi = int(25)
    pachet_acelasi = creeaza_pachet(data_inceput_acelasi,data_sfarsit_acelasi,destinatie_acelasi,pret_acelasi)
    try:
        adauga_pachet_lista(pachete,pachet_acelasi)
        assert False
    except ValueError as ve:
        assert(str(ve)=="pachet invalid!\n")
    assert (numar_pachete_lista(pachete)==1)

    lista_pachete = get_all_pachete(pachete)
    assert(len(lista_pachete)==1)
    assert (get_destinatie_pachet(lista_pachete[0]) == get_destinatie_pachet(pachet))

def ruleaza_teste_service_pachete():
    pachete = []
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
    adauga_pachet_service(pachete,data_inceput,data_sfarsit,destinatie,pret)
    assert (numar_pachete_service(pachete) == 1)

    try:
        adauga_pachet_service(pachete,data_inceput_gresita,data_sfarsit_gresita,destinatie_gresita,pret_gresit)
        assert False
    except ValueError as ve:
        assert(str(ve) == "data_inceput invalida!\ndata_sfarsit invalida!\ndestinatie invalida!\npret invalid!\n")

    try:
        adauga_pachet_service(pachete,data_inceput_acelasi,data_sfarsit_acelasi,destinatie_acelasi,pret_acelasi)
        assert False
    except ValueError as ve:
        assert(str(ve) == "pachet invalid!\n")

    assert (numar_pachete_service(pachete)==1)

def ruleaza_teste_creare_lista_noua():
    pachete=[]
    pachete_interval=[]
    data_inceput = date(2023, 10, 11)
    data_sfarsit = date(2023, 10, 15)
    destinatie = "Kolozsvar"
    pret = int(25)
    adauga_pachet_service(pachete,data_inceput,data_sfarsit,destinatie,pret)

    data_inceput_doi = date(2023, 10, 12)
    data_sfarsit_doi = date(2023, 10, 16)
    destinatie_doi = "Kolozsvar2"
    pret_doi = int(30)
    adauga_pachet_service(pachete,data_inceput_doi,data_sfarsit_doi,destinatie_doi,pret_doi)

    data_inceput_interval_gresit = date(2024, 1, 1)
    data_sfarsit_interval_gresit = date(2025, 12, 12)
    assert (numar_pachete_service(pachete_interval)==0)
    creeare_lista_interval(pachete_interval,pachete,data_inceput_interval_gresit,data_sfarsit_interval_gresit)
    assert (numar_pachete_service(pachete_interval)==0)

    data_inceput_interval_corect = date(2022, 1, 1)
    data_sfarsit_interval_corect = date(2024, 12, 12)
    creeare_lista_interval(pachete_interval,pachete,data_inceput_interval_corect,data_sfarsit_interval_corect)
    assert (numar_pachete_service(pachete_interval)==2)
    # ^^^ Testare cautare dupa Interval

    pachete_destinatie_pret = []

    destinatie_cautata_corecta = "Kolozsvar"
    pret_cautat_corect = 100
    creeare_lista_destinatie_pret(pachete_destinatie_pret,pachete,destinatie_cautata_corecta,pret_cautat_corect)
    assert(numar_pachete_service(pachete_destinatie_pret)==1)
    destinatie_cautata_gresita = "Florestini"
    pret_cautat_gresit = 1
    creeare_lista_destinatie_pret(pachete_destinatie_pret,pachete,destinatie_cautata_gresita,pret_cautat_corect)
    assert (numar_pachete_service(pachete_destinatie_pret) == 1)
    creeare_lista_destinatie_pret(pachete_destinatie_pret,pachete,destinatie_cautata_corecta,pret_cautat_gresit)
    assert (numar_pachete_service(pachete_destinatie_pret) == 1)
    destinatie_cautata_corecta_doi = "Kolozsvar2"
    creeare_lista_destinatie_pret(pachete_destinatie_pret,pachete,destinatie_cautata_corecta_doi,pret_cautat_corect)
    assert (numar_pachete_service(pachete_destinatie_pret) == 2)
    # ^^^ Testare cautare dupa Destinatie - Pret

    pachete_datasfarsit = []

    data_sfarsit_corecta = date(2023, 10, 15)
    creeare_lista_datasfarsit(pachete_datasfarsit,pachete,data_sfarsit_corecta)
    assert (numar_pachete_service(pachete_datasfarsit) == 1)
    data_sfarsit_gresita = date(2030, 12, 12)
    creeare_lista_datasfarsit(pachete_datasfarsit,pachete,data_sfarsit_gresita)
    assert (numar_pachete_service(pachete_datasfarsit) == 1)
    data_sfarsit_corecta_doi = date(2023, 10, 16)
    creeare_lista_datasfarsit(pachete_datasfarsit,pachete,data_sfarsit_corecta_doi)
    assert (numar_pachete_service(pachete_datasfarsit) == 2)

def ruleaza_teste_rapoarte():
    pachete = []
    data_inceput_unu = date(2022, 12, 12)
    data_sfarsit_unu = date(2023, 1, 12)
    destinatie = "Cluj"
    pret_unu = int(30)
    assert (nr_pachete_destinatie(pachete, destinatie)==0)
    adauga_pachet_service(pachete, data_inceput_unu, data_sfarsit_unu, destinatie, pret_unu)
    assert (nr_pachete_destinatie(pachete, destinatie)==1)

    data_inceput_doi = date(2023, 5, 5)
    data_sfarsit_doi = date(2023, 6, 6)
    pret_doi = int(55)
    adauga_pachet_service(pachete, data_inceput_doi, data_sfarsit_doi, destinatie, pret_unu)
    assert (nr_pachete_destinatie(pachete, destinatie)==2)

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

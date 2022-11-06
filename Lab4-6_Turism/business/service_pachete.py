from domain.pachet import creeaza_pachet, get_datainceput_pachet, get_datasfarsit_pachet, get_destinatie_pachet, \
    get_pret_pachet
from infrastructura.repository_persoane import adauga_pachet_lista, get_all_pachete, modificare_pachet, \
    stergere_pachet_index, adauga_pachet_lista_faraundo
from validare.validator_pachet import valideaza_pachet


def adauga_pachet_service(l, undo, data_inceput, data_sfarsit, destinatie, pret):
    """
    creaza un pachet pe baza date-ului data_inceput, a date-ului data_sfarsit, a string-ului destinatie si a intregului pret
    valideaza pachetul creat si daca e valid il adauga in lista de pachete unice l doar daca pachetul nu apare deja in lista l
    :param l: lista
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: int
    :return: - ( l' = l U pachet - daca validarea si adaugarea pachetului se face cu success )
    :raises: ValueError cu mesajele de validare daca pachetul creat e invalid
                        cu mesajul "pachet invalid!\n" daca pachetul exista deja in lista l
    """
    pachet = creeaza_pachet(data_inceput, data_sfarsit, destinatie, pret)
    valideaza_pachet(pachet)
    adauga_pachet_lista(l, undo, pachet)

def numar_pachete_service(l):
    """
    returneaza numarul de pachete pachet din lista l de pachete unice
    :param l: lista
    :return: rez - int : nr de pachete unice din lista l
    """
    return len(l)

def creeare_lista_interval_service(l_noua, l, data_inceput, data_sfarsit):
    """
    creeaza o noua lista l_noua formata din pachetele pachet din lista l care au ca data de inceput > data_inceput si data de sfarsit < data_sfarsit
    :param l_noua: list
    :param l: lista de pachete unice
    :param data_inceput: date
    :param data_sfarsit: date
    :return: - ( l_noua = l U pachete din lista l din intervalul data_inceput - data_sfarsit )
    """
    for key in l:
        if get_datainceput_pachet(l[key]) >= data_inceput and get_datasfarsit_pachet(l[key]) <= data_sfarsit:
            l_noua[numar_pachete_service(l_noua)+1] = l[key]

def creeare_lista_destinatie_pret_service(l_noua,l , destinatie,pret):
    """
    creeaza o noua lista l_noua formata din pachetele pachet din lista l care au destinatia destinatie si pretul mai mic decat pret
    :param l_noua: lista
    :param l: lista de pachete unice
    :param destinatie: string
    :param pret: integer
    :return: - ( l_noua = l U pachetele din lista l cu destinatia destinatie si pretul < pret )
    """
    for key in l:
        if get_destinatie_pachet(l[key]) == destinatie and get_pret_pachet(l[key]) < pret:
            l_noua[numar_pachete_service(l_noua)+1] = l[key]

def creeare_lista_datasfarsit_service(l_noua, l, data_sfarsit):
    """
    creeaza o noua lista l_noua formata din pachetele pachet din lista l care au data de sfarsit lafel ca data_sfarsit
    :param l_noua: lista
    :param l: lista de pachete unice
    :param data_sfarsit: date
    :return: - ( l_noua = l U pachetele din lista l cu data de sfarsit = data_sfarsit )
    """
    for key in l:
        if get_datasfarsit_pachet(l[key]) == data_sfarsit:
            l_noua[numar_pachete_service(l_noua)+1] = l[key]

def nr_pachete_destinatie_service(l, destinatie):
    """
    returneaza numarul de pachete pachet cu destinatia identica cu destinatie
    :param l: lista de pachete unice
    :param destinatie: string
    :return: rez - int : numarul de pachete pachet cu destinatia destinatie == destinatie
    """
    nr = 0
    for key in l:
        if get_destinatie_pachet(l[key]) == destinatie:
            nr += 1
    return nr

def creeare_lista_interval_crescator_service(l, data_inceput, data_sfarsit):
    """
    returneaza dictionarul cu pachetele din intervalul data_inceput -> data_sfarsit din dictionarul l ordonate crescator dupa pret
    :param l: lista de pachete unice
    :param data_inceput: date
    :param data_sfarsit: date
    :return:
    """
    lista_cautata = {}
    creeare_lista_interval_service(lista_cautata, l, data_inceput, data_sfarsit)
    lista_cautata_cresc = dict(sorted(lista_cautata.items(), key=lambda x: x[-1]))
    return lista_cautata_cresc


def medie_pret_destinatie_service(l, destinatie):
    """
    returneaza media de pret int a pachetelor cu destinatia destinatie din lista de pachete l
    :param l: lista de pachete unice
    :param destinatie: string
    :return: rez - int : media preturilor pret a pachetelor cu destinatia destinatie din lista
    """
    medie = 0
    nr_pachete = nr_pachete_destinatie_service(l, destinatie)
    if nr_pachete:
        for key in l:
            if get_destinatie_pachet(l[key]) == destinatie:
                medie += get_pret_pachet(l[key])
        return float(medie/nr_pachete)
    else:
        return 0

def modificare_pachet_service(pachet, data_inceput, data_sfarsit, destinatie, pret):
    """
    verifica daca datele sunt valide
    modifica valorile elementelor pachetul pachet cu noile elemente de acelasi tip data_inceput, data_sfarsit, destinatie, pret
    :param pachet: pachet
    :param data_inceput: date
    :param data_sfarsit: date
    :param destinatie: string
    :param pret: int
    :return: - ( elementele pachetului pachet au fost inlocuite cu noile elemente data_inceput, data_sfarsit, destinatie, pret )
    :raises: Value error cu mesajele de validare daca noile date sunt invalide
    """
    pachet_modificare = creeaza_pachet(data_inceput, data_sfarsit, destinatie, pret)
    valideaza_pachet(pachet_modificare)
    modificare_pachet(pachet, data_inceput, data_sfarsit, destinatie, pret)

def get_datainceput_pachet_service(pachet):
    """
    returneaza data date data_inceput a pachetului pachet
    :param pachet: pachet
    :return: rez : date - data_inceput a pachetului pachet
    """
    return get_datainceput_pachet(pachet)

def get_datasfarsit_pachet_service(pachet):
    """
    returneaza data date data_sfarsit a pachetului pachet
    :param pachet: pachet
    :return: rez : date - data_sfarsit a pachetului pachet
    """
    return get_datasfarsit_pachet(pachet)

def get_destinatie_pachet_service(pachet):
    """
    returneaza destinatia string destinatie a pachetului pachet
    :param pachet: pachet
    :return: rez : string - destinatie a pachetului pachet
    """
    return get_destinatie_pachet(pachet)

def get_pret_pachet_service(pachet):
    """
    returneaza pretul int pret a pachetului pachet
    :param pachet: pachet
    :return: rez : int - pret a pachetului pachet
    """
    return get_pret_pachet(pachet)

def stergere_destinatie_pachete_service(pachete, undo, destinatie):
    """
    sterge toate pachetele de tip pachet din lista pachete cu destinatia destinatie
    :param pachete: lista de pachete unice
    :param destinatie: string
    :return: - ( sterge toate pachetele cu destinatia destinatie din lista pachete )
    """
    indexi = []
    for key in pachete:
        if get_destinatie_pachet(pachete[key]) == destinatie:
            indexi.append(key)
    for i in indexi:
        undo.append({"f":adauga_pachet_lista_faraundo,"a":pachete,"p":pachete[i]})
        stergere_pachet_index(pachete, i)

def stergere_durata_pachete_service(pachete, undo, durata):
    """
    sterge toate pachetele de tip pachet din lista pachete care au un interval mai mic decat durata
    :param pachete: lista de pachete unice
    :param durata: integer
    :return: - ( sterge toate pachetele de tip pachet din lista pachete care au data_sfarsit - data_inceput < durata )
    """
    indexi = []
    for key in pachete:
        if int((get_datasfarsit_pachet(pachete[key])-get_datainceput_pachet(pachete[key])).days) < durata:
            indexi.append(key)
    for i in indexi:
        undo.append({"f":adauga_pachet_lista_faraundo,"a":pachete,"p":pachete[i]})
        stergere_pachet_index(pachete, i)
def stergere_pret_pachete_service(pachete, undo, pret):
    """
    sterge toate pachetele de tip pachet din lista pachete care au pretul mai mare decat pret
    :param pachete: lista de pachete unice
    :param pret: integer
    :return: - ( sterge toate pachetele pachet din lista pachete care au pretul pret > pret
    """
    indexi = []
    for key in pachete:
        if get_pret_pachet(pachete[key]) > pret:
            indexi.append(key)
    for i in indexi:
        undo.append({"f":adauga_pachet_lista_faraundo,"a":pachete,"p":pachete[i]})
        stergere_pachet_index(pachete, i)

def filtrare_pret_destinatie(pachete, undo, pret, destinatie):
    """
    sterge toate pachetele de tip pachet din dictionarul pachete care au pretul mai mai decat pret si destinatia diferita de destinatie
    :param pachete: dictionar de pachete
    :param pret: int
    :param destinatie: string
    :return: - ( Sterge toate pachetele care au pretul > pret si destinatia != destinatie )
    """
    indexi = []
    for key in pachete:
        if get_destinatie_pachet(pachete[key]) != destinatie or get_pret_pachet(pachete[key]) > pret:
            indexi.append(key)
    for i in indexi:
        undo.append({"f":adauga_pachet_lista_faraundo,"a":pachete,"p":pachete[i]})
        stergere_pachet_index(pachete, i)


def filtrare_luna(pachete, undo, luna):
    """
    sterge toate pachetele de tip pachet din dictionarul pachete daca luna luna se afla in intervalul data_inceput -> data_sfarsit
    :param pachete: dictionar
    :param luna: int
    :return: - ( sterge pachetele din dictionarul pachete ale caror intervale cuprind luna luna )
    """
    indexi = []
    for key in pachete:
        data_inceput = get_datainceput_pachet(pachete[key])
        data_sfarsit = get_datasfarsit_pachet(pachete[key])
        if data_inceput.year == data_sfarsit.year:
            if data_inceput.month <= luna <= data_sfarsit.month:
                indexi.append(key)
        else:
            if data_inceput.month <= luna or data_sfarsit.month >= luna:
                indexi.append(key)
            elif (data_sfarsit.year - data_inceput.year) * 12 + data_sfarsit.month - data_inceput.month > 12 :
                indexi.append(key)
    for i in indexi:
        undo.append({"f":adauga_pachet_lista_faraundo,"a":pachete,"p":pachete[i]})
        stergere_pachet_index(pachete, i)

def undoundo(l, undo):
    """
    executa ultima comanda din lista undo
    :param l: dictionar de pachete
    :param undo: list
    :return: - ( modifica dictionarul l dupa ultimul element din undo )
    """
    if undo:
        x = undo.pop()
        try:
            x()
        except:
            x['f'](x['a'], x['p'])

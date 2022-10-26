from domain.pachet import egal_pachete, get_datainceput_pachet, get_datasfarsit_pachet, get_destinatie_pachet, \
    get_pret_pachet


def adauga_pachet_lista(l,pachet):
    """
    adauga la lista l de pachete unice pachetul pachet daca pachet nu apare deja in lista l
    :param l: lista de pachete unice
    :param pachet: pachet
    :return: - ( l' = l U {pachet} , daca pachetul pachet nu apare in lista l
    :raise: ValueError cu mesajul string "pachet invalid!\n" daca pachetul pachet apare deja in lista l
    """
    for _pachet in l:
        if egal_pachete(_pachet,pachet):
            raise ValueError("pachet invalid!\n")
    l.append(pachet)

def numar_pachete_lista(l):
    """
    returneaza numarul de pachete pachet unice din lista l
    :param l: lista l de pachete pachet unice
    :return: rez - int : numarul de pachete pachet unice din lista l
    """
    return len(l)

def get_all_pachete(l):
    """
    returneaza lista l' a tuturor pachetelor pachet unice din lista l
    :param l: lista l de pachete pachet unice
    :return: l' = l[:]
    """
    return l[:]

def creeare_lista_interval(l_noua,l,data_inceput,data_sfarsit):
    """
    creeaza o noua lista l_noua formata din pachetele pachet din lista l care au ca data de inceput > data_inceput si data de sfarsit < data_sfarsit
    :param l_noua: list
    :param l: lista de pachete unice
    :param data_inceput: date
    :param data_sfarsit: date
    :return: - ( l_noua = l U pachete din lista l din intervalul data_inceput - data_sfarsit )
    """
    for pachet in l:
        if get_datainceput_pachet(pachet)>=data_inceput and get_datasfarsit_pachet(pachet)<=data_sfarsit:
            l_noua.append(pachet)

def creeare_lista_destinatie_pret(l_noua,l,destinatie,pret):
    """
    creeaza o noua lista l_noua formata din pachetele pachet din lista l care au destinatia destinatie si pretul mai mic decat pret
    :param l_noua: lista
    :param l: lista de pachete unice
    :param destinatie: string
    :param pret: integer
    :return: - ( l_noua = l U pachetele din lista l cu destinatia destinatie si pretul < pret )
    """
    for pachet in l:
        if get_destinatie_pachet(pachet)==destinatie and get_pret_pachet(pachet)<pret:
            l_noua.append(pachet)

def creeare_lista_datasfarsit(l_noua,l,data_sfarsit):
    """
    creeaza o noua lista l_noua formata din pachetele pachet din lista l care au data de sfarsit lafel ca data_sfarsit
    :param l_noua: lista
    :param l: lista de pachete unice
    :param data_sfarsit: date
    :return: - ( l_noua = l U pachetele din lista l cu data de sfarsit = data_sfarsit )
    """
    for pachet in l:
        if get_datasfarsit_pachet(pachet)==data_sfarsit:
            l_noua.append(pachet)